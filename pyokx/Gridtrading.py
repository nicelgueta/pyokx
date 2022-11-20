# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails


class Gridtrading(APIComponent):
    def place_grid_algo_order(
        self,
        instId: str,
        algoOrdType: str,
        maxPx: str,
        minPx: str,
        gridNum: str,
        runType: str = None,
        tpTriggerPx: str = None,
        slTriggerPx: str = None,
        tag: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Place grid algo order
        Rate Limit: 20 requests per 2 seconds
        Derivatives rate limit rule: UserID + (instrumentType + underlying)
        Spot & Margin rate limit rule: UserID + instrumentID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/tradingBot/grid/order-algo",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def amend_grid_algo_order(
        self,
        algoId: str,
        instId: str,
        slTriggerPx: str = None,
        tpTriggerPx: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Amend grid algo order
        Supported contract grid algo order amendment.
        Rate Limit: 20 requests per 2 seconds
        Derivatives rate limit rule: UserID + (instrumentType + underlying)
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/tradingBot/grid/amend-order-algo",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def stop_grid_algo_order(
        self,
        algoId: str,
        instId: str,
        algoOrdType: str,
        stopType: str,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Stop grid algo order
        A maximum of 10 orders can be canceled per request.
        Rate Limit: 20 requests per 2 seconds
        Derivatives rate limit rule: UserID + (instrumentType + underlying)
        Spot & Margin rate limit rule: UserID + instrumentID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/tradingBot/grid/stop-order-algo",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_grid_algo_order_list(
        self,
        algoOrdType: str,
        algoId: str = None,
        instId: str = None,
        instType: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get grid algo order list
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/tradingBot/grid/orders-algo-pending",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_grid_algo_order_history(
        self,
        algoOrdType: str,
        algoId: str = None,
        instId: str = None,
        instType: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get grid algo order history
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/tradingBot/grid/orders-algo-history",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_grid_algo_order_details(
        self, algoOrdType: str, algoId: str, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get grid algo order details
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/tradingBot/grid/orders-algo-details",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_grid_algo_sub_orders(
        self,
        algoOrdType: str,
        algoId: str,
        type: str,
        groupId: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get grid algo sub orders
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/tradingBot/grid/sub-orders",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_grid_algo_order_positions(
        self, algoOrdType: str, algoId: str, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get grid algo order positions
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/tradingBot/grid/positions",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def spot_moon_grid_withdraw_income(
        self, algoId: str, use_proxy: bool = False
    ) -> APIReturn:
        """
        Spot/Moon grid withdraw income
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/tradingBot/grid/withdraw-income",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def compute_margin_balance(
        self, algoId: str, type: str, amt: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Compute margin balance
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/tradingBot/grid/compute-margin-balance",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def adjust_margin_balance(
        self,
        algoId: str,
        type: str,
        amt: str = None,
        percent: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Adjust margin balance
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/tradingBot/grid/margin-balance",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_grid_ai_parameter_public(
        self,
        algoOrdType: str,
        instId: str,
        duration: str = None,
        direction: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get grid AI parameter (public)
        Authentication is not required for this public endpoint.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/tradingBot/grid/ai-param",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
