from pytest_hoverfly import hoverfly
import requests


@hoverfly("users")
def test_service_1():
    assert requests.get("https://localhost:8500/services/1").status_code == 200


@hoverfly("users")
def test_service_2():
    assert requests.get("https://localhost:8500/services/2").status_code == 200
