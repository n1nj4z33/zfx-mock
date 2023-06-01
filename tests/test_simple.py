from pytest_hoverfly import hoverfly
import requests


@hoverfly("simple")
def test_simple_pass():
    assert requests.get("https://localhost:8500/").status_code == 200


@hoverfly("simple")
def test_simple_fail():
    assert requests.get("https://localhost:8500/fail").status_code == 200
