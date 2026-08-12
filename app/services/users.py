import threading
from itertools import count

from app.schemas import User, UserCreate


class DuplicateEmailError(Exception):
    """Raised when a user with the same email already exists."""


class UserService:
    def __init__(self) -> None:
        self._users: dict[int, User] = {}
        self._emails: dict[str, int] = {}
        self._ids = count(1)
        self._lock = threading.Lock()

    def create_user(self, payload: UserCreate) -> User:
        email_key = payload.email.lower()
        with self._lock:
            if email_key in self._emails:
                raise DuplicateEmailError(payload.email)

            user = User(id=next(self._ids), name=payload.name, email=payload.email)
            self._users[user.id] = user
            self._emails[email_key] = user.id
        return user

    def clear(self) -> None:
        with self._lock:
            self._users.clear()
            self._emails.clear()
            self._ids = count(1)


user_service = UserService()
