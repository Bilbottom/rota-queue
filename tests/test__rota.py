"""
Test the ``rota_queue.rota_queue`` module.
"""
import pytest

from rota_queue import rota_queue


###
# User tests
###
def test__user__init():
    user = rota_queue.User("Wade Wilson")

    assert user.name == "Wade Wilson"


def test__user__str():
    user = rota_queue.User("Wade Wilson")

    assert str(user) == "Wade Wilson"
    assert repr(user) == "User(name='Wade Wilson')"


def test__user__eq():
    user_1 = rota_queue.User("Wade Wilson")
    user_2 = rota_queue.User("WADE WILSON")
    user_3 = rota_queue.User("wade wilson")

    assert user_1 == user_2 == user_3


###
# Rota tests
###
def test__rota__init():
    rota = rota_queue.Rota("test")

    assert rota.name == "test"
    assert rota.users == []


def test__rota__init__with_users():
    users = [
        rota_queue.User("Wade Wilson"),
        rota_queue.User("Peter Parker"),
        rota_queue.User("Bruce Banner"),
    ]
    rota = rota_queue.Rota(name="test", users=users)

    assert rota.name == "test"
    assert rota.users == users


def test__rota__name__raises():
    with pytest.raises(ValueError):
        rota_queue.Rota(name="This is a test.")
