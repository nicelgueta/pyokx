# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails
from typing import *


class Blocktrading(APIComponent):
    def get_counterparties(self, use_proxy: bool = False) -> APIReturn:
        """
        Get Counterparties
        Retrieves the list of counterparties that the user is permitted to trade with.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rfq/counterparties",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def create_rfq(
        self,
        counterparties: List[str],
        legs: List[dict],
        instId: str,
        sz: str,
        side: str,
        anonymous: bool = None,
        clRfqId: str = None,
        tgtCcy: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
                        Create RFQ
                        Creates a new RFQ


        Please select trading bot "WAGMI" as the counterparty when submitting RFQs in demo trading.
        Prices provided on RFQs by the trading bot are for reference only.

                        To learn more, please visit FAQ > Demo Trading
                        Rate Limit: 5 requests per 2 seconds
                        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rfq/create-rfq",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def cancel_rfq(
        self, rfqId: str = None, clRfqId: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Cancel RFQ
        Cancel an existing active RFQ that you has previously created.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rfq/cancel-rfq",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def cancel_multiple_rfqs(
        self,
        rfqIds: List[str] = None,
        clRfqIds: List[str] = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Cancel multiple RFQs
        Cancel one or multiple active RFQ(s) in a single batch. Maximum 100 RFQ orders can be canceled per request.
        Rate Limit: 2 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rfq/cancel-batch-rfqs",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def cancel_all_rfqs(self, use_proxy: bool = False) -> APIReturn:
        """
        Cancel all RFQs
        Cancels all active RFQs.
        Rate Limit: 2 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rfq/cancel-all-rfqs",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def execute_quote(
        self, rfqId: str, quoteId: str, use_proxy: bool = False
    ) -> APIReturn:
        """
        Execute Quote
        Executes a Quote. It is only used by the creator of the RFQ
        Rate Limit: 2 requests per 3 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rfq/execute-quote",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def set_quote_products(
        self,
        instType: str,
        data: List[dict],
        uly: str = None,
        instId: str = None,
        maxBlockSz: str = None,
        makerPxBand: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Set Quote products
        Customize the products which makers want to quote and receive RFQs for, and the corresponding price and size limit.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rfq/maker-instrument-settings",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def reset_mmp_status(self, use_proxy: bool = False) -> APIReturn:
        """
        Reset MMP status
        Reset the MMP status to be inactive.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rfq/mmp-reset",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def create_quote(
        self,
        rfqId: str,
        quoteSide: str,
        legs: List[dict],
        instId: str,
        sz: str,
        px: str,
        side: str,
        clQuoteId: str = None,
        anonymous: bool = None,
        expiresIn: str = None,
        tgtCcy: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Create Quote
        Allows the user to Quote an RFQ that they are a counterparty to. The user MUST quote the entire RFQ and not part of the legs or part of the quantity. Partial quoting or partial fills are not allowed.
        Rate Limit: 50 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rfq/create-quote",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def cancel_quote(
        self, quoteId: str = None, clQuoteId: str = None, use_proxy: bool = False
    ) -> APIReturn:
        """
        Cancel Quote
        Cancels an existing active Quote you have created in response to an RFQ.
        Rate Limit: 50 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rfq/cancel-quote",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def cancel_multiple_quotes(
        self,
        quoteIds: List[str] = None,
        clQuoteIds: List[str] = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Cancel multiple Quotes
        Cancel one or multiple active Quote(s) in a single batch. Maximum 100 quote orders can be canceled per request.
        Rate Limit: 2 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rfq/cancel-batch-quotes",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def cancel_all_quotes(self, use_proxy: bool = False) -> APIReturn:
        """
        Cancel all Quotes
        Cancels all active Quotes.
        Rate Limit: 2 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rfq/cancel-all-quotes",
            method="POST",
            body=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_rfqs(
        self,
        rfqId: str = None,
        clRfqId: str = None,
        state: str = None,
        beginId: str = None,
        endId: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get rfqs
        Retrieves details of RFQs that the user is a counterparty to (either as the creator or the receiver of the RFQ).
        Rate Limit: 2 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rfq/rfqs",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_quotes(
        self,
        rfqId: str = None,
        clRfqId: str = None,
        quoteId: str = None,
        clQuoteId: str = None,
        state: str = None,
        beginId: str = None,
        endId: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get quotes
        Retrieve all Quotes that the user is a counterparty to (either as the creator or the receiver).
        Rate Limit: 2 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rfq/quotes",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_trades(
        self,
        rfqId: str = None,
        clRfqId: str = None,
        quoteId: str = None,
        blockTdId: str = None,
        clQuoteId: str = None,
        state: str = None,
        beginId: str = None,
        endId: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get trades
        Retrieves the executed trades that the user is a counterparty to (either as the creator or the receiver).
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: UserID
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rfq/trades",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)

    def get_public_trades(
        self,
        beginId: str = None,
        endId: str = None,
        limit: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
        """
        Get public trades
        Retrieves the recent executed block trades.
        Rate Limit: 5 requests per 2 seconds
        Rate limit rule: IP
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/rfq/public-trades",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
