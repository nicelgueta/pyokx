import pytest
from pyokx.auth import OKXAuth


@pytest.mark.parametrize(
    "method,body_params,expected",
    [
        (
            "GET",
            {"hello": "world", "john": "smith", "something": None},
            "2022-05-24T22:55:23.408342GET/api/v5/account/balance?hello=world&john=smith&something=None",
        ),
        (
            "POST",
            {"hello": "world", "john": "smith", "something": None},
            '2022-05-24T22:55:23.408342POST/api/v5/account/balance{"hello": "world", "john": "smith", "something": null}',
        ),
    ],
)
def test_prehash_str(method, body_params, expected):
    assert (
        OKXAuth._prehash_str(
            "2022-05-24T22:55:23.408342",
            method,
            "/api/v5/account/balance",
            body_params,
        )
        == expected
    )


def test_sign():
    auth = OKXAuth(key="k", secret="s", phrase="p")
    sign = auth._sign(
        '2022-05-24T22:55:23.408342POST/api/v5/account/balance{"hello": "world", "john": "smith", "something": null}'
    )
    assert sign == "pqZgQHvEsNjS5PJ2q+QEm6yHoIwWUgyySXQjncNYXdo="


@pytest.mark.parametrize(
    "key,secret,phrase,method,request_path,timestamp,body,expected",
    [
        (
            "k",
            "s",
            "p",
            "POST",
            "/api/v5/account/balance",
            "2022-05-24T22:55:23.408342",
            {"hello": "world", "john": "smith", "something": None},
            {
                "OK-ACCESS-KEY": "k",
                "OK-ACCESS-SIGN": "pqZgQHvEsNjS5PJ2q+QEm6yHoIwWUgyySXQjncNYXdo=",
                "OK-ACCESS-TIMESTAMP": "2022-05-24T22:55:23.408342",
                "OK-ACCESS-PASSPHRASE": "p",
            },
        ),
        (
            "k",
            "s",
            "p",
            "GET",
            "/api/v5/account/balance",
            "2022-05-24T22:55:23.408342",
            None,
            {
                "OK-ACCESS-KEY": "k",
                "OK-ACCESS-SIGN": "5+oHnnnARXMumkYbcYpWV/Qy4AKDjQ7QR327Ne4bKeU=",
                "OK-ACCESS-TIMESTAMP": "2022-05-24T22:55:23.408342",
                "OK-ACCESS-PASSPHRASE": "p",
            },
        ),
    ],
)
def test_get_auth(key, secret, phrase, method, request_path, timestamp, body, expected):
    # monkey patch timestamp to return a fixed datetime
    _orig_method = OKXAuth._get_timestamp
    OKXAuth._get_timestamp = lambda self: timestamp
    a = OKXAuth(key=key, secret=secret, phrase=phrase)
    auth_headers = a.get_auth(method, request_path, body)
    assert auth_headers.to_dict() == expected
    # reset
    OKXAuth._get_timestamp = _orig_method
