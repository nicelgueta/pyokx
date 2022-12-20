from dataclasses import dataclass, field
import pandas as pd
from typing import Any, Dict, List, Optional, Union
from typeguard import typechecked
from .auth import OKXAuth
import requests
from .constants import BASE_URL, VALID_HTTP_METHOD
from .exceptions import OKXServerError, OKXClientError, OKXContentException
from loguru import logger


@typechecked
class OKXClient(object):
    """
    Base parent OKX client for interacting with the exchange

    Parameters
    --------------

    :param key: OKX API access key.
    :param secret: str - OKX API access secret.
    :param passphrase: str - OKX API access passphrase.
    :param proxies: dict - http and https proxies to use if you need to make the request from a proxy.
        May be particularly important if your API key only allows certain IP addresses
    :param test: bool - tells the client you're using this against the OKX demo trading instance.
    This make sure the "x-simulated-trading" header is contained in the request as per the docs
    """

    def __init__(
        self,
        key: str,
        secret: str,
        passphrase: str,
        proxies: Dict[str, str] = None,
        test: bool = False,
    ):
        self.auth = OKXAuth(key=key, secret=secret, phrase=passphrase)
        self.__test = test
        self.__proxies = proxies

    def make_request(
        self,
        request_path: str,
        method: VALID_HTTP_METHOD,
        params: dict = None,
        body: Optional[Union[Dict[str, Any], List[dict]]] = None,
        use_proxy: bool = False,
    ) -> requests.Response:
        """
        Prepare and make the request to the exchange and return the reponse
        """
        prepped = self._prepare_request(
            request_path=request_path, method=method, params=params, body=body
        )
        return self._send_request(prepped, use_proxy=use_proxy)

    def _prepare_request(
        self,
        request_path: str,
        method: VALID_HTTP_METHOD,
        params: dict = None,
        body: Optional[Union[Dict[str, Any], List[dict]]] = None,
    ) -> requests.PreparedRequest:
        params_to_encode = params if method == "GET" else body
        headers = self.auth.get_auth(method, request_path, params_to_encode).to_dict()
        if self.__test:
            headers.update({"x-simulated-trading": "1"})

        url = BASE_URL + request_path
        logger.debug(f"{method} {url}")
        logger.debug(f"{headers=}")
        logger.debug(f"{params_to_encode=}")

        req = requests.Request(
            method=method, url=url, headers=headers, params=params, json=body
        )
        return req.prepare()

    def _send_request(
        self, preq: requests.PreparedRequest, use_proxy: bool = False
    ) -> requests.Response:  # pragma: no cover
        proxies = self.__proxies if use_proxy else None
        with requests.session() as sess:
            response = sess.send(preq, proxies=proxies)
        self._check_successful_status_code(response)
        self._check_successful_content_code(response)
        return response

    def _check_successful_status_code(self, resp: requests.Response):
        logger.debug(f"API Status Code: {resp.status_code}")
        if resp.status_code < 400:
            # informational, success and redirects can all be treated
            # as successful
            return
        elif resp.status_code < 500:
            raise OKXClientError(resp.status_code, resp.text)
        else:
            raise OKXServerError(resp.status_code, resp.text)

    def _check_successful_content_code(self, resp: requests.Response):
        resp_json = resp.json()
        if int(resp_json["code"]) > 0:
            error_code = resp_json["code"]
            error_msg = resp_json["msg"]
            logger.error(error_code, error_msg)
            logger.error(f"Full response: {resp_json}")
            raise OKXContentException(error_code, error_msg, resp.request, resp_json)


@dataclass
class EndpointDetails:
    """
    Dataclass to house the details required to make a request
    """

    request_path: str
    method: VALID_HTTP_METHOD
    params: Optional[Dict[str, Any]] = field(default=None)
    body: Optional[Union[Dict[str, Any], List[dict]]] = field(default=None)
    use_proxy: bool = field(default=False)


@dataclass
class APIReturn:
    """
    Wrapper to hold standard methods to perform onthe response
    """

    response: requests.Response

    def to_df(self) -> pd.DataFrame:
        """
        Returns reponse data in the 'data' property as a
        pandas dataframe
        """
        return pd.DataFrame(self.response.json()["data"])

    def okx_code(self) -> int:
        """
        Returns the OKX response code (not the http response)
        """
        return int(self.response.json()["code"])


class APIComponent(object):
    """
    Sub component for each API
    """

    def __init__(self, base: OKXClient):
        self.base = base

    def request(
        self,
        details: EndpointDetails,
    ) -> APIReturn:
        """
        Make the request to the xchange and return
        the response object
        """
        response = self.base.make_request(
            request_path=details.request_path,
            method=details.method,
            params=details.params,
            body=details.body,
            use_proxy=details.use_proxy,
        )
        return APIReturn(response=response)
