# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails
from typing import *


class TradingData(APIComponent):
    def get_support_coin(self, contract: List[str] = None, option: List[str] = None, spot: List[str] = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the currencies supported by the trading data endpoints.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            contract: Currency supported by derivatives trading data
            option: Currency supported by option trading data
            spot: Currency supported by spot trading data
        _____________
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
        

    def get_taker_volume(self, ccy: str, instType: str, begin: str = None, end: str = None, period: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the taker volume for both buyers and sellers.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            ccy: Currency
            instType: Instrument type SPOT,CONTRACTS
            begin: Begin time, e.g. 1597026383085
            end: End time, e.g. 1597026383011
            period: Period, the default is 5m, e.g. [5m/1H/1D] 5m granularity can only
                query data within two days at most 1H granularity can only query data
                within 30 days at most 1D granularity can only query data within 180
                days at most
        _____________
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
        

    def get_margin_lending_ratio(self, ccy: str, begin: str = None, end: str = None, period: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the ratio of cumulative amount between currency margin quote currency and base currency.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            ccy: Currency
            begin: Begin time, e.g. 1597026383085
            end: End time, e.g. 1597026383085
            period: Period, the default is 5m, e.g. [5m/1H/1D] 5mgranularity can only
                query data within two days at most 1H granularity can only query data
                within 30 days at most 1D granularity can only query data within 180
                days at most
        _____________
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
        

    def get_long_short_ratio(self, ccy: str, begin: str = None, end: str = None, period: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the ratio of users with net long vs net short positions for futures and perpetual swaps.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            ccy: Currency
            begin: Begin time, e.g. 1597026383085
            end: End time, e.g. 1597026383011
            period: Period, the default is 5m, e.g. [5m/1H/1D] 5m granularity can only
                query data within two days at most 1H granularity can only query data
                within 30 days at most 1D granularity can only query data within 180
                days at most
        _____________
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
        

    def get_contracts_open_interest_and_volume(self, ccy: str, begin: str = None, end: str = None, period: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the open interest and trading volume for futures and perpetual swaps.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            ccy: Currency
            begin: Begin time, e.g. 1597026383085
            end: End time, e.g. 1597026383011
            period: Period, the default is 5m, e.g. [5m/1H/1D] 5m granularity can only
                query data within two days at most 1H granularity can only query data
                within 30 days at most 1D granularity can only query data within 180
                days at most
        _____________
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
        

    def get_options_open_interest_and_volume(self, ccy: str, period: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the open interest and trading volume for options.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            ccy: Currency
            period: Period, the default is 8H. e.g. [8H/1D] Each granularity can only
                query 72 pieces of data at the earliest
        _____________
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
        

    def get_put_call_ratio(self, ccy: str, period: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the open interest ratio and trading volume ratio of calls vs puts.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            ccy: Currency
            period: Period, the default is 8H. e.g. [8H/1D] Each granularity can only
                query 72 pieces of data at the earliest
        _____________
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
        

    def get_open_interest_and_volume_expiry(self, ccy: str, period: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the open interest and trading volume of calls and puts for each upcoming expiration.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            ccy: Currency
            period: Period, the default is 8H. e.g. [8H/1D] Each granularity can only
                query 72 pieces of data at the earliest
        _____________
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
        

    def get_open_interest_and_volume_strike(self, ccy: str, expTime: str, period: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the taker volume for both buyers and sellers of calls and puts.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            ccy: Currency
            expTime: Contract expiry date, the format is YYYYMMdd, e.g. 20210623
            period: Period, the default is 8H. e.g. [8H/1D] Each granularity can only
                query 72 pieces of data at the earliest
        _____________
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
        

    def get_taker_flow(self, ccy: str, period: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        This shows the relative buy/sell volume for calls and puts. It shows whether traders are bullish or bearish on price and volatility.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            ccy: currency
            period: period, the default is 8H. e.g. [8H/1D] Each granularity can only
                query 72 pieces of data at the earliest
        _____________
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
        

