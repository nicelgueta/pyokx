# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails
from typing import *


class RecurringBuy(APIComponent):
    def place_recurring_buy_order(self, stgyName: str, recurringList: List[dict], ccy: str, ratio: str, period: str, recurringDay: str, recurringTime: str, timeZone: str, amt: str, investmentCcy: str, tdMode: str, algoClOrdId: str = None, tag: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            stgyName: Custom name for trading bot, no more than 40 characters
            recurringList: Recurring buy info
            ccy: Recurring currency, e.g. BTC
            ratio: Proportion of recurring currency assets, e.g. "0.2" representing 20%
            period: Period monthly weekly daily
            recurringDay: Recurring buy date When the period is monthly, the value range is an
                integer of [1,28] When the period is weekly, the value range is an
                integer of [1,7] When the period is daily, the value is 1
            recurringTime: Recurring buy time, the value range is an integer of [0,23]
            timeZone: UTC time zone，the value range is an integer of [-12,14] e.g. "8"
                representing UTC+8 (East 8 District), Beijing Time
            amt: Quantity invested per cycle
            investmentCcy: The invested quantity unit, can only be USDT/USDC
            tdMode: Trading mode Margin mode: cross Non-Margin mode: cash
            algoClOrdId: Client-supplied Algo ID There will be a value when algo order
                attaching algoClOrdId is triggered, or it will be "". A combination of
                case-sensitive alphanumerics, all numbers, or all letters of up to 32
                characters.
            tag: Order tag A combination of case-sensitive alphanumerics, all numbers,
                or all letters of up to 16 characters.
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
        

    def amend_recurring_buy_order(self, algoId: str, stgyName: str, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            algoId: Algo ID
            stgyName: New custom name for trading bot after adjustment, no more than 40
                characters
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
        

    def stop_recurring_buy_order(self, body: List[dict] = None, use_proxy: bool = False) -> APIReturn:
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
                }
                ...
            ]
            api_helper = RecurringBuy(client)
            response = api_helper.stop_recurring_buy_order(body=body)
            ```


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
        

    def get_recurring_buy_order_list(self, algoId: str = None, after: str = None, before: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            algoId: Algo ID
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
        

    def get_recurring_buy_order_history(self, algoId: str = None, after: str = None, before: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            algoId: Algo ID
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
        

    def get_recurring_buy_order_details(self, algoId: str, use_proxy: bool = False) -> APIReturn:
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
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_recurring_buy_sub_orders(self, algoId: str, ordId: str = None, after: str = None, before: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        Rate Limit: 20 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            algoId: Algo ID
            ordId: Sub order ID
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
        

