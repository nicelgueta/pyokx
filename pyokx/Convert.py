# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails


class Convert(APIComponent):
    def get_convert_currencies(self, use_proxy: bool = False) -> APIReturn:
        """
        Get convert currencies
        Rate Limit: 6 requests per second
        Rate limit rule: UserID
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

    def get_convert_currency_pair(
        self, fromCcy: str, toCcy: str, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get convert currency pair
        Rate Limit: 6 requests per second
        Rate limit rule: UserID
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

    def estimate_quote(
        self,
        baseCcy: str,
        quoteCcy: str,
        side: str,
        rfqSz: str,
        rfqSzCcy: str,
        clQReqId: str = None,
        tag: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Estimate quote
        Rate Limit: 10 requests per second
        Rate limit rule: UserID
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

    def convert_trade(
        self,
        quoteId: str,
        baseCcy: str,
        quoteCcy: str,
        side: str,
        sz: str,
        szCcy: str,
        clTReqId: str = None,
        tag: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Convert trade
        Rate Limit: 10 requests per second
        Rate limit rule: UserID
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

    def get_convert_history(
        self,
        after: str = None,
        before: str = None,
        limit: str = None,
        tag: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get convert history
        Rate Limit: 6 requests per second
        Rate limit rule: UserID
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
