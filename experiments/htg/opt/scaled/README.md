# Scaled HTG opt track

The HTG counterpart of `experiments/ipc/opt/scaled/`: problems of opt-htg/symmetries whose best class grows up to 1000 objects, the class LMcutᵅ solved them fastest with, not necessarily the largest. The base problems are up to three per domain that both modes solve with that class, 15 over 9 domains, listed in `suite.py`. Copies never join the class in pipesworld-tankage.

`generate` copies objects as the IPC track does, and writes the grown class's rank at every size to `best_classes.csv`, since a class that is not the largest can overtake others as it grows. `submit` reads that file while the track has no `results.csv`.

## Commands

```bash
# Regenerate every problem, problems.txt and best_classes.csv from the base problems and opt-htg/symmetries
python -m experiments.htg.opt.scaled.generate

# Submit both modes, each abstract run on the grown class
python -m experiments.submit --track opt-htg-scaled --modes abs-lmcut lmcut --partition broadwell
```
