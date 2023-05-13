# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails
from typing import *


class Funding(APIComponent):
    def get_currencies(self, ccy: str = None, use_proxy: bool = False) -> APIReturn:
        """

        Retrieve a list of all currencies.
        Rate Limit: 6 requests per second
        Rate limit rule: UserID


        Args:
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
            request_path="/api/v5/asset/currencies",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_balance(self, ccy: str = None, use_proxy: bool = False) -> APIReturn:
        """

        Retrieve the funding account balances of all the assets and the amount that is available or on hold.

        Only asset information of a currency with a balance greater than 0 will be returned.

        Rate Limit: 6 requests per second
        Rate limit rule: UserID


        Args:
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
            request_path="/api/v5/asset/balances",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_non_tradable_assets(
        self, ccy: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """

        Rate Limit: 6 requests per second
        Rate limit rule: UserID


        Args:
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
            request_path="/api/v5/asset/non-tradable-assets",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_account_asset_valuation(
        self, ccy: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """

        View account asset valuation
        Rate Limit: 1 request per second
        Rate limit rule: UserID


        Args:
            ccy: Asset valuation calculation unit BTC, USDT USD, CNY, JP, KRW, RUB, EUR
                VND, IDR, INR, PHP, THB, TRY AUD, SGD, ARS, SAR, AED, IQD The default
                is the valuation in BTC.
        _____________
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
        type_: str = None,
        loanTrans: bool = None,
        clientId: str = None,
        omitPosRisk: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """

        Only API keys with Trade privilege can call this endpoint.
        This endpoint supports the transfer of funds between your funding account and trading account, and from the master account to sub-accounts.
        Sub-account can transfer out to master account by default. Need to call "Set Permission Of Transfer Out" to grant privilege first if you want sub-account transferring to another sub-account (sub-accounts need to belong to same master account.)

        Failure of the request does not mean the transfer has failed. Recommend to call "Get funds transfer state" to confirm the status.

        Rate Limit: 1 request per second
        Rate limit rule: UserID +  Currency


        Args:
            ccy: Currency, e.g. USDT
            amt: Amount to be transferred
            from: The remitting account 6: Funding account, 18: Trading account
            to: The beneficiary account 6: Funding account, 18: Trading account
            subAcct: Name of the sub-account When type is 1, 2 or 4, sub-account is
                required.
            type_: Transfer type 0: transfer within account 1: master account to sub-
                account (Only applicable to API Key from master account) 2: sub-
                account to master account (Only applicable to API Key from master
                account) 3: sub-account to master account (Only applicable to APIKey
                from sub-account) 4: sub-account to sub-account (Only applicable to
                APIKey from sub-account, and target account needs to be another sub-
                account which belongs to same master account) The default is 0.
            loanTrans: Whether or not borrowed coins can be transferred out under Multi-
                currency margin and Portfolio margin the default is false
            clientId: Client-supplied ID A combination of case-sensitive alphanumerics, all
                numbers, or all letters of up to 32 characters.
            omitPosRisk: Ignore position risk Default is false Applicable to Portfolio margin
        _____________
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
        type_: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """

        Retrieve the transfer state data of the last 2 weeks.
        Rate Limit: 1 request per second
        Rate limit rule: UserID


        Args:
            transId: Transfer ID Either transId or clientId is required. If both are
                passed, transId will be used.
            clientId: Client-supplied ID A combination of case-sensitive alphanumerics, all
                numbers, or all letters of up to 32 characters.
            type_: Transfer type 0: transfer within account 1: master account to sub-
                account (Only applicable to API Key from master account) 2: sub-
                account to master account (Only applicable to API Key from master
                account) 3: sub-account to master account (Only applicable to APIKey
                from sub-account) 4: sub-account to sub-account (Only applicable to
                APIKey from sub-account, and target account needs to be another sub-
                account which belongs to same master account) The default is 0
        _____________
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
        type_: str = None,
        clientId: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """

        Query the billing record. You can get the latest 1 month historical data.
        Rate Limit: 6 Requests per second
        Rate limit rule: UserID


        Args:
            ccy: Currency
            type_: Bill type 1: Deposit 2: Withdrawal 13: Canceled withdrawal 20:
                Transfer to sub account (for master account) 21: Transfer from sub
                account (for master account) 22: Transfer out from sub to master
                account (for sub-account) 23: Transfer in from master to sub account
                (for sub-account) 28: Manually claimed Airdrop 47: System reversal 48:
                Event Reward 49: Event Giveaway 50: Received from appointments 51:
                Deducted from appointments 52: Red packet sent 53: Red packet snatched
                54: Red packet refunded 61: Conversion 68: Claim rebate card 69:
                Distribute rebate card 72: Token received 73: Token given away 74:
                Token refunded 75: Subscription to savings 76: Redemption to savings
                77: Distribute 78: Lock up 79: Node voting 80: Staking 81: Vote
                redemption 82: Staking redemption 83: Staking yield 84: Violation fee
                85: PoW mining yield 86: Cloud mining pay 87: Cloud mining yield 88:
                Subsidy 89: Staking 90: Staking subscription 91: staking redemption
                92: Add collateral 93: Redeem collateral 94: Investment 95: Borrower
                borrows 96: Principal transferred in 97: Borrower transferred loan out
                98: Borrower transferred interest out 99: Investor transferred
                interest in 102: Prepayment penalty transferred in 103: Prepayment
                penalty transferred out 104: Mortgage fee transferred in 105: Mortgage
                fee transferred out 106: Overdue fee transferred in 107: Overdue fee
                transferred out 108: Overdue interest transferred out 109: Overdue
                interest transferred in 110: Collateral for closed position
                transferred in 111: Collateral for closed position transferred out
                112: Collateral for liquidation transferred in 113: Collateral for
                liquidation transferred out 114: Insurance fund transferred in 115:
                Insurance fund transferred out 116: Place an order 117: Fulfill an
                order 118: Cancel an order 119: Merchants unlock deposit 120:
                Merchants add deposit 121: FiatGateway Place an order 122: FiatGateway
                Cancel an order 123: FiatGateway Fulfill an order 124: Jumpstart
                unlocking 125: Manual deposit 126: Interest deposit 127: Investment
                fee transferred in 128: Investment fee transferred out 129: Rewards
                transferred in 130: Transferred from Trading account 131: Transferred
                to Trading account 132: Frozen by customer service 133: Unfrozen by
                customer service 134: Transferred by customer service 135: Cross chain
                exchange 136: Convert 137: ETH 2.0 Subscription 138: ETH 2.0 Swapping
                139: ETH 2.0 Earnings 143: System Reverse 144: Transfer out of unified
                account reserve 145: Reward Expired 146: Customer feedback 147: vested
                sushi rewards 150: Affiliate commission 151: Referral reward 152:
                Broker reward 153: Joiner reward 154: Mystery box reward 155: Rewards
                withdraw 156: Fee rebate 157: Collected crypto 160: Dual Investment
                subscribe 161: Dual Investment collection 162: Dual Investment profit
                163: Dual Investment refund 169: 2022 new year rewards 172: Sub-
                affiliate commission 173: Fee rebate 174: Pay 175: Locked collateral
                176: Loan 177: Added collateral 178: Returned collateral 179:
                Repayment 180: Unlocked collateral 181: Airdrop Payment 182: Feedback
                bounty 183: Invite friends rewards 184: Divide the reward pool 185:
                Broker Convert Reward 186: FreeETH 187: Convert transfer 188: Slot
                Auction Conversion 189: Mystery box bonus 193: Card payment Buy 195:
                Untradable asset withdrawal 196: Untradable asset withdrawal revoked
                197: Untradable asset deposit 198: Untradable asset collection reduce
                199: Untradable asset collection increase 200: Buy 202: Price Lock
                Subscribe 203: Price Lock Collection 204: Price Lock Profit 205: Price
                Lock Refund 207: Dual Investment Lite Subscribe 208: Dual Investment
                Lite Collection 209: Dual Investment Lite Profit 210: Dual Investment
                Lite Refund 211: Win crypto with Satoshi 212: Multi-collateral loan
                collateral locked 213: Collateral transfered out from user account
                214: Collateral returned to users 215: Multi-collateral loan
                collateral released 216: Loan transferred to user's account 217:
                Multi-collateral loan borrowed 218: Multi-collateral loan repaid 219:
                Repayment transferred from user's account 220: Delisted crypto 221:
                Blockchain's withdrawal fee 222: Withdrawal fee refund 223: Profit
                share 224: Service fee 225: Shark Fin subscribe 226: Shark Fin
                collection 227: Shark Fin profit 228: Shark Fin refund 229: Airdrop
                230: Token migration completed 232: Subsidized interest received 233:
                Broker rebate compensation 284: Transfer out trading sub-account 285:
                Transfer in trading sub-account 286: Transfer out custody funding
                account 287: Transfer in custody funding account 288: Custody fund
                delegation 289: Custody fund undelegation
            clientId: Client-supplied ID for transfer or withdrawal A combination of case-
                sensitive alphanumerics, all numbers, or all letters of up to 32
                characters.
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
            request_path="/api/v5/asset/bills",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def lightning_deposits(
        self,
        ccy: str,
        amt: str,
        to: str = None,
        invoice: str = None,
        cTime: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """

        Users can create up to 10,000 different invoices within 24 hours.
        Rate Limit: 2 requests per second
        Rate limit rule: UserID


        Args:
            ccy: Token symbol. Currently only BTC is supported.
            amt: Deposit amount between 0.000001 - 0.1
            to: Receiving account 6: Funding account 18: Trading account If empty,
                will default to funding account.
            invoice: Invoice text
            cTime: Invoice creation time
        _____________
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

        Retrieve the deposit addresses of currencies, including previously-used addresses.
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
        fromWdId: str = None,
        txId: str = None,
        type_: str = None,
        state: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """

        Retrieve the deposit records according to the currency, deposit status, and time range in reverse chronological order. The 100 most recent records are returned by default.
        Rate Limit: 6 requests per second
        Rate limit rule: UserID


        Args:
            ccy: Currency, e.g. BTC
            depId: Deposit ID
            fromWdId: Internal transfer initiator's withdrawal ID If the deposit comes from
                internal transfer, this field displays the withdrawal ID of the
                internal transfer initiator
            txId: Hash record of the deposit
            type_: Deposit Type 3: internal transfer 4: deposit from chain
            state: Status of deposit 0: waiting for confirmation 1: deposit credited 2:
                deposit successful 8: pending due to temporary deposit suspension on
                this crypto currency 11: match the address blacklist 12: account or
                deposit is frozen 13: sub-account deposit interception 14: KYC limit
            after: Pagination of data to return records earlier than the requested ts,
                Unix timestamp format in milliseconds, e.g. 1654041600000
            before: Pagination of data to return records newer than the requested ts, Unix
                timestamp format in milliseconds, e.g. 1656633600000
            limit: Number of results per request. The maximum is 100; The default is 100
        _____________
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
        areaCode: str = None,
        clientId: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """

        Withdrawal of tokens. Common sub-account does not support withdrawal.
        Rate Limit: 6 requests per second
        Rate limit rule: UserID


        Args:
            ccy: Currency, e.g. USDT
            amt: Withdrawal amount
            dest: Withdrawal method 3: internal 4: on chain
            toAddr: If your dest is 4,toAddr should be a trusted crypto currency address.
                Some crypto currency addresses are formatted as 'address:tag', e.g.
                'ARDOR-7JF3-8F2E-QUWZ-CAN7F:123456' If your dest is 3,toAddr should be
                a recipient address which can be email, phone or login account name.
            fee: Transaction fee
            chain: Chain name There are multiple chains under some currencies, such as
                USDT has USDT-ERC20, USDT-TRC20, and USDT-Omni. If the parameter is
                not filled in, the default will be the main chain. When you withdrawal
                the non-tradable asset, if the parameter is not filled in, the default
                will be the unique withdrawal chain.
            areaCode: Area code for the phone number If toAddr is a phone number, this
                parameter is required.
            clientId: Client-supplied ID A combination of case-sensitive alphanumerics, all
                numbers, or all letters of up to 32 characters.
        _____________
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

        The maximum withdrawal amount is 0.1 BTC per request, and 1 BTC in 24 hours. The minimum withdrawal amount is approximately 0.000001 BTC. Sub-account does not support withdrawal.
        Rate Limit: 2 requests per second
        Rate limit rule: UserID


        Args:
            ccy: Token symbol. Currently only BTC is supported.
            invoice: Invoice text
            memo: Lightning withdrawal memo
        _____________
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

        You can cancel normal withdrawal requests, but you cannot cancel withdrawal requests on Lightning.
        Rate Limit: 6 requests per second
        Rate limit rule: UserID


        Args:
            wdId: Withdrawal ID
        _____________
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
        type_: str = None,
        state: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """

        Retrieve the withdrawal records according to the currency, withdrawal status, and time range in reverse chronological order. The 100 most recent records are returned by default.
        Rate Limit: 6 requests per second
        Rate limit rule: UserID


        Args:
            ccy: Currency, e.g. BTC
            wdId: Withdrawal ID
            clientId: Client-supplied ID A combination of case-sensitive alphanumerics, all
                numbers, or all letters of up to 32 characters.
            txId: Hash record of the deposit
            type_: Withdrawal type 3: internal transfer 4: withdrawal to chain
            state: Status of withdrawal -3：canceling -2：canceled -1：failed 0：waiting
                withdrawal 1：withdrawing 2：withdraw success 7: approved 10: waiting
                transfer 4, 5, 6, 8, 9, 12: waiting mannual review
            after: Pagination of data to return records earlier than the requested ts,
                Unix timestamp format in milliseconds, e.g. 1654041600000
            before: Pagination of data to return records newer than the requested ts, Unix
                timestamp format in milliseconds, e.g. 1656633600000
            limit: Number of results per request. The maximum is 100; The default is 100
        _____________
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

    def get_deposit_withdraw_status(
        self,
        wdId: str = None,
        txId: str = None,
        ccy: str = None,
        to: str = None,
        chain: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """

        Retrieve deposit's and withdrawal's detailed status and estimated complete time.
        Rate Limit: 1 request per 2 seconds
        Rate limit rule: UserID


        Args:
            wdId: Withdrawl ID, use to retrieve withdrawal status Required to input one
                and only one of wdId and txId
            txId: Hash record of the deposit, use to retrieve deposit status Required to
                input one and only one of wdId and txId
            ccy: Currency type, e.g. USDT Required when retrieving deposit status with
                txId
            to: To address, the destination address in deposit Required when
                retrieving deposit status with txId
            chain: Currency chain infomation, e.g. USDT-ERC20 Required when retrieving
                deposit status with txId
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/asset/deposit-withdraw-status",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def small_assets_convert(
        self, ccy: List[str], use_proxy: bool = False
    ) -> APIReturn:
        """

        Convert small assets in funding account to OKB. Only 5 convert is allowed within 24 hours.
        Rate Limit: 1 request per second
        Rate limit rule: UserID


        Args:
            ccy: Small assets needed to be convert, e.g. ["BTC","USDT"]
        _____________
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
