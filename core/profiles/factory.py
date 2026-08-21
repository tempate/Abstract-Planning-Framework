from core.profiles.beluga import BelugaProfile
from core.profiles.no_mystery import NoMysteryProfile

_PROFILES = {"beluga": BelugaProfile, "no_mystery": NoMysteryProfile}
PROFILE_TYPES = tuple(_PROFILES)


def get_profile(name):
    try:
        return _PROFILES[name]()
    except KeyError as error:
        raise ValueError(f"Unknown profile: {name}.") from error
