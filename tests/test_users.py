from pytest_hoverfly import hoverfly
import requests


@hoverfly("users")
def test_user_1():
    assert requests.get("https://localhost:8500/users/1").status_code == 200


@hoverfly("users")
def test_user_2():
    assert requests.get("https://localhost:8500/users/2").status_code == 200
