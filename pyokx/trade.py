# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails
from typing import *


class Trade(APIComponent):
    def place_order(
        self,
        instId: str,
        tdMode: str,
        side: str,
        ordType: str,
        sz: str,
        ccy: str = None,
        clOrdId: str = None,
        tag: str = None,
        posSide: str = None,
        px: str = None,
        reduceOnly: bool = None,
        tgtCcy: str = None,
        banAmend: bool = None,
        tpTriggerPx: str = None,
        tpOrdPx: str = None,
        slTriggerPx: str = None,
        slOrdPx: str = None,
        tpTriggerPxType: str = None,
        slTriggerPxType: str = None,
        quickMgnType: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """

        You can place an order only if you have sufficient funds.
        For leading contracts, this endpoint supports placement, but can't close positions.
        Rate Limit: 60 requests per 2 seconds
        Rate Limit of leading contracts for Copy Trading: 1 requests per 2 seconds
        Rate limit rule (except Options): UserID + Instrument ID
        Rate limit rule (Options only): UserID + Instrument Family


        Args:
            instId: Instrument ID, e.g. BTC-USD-190927-5000-C
            tdMode: Trade mode Margin mode cross isolated Non-Margin mode cash
            side: Order side, buy sell
            ordType: Order type market: Market order limit: Limit order post_only: Post-
                only order fok: Fill-or-kill order ioc: Immediate-or-cancel order
                optimal_limit_ioc: Market order with immediate-or-cancel order
                (applicable only to Futures and Perpetual swap).
            sz: Quantity to buy or sell
            ccy: Margin currency Only applicable to cross MARGIN orders in Single-
                currency margin.
            clOrdId: Client Order ID as assigned by the client A combination of case-
                sensitive alphanumerics, all numbers, or all letters of up to 32
                characters.
            tag: Order tag A combination of case-sensitive alphanumerics, all numbers,
                or all letters of up to 16 characters.
            posSide: Position side The default is net in the net mode It is required in the
                long/short mode, and can only be long or short. Only applicable to
                FUTURES/SWAP.
            px: Order price. Only applicable to limit,post_only,fok,ioc order.
            reduceOnly: Whether orders can only reduce in position size. Valid options: true
                or false. The default value is false. Only applicable to MARGIN
                orders, and FUTURES/SWAP orders in net mode Only applicable to Single-
                currency margin and Multi-currency margin
            tgtCcy: Whether the target currency uses the quote or base currency. base_ccy:
                Base currency ,quote_ccy: Quote currency Only applicable to SPOT
                Market Orders Default is quote_ccy for buy, base_ccy for sell
            banAmend: Whether to disallow the system from amending the size of the SPOT
                Market Order. Valid options: true or false. The default value is
                false. If true, system will not amend and reject the market order if
                user does not have sufficient funds. Only applicable to SPOT Market
                Orders
            tpTriggerPx: Take-profit trigger price If you fill in this parameter, you should
                fill in the take-profit order price as well.
            tpOrdPx: Take-profit order price If you fill in this parameter, you should fill
                in the take-profit trigger price as well. If the price is -1, take-
                profit will be executed at the market price.
            slTriggerPx: Stop-loss trigger price  If you fill in this parameter, you should
                fill in the stop-loss order price.
            slOrdPx: Stop-loss order price  If you fill in this parameter, you should fill
                in the stop-loss trigger price. If the price is -1, stop-loss will be
                executed at the market price.
            tpTriggerPxType: Take-profit trigger price type last: last price index: index price
                mark: mark price The Default is last
            slTriggerPxType: Stop-loss trigger price type last: last price index: index price mark:
                mark price The Default is last
            quickMgnType: Quick Margin type. Only applicable to Quick Margin Mode of isolated
                margin manual, auto_borrow, auto_repay The default value is manual
        _____________
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

        Place orders in batches. Maximum 20 orders can be placed per request. Request parameters should be passed in the form of an array.
        For leading contracts, this endpoint supports placement, but can't close positions.
        Rate Limit: 300 orders per 2 seconds
        Rate Limit of leading contracts for Copy Trading: 1 requests per 2 seconds
        Rate limit rule (except Options): UserID + Instrument ID
        Rate limit rule (Options only): UserID + Instrument Family

        Unlike other endpoints, the rate limit of this endpoint is determined by the number of orders. If there is only one order in the request, it will consume the rate limit of `Place order`.



        Request format:
            This function body should be formatted as an array. Eg.
            ```python
            ...
            body = [
                {
                    "instId": str
                    "tdMode": str
                    "side": str
                    "ordType": str
                    "sz": str
                    "ccy": str  # optional
                    "clOrdId": str  # optional
                    "tag": str  # optional
                    "posSide": str  # optional
                    "px": str  # optional
                    "reduceOnly": bool  # optional
                    "tgtCcy": str  # optional
                    "banAmend": bool  # optional
                    "tpTriggerPx": str  # optional
                    "tpOrdPx": str  # optional
                    "slTriggerPx": str  # optional
                    "slOrdPx": str  # optional
                    "tpTriggerPxType": str  # optional
                    "slTriggerPxType": str  # optional
                    "quickMgnType": str  # optional
                }
                ...
            ]
            api_helper = Trade(client)
            response = api_helper.place_multiple_orders(body=body)
            ```


        Args:
            instId: Instrument ID, e.g. BTC-USD-190927-5000-C
            tdMode: Trade mode Margin mode cross isolated Non-Margin mode cash
            side: Order side buy sell
            ordType: Order type market: Market order limit: Limit order post_only: Post-
                only order fok: Fill-or-kill order ioc: Immediate-or-cancel order
                optimal_limit_ioc: Market order with immediate-or-cancel order
                (applicable only to Futures and Perpetual swap).
            sz: Quantity to buy or sell
            ccy: Margin currency Only applicable to cross MARGIN orders in Single-
                currency margin.
            clOrdId: Client Order ID as assigned by the client A combination of case-
                sensitive alphanumerics, all numbers, or all letters of up to 32
                characters.
            tag: Order tag A combination of case-sensitive alphanumerics, all numbers,
                or all letters of up to 16 characters.
            posSide: Position side The default is net in the net mode It is required in the
                long/short mode, and can only be long or short. Only applicable to
                FUTURES/SWAP.
            px: Order price. Only applicable to limit,post_only,fok,ioc order.
            reduceOnly: Whether the order can only reduce position size. Valid options: true
                or false. The default value is false. Only applicable to MARGIN
                orders, and FUTURES/SWAP orders in net mode Only applicable to Single-
                currency margin and Multi-currency margin
            tgtCcy: Order quantity unit setting for sz base_ccy: Base currency ,quote_ccy:
                Quote currency Only applicable to SPOT Market Orders Default is
                quote_ccy for buy, base_ccy for sell
            banAmend: Whether to disallow the system from amending the size of the SPOT
                Market Order. Valid options: true or false. The default value is
                false. If true, system will not amend and reject the market order if
                user does not have sufficient funds. Only applicable to SPOT Market
                Orders
            tpTriggerPx: Take-profit trigger price If you fill in this parameter, you should
                fill in the take-profit order price as well.
            tpOrdPx: Take-profit order price If you fill in this parameter, you should fill
                in the take-profit trigger price as well. If the price is -1, take-
                profit will be executed at the market price.
            slTriggerPx: Stop-loss trigger price  If you fill in this parameter, you should
                fill in the stop-loss order price.
            slOrdPx: Stop-loss order price  If you fill in this parameter, you should fill
                in the stop-loss trigger price. If the price is -1, stop-loss will be
                executed at the market price.
            tpTriggerPxType: Take-profit trigger price type last: last price index: index price
                mark: mark price The Default is last
            slTriggerPxType: Stop-loss trigger price type last: last price index: index price mark:
                mark price The Default is last
            quickMgnType: Quick Margin type. Only applicable to Quick Margin Mode of isolated
                margin manual, auto_borrow, auto_repay The default value is manual
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
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

        Cancel an incomplete order.
        Rate Limit: 60 requests per 2 seconds
        Rate limit rule (except Options): UserID + Instrument ID
        Rate limit rule (Options only): UserID + Instrument Family


        Args:
            instId: Instrument ID, e.g. BTC-USD-190927
            ordId: Order ID Either ordId or clOrdId is required. If both are passed,
                ordId will be used.
            clOrdId: Client Order ID as assigned by the client
        _____________
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

        Cancel incomplete orders in batches. Maximum 20 orders can be canceled per request. Request parameters should be passed in the form of an array.
        Rate Limit: 300 orders per 2 seconds
        Rate limit rule (except Options): UserID + Instrument ID
        Rate limit rule (Options only): UserID + Instrument Family

        Unlike other endpoints, the rate limit of this endpoint is determined by the number of orders. If there is only one order in the request, it will consume the rate limit of `Cancel order`.



        Request format:
            This function body should be formatted as an array. Eg.
            ```python
            ...
            body = [
                {
                    "instId": str
                    "ordId": str  # optional
                    "clOrdId": str  # optional
                }
                ...
            ]
            api_helper = Trade(client)
            response = api_helper.cancel_multiple_orders(body=body)
            ```


        Args:
            instId: Instrument ID, e.g. BTC-USD-190927
            ordId: Order ID Either ordId or clOrdId is required. If both are passed,
                ordId will be used.
            clOrdId: Client Order ID as assigned by the client
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
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
        ordId: str = None,
        clOrdId: str = None,
        reqId: str = None,
        newSz: str = None,
        newPx: str = None,
        newTpTriggerPx: str = None,
        newTpOrdPx: str = None,
        newSlTriggerPx: str = None,
        newSlOrdPx: str = None,
        newTpTriggerPxType: str = None,
        newSlTriggerPxType: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """

        Amend an incomplete order.
        Rate Limit: 60 requests per 2 seconds
        Rate Limit of leading contracts for Copy Trading: 1 requests per 2 seconds
        Rate limit rule (except Options): UserID + Instrument ID
        Rate limit rule (Options only): UserID + Instrument Family


        Args:
            instId: Instrument ID
            cxlOnFail: Whether the order needs to be automatically canceled when the order
                amendment fails Valid options: false or true, the default is false.
            ordId: Order ID Either ordId or clOrdId is required. If both are passed,
                ordId will be used.
            clOrdId: Client Order ID as assigned by the client
            reqId: Client Request ID as assigned by the client for order amendment A
                combination of case-sensitive alphanumerics, all numbers, or all
                letters of up to 32 characters. The response will include the
                corresponding reqId to help you identify the request if you provide it
                in the request.
            newSz: New quantity after amendment. When amending a partially-filled order,
                the newSz should include the amount that has been filled.
            newPx: New price after amendment.
            newTpTriggerPx: Take-profit trigger price. Either the take profit trigger price or
                order price is 0, it means that the take profit is deleted
            newTpOrdPx: Take-profit order price  If the price is -1, take-profit will be
                executed at the market price.
            newSlTriggerPx: Stop-loss trigger price  Either the stop loss trigger price or order
                price is 0, it means that the stop loss is deleted
            newSlOrdPx: Stop-loss order price  If the price is -1, stop-loss will be executed
                at the market price.
            newTpTriggerPxType: Take-profit trigger price type last: last price index: index price
                mark: mark price
            newSlTriggerPxType: Stop-loss trigger price type last: last price index: index price mark:
                mark price
        _____________
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

        Amend incomplete orders in batches. Maximum 20 orders can be amended per request. Request parameters should be passed in the form of an array.
        Rate Limit: 300 orders per 2 seconds
        Rate Limit of leading contracts for Copy Trading: 1 requests per 2 seconds
        Rate limit rule (except Options): UserID + Instrument ID
        Rate limit rule (Options only): UserID + Instrument Family

        Unlike other endpoints, the rate limit of this endpoint is determined by the number of orders. If there is only one order in the request, it will consume the rate limit of `Amend order`.



        Request format:
            This function body should be formatted as an array. Eg.
            ```python
            ...
            body = [
                {
                    "instId": str
                    "cxlOnFail": bool  # optional
                    "ordId": str  # optional
                    "clOrdId": str  # optional
                    "reqId": str  # optional
                    "newSz": str  # optional
                    "newPx": str  # optional
                    "newTpTriggerPx": str  # optional
                    "newTpOrdPx": str  # optional
                    "newSlTriggerPx": str  # optional
                    "newSlOrdPx": str  # optional
                    "newTpTriggerPxType": str  # optional
                    "newSlTriggerPxType": str  # optional
                }
                ...
            ]
            api_helper = Trade(client)
            response = api_helper.amend_multiple_orders(body=body)
            ```


        Args:
            instId: Instrument ID
            cxlOnFail: Whether the order needs to be automatically canceled when the order
                amendment fails false true, the default is false.
            ordId: Order ID Either ordId or clOrdIdis required, if both are passed, ordId
                will be used.
            clOrdId: Client Order ID as assigned by the client
            reqId: Client Request ID as assigned by the client for order amendment A
                combination of case-sensitive alphanumerics, all numbers, or all
                letters of up to 32 characters. The response will include the
                corresponding reqId to help you identify the request if you provide it
                in the request.
            newSz: New quantity after amendment. When amending a partially-filled order,
                the newSz should include the amount that has been filled.
            newPx: New price after amendment.
            newTpTriggerPx: Take-profit trigger price. Either the take-profit trigger price or
                order price is 0, it means that the take-profit is deleted
            newTpOrdPx: Take-profit order price  If the price is -1, take-profit will be
                executed at the market price.
            newSlTriggerPx: Stop-loss trigger price  Either the stop-loss trigger price or order
                price is 0, it means that the stop-loss is deleted
            newSlOrdPx: Stop-loss order price  If the price is -1, stop-loss will be executed
                at the market price.
            newTpTriggerPxType: Take-profit trigger price type last: last price index: index price
                mark: mark price
            newSlTriggerPxType: Stop-loss trigger price type last: last price index: index price mark:
                mark price
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
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
        posSide: str = None,
        ccy: str = None,
        autoCxl: bool = None,
        clOrdId: str = None,
        tag: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """

        Close the position of an instrument via a market order.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule (except Options): UserID + Instrument ID
        Rate limit rule (Options only): UserID + Instrument Family


        Args:
            instId: Instrument ID
            mgnMode: Margin mode  cross isolated
            posSide: Position side This parameter can be omitted in net mode, and the
                default value is net. You can only fill with net. This parameter must
                be filled in under the long/short mode. Fill in long for close-long
                and short for close-short.
            ccy: Margin currency, required in the case of closing cross MARGIN position
                for Single-currency margin.
            autoCxl: Whether any pending orders for closing out needs to be automatically
                canceled when close position via a market order.  false or true, the
                default is false.
            clOrdId: Client-supplied ID  A combination of case-sensitive alphanumerics, all
                numbers, or all letters of up to 32 characters.
            tag: Order tag A combination of case-sensitive alphanumerics, all numbers,
                or all letters of up to 16 characters.
        _____________
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

        Retrieve order details.
        Rate Limit: 60 requests per 2 seconds
        Rate limit rule (except Options): UserID + Instrument ID
        Rate limit rule (Options only): UserID + Instrument Family


        Args:
            instId: Instrument ID, e.g. BTC-USD-190927
            ordId: Order ID Either ordId or clOrdId is required, if both are passed,
                ordId will be used
            clOrdId: Client Order ID as assigned by the client If the clOrdId is associated
                with multiple orders, only the latest one will be returned.
        _____________
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

        Retrieve all incomplete orders under the current account.
        Rate Limit: 60 requests per 2 seconds
        Rate limit rule: UserID


        Args:
            instType: Instrument type SPOT MARGIN SWAP FUTURES OPTION
            uly: Underlying
            instFamily: Instrument family Applicable to FUTURES/SWAP/OPTION
            instId: Instrument ID, e.g. BTC-USD-200927
            ordType: Order type market: Market order limit: Limit order post_only: Post-
                only order fok: Fill-or-kill order ioc: Immediate-or-cancel order
                optimal_limit_ioc: Market order with immediate-or-cancel order
            state: State  live partially_filled
            after: Pagination of data to return records earlier than the requested ordId
            before: Pagination of data to return records newer than the requested ordId
            limit: Number of results per request. The maximum is 100; The default is 100
        _____________
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
        instType: str,
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

        Retrieve the completed order data for the last 7 days, including those placed 7 days ago but completed for the last 7 days.
        The incomplete orders that have been canceled are only reserved for 2 hours.
        Rate Limit: 40 requests per 2 seconds
        Rate limit rule: UserID


        Args:
            instType: Instrument type SPOT MARGIN SWAP FUTURES OPTION
            uly: Underlying Applicable to FUTURES/SWAP/OPTION
            instFamily: Instrument family Applicable to FUTURES/SWAP/OPTION
            instId: Instrument ID, e.g. BTC-USD-190927
            ordType: Order type market: market order limit: limit order post_only: Post-
                only order fok: Fill-or-kill order ioc: Immediate-or-cancel order
                optimal_limit_ioc: Market order with immediate-or-cancel order
            state: State canceled filled
            category: Category twap adl full_liquidation partial_liquidation delivery ddh
            after: Pagination of data to return records earlier than the requested ordId
            before: Pagination of data to return records newer than the requested ordId
            begin: Filter with a begin timestamp. Unix timestamp format in milliseconds,
                e.g. 1597026383085
            end: Filter with an end timestamp. Unix timestamp format in milliseconds,
                e.g. 1597026383085
            limit: Number of results per request. The maximum is 100; The default is 100
        _____________
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
        instType: str,
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

        Retrieve the completed order data for the last 3 months, including those placed 3 months ago but completed for the last 3 months.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID


        Args:
            instType: Instrument type SPOT MARGIN SWAP FUTURES OPTION
            uly: Underlying Applicable to FUTURES/SWAP/OPTION
            instFamily: Instrument family Applicable to FUTURES/SWAP/OPTION
            instId: Instrument ID, e.g. BTC-USD-200927
            ordType: Order type market: Market order limit: Limit order post_only: Post-
                only order fok: Fill-or-kill order ioc: Immediate-or-cancel order
                optimal_limit_ioc: Market order with immediate-or-cancel order
            state: State  canceled filled
            category: Category twap adl full_liquidation partial_liquidation  delivery ddh
            after: Pagination of data to return records earlier than the requested ordId
            before: Pagination of data to return records newer than the requested ordId
            begin: Filter with a begin timestamp. Unix timestamp format in milliseconds,
                e.g. 1597026383085
            end: Filter with an end timestamp. Unix timestamp format in milliseconds,
                e.g. 1597026383085
            limit: Number of results per request. The maximum is 100; The default is 100
        _____________
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

        Retrieve recently-filled transaction details in the last 3 day.
        Rate Limit: 60 requests per 2 seconds
        Rate limit rule: UserID


        Args:
            instType: Instrument type SPOT MARGIN SWAP FUTURES OPTION
            uly: Underlying Applicable to FUTURES/SWAP/OPTION
            instFamily: Instrument family Applicable to FUTURES/SWAP/OPTION
            instId: Instrument ID, e.g. BTC-USD-190927
            ordId: Order ID
            after: Pagination of data to return records earlier than the requested billId
            before: Pagination of data to return records newer than the requested billId
            begin: Filter with a begin timestamp. Unix timestamp format in milliseconds,
                e.g. 1597026383085
            end: Filter with an end timestamp. Unix timestamp format in milliseconds,
                e.g. 1597026383085
            limit: Number of results per request. The maximum is 100; The default is 100
        _____________
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
        instType: str,
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

        Retrieve recently-filled transaction details in the last 3 months.
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: UserID


        Args:
            instType: Instrument type SPOT MARGIN SWAP FUTURES OPTION
            uly: Underlying Applicable to FUTURES/SWAP/OPTION
            instFamily: Instrument family Applicable to FUTURES/SWAP/OPTION
            instId: Instrument ID, e.g. BTC-USD-190927
            ordId: Order ID
            after: Pagination of data to return records earlier than the requested billId
            before: Pagination of data to return records newer than the requested billId
            begin: Filter with a begin timestamp. Unix timestamp format in milliseconds,
                e.g. 1597026383085
            end: Filter with an end timestamp. Unix timestamp format in milliseconds,
                e.g. 1597026383085
            limit: Number of results per request. The maximum is 100; The default is 100
        _____________
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
        ccy: str = None,
        posSide: str = None,
        sz: str = None,
        tag: str = None,
        reduceOnly: bool = None,
        tgtCcy: str = None,
        algoClOrdId: str = None,
        closeFraction: str = None,
        quickMgnType: str = None,
        tpTriggerPx: str = None,
        tpTriggerPxType: str = None,
        tpOrdPx: str = None,
        slTriggerPx: str = None,
        slTriggerPxType: str = None,
        slOrdPx: str = None,
        triggerPx: str = None,
        orderPx: str = None,
        triggerPxType: str = None,
        callbackRatio: str = None,
        callbackSpread: str = None,
        activePx: str = None,
        pxVar: str = None,
        pxSpread: str = None,
        szLimit: str = None,
        pxLimit: str = None,
        timeInterval: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """

        The algo order includes trigger order, oco order, conditional order,iceberg order, twap order and trailing order.
        Rate Limit: 20 requests per 2 seconds
        Rate Limit of leading contracts for Copy Trading: 1 requests per 2 seconds
        Rate limit rule (except Options): UserID + Instrument ID
        Rate limit rule (Options only): UserID + Instrument Family


        Args:
            instId: Instrument ID, e.g. BTC-USD-190927-5000-C
            tdMode: Trade mode Margin mode cross isolated Non-Margin mode cash
            side: Order side, buy sell
            ordType: Order type conditional: One-way stop order oco: One-cancels-the-other
                order trigger: Trigger order move_order_stop: Trailing order iceberg:
                Iceberg order twap: TWAP order
            ccy: Margin currency Only applicable to cross MARGIN orders in Single-
                currency margin.
            posSide: Position side Required in long/short mode and only be long or short
            sz: Quantity to buy or sell Either sz or closeFraction is required.
            tag: Order tag A combination of case-sensitive alphanumerics, all numbers,
                or all letters of up to 16 characters.
            reduceOnly: Whether the order can only reduce the position size. Valid options:
                true or false. The default value is false. Only applicable to MARGIN
                orders, and FUTURES/SWAP orders in net mode Only applicable to Single-
                currency margin and Multi-currency margin
            tgtCcy: Order quantity unit setting for sz base_ccy: Base currency ,quote_ccy:
                Quote currency Only applicable to SPOT traded with Market buy
                conditional order Default is quote_ccy for buy, base_ccy for sell
            algoClOrdId: Client-supplied Algo ID A combination of case-sensitive alphanumerics,
                all numbers, or all letters of up to 32 characters.
            closeFraction: Fraction of position to be closed when the algo order is triggered.
                Currently the system supports fully closing the position only so the
                only accepted value is 1. This is only applicable to FUTURES or SWAP
                instruments. This is only applicable if posSide is net. This is only
                applicable if reduceOnly is true. This is only applicable if ordType
                is conditional or oco. This is only applicable if the stop loss and
                take profit order is executed as market order Either sz or
                closeFraction is required.
            quickMgnType: Quick Margin type. Only applicable to Quick Margin Mode of isolated
                margin manual, auto_borrow, auto_repay The default value is manual
            tpTriggerPx: Take-profit trigger price If you fill in this parameter, you should
                fill in the take-profit order price as well.
            tpTriggerPxType: Take-profit trigger price type last: last price index: index price
                mark: mark price The Default is last
            tpOrdPx: Take-profit order price If you fill in this parameter, you should fill
                in the take-profit trigger price as well. If the price is -1, take-
                profit will be executed at the market price.
            slTriggerPx: Stop-loss trigger price If you fill in this parameter, you should fill
                in the stop-loss order price.
            slTriggerPxType: Stop-loss trigger price type last: last price index: index price mark:
                mark price The Default is last
            slOrdPx: Stop-loss order price If you fill in this parameter, you should fill
                in the stop-loss trigger price. If the price is -1, stop-loss will be
                executed at the market price.
            triggerPx: Trigger price
            orderPx: Order Price If the price is -1, the order will be executed at the
                market price.
            triggerPxType: Trigger price type last: last price index: index price mark: mark
                price The Default is last
            callbackRatio: Callback price ratio , e.g. 0.01 Either callbackRatio or
                callbackSpread is allowed to be passed.
            callbackSpread: Callback price variance
            activePx: Active price
            pxVar: Price ratio Either pxVar or pxSpread is allowed to be passed.
            pxSpread: Price variance
            szLimit: Average amount
            pxLimit: Price Limit
            pxVar: Price ratio Either pxVar or pxSpread is allowed to be passed.
            pxSpread: Price variance
            szLimit: Average amount
            pxLimit: Price Limit
            timeInterval: Time interval
        _____________
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

        Cancel unfilled algo orders (not including Iceberg order, TWAP order, Trailing Stop order). A maximum of 10 orders can be canceled per request. Request parameters should be passed in the form of an array.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule (except Options): UserID + Instrument ID
        Rate limit rule (Options only): UserID + Instrument Family


        Request format:
            This function body should be formatted as an array. Eg.
            ```python
            ...
            body = [
                {
                    "algoId": str
                    "instId": str
                }
                ...
            ]
            api_helper = Trade(client)
            response = api_helper.cancel_algo_order(body=body)
            ```


        Args:
            algoId: Algo ID
            instId: Instrument ID, e.g. BTC-USDT
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trade/cancel-algos",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def amend_algo_order(
        self,
        instId: str,
        algoId: str,
        algoClOrdId: str,
        cxlOnFail: bool = None,
        reqId: str = None,
        newSz: str = None,
        newTpTriggerPx: str = None,
        newTpOrdPx: str = None,
        newSlTriggerPx: str = None,
        newSlOrdPx: str = None,
        newTpTriggerPxType: str = None,
        newSlTriggerPxType: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """

        Amend unfilled algo orders (Support stop order only,not including Move_order_stop order, Trigger order, Iceberg order, TWAP order, Trailing Stop order).
        Only applicable to Futures and Perpetual swap.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID + Instrument ID


        Args:
            instId: Instrument ID
            algoId: Algo ID
            algoClOrdId: Client-supplied Algo ID
            cxlOnFail: Whether the order needs to be automatically canceled when the order
                amendment fails Valid options: false or true, the default is false.
            reqId: Client Request ID as assigned by the client for order amendment A
                combination of case-sensitive alphanumerics, all numbers, or all
                letters of up to 32 characters. The response will include the
                corresponding reqId to help you identify the request if you provide it
                in the request.
            newSz: New quantity after amendment.
            newTpTriggerPx: Take-profit trigger price. Either the take-profit trigger price or
                order price is 0, it means that the take-profit is deleted
            newTpOrdPx: Take-profit order price If the price is -1, take-profit will be
                executed at the market price.
            newSlTriggerPx: Stop-loss trigger price.  Either the stop-loss trigger price or order
                price is 0, it means that the stop-loss is deleted
            newSlOrdPx: Stop-loss order price If the price is -1, stop-loss will be executed
                at the market price.
            newTpTriggerPxType: Take-profit trigger price type last: last price index: index price
                mark: mark price
            newSlTriggerPxType: Stop-loss trigger price type last: last price index: index price mark:
                mark price
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trade/amend-algos",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def cancel_advance_algo_order(
        self, body: List[dict] = None, use_proxy: bool = False
    ) -> APIReturn:
        """

        Cancel unfilled algo orders (including Iceberg order, TWAP order, Trailing Stop order). A maximum of 10 orders can be canceled per request. Request parameters should be passed in the form of an array.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule (except Options): UserID + Instrument ID
        Rate limit rule (Options only): UserID + Instrument Family


        Request format:
            This function body should be formatted as an array. Eg.
            ```python
            ...
            body = [
                {
                    "algoId": str
                    "instId": str
                }
                ...
            ]
            api_helper = Trade(client)
            response = api_helper.cancel_advance_algo_order(body=body)
            ```


        Args:
            algoId: Algo ID
            instId: Instrument ID, e.g. BTC-USDT
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trade/cancel-advance-algos",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_algo_order_details(
        self, algoId: str = None, algoClOrdId: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """

        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID


        Args:
            algoId: Algo ID Either algoId or algoClOrdId is required.If both are passed,
                algoId will be used.
            algoClOrdId: Client-supplied Algo ID A combination of case-sensitive alphanumerics,
                all numbers, or all letters of up to 32 characters.
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trade/order-algo",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_algo_order_list(
        self,
        ordType: str,
        algoId: str = None,
        algoClOrdId: str = None,
        instType: str = None,
        instId: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """

        Retrieve a list of untriggered Algo orders under the current account.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID


        Args:
            ordType: Order type conditional: One-way stop order oco: One-cancels-the-other
                order trigger: Trigger order move_order_stop: Trailing order iceberg:
                Iceberg order twap: TWAP order
            algoId: Algo ID
            algoClOrdId: Client-supplied Algo ID A combination of case-sensitive alphanumerics,
                all numbers, or all letters of up to 32 characters.
            instType: Instrument type SPOT SWAP FUTURES MARGIN
            instId: Instrument ID, e.g. BTC-USD-190927
            after: Pagination of data to return records earlier than the requested
                algoId.
            before: Pagination of data to return records newer than the requested algoId.
            limit: Number of results per request. The maximum is 100; The default is 100
        _____________
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
        state: str = None,
        algoId: str = None,
        instType: str = None,
        instId: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """

        Retrieve a list of all algo orders under the current account in the last 3 months.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID


        Args:
            ordType: Order type conditional: One-way stop order oco: One-cancels-the-other
                order trigger: Trigger order move_order_stop: Trailing order iceberg:
                Iceberg order twap: TWAP order
            state: State effective canceled order_failed Either state or algoId is
                requied
            algoId: Algo ID Either state or algoId is required.
            instType: Instrument type SPOT SWAP FUTURES MARGIN
            instId: Instrument ID, e.g. BTC-USD-190927
            after: Pagination of data to return records earlier than the requested algoId
            before: Pagination of data to return records new than the requested algoId
            limit: Number of results per request. The maximum is 100; The default is 100
        _____________
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

        Get list of small convertibles and mainstream currencies. Only applicable to the crypto balance less than $10.
        Rate Limit: 1 request per 2 seconds
        Rate limit rule: UserID
                _____________
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

        Convert small currencies to mainstream currencies. Only applicable to the crypto balance less than $10.
        Rate Limit: 1 request per 2 seconds
        Rate limit rule: UserID


        Args:
            fromCcy: Type of small payment currency convert from Maximum 5 currencies can
                be selected in one order. If there are multiple currencies, separate
                them with commas.
            toCcy: Type of mainstream currency convert to Only one receiving currency
                type can be selected in one order and cannot be the same as the small
                payment currencies.
        _____________
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

        Get the history and status of easy convert trades.
        Rate Limit: 1 request per 2 seconds
        Rate limit rule: UserID


        Args:
            after: Pagination of data to return records earlier than the requested time,
                Unix timestamp format in milliseconds, e.g. 1597026383085
            before: Pagination of data to return records newer than the requested time,
                Unix timestamp format in milliseconds, e.g. 1597026383085
            limit: Number of results per request. The maximum is 100. The default is 100.
        _____________
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

        Get list of debt currency data and repay currencies. Debt currencies include both cross and isolated debts.
        Rate Limit: 1 request per 2 seconds
        Rate limit rule: UserID


        Args:
            debtType: Debt type cross: cross isolated: isolated
        _____________
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

        Trade one-click repay to repay cross debts. Isolated debts are not applicable.
        The maximum repayment amount is based on the remaining available balance of funding and trading accounts.
        Rate Limit: 1 request per 2 seconds
        Rate limit rule: UserID


        Args:
            debtCcy: Debt currency type Maximum 5 currencies can be selected in one order.
                If there are multiple currencies, separate them with commas.
            repayCcy: Repay currency type Only one receiving currency type can be selected
                in one order and cannot be the same as the small payment currencies.
        _____________
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

        Get the history and status of one-click repay trades.
        Rate Limit: 1 request per 2 seconds
        Rate limit rule: UserID


        Args:
            after: Pagination of data to return records earlier than the requested time,
                Unix timestamp format in milliseconds, e.g. 1597026383085
            before: Pagination of data to return records newer than the requested time,
                Unix timestamp format in milliseconds, e.g. 1597026383085
            limit: Number of results per request. The maximum is 100. The default is 100.
        _____________
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
