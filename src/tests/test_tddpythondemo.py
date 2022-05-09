from TddPythonDemo import __version__
from TddPythonDemo.main import requestTest
import pytest


def test_version():
    assert __version__ == "0.1.0"


def test_request_exist():
    localreq = requestTest("http://www.google.com")
    req_result = localreq.make_request()
    assert req_result == 200

@pytest.mark.xfail
def test_request_fails():
    localreq = requestTest("http://www.google.com")
    req_result = localreq.make_request()
    assert req_result == 400
