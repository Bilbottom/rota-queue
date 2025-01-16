"""
Test the ``rota_queue.rota_queue`` module.
"""

import pytest

from rota_queue import rota_queue


@pytest.fixture
def test_user() -> rota_queue.User:
    rota_queue.DB.connect(reuse_if_open=True)
    rota_queue.DB.create_tables([rota_queue.User])
    user = rota_queue.User(name="Wade Wilson")
    user.save()
    yield user
    rota_queue.DB.drop_tables([rota_queue.User])


@pytest.fixture
def another_test_user() -> rota_queue.User:
    rota_queue.DB.connect(reuse_if_open=True)
    rota_queue.DB.create_tables([rota_queue.User])
    user = rota_queue.User(name="WADE WILSON")
    user.save()
    yield user
    rota_queue.DB.drop_tables([rota_queue.User])


###
# User tests
###
def test__user__init(test_user: rota_queue.User):
    assert test_user.name == "Wade Wilson"


def test__user__str(test_user: rota_queue.User):
    assert str(test_user) == "Wade Wilson"
    assert repr(test_user) == "<User: Wade Wilson>"


def test__user__eq(
    test_user: rota_queue.User,
    another_test_user: rota_queue.User,
):
    assert test_user != another_test_user


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
