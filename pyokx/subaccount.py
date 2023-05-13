# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails
from typing import *


class Subaccount(APIComponent):
    def view_sub_account_list(self, enable: str = None, subAcct: str = None, after: str = None, before: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Applies to master accounts only
        Rate limit：2 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            enable: Sub-account status, true: Normal ; false: Frozen
            subAcct: Sub-account name
            after: If you query the data prior to the requested creation time ID, the
                value will be a Unix timestamp in millisecond format.
            before: If you query the data after the requested creation time ID, the value
                will be a Unix timestamp in millisecond format.
            limit: Number of results per request. The maximum is 100. The default is 100.
        _____________
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
        

    def reset_the_api_key_of_a_sub_account(self, subAcct: str, apiKey: str, label: str = None, perm: str = None, ip: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Applies to master accounts only and master accounts API Key must be linked to IP addresses.
        Rate limit：1 request per second
        Rate limit rule: UserID
        

        Args:
            subAcct: Sub-account name
            apiKey: Sub-account APIKey
            label: Sub-account API Key label. The label will be reset if this is passed
                through.
            perm: Sub-account API Key permissions read_only : Read only trade : Trade
                Separate with commas if more than one. The permission will be reset if
                this is passed through.
            ip: Sub-account API Key linked IP addresses, separate with commas if more
                than one. Support up to 20 IP addresses. The IP will be reset if this
                is passed through. If ip is set to "", then no IP addresses is linked
                to the APIKey.
        _____________
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
        

    def get_sub_account_trading_balance(self, subAcct: str, use_proxy: bool = False) -> APIReturn:
        """
    
        Query detailed balance info of Trading Account of a sub-account via the master account (applies to master accounts only)
        Rate limit：6 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            subAcct: Sub-account name
        _____________
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
        

    def get_sub_account_funding_balance(self, subAcct: str, ccy: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Query detailed balance info of Funding Account of a sub-account via the master account (applies to master accounts only)
        Rate limit：6 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            subAcct: Sub-account name
            ccy: Single currency or multiple currencies (no more than 20) separated
                with comma, e.g. BTC or BTC,ETH.
        _____________
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
        

    def history_of_sub_account_transfer(self, ccy: str = None, type_: str = None, subAcct: str = None, after: str = None, before: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Applies to master accounts only.
        Retrieve the transfer data for the last 3 months.
        Rate limit：6 requests per second
        Rate limit rule: UserID
        

        Args:
            ccy: Currency, such as BTC
            type_: 0: Transfers from master account to sub-account ;1 : Transfers from
                sub-account to master account.
            subAcct: Sub-account name
            after: If you query the data prior to the requested bill ID, the value will
                be a Unix timestamp in millisecond format.
            before: If you query the data after the requested bill ID, the value will be a
                Unix timestamp in millisecond format.
            limit: Number of results per request. The maximum is 100. The default is 100.
        _____________
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
        

    def master_accounts_manage_the_transfers_between_sub_accounts(self, ccy: str, amt: str, from_: str, to: str, fromSubAccount: str, toSubAccount: str, loanTrans: bool = None, omitPosRisk: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Applies to master accounts only. 
        Only API keys with Trade privilege can call this endpoint.
        Rate limit：1 request per second
        Rate limit rule: UserID
        

        Args:
            ccy: Currency
            amt: Transfer amount
            from: 6:Funding Account 18:Trading account
            to: 6:Funding Account 18:Trading account
            fromSubAccount: Sub-account name of the account that transfers funds out.
            toSubAccount: Sub-account name of the account that transfers funds in.
            loanTrans: Whether or not borrowed coins can be transferred out under Multi-
                currency margin and Portfolio margin the default is false
            omitPosRisk: Ignore position risk Default is false Applicable to Portfolio margin
        _____________
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
        

    def set_permission_of_transfer_out(self, subAcct: str, canTransOut: bool = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Set permission of transfer out for sub-account (only applicable to master account). Sub-account can transfer out to master account by default.
        Rate Limit: 1 request per second
        Rate limit rule: UserID
        

        Args:
            subAcct: Name of the sub-account. Single sub-account or multiple sub-account
                (no more than 20) separated with comma.
            canTransOut: Whether the sub-account has the right to transfer out. The default is
                true. false: cannot transfer out true: can transfer
        _____________
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
        

    def get_custody_trading_sub_account_list(self, subAcct: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        The trading team uses this interface to view the list of sub-accounts currently under escrow
        Rate limit：1 request per second
        Rate limit rule: UserID
        

        Args:
            subAcct: Sub-account name
        _____________
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
        

    def get_the_user_39_s_affiliate_rebate_information(self, apiKey: str, use_proxy: bool = False) -> APIReturn:
        """
    
        This endpoint is used to get the user's affiliate rebate information for affiliate.
        Rate limit：20 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            apiKey: The user's API key
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/users/partner/if-rebate",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def set_sub_accounts_vip_loan(self, enable: bool, subAcct: str, loanAlloc: str, alloc: List[dict] = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Set the VIP loan allocation of sub-accounts. Only Applicable to master account API keys with Trade access.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            enable: true or false
            subAcct: Name of the sub-account
            loanAlloc: VIP Loan allocation. The unit is percent(%). Range is [0, 100].
                Precision is 0.01% (2 decimal places) "0" to remove loan allocation
                for the sub-account
            alloc: If enable = false, this will not be validated
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/subaccount/set-loan-allocation",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_sub_account_borrow_interest_and_limit(self, subAcct: str = None, ccy: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Only applicable to master account API keys. Only return VIP loan information
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            subAcct: Name of the sub-account. Can only put 1 sub account.
            ccy: Loan currency, e.g. BTC
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/subaccount/interest-limits",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

