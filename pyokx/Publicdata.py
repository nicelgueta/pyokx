# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails


class Publicdata(APIComponent):
    def get_instruments(
        self,
        instType: str,
        uly: str = None,
        instId: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get instruments
        Retrieve a list of instruments with open contracts.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP +instrumentType
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/public/instruments",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_delivery_exercise_history(
        self,
        instType: str,
        uly: str,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get delivery/exercise history
        Retrieve the estimated delivery price of the last 3 months, which will only have a return value one hour before the delivery/exercise.
        Rate Limit: 40 requests per 2 seconds
        Rate limit rule: IP +(instrumentType、uly)
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/public/delivery-exercise-history",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_open_interest(
        self,
        instType: str,
        uly: str = None,
        instId: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get open interest
        Retrieve the total open interest for contracts on OKX.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP +instrumentID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/public/open-interest",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_funding_rate(self, instId: str, use_proxy: bool = False) -> APIReturn:
        """
        Get funding rate
        Retrieve funding rate.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP +instrumentID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/public/funding-rate",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_funding_rate_history(
        self,
        instId: str,
        before: str = None,
        after: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get funding rate history
        Retrieve funding rate history. This endpoint can retrieve data from the last 3 months.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP +instrumentID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/public/funding-rate-history",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_limit_price(self, instId: str, use_proxy: bool = False) -> APIReturn:
        """
        Get limit price
        Retrieve the highest buy limit and lowest sell limit of the instrument.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/public/price-limit",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_option_market_data(
        self, uly: str, expTime: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get option market data
        Retrieve option market data.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP +uly
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/public/opt-summary",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_estimated_delivery_exercise_price(
        self, instId: str, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get estimated delivery/exercise price
        Retrieve the estimated delivery price which will only have a return value one hour before the delivery/exercise.
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: IP +instId
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/public/estimated-price",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_discount_rate_and_interest_free_quota(
        self, ccy: str = None, discountLv: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get discount rate and interest-free quota
        Retrieve discount rate level and interest-free quota.
        Rate Limit: 2 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/public/discount-rate-interest-free-quota",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_system_time(self, use_proxy: bool = False) -> APIReturn:
        """
        Get system time
        Retrieve API server time.
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/public/time",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_liquidation_orders(
        self,
        instType: str,
        uly: str = None,
        alias: str = None,
        mgnMode: str = None,
        instId: str = None,
        ccy: str = None,
        state: str = None,
        before: str = None,
        after: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get liquidation orders
        Retrieve information on liquidation orders in the last day.
        Rate Limit: 40 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/public/liquidation-orders",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_mark_price(
        self,
        instType: str,
        uly: str = None,
        instId: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get mark price
        Retrieve mark price.
        We set the mark price based on the SPOT index and at a reasonable basis to prevent individual users from manipulating the market and causing the contract price to fluctuate.
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: IP +instrumentID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/public/mark-price",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_position_tiers(
        self,
        instType: str,
        tdMode: str,
        uly: str = None,
        instId: str = None,
        tier: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get position tiers
        Retrieve position tiers information， maximum leverage depends on your borrowings and margin ratio.
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/public/position-tiers",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_interest_rate_and_loan_quota(self, use_proxy: bool = False) -> APIReturn:
        """
        Get interest rate and loan quota
        Retrieve interest rate
        Rate Limit: 2 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/public/interest-rate-loan-quota",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_interest_rate_and_loan_quota_for_vip_loans(
        self, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get interest rate and loan quota for VIP loans
        Rate Limit: 2 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/public/vip-interest-rate-loan-quota",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_underlying(self, instType: str, use_proxy: bool = False) -> APIReturn:
        """
        Get underlying
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/public/underlying",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_insurance_fund(
        self,
        instType: str,
        type: str = None,
        uly: str = None,
        ccy: str = None,
        before: str = None,
        after: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get insurance fund
        Get insurance fund balance information
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/public/insurance-fund",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def unit_convert(
        self,
        instId: str,
        sz: str,
        px: str = None,
        type: str = None,
        unit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Unit convert
        Convert currency to contract, or contract to currency.
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/public/convert-contract-coin",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
