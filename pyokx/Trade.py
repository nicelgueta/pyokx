# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails
from typing import *


class Trade(APIComponent):
    def place_order(
        self,
        instId: str,
        side: str,
        ordType: str,
        sz: str,
        tdMode: str,
        banAmend: bool = None,
        tpTriggerPxType: str = None,
        slOrdPx: str = None,
        slTriggerPx: str = None,
        tpOrdPx: str = None,
        tpTriggerPx: str = None,
        slTriggerPxType: str = None,
        tgtCcy: str = None,
        reduceOnly: bool = None,
        tag: str = None,
        clOrdId: str = None,
        ccy: str = None,
        posSide: str = None,
        px: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
                        Place order
                        You can place an order only if you have sufficient funds.
        For leading contracts, this endpoint supports placement, but can't close positions.
                        Rate Limit: 60 requests per 2 seconds
                        Rate Limit of leading contracts: 1 requests per 2 seconds
                        Rate limit rule (except Options): UserID + Instrument ID
                        Rate limit rule (Options only): UserID + Instrument Family
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trade/order",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def place_multiple_orders(
        self, body: List[dict] = None, use_proxy: bool = False
    ) -> APIReturn:
        """
                        Place multiple orders
                        Place orders in batches. Maximum 20 orders can be placed per request. Request parameters should be passed in the form of an array.
        For leading contracts, this endpoint supports placement, but can't close positions.
                        Rate Limit: 300 orders per 2 seconds
                        Rate Limit of leading contracts: 1 requests per 2 seconds
                        Rate limit rule (except Options): UserID + Instrument ID
                        Rate limit rule (Options only): UserID + Instrument Family

        Unlike other endpoints, the rate limit of this endpoint is determined by the number of orders. If there is only one order in the request, it will consume the rate limit of `Place order`.

        """
        kwargs = body
        details = EndpointDetails(
            request_path="/api/v5/trade/batch-orders",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def cancel_order(
        self,
        instId: str,
        ordId: str = None,
        clOrdId: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Cancel order
        Cancel an incomplete order.
        Rate Limit: 60 requests per 2 seconds
        Rate limit rule (except Options): UserID + Instrument ID
        Rate limit rule (Options only): UserID + Instrument Family
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trade/cancel-order",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def cancel_multiple_orders(
        self, body: List[dict] = None, use_proxy: bool = False
    ) -> APIReturn:
        """
                        Cancel multiple orders
                        Cancel incomplete orders in batches. Maximum 20 orders can be canceled per request. Request parameters should be passed in the form of an array.
                        Rate Limit: 300 orders per 2 seconds
                        Rate limit rule (except Options): UserID + Instrument ID
                        Rate limit rule (Options only): UserID + Instrument Family

        Unlike other endpoints, the rate limit of this endpoint is determined by the number of orders. If there is only one order in the request, it will consume the rate limit of `Cancel order`.

        """
        kwargs = body
        details = EndpointDetails(
            request_path="/api/v5/trade/cancel-batch-orders",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def amend_order(
        self,
        instId: str,
        cxlOnFail: bool = None,
        reqId: str = None,
        ordId: str = None,
        clOrdId: str = None,
        newSz: str = None,
        newPx: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Amend order
        Amend an incomplete order.
        Rate Limit: 60 requests per 2 seconds
        Rate Limit of leading contracts: 1 requests per 2 seconds
        Rate limit rule (except Options): UserID + Instrument ID
        Rate limit rule (Options only): UserID + Instrument Family
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trade/amend-order",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def amend_multiple_orders(
        self, body: List[dict] = None, use_proxy: bool = False
    ) -> APIReturn:
        """
                        Amend multiple orders
                        Amend incomplete orders in batches. Maximum 20 orders can be amended per request. Request parameters should be passed in the form of an array.
                        Rate Limit: 300 orders per 2 seconds
                        Rate Limit of leading contracts: 1 requests per 2 seconds
                        Rate limit rule (except Options): UserID + Instrument ID
                        Rate limit rule (Options only): UserID + Instrument Family

        Unlike other endpoints, the rate limit of this endpoint is determined by the number of orders. If there is only one order in the request, it will consume the rate limit of `Amend order`.

        """
        kwargs = body
        details = EndpointDetails(
            request_path="/api/v5/trade/amend-batch-orders",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def close_positions(
        self,
        instId: str,
        mgnMode: str,
        autoCxl: bool = None,
        clOrdId: str = None,
        tag: str = None,
        posSide: str = None,
        ccy: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Close positions
        Close all positions of an instrument via a market order.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule (except Options): UserID + Instrument ID
        Rate limit rule (Options only): UserID + Instrument Family
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trade/close-position",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_order_details(
        self,
        instId: str,
        ordId: str = None,
        clOrdId: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get order details
        Retrieve order details.
        Rate Limit: 60 requests per 2 seconds
        Rate limit rule (except Options): UserID + Instrument ID
        Rate limit rule (Options only): UserID + Instrument Family
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trade/order",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_order_list(
        self,
        instType: str = None,
        uly: str = None,
        instFamily: str = None,
        instId: str = None,
        ordType: str = None,
        state: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get order List
        Retrieve all incomplete orders under the current account.
        Rate Limit: 60 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trade/orders-pending",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_order_history_last_7_days(
        self,
        instType: str = None,
        uly: str = None,
        instFamily: str = None,
        instId: str = None,
        ordType: str = None,
        state: str = None,
        category: str = None,
        after: str = None,
        before: str = None,
        begin: str = None,
        end: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get order history (last 7 days)
        Retrieve the completed order data for the last 7 days, and the incomplete orders that have been canceled are only reserved for 2 hours.
        Rate Limit: 40 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trade/orders-history",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_order_history_last_3_months(
        self,
        instType: str = None,
        uly: str = None,
        instFamily: str = None,
        instId: str = None,
        ordType: str = None,
        state: str = None,
        category: str = None,
        after: str = None,
        before: str = None,
        begin: str = None,
        end: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get order history (last 3 months)
        Retrieve the completed order data of the last 3 months.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trade/orders-history-archive",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_transaction_details_last_3_days(
        self,
        instType: str = None,
        uly: str = None,
        instFamily: str = None,
        instId: str = None,
        ordId: str = None,
        after: str = None,
        before: str = None,
        begin: str = None,
        end: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get transaction details (last 3 days???
        Retrieve recently-filled transaction details in the last 3 day.
        Rate Limit: 60 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trade/fills",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_transaction_details_last_3_months(
        self,
        instType: str = None,
        uly: str = None,
        instFamily: str = None,
        instId: str = None,
        ordId: str = None,
        after: str = None,
        before: str = None,
        begin: str = None,
        end: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get transaction details (last 3 months)
        Retrieve recently-filled transaction details in the last 3 months.
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trade/fills-history",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def place_algo_order(
        self,
        instId: str,
        tdMode: str,
        side: str,
        ordType: str,
        pxSpread: str = None,
        triggerPxType: str = None,
        callbackRatio: str = None,
        callbackSpread: str = None,
        activePx: str = None,
        pxVar: str = None,
        szLimit: str = None,
        triggerPx: str = None,
        pxLimit: str = None,
        orderPx: str = None,
        slTriggerPxType: str = None,
        slOrdPx: str = None,
        slTriggerPx: str = None,
        tpOrdPx: str = None,
        tpTriggerPxType: str = None,
        tpTriggerPx: str = None,
        clOrdId: str = None,
        tgtCcy: str = None,
        reduceOnly: bool = None,
        tag: str = None,
        ccy: str = None,
        timeInterval: str = None,
        closeFraction: str = None,
        sz: str = None,
        posSide: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Place algo order
        The algo order includes trigger order, oco order, conditional order,iceberg order, twap order and trailing order.
        Rate Limit: 20 requests per 2 seconds
        Rate Limit of leading contracts: 1 requests per 2 seconds
        Rate limit rule (except Options): UserID + Instrument ID
        Rate limit rule (Options only): UserID + Instrument Family
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trade/order-algo",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def cancel_algo_order(
        self, body: List[dict] = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Cancel algo order
        Cancel unfilled algo orders (not including Iceberg order, TWAP order, Trailing Stop order). A maximum of 10 orders can be canceled per request. Request parameters should be passed in the form of an array.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule (except Options): UserID + Instrument ID
        Rate limit rule (Options only): UserID + Instrument Family
        """
        kwargs = body
        details = EndpointDetails(
            request_path="/api/v5/trade/cancel-algos",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def cancel_advance_algo_order(
        self, body: List[dict] = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Cancel advance algo order
        Cancel unfilled algo orders (including Iceberg order, TWAP order, Trailing Stop order). A maximum of 10 orders can be canceled per request. Request parameters should be passed in the form of an array.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule (except Options): UserID + Instrument ID
        Rate limit rule (Options only): UserID + Instrument Family
        """
        kwargs = body
        details = EndpointDetails(
            request_path="/api/v5/trade/cancel-advance-algos",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_algo_order_list(
        self,
        ordType: str,
        algoId: str = None,
        clOrdId: str = None,
        instType: str = None,
        instId: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get algo order list
        Retrieve a list of untriggered Algo orders under the current account.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trade/orders-algo-pending",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_algo_order_history(
        self,
        ordType: str,
        instType: str = None,
        instId: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        state: str = None,
        algoId: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get algo order history
        Retrieve a list of all algo orders under the current account in the last 3 months.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trade/orders-algo-history",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_easy_convert_currency_list(self, use_proxy: bool = False) -> APIReturn:
        """
        Get easy convert currency list
        Get list of small convertibles and mainstream currencies. Only applicable to the crypto balance less than $10.
        Rate Limit: 1 request per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trade/easy-convert-currency-list",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def place_easy_convert(
        self, fromCcy: list, toCcy: str, use_proxy: bool = False
    ) -> APIReturn:
        """
        Place easy convert
        Convert small currencies to mainstream currencies. Only applicable to the crypto balance less than $10.
        Rate Limit: 1 request per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trade/easy-convert",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_easy_convert_history(
        self,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get easy convert history
        Get the history and status of easy convert trades.
        Rate Limit: 1 request per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trade/easy-convert-history",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_one_click_repay_currency_list(
        self, debtType: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get one-click repay currency list
        Get list of debt currency data and repay currencies. Debt currencies include both cross and isolated debts.
        Rate Limit: 1 request per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trade/one-click-repay-currency-list",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def trade_one_click_repay(
        self, debtCcy: list, repayCcy: str, use_proxy: bool = False
    ) -> APIReturn:
        """
                        Trade one-click repay
                        Trade one-click repay to repay cross debts. Isolated debts are not applicable.
        The maximum repayment amount is based on the remaining available balance of funding and trading accounts.
                        Rate Limit: 1 request per 2 seconds
                        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trade/one-click-repay",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_one_click_repay_history(
        self,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get one-click repay history
        Get the history and status of one-click repay trades.
        Rate Limit: 1 request per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trade/one-click-repay-history",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
