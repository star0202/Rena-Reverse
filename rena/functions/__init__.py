# for mypy type checking
from .register import Register
from .school import School
from .setting import Setting
from .user import UserCog


__all__ = [
    "Register",
    "School",
    "Setting",
    "UserCog"
]