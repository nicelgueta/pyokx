# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails


class Tradingdata(APIComponent):
    def get_support_coin(self, use_proxy: bool = False) -> APIReturn:
        """
        Get support coin
        Retrieve the currencies supported by the trading data endpoints.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rubik/stat/trading-data/support-coin",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_taker_volume(
        self,
        ccy: str,
        instType: str,
        begin: str = None,
        end: str = None,
        period: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get taker volume
        Retrieve the taker volume for both buyers and sellers.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rubik/stat/taker-volume",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_margin_lending_ratio(
        self,
        ccy: str,
        begin: str = None,
        end: str = None,
        period: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get margin lending ratio
        Retrieve the ratio of cumulative amount between currency margin quote currency and base currency.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rubik/stat/margin/loan-ratio",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_long_short_ratio(
        self,
        ccy: str,
        begin: str = None,
        end: str = None,
        period: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get long/short ratio
        Retrieve the ratio of users with net long vs net short positions for futures and perpetual swaps.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rubik/stat/contracts/long-short-account-ratio",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_contracts_open_interest_and_volume(
        self,
        ccy: str,
        begin: str = None,
        end: str = None,
        period: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get contracts open interest and volume
        Retrieve the open interest and trading volume for futures and perpetual swaps.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rubik/stat/contracts/open-interest-volume",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_options_open_interest_and_volume(
        self, ccy: str, period: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get options open interest and volume
        Retrieve the open interest and trading volume for options.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rubik/stat/option/open-interest-volume",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_put_call_ratio(
        self, ccy: str, period: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get put/call ratio
        Retrieve the open interest ratio and trading volume ratio of calls vs puts.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rubik/stat/option/open-interest-volume-ratio",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_open_interest_and_volume__expiry_(
        self, ccy: str, period: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get open interest and volume (expiry)
        Retrieve the open interest and trading volume of calls and puts for each upcoming expiration.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rubik/stat/option/open-interest-volume-expiry",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_open_interest_and_volume__strike_(
        self, ccy: str, expTime: str, period: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get open interest and volume (strike)
        Retrieve the taker volume for both buyers and sellers of calls and puts.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rubik/stat/option/open-interest-volume-strike",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_taker_flow(
        self, ccy: str, period: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get taker flow
        This shows the relative buy/sell volume for calls and puts. It shows whether traders are bullish or bearish on price and volatility.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rubik/stat/option/taker-block-volume",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
