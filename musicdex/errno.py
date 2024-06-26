
__all__ = (
    "HolodexEndpointError",
    "MusicdexEndpointError",
    "MusicdexParamError"
)


class HolodexEndpointError(Exception):
    """Holodex Endpoint Error"""


class MusicdexEndpointError(Exception):
    """Musicdex Endpoint Error"""


class MusicdexParamError(Exception):
    """Wrong query parameter error"""


class MusicdexEndpointParamError(Exception):
    """Wrong url parameter error"""
