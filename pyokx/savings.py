# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails


class Savings(APIComponent):
    def get_saving_balance(self, ccy: str = None, use_proxy: bool = False) -> APIReturn:
        """

        Rate Limit: 6 requests per second
        Rate limit rule: UserID


        Args:
            ccy: Currency, e.g. BTC
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/finance/savings/balance",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def savings_purchase_redemption(
        self, ccy: str, amt: str, side: str, rate: str, use_proxy: bool = False
    ) -> APIReturn:
        """

        Only the assets in the funding account can be used for saving.
        Rate Limit: 6 requests per second
        Rate limit rule: UserID


        Args:
            ccy: Currency, e.g. BTC
            amt: Purchase/redemption amount
            side: Action type. purchase: purchase saving shares redempt: redeem saving
                shares
            rate: Annual purchase rate Only applicable to purchase saving shares The
                interest rate of the new subscription will cover the interest rate of
                the last subscription The rate value range is between 1% and 365%
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/finance/savings/purchase-redempt",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def set_lending_rate(
        self, ccy: str, rate: str, use_proxy: bool = False
    ) -> APIReturn:
        """

        Rate Limit: 6 requests per second
        Rate limit rule: UserID


        Args:
            ccy: Currency, e.g. BTC
            rate: Annual lending rate The rate value range is between 1% and 365%
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/finance/savings/set-lending-rate",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_lending_history(
        self,
        ccy: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """

        Rate Limit: 6 requests per second
        Rate limit rule: UserID


        Args:
            ccy: Currency, e.g. BTC
            after: Pagination of data to return records earlier than the requested ts,
                Unix timestamp format in milliseconds, e.g. 1597026383085
            before: Pagination of data to return records newer than the requested ts, Unix
                timestamp format in milliseconds, e.g. 1597026383085
            limit: Number of results per request. The maximum is 100. The default is 100.
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/finance/savings/lending-history",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_public_borrow_info_public(
        self, ccy: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """

        Authentication is not required for this public endpoint.
        Rate Limit: 6 requests per second
        Rate limit rule: IP


        Args:
            ccy: Currency, e.g. BTC
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/finance/savings/lending-rate-summary",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_public_borrow_history_public(
        self,
        ccy: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """

        Authentication is not required for this public endpoint.
        Rate Limit: 6 requests per second
        Rate limit rule: IP


        Args:
            ccy: Currency, e.g. BTC
            after: Pagination of data to return records earlier than the requested ts,
                Unix timestamp format in milliseconds, e.g. 1597026383085
            before: Pagination of data to return records newer than the requested ts, Unix
                timestamp format in milliseconds, e.g. 1597026383085
            limit: Number of results per request. The maximum is 100. The default is 100.
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/finance/savings/lending-rate-history",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
