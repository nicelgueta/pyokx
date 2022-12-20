# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails


class Account(APIComponent):
    def get_balance(self, ccy: str = None, use_proxy: bool = False) -> APIReturn:
        """
                        Get balance
                        Retrieve a list of assets (with non-zero balance), remaining balance, and available amount in the trading account.

        Interest-free quota and discount rates are public data and not displayed on the account interface.

                        Rate Limit: 10 requests per 2 seconds
                        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/balance",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_positions(
        self,
        instType: str = None,
        instId: str = None,
        posId: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get positions
        Retrieve information on your positions. When the account is in net mode, net positions will be displayed, and when the account is in long/short mode, long or short positions will be displayed. Return in reverse chronological order using ctime.
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/positions",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_positions_history(
        self,
        instType: str = None,
        instId: str = None,
        mgnMode: str = None,
        type: str = None,
        posId: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get positions history
        Retrieve the updated position data for the last 3 months. Return in reverse chronological order using utime.
        Rate Limit: 1 request per 10 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/positions-history",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_account_and_position_risk(self, use_proxy: bool = False) -> APIReturn:
        """
                        Get account and position risk
                        Get account and position risk

        Obtain basic information about accounts and positions on the same time slice

                        Rate Limit: 10 requests per 2 seconds
                        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/account-position-risk",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_bills_details_last_7_days(
        self,
        instType: str = None,
        ccy: str = None,
        mgnMode: str = None,
        ctType: str = None,
        type: str = None,
        subType: str = None,
        after: str = None,
        before: str = None,
        begin: str = None,
        end: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get bills details (last 7 days)
        Retrieve the bills of the account. The bill refers to all transaction records that result in changing the balance of an account. Pagination is supported, and the response is sorted with the most recent first. This endpoint can retrieve data from the last 7 days.
        Rate Limit: 6 requests per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/bills",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_bills_details_last_3_months(
        self,
        instType: str = None,
        ccy: str = None,
        mgnMode: str = None,
        ctType: str = None,
        type: str = None,
        subType: str = None,
        after: str = None,
        before: str = None,
        begin: str = None,
        end: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get bills details (last 3 months)
        Retrieve the account’s bills. The bill refers to all transaction records that result in changing the balance of an account. Pagination is supported, and the response is sorted with most recent first. This endpoint can retrieve data from the last 3 months.
        Rate Limit: 6 requests per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/bills-archive",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_account_configuration(self, use_proxy: bool = False) -> APIReturn:
        """
        Get account configuration
        Retrieve current account configuration.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/config",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def set_position_mode(self, posMode: str, use_proxy: bool = False) -> APIReturn:
        """
                        Set position mode
                        Single-currency mode and Multi-currency mode: FUTURES and SWAP support both long/short mode and net mode. In net mode, users can only have positions in one direction; In long/short mode, users can hold positions in long and short directions.
        Portfolio margin mode: FUTURES and SWAP only support net mode
                        Rate Limit: 5 requests per 2 seconds
                        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/set-position-mode",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def set_leverage(
        self,
        lever: str,
        mgnMode: str,
        instId: str = None,
        ccy: str = None,
        posSide: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
                        Set leverage
                        There are 9 different scenarios for leverage setting:
        1. Set leverage for MARGIN instruments under isolated-margin trade mode at pairs level.
        2. Set leverage for MARGIN instruments under cross-margin trade mode and Single-currency margin account mode at pairs level.
        3. Set leverage for MARGIN instruments under cross-margin trade mode and Multi-currency margin at currency level.
        4. Set leverage for FUTURES instruments under cross-margin trade mode at underlying level.
        5. Set leverage for FUTURES instruments under isolated-margin trade mode and buy/sell position mode at contract level.
        6. Set leverage for FUTURES instruments under isolated-margin trade mode and long/short position mode at contract and position side level.
        7. Set leverage for SWAP instruments under cross-margin trade at contract level.
        8. Set leverage for SWAP instruments under isolated-margin trade mode and buy/sell position mode at contract level.
        9. Set leverage for SWAP instruments under isolated-margin trade mode and long/short position mode at contract and position side level.
                        Note that the request parameter posSide is only required when margin mode is isolated in long/short position mode for FUTURES/SWAP instruments (see scenario 6 and 9 above).
        Please refer to the request examples on the right side for each case.
                        Rate Limit: 20 requests per 2 seconds
                        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/set-leverage",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_maximum_buy_sell_amount_or_open_amount(
        self,
        instId: str,
        tdMode: str,
        px: str = None,
        leverage: str = None,
        unSpotOffset: bool = None,
        ccy: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
                        Get maximum buy/sell amount or open amount

        Under the Portfolio Margin account, the cross mode of derivatives does not support the calculation of the maximum buy/sell amount or open amount.

                        Rate Limit: 20 requests per 2 seconds
                        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/max-size",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_maximum_available_tradable_amount(
        self,
        instId: str,
        tdMode: str,
        reduceOnly: bool = None,
        unSpotOffset: bool = None,
        ccy: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get maximum available tradable amount
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/max-avail-size",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def increase_decrease_margin(
        self,
        instId: str,
        posSide: str,
        type: str,
        amt: str,
        ccy: str = None,
        auto: bool = None,
        loanTrans: bool = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Increase/decrease margin
        Increase or decrease the margin of the isolated position. Margin reduction may result in the change of the actual leverage.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/position/margin-balance",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_leverage(
        self, instId: str, mgnMode: str, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get leverage
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/leverage-info",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_the_maximum_loan_of_instrument(
        self, instId: str, mgnMode: str, mgnCcy: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get the maximum loan of instrument
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/max-loan",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_fee_rates(
        self,
        instType: str,
        instId: str = None,
        uly: str = None,
        instFamily: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get fee rates
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/trade-fee",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_interest_accrued_data(
        self,
        type: str = None,
        ccy: str = None,
        instId: str = None,
        mgnMode: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get interest accrued data
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/interest-accrued",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_interest_rate(self, ccy: str = None, use_proxy: bool = False) -> APIReturn:
        """
        Get interest rate
        Get the user's current leveraged currency borrowing interest rate
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/interest-rate",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def set_greeks_pa_bs(self, greeksType: str, use_proxy: bool = False) -> APIReturn:
        """
        Set greeks (PA/BS)
        Set the display type of Greeks.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/set-greeks",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def isolated_margin_trading_settings(
        self, isoMode: str, type: str, use_proxy: bool = False
    ) -> APIReturn:
        """
        Isolated margin trading settings
        You can set the currency margin and futures/perpetual Isolated margin trading mode
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/set-isolated-mode",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_maximum_withdrawals(
        self, ccy: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get maximum withdrawals
        Retrieve the maximum transferable amount from trading account to funding account. If no currency is specified, the transferable amount of all owned currencies will be returned.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/max-withdrawal",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_account_risk_state(self, use_proxy: bool = False) -> APIReturn:
        """
        Get account risk state
        Only applicable to Portfolio margin account
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/risk-state",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def manual_borrow_and_repay_in_quick_margin_mode(
        self, instId: str, ccy: str, side: str, amt: str, use_proxy: bool = False
    ) -> APIReturn:
        """
        Manual borrow and repay in Quick Margin Mode
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/quick-margin-borrow-repay",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_manual_borrow_and_repay_history_in_quick_margin_mode(
        self,
        instId: str = None,
        ccy: str = None,
        side: str = None,
        after: str = None,
        before: str = None,
        begin: str = None,
        end: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get manual borrow and repay history in Quick Margin Mode
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/quick-margin-borrow-repay-history",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def vip_loans_borrow_and_repay(
        self, ccy: str, side: str, amt: str, ordId: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        VIP loans borrow and repay
        Rate Limit: 6 requests per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/borrow-repay",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_borrow_and_repay_history_for_vip_loans(
        self,
        ccy: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get borrow and repay history for VIP loans
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/borrow-repay-history",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_vip_interest_accrued_data(
        self,
        ccy: str = None,
        ordId: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get VIP interest accrued data
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/vip-interest-accrued",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_vip_interest_deducted_data(
        self,
        ccy: str = None,
        ordId: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get VIP interest deducted data
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/vip-interest-deducted",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_vip_loan_order_list(
        self,
        ordId: str = None,
        state: str = None,
        ccy: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get VIP loan order list
        Rate Limit: 5次/2s
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/vip-loan-order-list",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_vip_loan_order_detail(
        self,
        ordId: str = None,
        ccy: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get VIP loan order detail
        Rate Limit: 5次/2s
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/vip-loan-order-detail",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_borrow_interest_and_limit(
        self, type: str = None, ccy: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get borrow interest and limit
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/interest-limits",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def position_builder(self, use_proxy: bool = False) -> APIReturn:
        """
                        Position builder
                        Calculates portfolio margin information for simulated position or current position of the user.
        You can add up to 200 simulated positions in one request.
                        Rate Limit: 2 requests per 2 seconds
                        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/simulated_margin",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_greeks(self, ccy: str = None, use_proxy: bool = False) -> APIReturn:
        """
        Get Greeks
        Retrieve a greeks list of all assets in the account.
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/greeks",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_pm_limitation(
        self,
        instType: str,
        uly: str = None,
        instFamily: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get PM limitation
        Retrieve cross position limitation of SWAP/FUTURES/OPTION under Portfolio margin mode.
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/position-tiers",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def set_risk_offset_type(self, type: str, use_proxy: bool = False) -> APIReturn:
        """
        Set risk offset type
        Configure the risk offset type in portfolio margin mode.
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/set-riskOffset-type",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
