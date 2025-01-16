"""
A rota queue.
"""

from __future__ import annotations

import datetime
import pathlib
import re
import sqlite3

# https://github.com/coleifer/peewee
import peewee

HERE = pathlib.Path(__file__).parent
DB = peewee.SqliteDatabase(HERE.parent / "rota.db")  # TODO: Bind to rota name


class BaseModel(peewee.Model):
    class Meta:
        database = DB


class User(BaseModel):
    """
    A user who can be assigned to a rota.
    """

    name = peewee.CharField(unique=True)

    def __str__(self):
        return self.name

    # def __eq__(self, other: User):
    #     return self.name.casefold() == other.name.casefold()


class Tweet(BaseModel):
    user = peewee.ForeignKeyField(User, backref="tweets")
    message = peewee.TextField()
    created_date = peewee.DateTimeField(default=datetime.datetime.now)
    is_published = peewee.BooleanField(default=True)


class Rota:
    """
    A rota, which is a queue of users.

    To persist the rota, an SQLite database is used.
    """

    name: str
    users: list[User]

    def __init__(self, name: str, users: list[User] | None = None):
        self.name = name
        self.users = users or []
        self._database = sqlite3.connect(f"rota__{name}.db")

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        if re.match(r"^[A-Za-z0-9_ -]+$", name):
            self._name = name
        else:
            raise ValueError(
                "Rota name must be alphanumeric and contain only underscores, hyphens, or spaces."
            )
