# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails


class Marketdata(APIComponent):
    def get_tickers(
        self, instType: str, uly: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get tickers
        Retrieve the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/market/tickers",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_ticker(self, instId: str, use_proxy: bool = False) -> APIReturn:
        """
        Get ticker
        Retrieve the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/market/ticker",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_index_tickers(
        self, quoteCcy: str = None, instId: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get index tickers
        Retrieve index tickers.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/market/index-tickers",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_order_book(
        self, instId: str, sz: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get order book
        Retrieve order book of the instrument.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/market/books",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_candlesticks(
        self,
        instId: str,
        bar: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get candlesticks
        Retrieve the candlestick charts. This endpoint can retrieve the latest 1,440 data entries. Charts are returned in groups based on the requested bar.
        Rate Limit: 40 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/market/candles",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_candlesticks_history(
        self,
        instId: str,
        after: str = None,
        before: str = None,
        bar: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get candlesticks history
        Retrieve history candlestick charts from recent years.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/market/history-candles",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_index_candlesticks(
        self,
        instId: str,
        after: str = None,
        before: str = None,
        bar: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get index candlesticks
        Retrieve the candlestick charts of the index. This endpoint can retrieve the latest 1,440 data entries. Charts are returned in groups based on the requested bar.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/market/index-candles",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_mark_price_candlesticks(
        self,
        instId: str,
        after: str = None,
        before: str = None,
        bar: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get mark price candlesticks
        Retrieve the candlestick charts of mark price. This endpoint can retrieve the latest 1,440 data entries. Charts are returned in groups based on the requested bar.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/market/mark-price-candles",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_trades(
        self, instId: str, limit: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get trades
        Retrieve the recent transactions of an instrument.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/market/trades",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_trades_history(
        self,
        instId: str,
        type: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get trades history
        Retrieve the recent transactions of an instrument from the last 3 months with pagination.
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/market/history-trades",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_24h_total_volume(self, use_proxy: bool = False) -> APIReturn:
        """
        Get 24H total volume
        The 24-hour trading volume is calculated on a rolling basis, using USD as the pricing unit, including block trading volume.
        Rate Limit: 2 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/market/platform-24-volume",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_oracle(self, use_proxy: bool = False) -> APIReturn:
        """
        Get oracle
        Get the crypto price of signing using Open Oracle smart contract.
        Rate Limit: 1 request per 5 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/market/open-oracle",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_exchange_rate(self, use_proxy: bool = False) -> APIReturn:
        """
        Get exchange rate
        This interface provides the average exchange rate data for 2 weeks
        Rate Limit: 1 request per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/market/exchange-rate",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_index_components(self, index: str, use_proxy: bool = False) -> APIReturn:
        """
        Get index components
        Get the index component information data on the market
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/market/index-components",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_block_tickers(
        self, instType: str, uly: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get block tickers
        Retrieve the latest block trading volume in the last 24 hours.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/market/block-tickers",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_block_ticker(self, instId: str, use_proxy: bool = False) -> APIReturn:
        """
        Get block ticker
        Retrieve the latest block trading volume in the last 24 hours.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/market/block-ticker",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_block_trades(self, instId: str, use_proxy: bool = False) -> APIReturn:
        """
        Get block trades
        Retrieve the recent block trading transactions of an instrument. Descending order by tradeId.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/market/block-trades",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
