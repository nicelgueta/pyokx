# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails
from typing import *


class Convert(APIComponent):
    def get_convert_currencies(self, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 6 requests per second
        Rate limit rule: UserID
                _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/convert/currencies",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_convert_currency_pair(self, fromCcy: str, toCcy: str, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 6 requests per second
        Rate limit rule: UserID
        

        Args:
            fromCcy: Currency to convert from, e.g. USDT
            toCcy: Currency to convert to, e.g. BTC
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/convert/currency-pair",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def estimate_quote(self, baseCcy: str, quoteCcy: str, side: str, rfqSz: str, rfqSzCcy: str, clQReqId: str = None, tag: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 10 requests per second
        Rate limit rule: UserID
        

        Args:
            baseCcy: Base currency, e.g. BTC in BTC-USDT
            quoteCcy: Quote currency, e.g. USDT in BTC-USDT
            side: Trade side based on baseCcy buy sell
            rfqSz: RFQ amount
            rfqSzCcy: RFQ currency
            clQReqId: Client Order ID as assigned by the client A combination of case-
                sensitive alphanumerics, all numbers, or all letters of up to 32
                characters.
            tag: Order tag Applicable to broker user
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/convert/estimate-quote",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def convert_trade(self, quoteId: str, baseCcy: str, quoteCcy: str, side: str, sz: str, szCcy: str, clTReqId: str = None, tag: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 10 requests per second
        Rate limit rule: UserID
        

        Args:
            quoteId: Quote ID
            baseCcy: Base currency, e.g. BTC in BTC-USDT
            quoteCcy: Quote currency, e.g. USDT in BTC-USDT
            side: Trade side based on baseCcy buy sell
            sz: Quote amount The quote amount should no more then RFQ amount
            szCcy: Quote currency
            clTReqId: Client Order ID as assigned by the client A combination of case-
                sensitive alphanumerics, all numbers, or all letters of up to 32
                characters.
            tag: Order tag Applicable to broker user
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/convert/trade",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_convert_history(self, after: str = None, before: str = None, limit: str = None, tag: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 6 requests per second
        Rate limit rule: UserID
        

        Args:
            after: Pagination of data to return records earlier than the requested ts,
                Unix timestamp format in milliseconds, e.g. 1597026383085
            before: Pagination of data to return records newer than the requested ts, Unix
                timestamp format in milliseconds, e.g. 1597026383085
            limit: Number of results per request. The maximum is 100. The default is 100.
            tag: Order tag Applicable to broker user
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/convert/history",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

