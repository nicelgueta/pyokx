# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails
from typing import *


class CopyTrading(APIComponent):
    def get_existing_leading_positions(self, instId: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        The leading trader gets leading positions that are not closed.
        Returns reverse chronological order with openTime
        Rate limit: 2 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            instId: Instrument ID, e.g. BTC-USDT-SWAP
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/copytrading/current-subpositions",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_leading_position_history(self, instId: str = None, after: str = None, before: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        The leading trader retrieves the completed leading position of the last 3 months.
        Returns reverse chronological order with closeTime. 
        Rate limit: 2 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            instId: Instrument ID, e.g. BTC-USDT-SWAP
            after: Pagination of data to return records earlier than the requested
                subPosId.
            before: Pagination of data to return records newer than the requested
                subPosId.
            limit: Number of results per request. Maximum is 100. Default is 100.
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/copytrading/subpositions-history",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def place_leading_stop_order(self, subPosId: str, tpTriggerPx: str = None, slTriggerPx: str = None, tpTriggerPxType: str = None, slTriggerPxType: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        The leading trader sets TP/SL for the current leading position that are not closed.
        Rate limit: 1 request per 2 seconds
        Rate limit rule: UserID
        

        Args:
            subPosId: Leading position ID
            tpTriggerPx: Take-profit trigger price. Take-profit order price will be the market
                price after triggering. At least one of tpTriggerPx and slTriggerPx
                must be filled
            slTriggerPx: Stop-loss trigger price. Stop-loss order price will be the market
                price after triggering.
            tpTriggerPxType: Take-profit trigger price type last: last price index: index price
                mark: mark price Default is last
            slTriggerPxType: Stop-loss trigger price type last: last price index: index price mark:
                mark price Default is last
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/copytrading/algo-order",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def close_leading_position(self, subPosId: str, use_proxy: bool = False) -> APIReturn:
        """
    
        The leading trader can only close a leading position once a time. 
        It is required to pass subPosId which can get from Get existing leading positions.
        Rate limit: 2 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            subPosId: Leading position ID
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/copytrading/close-subposition",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_leading_instruments(self, use_proxy: bool = False) -> APIReturn:
        """
    
        The leading trader gets contracts that are supported to lead by the platform. 
        Rate limit: 2 requests per 2 seconds
        Rate limit rule: UserID
                _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/copytrading/instruments",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def amend_leading_instruments(self, instId: str, use_proxy: bool = False) -> APIReturn:
        """
    
        The leading trder can amend current leading instruments, need to set initial leading instruments while applying to become a leading trader.
        All non-leading contracts can't have position or pending orders for the current request when setting non-leading contracts as leading contracts.
        Rate limit: 2 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            instId: Instrument ID, e.g. BTC-USDT-SWAP. If there are multiple instruments,
                separate them with commas. Maximum of 31 instruments can be selected.
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/copytrading/set-instruments",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_profit_sharing_details(self, after: str = None, before: str = None, limit: str = None, use_proxy: bool = False) -> APIReturn:
        """
    
        The leading trader gets all profits shared details since joining the platform.
        Rate limit: 2 requests per 2 seconds
        Rate limit rule: UserID
        

        Args:
            after: Pagination of data to return records earlier than the requested
                profitSharingId
            before: Pagination of data to return records newer than the requested
                profitSharingId
            limit: Number of results per request. Maximum is 100. Default is 100.
        _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/copytrading/profit-sharing-details",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_total_profit_sharing(self, use_proxy: bool = False) -> APIReturn:
        """
    
        The leading trader gets the total amount of profit shared since joining the platform.
        Rate limit: 2 requests per 2 seconds
        Rate limit rule: UserID
                _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/copytrading/total-profit-sharing",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

    def get_unrealized_profit_sharing_details(self, use_proxy: bool = False) -> APIReturn:
        """
    
        The leading trader gets the profit sharing details that are expected to be shared in the next settlement cycle.
        The unrealized profit sharing details will update once there copy position is closed.
        Rate limit: 2 requests per 2 seconds
        Rate limit rule: UserID
                _____________
        """

        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/copytrading/unrealized-profit-sharing-details",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
        

