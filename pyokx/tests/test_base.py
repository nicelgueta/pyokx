import json
import pytest
import requests
from pyokx.base import OKXClient
from pyokx.constants import BASE_URL
from pyokx.exceptions import OKXClientError, OKXContentException, OKXServerError


@pytest.fixture(scope="module")
def okxcli():
    return OKXClient(key="fake", secret="fake", passphrase="fake")


@pytest.fixture(scope="module")
def okxcli_test():
    return OKXClient(key="fake", secret="fake", passphrase="fake", test=True)


def mock_okx_response(status_code, data, content_fail=True):
    def get_json():
        return {
            "code": "1" if content_fail else "0",
            "msg": "Some message from OKX" if content_fail else "",
            "data": data,
        }

    resp = requests.Response()
    resp.request = requests.PreparedRequest()
    resp.status_code = status_code
    resp.json = get_json
    return resp


def test_prepare_request_get(okxcli):
    prep = okxcli._prepare_request(
        request_path="/some/request/path-v3",
        method="GET",
        params={"test1": 1, "test2": "hello world"},
        body=None,
    )
    assert prep.url == (f"{BASE_URL}/some/request/path-v3" "?test1=1&test2=hello+world")
    assert prep.body == None
    assert prep.method == "GET"


def test_prepare_request_post(okxcli):
    prep = okxcli._prepare_request(
        request_path="/some/request/path-v3",
        method="POST",
        params=None,
        body={"test1": 1, "test2": "hello world"},
    )
    assert prep.url == f"{BASE_URL}/some/request/path-v3"
    assert prep.body == bytes(json.dumps({"test1": 1, "test2": "hello world"}), "utf-8")
    assert prep.method == "POST"
    assert "x-simulated-trading" not in prep.headers


def test_prepare_request_post_check_test_header(okxcli_test):
    prep = okxcli_test._prepare_request(
        request_path="/some/request/path-v3",
        method="POST",
        params=None,
        body={"test1": 1, "test2": "hello world"},
    )
    assert prep.url == f"{BASE_URL}/some/request/path-v3"
    assert prep.body == bytes(json.dumps({"test1": 1, "test2": "hello world"}), "utf-8")
    assert prep.method == "POST"
    assert "x-simulated-trading" in prep.headers


def test_check_status_code_happy(okxcli):
    resp = mock_okx_response(
        status_code=200, data={"irrelevant": "item"}, content_fail=False
    )
    # no errors raised == pass
    okxcli._check_successful_status_code(resp)


def test_check_status_code_client(okxcli):
    resp = mock_okx_response(
        status_code=400, data={"irrelevant": "item"}, content_fail=False
    )
    with pytest.raises(OKXClientError):
        okxcli._check_successful_status_code(resp)


def test_check_status_code_server(okxcli):
    resp = mock_okx_response(
        status_code=500, data={"irrelevant": "item"}, content_fail=False
    )
    with pytest.raises(OKXServerError):
        okxcli._check_successful_status_code(resp)


def test_content_success(okxcli):
    resp = mock_okx_response(status_code=500, data=[], content_fail=False)
    okxcli._check_successful_content_code(resp)  # no errors


def test_content_fail(okxcli):
    resp = mock_okx_response(status_code=200, data=[], content_fail=True)
    with pytest.raises(OKXContentException) as e:
        try:
            okxcli._check_successful_content_code(resp)
        except Exception as e:
            assert e.args[0] == "1"
            assert e.args[1] == "Some message from OKX"
            assert isinstance(e.args[2], requests.PreparedRequest)
            assert e.args[3] == {
                "code": "1",
                "msg": "Some message from OKX",
                "data": [],
            }
            raise e
