# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails


class Funding(APIComponent):
    def get_currencies(self, ccy: str = None, use_proxy: bool = False) -> APIReturn:
        """
        Get currencies
        Retrieve a list of all currencies.
        Rate Limit: 6 requests per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/currencies",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_balance(self, ccy: str = None, use_proxy: bool = False) -> APIReturn:
        """
                        Get balance
                        Retrieve the balances of all the assets and the amount that is available or on hold.

        Only asset information of a currency with a balance greater than 0 will be returned.

                        Rate Limit: 6 requests per second
                        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/balances",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_account_asset_valuation(
        self, ccy: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get account asset valuation
        View account asset valuation
        Rate Limit: 1 request 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/asset-valuation",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def funds_transfer(
        self,
        ccy: str,
        amt: str,
        from_: str,
        to: str,
        subAcct: str = None,
        type: str = None,
        loanTrans: bool = None,
        clientId: str = None,
        omitPosRisk: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
                        Funds transfer
                        Only API keys with Trade privilege can call this endpoint.
                        This endpoint supports the transfer of funds between your funding account and trading account, and from the master account to sub-accounts.
                        Sub-account can transfer out to master account by default. Need to call "Set Permission Of Transfer Out" to grant privilege first if you want sub-account transferring to another sub-account(subaccounts need to belong to same master account.)

        Failure of the request does not mean the transfer has failed. Recommend to call "Get funds transfer state" to confirm the status.

                        Rate Limit: 1 request per second
                        Rate limit rule: UserID + Currency
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/transfer",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_funds_transfer_state(
        self,
        transId: str = None,
        clientId: str = None,
        type: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get funds transfer state
        Retrieve the transfer state data of the last 2 weeks.
        Rate Limit: 1 request per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/transfer-state",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def asset_bills_details(
        self,
        ccy: str = None,
        type: str = None,
        clientId: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Asset bills details
        Query the billing record. You can get the latest 1 month historical data.
        Rate Limit: 6 Requests per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/bills",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def lightning_deposits(
        self, ccy: str, amt: str, to: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Lightning deposits
        Users can create up to 10,000 different invoices within 24 hours.
        Rate Limit: 2 requests per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/deposit-lightning",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_deposit_address(self, ccy: str, use_proxy: bool = False) -> APIReturn:
        """
        Get deposit address
        Retrieve the deposit addresses of currencies, including previously-used addresses.
        Rate Limit: 6 requests per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/deposit-address",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_deposit_history(
        self,
        ccy: str = None,
        depId: str = None,
        txId: str = None,
        state: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get deposit history
        Retrieve the deposit records according to the currency, deposit status, and time range in reverse chronological order. The 100 most recent records are returned by default.
        Rate Limit: 6 requests per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/deposit-history",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def withdrawal(
        self,
        ccy: str,
        amt: str,
        dest: str,
        toAddr: str,
        fee: str,
        chain: str = None,
        clientId: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Withdrawal
        Withdrawal of tokens. Sub-account does not support withdrawal.
        Rate Limit: 6 requests per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/withdrawal",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def lightning_withdrawals(
        self, ccy: str, invoice: str, memo: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Lightning withdrawals
        The maximum withdrawal amount is 0.1 BTC per request, and 1 BTC in 24 hours. The minimum withdrawal amount is approximately 0.000001 BTC. Sub-account does not support withdrawal.
        Rate Limit: 2 requests per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/withdrawal-lightning",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def cancel_withdrawal(self, wdId: str, use_proxy: bool = False) -> APIReturn:
        """
        Cancel withdrawal
        You can cancel normal withdrawal requests, but you cannot cancel withdrawal requests on Lightning.
        Rate Limit: 6 requests per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/cancel-withdrawal",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_withdrawal_history(
        self,
        ccy: str = None,
        wdId: str = None,
        clientId: str = None,
        txId: str = None,
        state: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get withdrawal history
        Retrieve the withdrawal records according to the currency, withdrawal status, and time range in reverse chronological order. The 100 most recent records are returned by default.
        Rate Limit: 6 requests per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/withdrawal-history",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def small_assets_convert(self, ccy: list, use_proxy: bool = False) -> APIReturn:
        """
        Small assets convert
        Convert small assets in funding account to OKB. Only one convert is allowed within 24 hours.
        Rate Limit: 1 request per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/convert-dust-assets",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_saving_balance(self, ccy: str = None, use_proxy: bool = False) -> APIReturn:
        """
        Get saving balance
        Only the assets in the funding account can be used for saving.
        Rate Limit: 6 requests per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/saving-balance",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def savings_purchase_redemption(
        self, ccy: str, amt: str, side: str, rate: str, use_proxy: bool = False
    ) -> APIReturn:
        """
        Savings purchase/redemption
        Rate Limit: 6 requests per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/purchase_redempt",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def set_lending_rate(
        self, ccy: str, rate: str, use_proxy: bool = False
    ) -> APIReturn:
        """
        Set lending rate
        Rate Limit: 6 requests per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/set-lending-rate",
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
        Get lending history
        Rate Limit: 6 requests per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/lending-history",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_public_borrow_info_public(
        self, ccy: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get public borrow info (public)
        Authentication is not required for this public endpoint.
        Rate Limit: 6 requests per second
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/lending-rate-summary",
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
        Get public borrow history (public)
        Authentication is not required for this public endpoint.
        Rate Limit: 6 requests per second
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/lending-rate-history",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
