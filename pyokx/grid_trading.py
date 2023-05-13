# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails
from typing import *


class GridTrading(APIComponent):
    def place_grid_algo_order(self, instId: str, algoOrdType: str, maxPx: str, minPx: str, gridNum: str, triggerAction: str, triggerStrategy: str, runType: str = None, tpTriggerPx: str = None, slTriggerPx: str = None, tag: str = None, algoClOrdId: str = None, triggerParams: List[dict] = None, delaySeconds: str = None, timeframe: str = None, thold: str = None, triggerCond: str = None, timePeriod: str = None, triggerPx: str = None, stopType: str = None, quoteSz: str = None, baseSz: str = None, sz: str = None, direction: str = None, lever: str = None, basePos: bool = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID + Instrument ID
        

        Args:
            instId: Instrument ID, e.g. BTC-USDT-SWAP
            algoOrdType: Algo order type grid: Spot grid contract_grid: Contract grid
                moon_grid: Moon grid
            maxPx: Upper price of price range
            minPx: Lower price of price range
            gridNum: Grid quantity
            triggerAction: Trigger action start stop
            triggerStrategy: Trigger strategy instant price rsi
            runType: Grid type 1: Arithmetic, 2: Geometric Default is Arithmetic moon_grid
                only support 2
            tpTriggerPx: TP tigger price Applicable to Spot grid/Contract grid
            slTriggerPx: SL tigger price Applicable to Spot grid/Contract grid
            tag: Order tag
            algoClOrdId: Client-supplied Algo ID A combination of case-sensitive alphanumerics,
                all numbers, or all letters of up to 32 characters.
            triggerParams: Trigger Parameters
            delaySeconds: Delay seconds after action triggered
            timeframe: K-line type 3m, 5m, 15m, 30m (m: minute) 1H, 4H (H: hour) 1D (D: day)
                This field is only valid when triggerStrategy is rsi
            thold: Threshold The value should be an integer between 1 to 100 This field
                is only valid when triggerStrategy is rsi
            triggerCond: Trigger condition cross_up cross_down above below cross This field is
                only valid when triggerStrategy is rsi
            timePeriod: Time Period 14 This field is only valid when triggerStrategy is rsi
            triggerPx: Trigger Price This field is only valid when triggerStrategy is price
            stopType: Stop type Spot grid 1: Sell base currency 2: Keep base currency
                Contract grid 1: Market Close All positions 2: Keep positions This
                field is only valid when triggerAction is stop
            quoteSz: Invest amount for quote currency Either quoteSz or baseSz is required
            baseSz: Invest amount for base currency Either quoteSz or baseSz is required
            sz: Used margin based on USDT
            direction: Contract grid type long,short,neutral
            lever: Leverage
            basePos: Whether or not open a position when the strategy activates Default is
                false Neutral contract grid should omit the parameter
            quoteSz: Invest amount for quote currency
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trading",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def amend_grid_algo_order(self, algoId: str, instId: str, triggerAction: str, triggerStrategy: str, slTriggerPx: str = None, tpTriggerPx: str = None, triggerParams: List[dict] = None, triggerPx: str = None, stopType: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Supported contract grid algo order amendment.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            algoId: Algo ID
            instId: Instrument ID, e.g. BTC-USDT-SWAP
            triggerAction: Trigger action start stop
            triggerStrategy: Trigger strategy instant price rsi
            slTriggerPx: New stop-loss trigger price if slTriggerPx is set "" means stop-loss
                trigger price is canceled. Either slTriggerPx or tpTriggerPx is
                required.
            tpTriggerPx: New take-profit trigger price if tpTriggerPx is set "" means take-
                profit trigger price is canceled.
            triggerParams: Trigger Parameters
            triggerPx: Trigger Price This field is only valid when triggerStrategy is price
            stopType: Stop type Spot grid 1: Sell base currency 2: Keep base currency
                Contract grid 1: Market Close All positions 2: Keep positions This
                field is only valid when triggerAction is stop
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trading",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def stop_grid_algo_order(self, body: List[dict] = None, use_proxy: bool = False) -> APIReturn:
        """
    
        A maximum of 10 orders can be stopped per request.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        

        Request format:
            This function body should be formatted as an array. Eg.
            ```python
            ...
            body = [
                {
                    "algoId": str
                    "instId": str
                    "algoOrdType": str
                    "stopType": str
                }
                ...
            ]
            api_helper = GridTrading(client)
            response = api_helper.stop_grid_algo_order(body=body)
            ```


        Args:
            algoId: Algo ID
            instId: Instrument ID, e.g. BTC-USDT
            algoOrdType: Algo order type grid: Spot grid contract_grid: Contract grid
                moon_grid: Moon grid
            stopType: Stop type Spot grid/Moon grid 1: Sell base currency 2: Keep base
                currency Contract grid 1: Market Close All positions 2: Keep positions
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trading",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def close_position_for_contract_grid(self, algoId: str, mktClose: bool, sz: str = None, px: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Close position when the contract grid stop type is 'keep position'.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            algoId: Algo ID
            mktClose: Market close all the positions or not
            sz: Close position amount, with unit of contract If mktClose is false, the
                parameter is required.
            px: Close position price If mktClose is false, the parameter is required.
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trading",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def cancel_close_position_order_for_contract_grid(self, algoId: str, ordId: str, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            algoId: Algo ID
            ordId: Close position order ID
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trading",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def instant_trigger_grid_algo_order(self, algoId: str, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID + Instrument ID
        

        Args:
            algoId: Algo ID
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trading",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_grid_algo_order_list(self, algoOrdType: str, algoId: str = None, instId: str = None, instType: str = None, after: str = None, before: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            algoOrdType: Algo order type grid: Spot grid contract_grid: Contract grid
                moon_grid: Moon grid
            algoId: Algo ID
            instId: Instrument ID, e.g. BTC-USDT
            instType: Instrument type SPOT MARGIN FUTURES SWAP
            after: Pagination of data to return records earlier than the requested
                algoId.
            before: Pagination of data to return records newer than the requested algoId.
            limit: Number of results per request. The maximum is 100; The default is 100
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trading",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_grid_algo_order_history(self, algoOrdType: str, algoId: str = None, instId: str = None, instType: str = None, after: str = None, before: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            algoOrdType: Algo order type grid: Spot grid contract_grid: Contract grid
                moon_grid: Moon grid
            algoId: Algo ID
            instId: Instrument ID, e.g. BTC-USDT
            instType: Instrument type SPOT MARGIN FUTURES SWAP
            after: Pagination of data to return records earlier than the requested
                algoId.
            before: Pagination of data to return records newer than the requested algoId.
            limit: Number of results per request. The maximum is 100; The default is 100
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trading",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_grid_algo_order_details(self, algoOrdType: str, algoId: str, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            algoOrdType: Algo order type grid: Spot grid contract_grid: Contract grid
                moon_grid: Moon grid
            algoId: Algo ID
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trading",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_grid_algo_sub_orders(self, algoOrdType: str, algoId: str, type_: str, groupId: str = None, after: str = None, before: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            algoOrdType: Algo order type grid: Spot grid contract_grid: Contract grid
                moon_grid: Moon grid
            algoId: Algo ID
            type_: Sub order state live filled
            groupId: Group ID
            after: Pagination of data to return records earlier than the requested
                algoId.
            before: Pagination of data to return records newer than the requested algoId.
            limit: Number of results per request. The maximum is 100; The default is 100
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trading",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_grid_algo_order_positions(self, algoOrdType: str, algoId: str, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            algoOrdType: Algo order type contract_grid: contract grid
            algoId: Algo ID
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trading",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def spot_moon_grid_withdraw_income(self, algoId: str, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            algoId: Algo ID
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trading",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def compute_margin_balance(self, algoId: str, type_: str, amt: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            algoId: Algo ID
            type_: Adjust margin balance type add reduce
            amt: Adjust margin balance amount Default is zero.
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trading",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def adjust_margin_balance(self, algoId: str, type_: str, amt: str = None, percent: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            algoId: Algo ID
            type_: Adjust margin balance type add reduce
            amt: Adjust margin balance amount Either amt or percent is required.
            percent: Adjust margin balance percentage
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trading",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_grid_ai_parameter_public(self, algoOrdType: str, instId: str, direction: str = None, duration: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Authentication is not required for this public endpoint.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            algoOrdType: Algo order type grid: Spot grid contract_grid: Contract grid
                moon_grid: Moon grid
            instId: Instrument ID, e.g. BTC-USDT
            direction: Contract grid type long,short,neutral Required in the case of
                contract_grid
            duration: Back testing duration 7D: 7 Days, 30D: 30 Days, 180D: 180 Days The
                default is 7D for Spot grid,180D for Moon grid Only 7D is available
                for Contract grid
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trading",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def compute_min_investment_public(self, instId: str, algoOrdType: str, maxPx: str, minPx: str, gridNum: str, runType: str, amt: str, ccy: str, direction: str = None, lever: str = None, basePos: bool = None, investmentData: List[dict] = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Authentication is not required for this public endpoint.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instId: Instrument ID, e.g. BTC-USDT-SWAP
            algoOrdType: Algo order type grid: Spot grid contract_grid: Contract grid
            maxPx: Upper price of price range
            minPx: Lower price of price range
            gridNum: Grid quantity
            runType: Grid type 1: Arithmetic, 2: Geometric
            amt: Invest amount
            ccy: Invest currency
            direction: Contract grid type long,short,neutral Only applicable to contract grid
            lever: Leverage Only applicable to contract grid
            basePos: Whether or not open a position when the strategy activates Default is
                false Neutral contract grid should omit the parameter Only applicable
                to contract grid
            investmentData: Invest Data
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trading",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def rsi_back_testing_public(self, instId: str, timeframe: str, thold: str, timePeriod: str, triggerCond: str = None, duration: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Authentication is not required for this public endpoint.
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: IP
        

        Args:
            instId: Instrument ID, e.g. BTC-USDT Only applicable to SPOT
            timeframe: K-line type 3m, 5m, 15m, 30m (m: minute) 1H, 4H (H: hour) 1D (D: day)
                This field is only valid when triggerStrategy is rsi
            thold: Threshold The value should be an integer between 1 to 100
            timePeriod: Time Period 14
            triggerCond: Trigger condition cross_up cross_down above below cross Default is
                cross_down
            duration: Back testing duration 1M (M: month) Default is 1M
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/trading",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

