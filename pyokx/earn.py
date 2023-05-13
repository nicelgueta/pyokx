# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails
from typing import *


class Earn(APIComponent):
    def get_offers(self, productId: str = None, protocolType: str = None, ccy: str = None, protocol: str = None, term: str = None, apy: str = None, earlyRedeem: bool = None, investData: list = None, bal: str = None, minAmt: str = None, maxAmt: str = None, earningData: list = None, earningType: str = None, state: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 3 requests per second
        Rate limit rule: UserID
        

        Args:
            productId: Product ID
            protocolType: Protocol type staking: staking defi: DEFI
            ccy: Investment currency, e.g. BTC
            ccy: Currency type, e.g. BTC
            productId: Product ID
            protocol: Protocol
            protocolType: Protocol type staking：staking defi：DEFI
            term: Protocol term For current, this field is 0, and for others it shows
                the number of deposit days
            apy: Estimated annualization If the annualization is 7% , this field is
                0.07
            earlyRedeem: Whether the protocol supports early redemption
            investData: Current target currency information available for investment
            ccy: Investment currency, e.g. BTC
            bal: Available balance to invest
            minAmt: Minimum subscription amount
            maxAmt: Maximum subscription amount
            earningData: Earning data
            ccy: Earning currency, e.g. BTC
            earningType: Earning type 0: Estimated earning 1: Cumulative earning
            state: Product state purchasable: Purchasable sold_out: Sold out Stop:
                Suspension of subscription
        _____________
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
        

    def purchase(self, productId: str, investData: list, ccy: str, amt: str, term: str = None, tag: str = None, ordId: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 2 requests per second
        Rate limit rule: UserID
        

        Args:
            productId: Product ID
            investData: Investment data
            ccy: Investment currency, e.g. BTC
            amt: Investment amount
            term: Investment term Investment term must be specified for fixed-term
                projects
            tag: Order tag A combination of case-sensitive alphanumerics, all numbers,
                or all letters of up to 16 characters.
            ordId: Order ID
            tag: Order tag
        _____________
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
        

    def redeem(self, ordId: str, protocolType: str, allowEarlyRedeem: bool = None, tag: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 2 requests per second
        Rate limit rule: UserID
        

        Args:
            ordId: Order ID
            protocolType: Protocol type staking: staking defi: DEFI
            allowEarlyRedeem: Whether allows early redemption Default is false
            tag: Order tag
        _____________
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
        

    def cancel_purchases_redemptions(self, ordId: str, protocolType: str, tag: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        
        After cancelling, returning funds will go to the funding account.
        
        Rate Limit: 2 requests per second
        Rate limit rule: UserID
        

        Args:
            ordId: Order ID
            protocolType: Protocol type staking: staking defi: DEFI
            tag: Order tag
        _____________
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
        

    def get_active_orders(self, productId: str = None, protocolType: str = None, ccy: str = None, state: str = None, ordId: str = None, protocol: str = None, term: str = None, apy: str = None, investData: list = None, amt: str = None, earningData: list = None, earningType: str = None, earnings: str = None, purchasedTime: str = None, estSettlementTime: str = None, cancelRedemptionDeadline: str = None, tag: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 3 requests per second
        Rate limit rule: UserID
        

        Args:
            productId: Product ID
            protocolType: Protocol type staking: staking defi: DEFI
            ccy: Investment currency, e.g. BTC
            state: Order state 8: Pending 13: Cancelling 9: Onchain 1: Earning 2:
                Redeeming
            ccy: Currency, e.g. BTC
            ordId: Order ID
            productId: Product ID
            state: Order state 8: Pending 13: Cancelling 9: Onchain 1: Earning 2:
                Redeeming
            protocol: Protocol
            protocolType: Protocol type staking: staking defi: DEFI
            term: Protocol term For current, this field is 0, and for others it shows
                the number of deposit days
            apy: Estimated annualization If the annualization is 7% , this field is
                0.07 Retain to 4 decimal places (truncated)
            investData: Investment data
            ccy: Investment currency, e.g. BTC
            amt: Invested amount
            earningData: Earning data
            ccy: Earning currency, e.g. BTC
            earningType: Earning type 0: Estimated earning 1: Cumulative earning
            earnings: Earning amount
            purchasedTime: Order purchased time, Unix timestamp format in milliseconds, e.g.
                1597026383085
            estSettlementTime: Estimated redemption settlement time
            cancelRedemptionDeadline: Deadline for cancellation of redemption application
            tag: Order tag
        _____________
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
        

    def get_order_history(self, productId: str = None, protocolType: str = None, ccy: str = None, after: str = None, before: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 3 requests per second
        Rate limit rule: UserID
        

        Args:
            productId: Product ID
            protocolType: Protocol type staking: staking defi: DEFI
            ccy: Investment currency, e.g. BTC
            after: Pagination of data to return records earlier than the requested ID.
                The value passed is the corresponding ordId
            before: Pagination of data to return records newer than the requested ID. The
                value passed is the corresponding ordId
            limit: Number of results per request. The default is 100. The maximum is 100.
        _____________
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
        

