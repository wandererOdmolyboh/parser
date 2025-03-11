import os

from django.core.exceptions import ImproperlyConfigured


def get_env(name: str, default: str = "", required: bool = False) -> str:
    if name in os.environ:
        return os.environ[name]

    if required:
        raise ImproperlyConfigured(f"Set the {name} env variable")

    return default


def get_env_int(name: str, default: int = 0, required: bool = False) -> int:
    return int(get_env(name, str(default), required))


def get_env_bool(name: str, default: bool) -> bool:
    if name in os.environ:
        value = os.environ[name]
        return value == "True"

    return default
