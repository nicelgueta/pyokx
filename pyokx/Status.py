# auto-generated code #
from .base import APIComponent, APIReturn, EndpointDetails


class Status(APIComponent):
    def status(self, state: str = None, use_proxy: bool = False) -> APIReturn:
        """
        Status
        Get event status of system upgrade
        Rate Limit: 1 request per 5 seconds
        """
        kwargs = {
            k: v
            for k, v in locals().items()
            if k not in ["use_proxy", "self"] and v is not None
        }
        details = EndpointDetails(
            request_path="/api/v5/system/status",
            method="GET",
            params=kwargs,
            use_proxy=use_proxy,
        )
        return self.request(details)
