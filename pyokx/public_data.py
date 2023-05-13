# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails
from typing import *


class PublicData(APIComponent):
    def get_instruments(self, instType: str, uly: str = None, instFamily: str = None, instId: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve a list of instruments with open contracts.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP + instrumentType
        

        Args:
            instType: Instrument type SPOT MARGIN SWAP FUTURES OPTION
            uly: Underlying Only applicable to FUTURES/SWAP/OPTION.If instType is
                OPTION, either uly or instFamily is required.
            instFamily: Instrument family Only applicable to FUTURES/SWAP/OPTION. If instType
                is OPTION, either uly or instFamily is required.
            instId: Instrument ID
        _____________
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
        

    def get_delivery_exercise_history(self, instType: str, uly: str = None, instFamily: str = None, after: str = None, before: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve delivery records of Futures and exercise records of Options in the last 3 months.
        Rate Limit: 40 requests per 2 seconds
        Rate limit rule: IP + (instrumentType + uly)
        

        Args:
            instType: Instrument type  FUTURES OPTION
            uly: Underlying, only applicable to FUTURES/OPTION Either uly or instFamily
                is required. If both are passed, instFamily will be used.
            instFamily: Instrument family, only applicable to FUTURES/OPTION Either uly or
                instFamily is required. If both are passed, instFamily will be used.
            after: Pagination of data to return records earlier than the requested ts
            before: Pagination of data to return records newer than the requested ts
            limit: Number of results per request. The maximum is 100; The default is 100
        _____________
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
        

    def get_open_interest(self, instType: str, uly: str = None, instFamily: str = None, instId: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the total open interest for contracts on OKX.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP +instrumentID
        

        Args:
            instType: Instrument type SWAP FUTURES OPTION
            uly: Underlying Applicable to FUTURES/SWAP/OPTION. If instType is OPTION,
                either uly or instFamily is required.
            instFamily: Instrument family Applicable to FUTURES/SWAP/OPTION If instType is
                OPTION, either uly or instFamily is required.
            instId: Instrument ID, e.g. BTC-USD-180216 Applicable to FUTURES/SWAP/OPTION
        _____________
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
    
        Retrieve funding rate.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP +instrumentID
        

        Args:
            instId: Instrument ID, e.g. BTC-USD-SWAP only applicable to SWAP
        _____________
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
        

    def get_funding_rate_history(self, instId: str, before: str = None, after: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve funding rate history. This endpoint can retrieve data from the last 3 months.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP +instrumentID
        

        Args:
            instId: Instrument ID, e.g. BTC-USD-SWAP only applicable to SWAP
            before: Pagination of data to return records newer than the requested
                fundingTime
            after: Pagination of data to return records earlier than the requested
                fundingTime
            limit: Number of results per request. The maximum is 100; The default is 100
        _____________
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
    
        Retrieve the highest buy limit and lowest sell limit of the instrument.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instId: Instrument ID, e.g. BTC-USDT-SWAP only applicable to
                FUTURES/SWAP/OPTION
        _____________
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
        

    def get_option_market_data(self, uly: str = None, instFamily: str = None, expTime: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve option market data.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP +uly
        

        Args:
            uly: Underlying, only applicable to OPTION Either uly or instFamily is
                required. If both are passed, instFamily will be used.
            instFamily: Instrument family, only applicable to OPTION Either uly or instFamily
                is required. If both are passed, instFamily will be used.
            expTime: Contract expiry date, the format is "YYMMDD", e.g. "200527"
        _____________
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
        

    def get_estimated_delivery_exercise_price(self, instId: str, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve the estimated delivery price which will only have a return value one hour before the delivery/exercise.
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: IP +instId
        

        Args:
            instId: Instrument ID, e.g. BTC-USD-200214 only applicable to FUTURES/OPTION
        _____________
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
        

    def get_discount_rate_and_interest_free_quota(self, ccy: str = None, discountLv: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve discount rate level and interest-free quota.
        Rate Limit: 2 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            ccy: Currency
            discountLv: Discount level 1:level 1 2:level 2 3:level 3 4:level 4 5:level 5
        _____________
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
        

    def get_system_time(self, ts: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve API server time.
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            ts: System time, Unix timestamp format in milliseconds, e.g. 1597026383085
        _____________
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
        

    def get_mark_price(self, instType: str, uly: str = None, instFamily: str = None, instId: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve mark price.
        We set the mark price based on the SPOT index and at a reasonable basis to prevent individual users from manipulating the market and causing the contract price to fluctuate.
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: IP +instrumentID
        

        Args:
            instType: Instrument type  MARGIN  SWAP FUTURES  OPTION
            uly: Underlying Applicable to FUTURES/SWAP/OPTION
            instFamily: Instrument family Applicable to FUTURES/SWAP/OPTION
            instId: Instrument ID, e.g. BTC-USD-SWAP
        _____________
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
        

    def get_position_tiers(self, instType: str, tdMode: str, uly: str = None, instFamily: str = None, instId: str = None, ccy: str = None, tier: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve position tiers information, maximum leverage depends on your borrowings and margin ratio.
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instType: Instrument type MARGIN SWAP FUTURES OPTION
            tdMode: Trade mode Margin mode cross isolated
            uly: Single underlying or multiple underlyings (no more than 3) separated
                with comma. If instType is SWAP/FUTURES/OPTION, either uly or
                instFamily is required. If both are passed, instFamily will be used.
            instFamily: Single instrument familiy or multiple instrument families (no more
                than 5) separated with comma. If instType is SWAP/FUTURES/OPTION,
                either uly or instFamily is required. If both are passed, instFamily
                will be used.
            instId: Single instrument or multiple instruments (no more than 5) separated
                with comma. Either instId or ccy is required, if both are passed,
                instId will be used, ignore when instType is one of
                SWAP,FUTURES,OPTION
            ccy: Margin currency Only applicable to cross MARGIN. It will return
                borrowing amount for Multi-currency margin and Portfolio margin when
                ccy takes effect.
            tier: Tiers
        _____________
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
        

    def get_interest_rate_and_loan_quota(self, basic: list = None, ccy: str = None, rate: str = None, quota: str = None, vip: list = None, level: str = None, loanQuotaCoef: str = None, irDiscount: str = None, regular: list = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Retrieve interest rate
        Rate Limit: 2 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            basic: Basic interest rate
            ccy: Currency
            rate: Daily rate
            quota: Max borrow
            vip: Interest info for vip users
            level: VIP Level, e.g. VIP1
            loanQuotaCoef: Loan quota coefficient
            irDiscount: Interest rate discount
            regular: Interest info for regular users
            level: Regular user Level, e.g. Lv1
            loanQuotaCoef: Loan quota coefficient
            irDiscount: Interest rate discount
        _____________
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
        

    def get_interest_rate_and_loan_quota_for_vip_loans(self, ccy: str = None, rate: str = None, quota: str = None, levelList: list = None, level: str = None, loanQuota: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 2 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            ccy: Currency, e.g. BTC
            rate: Daily rate
            quota: Max borrow
            levelList: Loan quota information under different VIP levels
            level: VIP Level, e.g. VIP5
            loanQuota: Loan quota
        _____________
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
    
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instType: Instrument type  SWAP FUTURES  OPTION
        _____________
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
        

    def get_insurance_fund(self, instType: str, type_: str = None, uly: str = None, instFamily: str = None, ccy: str = None, before: str = None, after: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Get insurance fund balance information
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instType: Instrument type  MARGIN SWAP FUTURES  OPTION
            type_: Type liquidation_balance_deposit bankruptcy_loss platform_revenue The
                default is all type
            uly: Underlying Required for FUTURES/SWAP/OPTION Either uly or instFamily
                is required. If both are passed, instFamily will be used.
            instFamily: Instrument family Required for FUTURES/SWAP/OPTION Either uly or
                instFamily is required. If both are passed, instFamily will be used.
            ccy: Currency, only applicable to MARGIN
            before: Pagination of data to return records newer than the requested ts
            after: Pagination of data to return records earlier than the requested ts
            limit: Number of results per request. The maximum is 100; The default is 100
        _____________
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
        

    def unit_convert(self, instId: str, sz: str, type_: str = None, px: str = None, unit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Convert the crypto value to the number of contracts, or vice versa
        Rate Limit: 10 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instId: Instrument ID, only applicable to FUTURES/SWAP/OPTION
            sz: Quantity to buy or sell It is quantity of currency while converting
                currency to contract; It is quantity of contract while contract to
                currency. Quantity of coin needs to be positive integer
            type_: Convert type  1: Convert currency to contract. It will be rounded up
                when the value of contract is decimal 2: Convert contract to currency
                The defautl is 1
            px: Order price For crypto-margined contracts, it is necessary while
                converting; For USDT-margined contracts, it is necessary while
                converting between usdt and contract, it is optional while converting
                between coin and contract. For OPTION, it is optional.
            unit: The unit of currency. coin usds: usdt or usdc, only applicable to
                USDⓈ-margined contracts from FUTURES/SWAP
        _____________
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
        

    def get_option_trades(self, instId: str = None, instFamily: str = None, optType: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        The maximum is 100.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instId: Instrument ID, e.g. BTC-USD-221230-4000-C, Either instId or instFamily
                is required. If both are passed, instId will be used.
            instFamily: Instrument family, e.g. BTC-USD
            optType: Option type, C: Call P: put
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/public/option-trades",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_option_tickbands(self, instType: str, instFamily: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Get option tickBands information
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instType: Instrument type OPTION
            instFamily: Instrument family Only applicable to OPTION
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/public/instrument-tick-bands",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

