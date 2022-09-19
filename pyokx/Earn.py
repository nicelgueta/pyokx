# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails


class Earn(APIComponent):
    def get_offers(
        self,
        productId: str = None,
        protocolType: str = None,
        ccy: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get offers
        Rate Limit: 3 requests per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/finance/staking-defi/offers",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def purchase(
        self,
        productId: str,
        investData: list,
        ccy: str,
        amt: str,
        term: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Purchase
        Rate Limit: 2 requests per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/finance/staking-defi/purchase",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def redeem(
        self,
        ordId: str,
        protocolType: str,
        allowEarlyRedeem: bool = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Redeem
        Rate Limit: 2 requests per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/finance/staking-defi/redeem",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def cancel_purchases_redemptions(
        self, ordId: str, protocolType: str, use_proxy: bool = False
    ) -> APIReturn:
        """
                        Cancel purchases/redemptions

        After cancelling, returning funds will go to the funding account.

                        Rate Limit: 2 requests per second
                        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/finance/staking-defi/cancel",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_active_orders(
        self,
        productId: str = None,
        protocolType: str = None,
        ccy: str = None,
        state: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get active orders
        Rate Limit: 3 requests per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/finance/staking-defi/orders-active",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_order_history(
        self,
        productId: str = None,
        protocolType: str = None,
        ccy: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get order history
        Rate Limit: 3 requests per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/finance/staking-defi/orders-history",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
