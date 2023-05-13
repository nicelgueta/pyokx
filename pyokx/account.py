# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails
from typing import *


class Account(APIComponent):
    def get_balance(self, ccy: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve a list of assets (with non-zero balance), remaining balance, and available amount in the trading account.
        
        Interest-free quota and discount rates are public data and not displayed on the account interface.
        
        Rate Limit: 10 requests per 2 seconds
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
            request_path="/api/v5/account/balance",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_positions(self, instType: str = None, instId: str = None, posId: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve information on your positions. When the account is in net mode, net positions will be displayed, and when the account is in long/short mode, long or short positions will be displayed. Return in reverse chronological order using ctime.
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            instType: Instrument type MARGIN SWAP FUTURES OPTION instId will be checked
                against instType when both parameters are passed.
            instId: Instrument ID, e.g. BTC-USD-190927-5000-C. Single instrument ID or
                multiple instrument IDs (no more than 10) separated with comma
            posId: Single position ID or multiple position IDs (no more than 20)
                separated with comma. There is attribute expiration, the posId and
                position information will be cleared if it is more than 30 days after
                the last close position.
        _____________
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
        

    def get_positions_history(self, instType: str = None, instId: str = None, mgnMode: str = None, type_: str = None, posId: str = None, after: str = None, before: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the updated position data for the last 3 months. Return in reverse chronological order using utime.
        Rate Limit: 1 request per 10 seconds
        Rate limit rule: UserID
        

        Args:
            instType: Instrument type MARGIN SWAP FUTURES OPTION
            instId: Instrument ID, e.g. BTC-USD-SWAP
            mgnMode: Margin mode cross isolated
            type_: The type of closing position 1：Close position partially;2：Close
                all;3：Liquidation;4：Partial liquidation; 5：ADL; It is the latest type
                if there are several types for the same position.
            posId: Position ID. There is attribute expiration, the posId and position
                information will be cleared if it is more than 30 days after the last
                close position.
            after: Pagination of data to return records earlier than the requested uTime,
                Unix timestamp format in milliseconds, e.g. 1597026383085
            before: Pagination of data to return records newer than the requested uTime,
                Unix timestamp format in milliseconds, e.g. 1597026383085
            limit: Number of results per request. The maximum is 100. The default is 100.
        _____________
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
        

    def get_account_and_position_risk(self, instType: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Get account and position risk
        
        Obtain basic information about accounts and positions on the same time slice
        
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            instType: Instrument type MARGIN SWAP FUTURES OPTION
        _____________
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
        

    def get_bills_details_last_7_days(self, instType: str = None, ccy: str = None, mgnMode: str = None, ctType: str = None, type_: str = None, subType: str = None, after: str = None, before: str = None, begin: str = None, end: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the bills of the account. The bill refers to all transaction records that result in changing the balance of an account. Pagination is supported, and the response is sorted with the most recent first. This endpoint can retrieve data from the last 7 days.
        Rate Limit: 6 requests per second
        Rate limit rule: UserID
        

        Args:
            instType: Instrument type SPOT MARGIN SWAP FUTURES OPTION
            ccy: Bill currency
            mgnMode: Margin mode isolated cross
            ctType: Contract type linear inverse Only applicable to FUTURES/SWAP
            type_: Bill type 1: Transfer 2: Trade 3: Delivery 4: Auto token conversion 5:
                Liquidation 6: Margin transfer 7: Interest deduction 8: Funding fee 9:
                ADL 10: Clawback 11: System token conversion 12: Strategy transfer 13:
                ddh 14: Block trade 15: Quick Margin 18: Profit sharing 22: Repay
            subType: Bill subtype 1: Buy 2: Sell 3: Open long 4: Open short 5: Close long
                6: Close short 9: Interest deduction for Market loans 11: Transfer in
                12: Transfer out 14: Interest deduction for VIP loans 160: Manual
                margin increase 161: Manual margin decrease 162: Auto margin increase
                114: Auto buy 115: Auto sell 118: System token conversion transfer in
                119: System token conversion transfer out 100: Partial liquidation
                close long 101: Partial liquidation close short 102: Partial
                liquidation buy 103: Partial liquidation sell 104: Liquidation long
                105: Liquidation short 106: Liquidation buy 107: Liquidation sell
                108:clawback 110: Liquidation transfer in 111: Liquidation transfer
                out 125: ADL close long 126: ADL close short 127: ADL buy 128: ADL
                sell 131: ddh buy 132: ddh sell 170: Exercised 171: Counterparty
                exercised 172: Expired OTM 112: Delivery long 113: Delivery short 117:
                Delivery/Exercise clawback 173: Funding fee expense 174: Funding fee
                income 200:System transfer in 201: Manually transfer in 202: System
                transfer out 203: Manually transfer out 204: block trade buy 205:
                block trade sell 206: block trade open long 207: block trade open
                short 208: block trade close open 209: block trade close short 210:
                Manual Borrowing 211: Manual Repayment 212: Auto borrow 213: Auto
                repay 16: Repay forcibly 17: Repay interest by borrowing forcibly 224:
                repayment transfer in 225: repayment transfer out 250: Profit sharing
                expenses; 251: Profit sharing refund; 252: Profit sharing income;
            after: Pagination of data to return records earlier than the requested bill
                ID.
            before: Pagination of data to return records newer than the requested bill ID.
            begin: Filter with a begin timestamp. Unix timestamp format in milliseconds,
                e.g. 1597026383085
            end: Filter with an end timestamp. Unix timestamp format in milliseconds,
                e.g. 1597026383085
            limit: Number of results per request. The maximum is 100. The default is 100.
        _____________
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
        

    def get_bills_details_last_3_months(self, instType: str = None, ccy: str = None, mgnMode: str = None, ctType: str = None, type_: str = None, subType: str = None, after: str = None, before: str = None, begin: str = None, end: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the account’s bills. The bill refers to all transaction records that result in changing the balance of an account. Pagination is supported, and the response is sorted with most recent first. This endpoint can retrieve data from the last 3 months.
        Rate Limit: 6 requests per second
        Rate limit rule: UserID
        

        Args:
            instType: Instrument type SPOT MARGIN SWAP FUTURES OPTION
            ccy: Bill currency
            mgnMode: Margin mode isolated cross
            ctType: Contract type linear inverse Only applicable to FUTURES/SWAP
            type_: Bill type 1: Transfer 2: Trade 3: Delivery 4: Auto token conversion 5:
                Liquidation 6: Margin transfer 7: Interest deduction 8: Funding fee 9:
                ADL 10: Clawback 11: System token conversion 12: Strategy transfer 13:
                ddh 14: Block trade 15: Quick Margin 18: Profit sharing 22: Repay
            subType: Bill subtype 1: Buy 2: Sell 3: Open long 4: Open short 5: Close long
                6: Close short 9: Interest deduction for Market loans 11: Transfer in
                12: Transfer out 14: Interest deduction for VIP loans 160: Manual
                margin increase 161: Manual margin decrease 162: Auto margin increase
                114: Auto buy 115: Auto sell 118: System token conversion transfer in
                119: System token conversion transfer out 100: Partial liquidation
                close long 101: Partial liquidation close short 102: Partial
                liquidation buy 103: Partial liquidation sell 104: Liquidation long
                105: Liquidation short 106: Liquidation buy 107: Liquidation sell
                108:clawback 110: Liquidation transfer in 111: Liquidation transfer
                out 125: ADL close long 126: ADL close short 127: ADL buy 128: ADL
                sell 131: ddh buy 132: ddh sell 170: Exercised 171: Counterparty
                exercised 172: Expired OTM 112: Delivery long 113: Delivery short 117:
                Delivery/Exercise clawback 173: Funding fee expense 174: Funding fee
                income 200:System transfer in 201: Manually transfer in 202: System
                transfer out 203: Manually transfer out 204: block trade buy 205:
                block trade sell 206: block trade open long 207: block trade open
                short 208: block trade close open 209: block trade close short 210:
                Manual Borrowing 211: Manual Repayment 212: Auto borrow 213: Auto
                repay 16: Repay forcibly 17: Repay interest by borrowing forcibly 224:
                repayment transfer in 225: repayment transfer out 250: Profit sharing
                expenses; 251: Profit sharing refund; 252: Profit sharing income;
            after: Pagination of data to return records earlier than the requested bill
                ID.
            before: Pagination of data to return records newer than the requested bill ID.
            begin: Filter with a begin timestamp. Unix timestamp format in milliseconds,
                e.g. 1597026383085
            end: Filter with an end timestamp. Unix timestamp format in milliseconds,
                e.g. 1597026383085
            limit: Number of results per request. The maximum is 100. The default is 100.
        _____________
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
    
        Retrieve current account configuration.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
                _____________
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
    
        Single-currency mode and Multi-currency mode: FUTURES and SWAP support both long/short mode and net mode. In net mode, users can only have positions in one direction; In long/short mode, users can hold positions in long and short directions.
        Portfolio margin mode: FUTURES and SWAP only support net mode
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            posMode: Position mode long_short_mode: long/short, only applicable to
                FUTURES/SWAP net_mode: net
        _____________
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
        

    def set_leverage(self, lever: str, mgnMode: str, instId: str = None, ccy: str = None, posSide: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
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
        Please refer to the request examples on the right for each case.
        Rate limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            lever: Leverage
            mgnMode: Margin mode isolated cross  Can only be cross if ccy is passed.
            instId: Instrument ID Either instId or ccy is required; if both are passed,
                instId will be used by default.
            ccy: Currency used for margin Only applicable to cross MARGIN of Multi-
                currency margin  Required when setting the leverage for automatically
                borrowing coin.
            posSide: Position side long short  Only required when margin mode is isolated
                in long/short mode for FUTURES/SWAP.
        _____________
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
        

    def get_maximum_buy_sell_amount_or_open_amount(self, instId: str, tdMode: str, ccy: str = None, px: str = None, leverage: str = None, unSpotOffset: bool = None, use_proxy: bool = False) -> APIReturn:
        """
    
        
        Under the Portfolio Margin account, the cross mode of derivatives does not support the calculation of the maximum buy/sell amount or open amount.
        
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            instId: Single instrument or multiple instruments (no more than 5) separated
                with comma, e.g. BTC-USDT,ETH-USDT
            tdMode: Trade mode cross isolated cash
            ccy: Currency used for margin Only applicable to MARGIN of Single-currency
                margin.
            px: Price When the price is not specified, it will be calculated according
                to the last traded price. The parameter will be ignored when multiple
                instruments are specified.
            leverage: Leverage for instrument The default is current leverage Only
                applicable to MARGIN/FUTURES/SWAP
            unSpotOffset: true: disable Spot-Derivatives risk offset, false: enable Spot-
                Derivatives risk offset Default is false Applicable to `Portfolio It
                is effective when Spot-Derivatives risk offset is turned on, otherwise
                this parameter is ignored.
        _____________
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
        

    def get_maximum_available_tradable_amount(self, instId: str, tdMode: str, ccy: str = None, reduceOnly: bool = None, unSpotOffset: bool = None, quickMgnType: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            instId: Single instrument or multiple instruments (no more than 5) separated
                with comma, e.g. BTC-USDT,ETH-USDT
            tdMode: Trade mode cross isolated cash
            ccy: Currency used for margin Only applicable to cross MARGIN of Single-
                currency margin.
            reduceOnly: Whether to reduce position only Only applicable to MARGIN
            unSpotOffset: true: disable Spot-Derivatives risk offset, false: enable Spot-
                Derivatives risk offset Default is false Only applicable to Portfolio
                margin It is effective when Spot-Derivatives risk offset is turned on,
                otherwise this parameter is ignored.
            quickMgnType: Quick Margin type. Only applicable to Quick Margin Mode of isolated
                margin manual, auto_borrow, auto_repay The default value is manual
        _____________
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
        

    def increase_decrease_margin(self, instId: str, posSide: str, type_: str, amt: str, ccy: str = None, auto: bool = None, loanTrans: bool = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Increase or decrease the margin of the isolated position. Margin reduction may result in the change of the actual leverage.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            instId: Instrument ID
            posSide: Position side, the default is net long short net
            type_: add: add margin, or transfer collaterals in (Quick Margin Mode)
                reduce: reduce margin, transfer collaterals out (Quick Margin Mode)
            amt: Amount to be increased or decreased.
            ccy: Currency, only applicable to MARGIN（Manual transfers and Quick Margin
                Mode）
            auto: Automatic loan transfer out, true or false, the default is false only
                applicable to MARGIN（Manual transfers）
            loanTrans: Whether or not borrowed coins can be transferred out under Multi-
                currency margin and Portfolio margin the default is false
        _____________
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
        

    def get_leverage(self, instId: str, mgnMode: str, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            instId: Instrument ID Single instrument ID or multiple instrument IDs (no more
                than 20) separated with comma
            mgnMode: Margin mode cross isolated
        _____________
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
        

    def get_the_maximum_loan_of_instrument(self, instId: str, mgnMode: str, mgnCcy: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            instId: Single instrument or multiple instruments (no more than 5) separated
                with comma, e.g. BTC-USDT,ETH-USDT
            mgnMode: Margin mode isolated cross
            mgnCcy: Margin currency Only applicable to cross MARGIN in Single-currency
                margin
        _____________
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
        

    def get_fee_rates(self, instType: str, instId: str = None, uly: str = None, instFamily: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            instType: Instrument type SPOT MARGIN SWAP FUTURES OPTION
            instId: Instrument ID, e.g. BTC-USDT Applicable to SPOT/MARGIN
            uly: Underlying, e.g. BTC-USD Applicable to FUTURES/SWAP/OPTION
            instFamily: Instrument family, e.g. BTC-USD Applicable to FUTURES/SWAP/OPTION
        _____________
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
        

    def get_interest_accrued_data(self, type_: str = None, ccy: str = None, instId: str = None, mgnMode: str = None, after: str = None, before: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            type_: Loan type 1: VIP loans 2: Market loans Default is Market loans
            ccy: Loan currency, e.g. BTC Only applicable to Market loans Only
                applicable toMARGIN
            instId: Instrument ID, e.g. BTC-USDT Only applicable to Market loans
            mgnMode: Margin mode cross isolated Only applicable to Market loans
            after: Pagination of data to return records earlier than the requested
                timestamp, Unix timestamp format in milliseconds, e.g. 1597026383085
            before: Pagination of data to return records newer than the requested, Unix
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
            request_path="/api/v5/account/interest-accrued",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_interest_rate(self, ccy: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Get the user's current leveraged currency borrowing interest rate
        Rate Limit: 5 requests per 2 seconds
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
            request_path="/api/v5/account/interest-rate",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def set_greeks_pa_bs(self, greeksType: str, use_proxy: bool = False) -> APIReturn:
        """
    
        Set the display type of Greeks.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            greeksType: Display type of Greeks. PA: Greeks in coins BS: Black-Scholes Greeks
                in dollars
        _____________
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
        

    def isolated_margin_trading_settings(self, isoMode: str, type_: str, use_proxy: bool = False) -> APIReturn:
        """
    
        You can set the currency margin and futures/perpetual Isolated margin trading mode
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            isoMode: Isolated margin trading settings automatic:Auto transfers
                autonomy:Manual transfers quick_margin:Quick Margin Mode
            type_: Instrument type MARGIN CONTRACTS
        _____________
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
        

    def get_maximum_withdrawals(self, ccy: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the maximum transferable amount from trading account to funding account. If no currency is specified, the transferable amount of all owned currencies will be returned.
        Rate Limit: 20 requests per 2 seconds
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
            request_path="/api/v5/account/max-withdrawal",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_account_risk_state(self, atRisk: str = None, atRiskIdx: list = None, atRiskMgn: list = None, ts: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Only applicable to Portfolio margin account
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            atRisk: Account risk status in auto-borrow mode true： the account is currently
                in a specific risk state false： the account is currently not in a
                specific risk state
            atRiskIdx: derivatives risk unit list
            atRiskMgn: margin risk unit list
            ts: Unix timestamp format in milliseconds, e.g.1597026383085
        _____________
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
        

    def manual_borrow_and_repay_in_quick_margin_mode(self, instId: str, ccy: str, side: str, amt: str, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            instId: Instrument ID, e.g. BTC-USDT
            ccy: Loan currency, e.g. BTC
            side: borrow repay
            amt: borrow/repay amount
        _____________
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
        

    def get_borrow_and_repay_history_in_quick_margin_mode(self, instId: str = None, ccy: str = None, side: str = None, after: str = None, before: str = None, begin: str = None, end: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            instId: Instrument ID, e.g. BTC-USDT
            ccy: Loan currency, e.g. BTC
            side: borrow repay
            after: Pagination of data to return records earlier than the requested refId
            before: Pagination of data to return records newer than the requested refId
            begin: Filter with a begin timestamp. Unix timestamp format in milliseconds,
                e.g. 1597026383085
            end: Filter with an end timestamp. Unix timestamp format in milliseconds,
                e.g. 1597026383085
            limit: Number of results per request. The maximum is 100; The default is 100
        _____________
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
        

    def vip_loans_borrow_and_repay(self, ccy: str, side: str, amt: str, ordId: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Maximum number of borrowing orders for a single currency is 20
        Rate Limit: 6 requests per second
        Rate limit rule: UserID
        

        Args:
            ccy: Loan currency, e.g. BTC
            side: borrow repay
            amt: borrow/repay amount
            ordId: Order ID of borrowing, it is necessary while repaying
        _____________
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
        

    def get_borrow_and_repay_history_for_vip_loans(self, ccy: str = None, after: str = None, before: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            ccy: Loan currency, e.g. BTC
            after: Pagination of data to return records earlier than the requested
                timestamp, Unix timestamp format in milliseconds, e.g. 1597026383085
            before: Pagination of data to return records newer than the requested, Unix
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
            request_path="/api/v5/account/borrow-repay-history",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_vip_interest_accrued_data(self, ccy: str = None, ordId: str = None, after: str = None, before: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            ccy: Loan currency, e.g. BTC Only applicable toMARGIN
            ordId: Order ID of borrowing
            after: Pagination of data to return records earlier than the requested
                timestamp, Unix timestamp format in milliseconds, e.g. 1597026383085
            before: Pagination of data to return records newer than the requested, Unix
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
            request_path="/api/v5/account/vip-interest-accrued",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_vip_interest_deducted_data(self, ccy: str = None, ordId: str = None, after: str = None, before: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            ccy: Loan currency, e.g. BTC Only applicable toMARGIN
            ordId: Order ID of borrowing
            after: Pagination of data to return records earlier than the requested
                timestamp, Unix timestamp format in milliseconds, e.g. 1597026383085
            before: Pagination of data to return records newer than the requested, Unix
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
            request_path="/api/v5/account/vip-interest-deducted",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_vip_loan_order_list(self, ordId: str = None, state: str = None, ccy: str = None, after: str = None, before: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            ordId: Order ID of borrowing
            state: State 1:Borrowing 2:Borrowed 3:Repaying 4:Repaid 5:Borrow failed
            ccy: Loan currency, e.g. BTC
            after: Pagination of data to return records earlier than the requested ordId
            before: Pagination of data to return records newer than the requested ordId
            limit: Number of results per request. The maximum is 100; The default is 100
        _____________
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
        

    def get_vip_loan_order_detail(self, ordId: str, ccy: str = None, after: str = None, before: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            ordId: Order ID of loan
            ccy: Loan currency, e.g. BTC
            after: Pagination of data to return records earlier than the requested
                timestamp, Unix timestamp format in milliseconds, e.g. 1597026383085
            before: Pagination of data to return records newer than the requested
                timestamp, Unix timestamp format in milliseconds, e.g. 1597026383085
            limit: Number of results per request. The maximum is 100; The default is 100
        _____________
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
        

    def get_borrow_interest_and_limit(self, type_: str = None, ccy: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            type_: Loan type 1: VIP loans 2: Market loans Default is Market loans
            ccy: Loan currency, e.g. BTC
        _____________
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
        

    def position_builder(self, instType: str = None, inclRealPos: bool = None, spotOffsetType: str = None, simPos: list = None, instId: str = None, pos: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Calculates portfolio margin information for simulated position or current position of the user.
        You can add up to 200 simulated positions in one request.
        Rate Limit: 2 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            instType: Instrument type SWAP FUTURES OPTION
            inclRealPos: Whether import existing positions true：Import existing positions and
                hedge with simulated ones false：Only use simulated positions The
                default is true
            spotOffsetType: Spot-derivatives risk offset mode 1: Spot-derivatives (USDT) 2: Spot-
                derivatives (crypto) 3: Derivatives-only The default is 3
            simPos: List of positions
            instId: Instrument ID
            pos: Quantity of positions
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/simulated",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_greeks(self, ccy: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve a greeks list of all assets in the account.
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            ccy: Single currency, e.g. BTC.
        _____________
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
        

    def get_pm_position_limitation(self, instType: str, uly: str = None, instFamily: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve cross position limitation of SWAP/FUTURES/OPTION under Portfolio margin mode.
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            instType: Instrument type SWAP FUTURES OPTION
            uly: Single underlying or multiple underlyings (no more than 3) separated
                with comma. Either uly or instFamily is required. If both are passed,
                instFamily will be used.
            instFamily: Single instrument family or instrument families (no more than 5)
                separated with comma. Either uly or instFamily is required. If both
                are passed, instFamily will be used.
        _____________
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
        

    def set_risk_offset_type(self, type_: str, use_proxy: bool = False) -> APIReturn:
        """
    
        Configure the risk offset type in portfolio margin mode.
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            type_: Risk offset type 1: Spot-derivatives (USDT) risk offset 2: Spot-
                derivatives (Crypto) risk offset 3:Derivatives only mode
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/set-risk",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def activate_option(self, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
                _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/activate-option",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def set_auto_loan(self, autoLoan: bool = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Only applicalbe to Multi-currency margin and Portfolio margin
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            autoLoan: Whether to automatically make loans Valid values are true, false The
                default is true
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/account/set-auto-loan",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

