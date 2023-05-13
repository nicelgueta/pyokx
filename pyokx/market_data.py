# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails
from typing import *


class MarketData(APIComponent):
    def get_tickers(self, instType: str, uly: str = None, instFamily: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instType: Instrument type  SPOT SWAP  FUTURES OPTION
            uly: Underlying, e.g. BTC-USD Applicable to FUTURES/SWAP/OPTION
            instFamily: Instrument family Applicable to FUTURES/SWAP/OPTION
        _____________
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
    
        Retrieve the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instId: Instrument ID, e.g. BTC-USD-SWAP
        _____________
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
        

    def get_index_tickers(self, quoteCcy: str = None, instId: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve index tickers.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            quoteCcy: Quote currency Currently there is only an index with USD/USDT/BTC as
                the quote currency.
            instId: Index, e.g. BTC-USD Either quoteCcy or instId is required.
        _____________
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
        

    def get_order_book(self, instId: str, sz: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve order book of the instrument.
        Rate Limit: 40 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instId: Instrument ID, e.g. BTC-USDT
            sz: Order book depth per side. Maximum 400, e.g. 400 bids + 400 asks
                Default returns to 1 depth data
        _____________
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
        

    def get_order_lite_book(self, instId: str, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve order top 25 book of the instrument more quickly
        Rate Limit: 6 requests per 1 seconds
        Rate limit rule: IP
        

        Args:
            instId: Instrument ID, e.g. BTC-USDT
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/market/books-lite",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_candlesticks(self, instId: str, bar: str = None, after: str = None, before: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the candlestick charts. This endpoint can retrieve the latest 1,440 data entries. Charts are returned in groups based on the requested bar. 
        Rate Limit: 40 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instId: Instrument ID, e.g. BTC-USD-190927-5000-C
            bar: Bar size, the default is 1m e.g. [1m/3m/5m/15m/30m/1H/2H/4H] Hong Kong
                time opening price k-line：[6H/12H/1D/2D/3D/1W/1M/3M] UTC time opening
                price k-line：[/6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/1Wutc/1Mutc/3Mutc]
            after: Pagination of data to return records earlier than the requested ts
            before: Pagination of data to return records newer than the requested ts
            limit: Number of results per request. The maximum is 300. The default is 100.
        _____________
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
        

    def get_candlesticks_history(self, instId: str, after: str = None, before: str = None, bar: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve history candlestick charts from recent years.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instId: Instrument ID, e.g. BTC-USD-200927
            after: Pagination of data to return records earlier than the requested ts
            before: Pagination of data to return records newer than the requested ts
            bar: Bar size, the default is 1m e.g. [1m/3m/5m/15m/30m/1H/2H/4H] Hong Kong
                time opening price k-line：[6H/12H/1D/2D/3D/1W/1M/3M] UTC time opening
                price k-line：[6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/1Wutc/1Mutc/3Mutc]
            limit: Number of results per request. The maximum is 100. The default is 100.
        _____________
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
        

    def get_index_candlesticks(self, instId: str, after: str = None, before: str = None, bar: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the candlestick charts of the index. This endpoint can retrieve the latest 1,440 data entries. Charts are returned in groups based on the requested bar. 
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instId: Index, e.g. BTC-USD
            after: Pagination of data to return records earlier than the requested ts
            before: Pagination of data to return records newer than the requested ts
            bar: Bar size, the default is 1m e.g. [1m/3m/5m/15m/30m/1H/2H/4H] Hong Kong
                time opening price k-line：[6H/12H/1D/1W/1M/3M] UTC time opening price
                k-line：[/6Hutc/12Hutc/1Dutc/1Wutc/1Mutc/3Mutc]
            limit: Number of results per request. The maximum is 100; The default is 100
        _____________
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
        

    def get_index_candlesticks_history(self, instId: str, after: str = None, before: str = None, bar: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the candlestick charts of the index from recent years.
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instId: Index, e.g. BTC-USD
            after: Pagination of data to return records earlier than the requested ts
            before: Pagination of data to return records newer than the requested ts
            bar: Bar size, the default is 1m e.g. [1m/3m/5m/15m/30m/1H/2H/4H] Hong Kong
                time opening price k-line：[6H/12H/1D/1W/1M] UTC time opening price
                k-line：[/6Hutc/12Hutc/1Dutc/1Wutc/1Mutc]
            limit: Number of results per request. The maximum is 100; The default is 100
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/market/history-index-candles",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_mark_price_candlesticks(self, instId: str, after: str = None, before: str = None, bar: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the candlestick charts of mark price. This endpoint can retrieve the latest 1,440 data entries. Charts are returned in groups based on the requested bar.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instId: Instrument ID, e.g. BTC-USD-SWAP
            after: Pagination of data to return records earlier than the requested ts
            before: Pagination of data to return records newer than the requested ts
            bar: Bar size, the default is 1m e.g. [1m/3m/5m/15m/30m/1H/2H/4H] Hong Kong
                time opening price k-line：[6H/12H/1D/1W/1M/3M] UTC time opening price
                k-line：[6Hutc/12Hutc/1Dutc/1Wutc/1Mutc/3Mutc]
            limit: Number of results per request. The maximum is 100; The default is 100
        _____________
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
        

    def get_mark_price_candlesticks_history(self, instId: str, after: str = None, before: str = None, bar: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the candlestick charts of mark price from recent years.
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instId: Instrument ID, e.g. BTC-USD-SWAP
            after: Pagination of data to return records earlier than the requested ts
            before: Pagination of data to return records newer than the requested ts
            bar: Bar size, the default is 1m e.g. [1m/3m/5m/15m/30m/1H/2H/4H] Hong Kong
                time opening price k-line：[6H/12H/1D/1W/1M] UTC time opening price
                k-line：[6Hutc/12Hutc/1Dutc/1Wutc/1Mutc]
            limit: Number of results per request. The maximum is 100; The default is 100
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/market/history-mark-price-candles",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_trades(self, instId: str, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the recent transactions of an instrument.
        Rate Limit: 100 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instId: Instrument ID, e.g. BTC-USDT
            limit: Number of results per request. The maximum is 500; The default is 100
        _____________
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
        

    def get_trades_history(self, instId: str, type_: str = None, after: str = None, before: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the recent transactions of an instrument from the last 3 months with pagination.
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instId: Instrument ID, e.g. BTC-USDT
            type_: Pagination Type 1: tradeId 2: timestamp  The default is 1
            after: Pagination of data to return records earlier than the requested
                tradeId or ts.
            before: Pagination of data to return records newer than the requested tradeId.
                Do not support timestamp for pagination
            limit: Number of results per request. The maximum and default both are 100
        _____________
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
        

    def get_option_trades(self, instFamily: str, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the recent transactions of an instrument under same instFamily. The maximum is 100.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instFamily: Instrument family, e.g. BTC-USD Applicable to OPTION
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/market/option/instrument-family-trades",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_24h_total_volume(self, volUsd: str = None, volCny: str = None, ts: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        The 24-hour trading volume is calculated on a rolling basis.
        Rate Limit: 2 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            volUsd: 24-hour total trading volume from the order book trading in "USD"
            volCny: 24-hour total trading volume from the order book trading in "CNY"
            ts: Data return time, Unix timestamp format in milliseconds, e.g.
                1597026383085
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/market/platform-",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_oracle(self, messages: str = None, prices: str = None, signatures: str = None, timestamp: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Get the crypto price of signing using Open Oracle smart contract.
        Rate Limit: 1 request per 5 seconds
        Rate limit rule: IP
        

        Args:
            messages: ABI-encoded values [kind, timestamp, key, value], where kind equals
                'prices', timestamp is the time when price was obtained, key is the
                asset ticker (e.g. btc) and value is the asset price.
            prices: Readable asset prices
            signatures: Ethereum-compatible ECDSA signatures for each message
            timestamp: Time of latest datapoint, Unix timestamp, e.g. 1597026387
        _____________
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
        

    def get_exchange_rate(self, usdCny: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        This interface provides the average exchange rate data for 2 weeks
        Rate Limit: 1 request per 2 seconds
        Rate limit rule: IP
        

        Args:
            usdCny: Exchange rate
        _____________
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
    
        Get the index component information data on the market
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            index: index, e.g BTC-USDT
        _____________
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
        

    def get_block_tickers(self, instType: str, uly: str = None, instFamily: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the latest block trading volume in the last 24 hours.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instType: Instrument type  SPOT SWAP  FUTURES OPTION
            uly: Underlying, e.g. BTC-USD Applicable to FUTURES/SWAP/OPTION
            instFamily: Instrument family, e.g. BTC-USD Applicable to FUTURES/SWAP/OPTION
        _____________
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
    
        Retrieve the latest block trading volume in the last 24 hours.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instId: Instrument ID, e.g. BTC-USD-SWAP
        _____________
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
    
        Retrieve the recent block trading transactions of an instrument. Descending order by tradeId. 
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instId: Instrument ID, e.g. BTC-USDT
        _____________
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
        

