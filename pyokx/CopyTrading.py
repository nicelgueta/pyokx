# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails


class CopyTrading(APIComponent):
    def get_existing_leading_positions(
        self, instId: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get existing leading positions
        Returns reverse chronological order with openTime
        Rate limit: 2 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/copytrading/current-subpositions",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_leading_position_history(
        self,
        instId: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get leading position history
        Returns reverse chronological order with closeTime.
        Rate limit: 2 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/copytrading/subpositions-history",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def place_leading_stop_order(
        self,
        subPosId: str,
        tpTriggerPxType: str = None,
        slTriggerPxType: str = None,
        tpTriggerPx: str = None,
        slTriggerPx: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Place leading stop order
        Rate limit: 1 request per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/copytrading/algo-order",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def close_leading_position(
        self, subPosId: str, use_proxy: bool = False
    ) -> APIReturn:
        """
        Close leading position
        Rate limit: 2 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/copytrading/close-subposition",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_leading_instruments(self, use_proxy: bool = False) -> APIReturn:
        """
        Get leading instruments
        Rate limit: 2 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/copytrading/instruments",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def amend_leading_instruments(
        self, instId: str, use_proxy: bool = False
    ) -> APIReturn:
        """
        Amend leading instruments
        Rate limit: 2 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/copytrading/set-instruments",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_profit_sharing_details(
        self,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get profit sharing details
        Rate limit: 2 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/copytrading/profit-sharing-details",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_total_profit_sharing(self, use_proxy: bool = False) -> APIReturn:
        """
        Get total profit sharing
        Rate limit: 2 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/copytrading/total-profit-sharing",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_unrealized_profit_sharing_details(
        self, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get unrealized profit sharing details
        Rate limit: 2 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/copytrading/unrealized-profit-sharing-details",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
