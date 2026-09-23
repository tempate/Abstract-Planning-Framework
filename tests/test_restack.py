import contextlib
import io
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import restack


def _git(directory, *arguments):
    return subprocess.run(["git", "-C", str(directory), *arguments], capture_output=True, text=True, check=True).stdout


def _commit(directory, name, text):
    Path(directory, name).write_text(text, encoding="utf-8")
    _git(directory, "add", name)
    _git(directory, "commit", "--quiet", "--no-verify", "-m", f"Add {name}")


class RestackTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        self.origin = root / "origin.git"
        self.clone = root / "clone"
        subprocess.run(["git", "init", "--quiet", "--bare", "-b", "main", str(self.origin)], check=True)
        subprocess.run(["git", "clone", "--quiet", str(self.origin), str(self.clone)], check=True, capture_output=True)
        for key, value in (("user.name", "test"), ("user.email", "test@example.com"), ("commit.gpgsign", "false")):
            _git(self.clone, "config", key, value)

        # main, then parent, child and grandchild each on the one before: #1 <- #2 <- #3.
        _commit(self.clone, "base.txt", "base\n")
        _git(self.clone, "push", "--quiet", "origin", "main")
        _git(self.clone, "checkout", "--quiet", "-b", "parent")
        _commit(self.clone, "parent.txt", "parent\n")
        _git(self.clone, "push", "--quiet", "origin", "parent")
        _git(self.clone, "checkout", "--quiet", "-b", "child")
        _commit(self.clone, "child.txt", "child\n")
        _git(self.clone, "push", "--quiet", "origin", "child")
        _git(self.clone, "checkout", "--quiet", "-b", "grandchild")
        _commit(self.clone, "grandchild.txt", "grandchild\n")
        _git(self.clone, "push", "--quiet", "origin", "grandchild")

        # The squash-merge: main gains parent's change as one new commit.
        _git(self.clone, "checkout", "--quiet", "main")
        _commit(self.clone, "parent.txt", "parent\n")
        _git(self.clone, "push", "--quiet", "origin", "main")

        previous = os.getcwd()
        os.chdir(self.clone)
        self.addCleanup(os.chdir, previous)

    def _restack(self, *argv):
        pull_requests = {
            ("--head", "parent"): [{"number": 1}],
            ("--base", "parent"): [{"number": 2, "headRefName": "child"}],
            ("--base", "child"): [{"number": 3, "headRefName": "grandchild"}],
        }
        edits = []

        def gh(*arguments, parse=True):
            if arguments[:2] == ("pr", "edit"):
                edits.append(arguments)
                return ""
            return pull_requests.get(arguments[2:4], [])

        with (
            patch.object(restack, "_gh", side_effect=gh),
            patch("sys.argv", ["restack", *argv]),
            contextlib.redirect_stdout(io.StringIO()),
        ):
            restack.main()
        return edits

    def test_the_stack_lands_on_main_without_the_parents_commits(self):
        edits = self._restack("parent")

        _git(self.clone, "fetch", "--quiet", "--prune", "origin")
        for branch, commits in (("child", ["Add child.txt"]), ("grandchild", ["Add grandchild.txt", "Add child.txt"])):
            own_commits = _git(self.clone, "log", "--format=%s", f"origin/main..origin/{branch}").split("\n")[:-1]
            self.assertEqual(own_commits, commits, branch)
        self.assertEqual(
            _git(self.clone, "merge-base", "origin/main", "origin/child"), _git(self.clone, "rev-parse", "origin/main")
        )
        # Only the direct child changes base; the grandchild stays on the child.
        self.assertEqual(edits, [("pr", "edit", "2", "--base", "main")])
        self.assertNotIn("parent", _git(self.clone, "branch", "-r"))

    def test_a_dry_run_moves_nothing(self):
        before = _git(self.origin, "for-each-ref")

        self._restack("parent", "--dry-run")

        self.assertEqual(_git(self.origin, "for-each-ref"), before)


if __name__ == "__main__":
    unittest.main()
