from dataclasses import dataclass
import json
import hashlib
import hmac
import base64
import datetime
import urllib.parse
from typeguard import typechecked


@dataclass
class OKXAuthHeaders:
    """
    Headers required to authenticate to OKX
    """

    ok_access_key: str
    ok_access_sign: str
    ok_access_timestamp: str
    ok_access_passphrase: str

    def to_dict(self) -> dict:
        """
        Required auth headers:

        "OK-ACCESS-KEY",  # The APIKey as a String.
        "OK-ACCESS-SIGN",  # The Base64-encoded signature
        "OK-ACCESS-TIMESTAMP",  # Timestamp .e.g : 2020-12-08T09:08:57.715Z
        "OK-ACCESS-PASSPHRASE",  # api passphrase
        """

        return {
            "OK-ACCESS-KEY": self.ok_access_key,
            "OK-ACCESS-SIGN": self.ok_access_sign,
            "OK-ACCESS-TIMESTAMP": self.ok_access_timestamp,
            "OK-ACCESS-PASSPHRASE": self.ok_access_passphrase,
        }


@typechecked
class OKXAuth(object):
    """
    Authentication creator
    """

    def __init__(self, key: str, secret: str, phrase: str):
        self.ok_access_key = key
        self.ok_access_secret = secret
        self.ok_access_passphrase = phrase

    def get_auth(
        self, method: str, request_path: str, body: dict = None
    ) -> OKXAuthHeaders:
        """
        Get the auth headers used for making a request to OKX
        """
        ts = self._get_timestamp()
        prehash = self._prehash_str(ts, method, request_path, body)
        sign = self._sign(prehash)
        return OKXAuthHeaders(
            ok_access_key=self.ok_access_key,
            ok_access_sign=sign,
            ok_access_timestamp=ts,
            ok_access_passphrase=self.ok_access_passphrase,
        )

    def _sign(self, prehash: str) -> str:
        hm = hmac.new(
            bytes(self.ok_access_secret, "ascii"),
            msg=bytes(prehash, "ascii"),
            digestmod=hashlib.sha256,
        )
        return base64.b64encode(hm.digest()).decode("ascii")

    @staticmethod
    def _prehash_str(
        timestamp: str, method: str, request_path: str, body: dict = None
    ) -> str:
        if body:
            if method == "GET":
                body_str = "?"
                body_str += urllib.parse.urlencode(body)
            elif method == "POST":
                body_str = json.dumps(body)
        else:
            body_str = ""
        return f"{timestamp}{method}{request_path}{body_str}"

    def _get_timestamp(self) -> str:
        return (
            datetime.datetime.utcnow().isoformat(timespec="milliseconds") + "Z"
        )  # pragma: no cover
