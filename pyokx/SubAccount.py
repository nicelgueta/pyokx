# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails


class SubAccount(APIComponent):
    def view_sub_account_list(
        self,
        enable: str = None,
        subAcct: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        View sub-account list
        Applies to master accounts only
        Rate limit：2 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/users/subaccount/list",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def reset_the_apikey_of_a_sub_account(
        self,
        subAcct: str,
        apiKey: str,
        label: str = None,
        perm: str = None,
        ip: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Reset the APIKey of a sub-account
        Applies to master accounts only and master accounts APIKey must be linked to IP addresses.
        Rate limit：1 request per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/users/subaccount/modify-apikey",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_sub_account_trading_balance(self, use_proxy: bool = False) -> APIReturn:
        """
        Get sub-account trading balance
        Query detailed balance info of Trading Account of a sub-account via the master account (applies to master accounts only)
        Rate limit：2 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/subaccount/balances",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_sub_account_funding_balance(
        self, subAcct: str, ccy: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get sub-account funding balance
        Query detailed balance info of Funding Account of a sub-account via the master account (applies to master accounts only)
        Rate limit：2 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/subaccount/balances",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def history_of_sub_account_transfer(
        self,
        ccy: str = None,
        type: str = None,
        subAcct: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
                        History of sub-account transfer
                        Applies to master accounts only.
        Retrieve the transfer data for the last 3 months.
                        Rate limit：6 requests per second
                        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/subaccount/bills",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def master_accounts_manage_the_transfers_between_sub_accounts(
        self,
        ccy: str,
        amt: str,
        from_: str,
        to: str,
        fromSubAccount: str,
        toSubAccount: str,
        loanTrans: bool = None,
        omitPosRisk: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Master accounts manage the transfers between sub-accounts
        Applies to master accounts only
        Rate limit：1 request per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/subaccount/transfer",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def set_permission_of_transfer_out(
        self, subAcct: str, canTransOut: bool = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Set Permission Of Transfer Out
        Set permission of transfer out for sub-account(only applicable to master account). Sub-account can transfer out to master account by default.
        Rate Limit: 1 request per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/users/subaccount/set-transfer-out",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_custody_trading_sub_account_list(
        self, subAcct: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Get custody trading sub-account list
        The trading team uses this interface to view the list of sub-accounts currently under escrow
        Rate limit：1 request per second
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/users/entrust-subaccount-list",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
