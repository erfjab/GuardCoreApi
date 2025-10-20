class GuardCoreApiException(Exception):
    """Base class for request errors."""

    pass


class RequestTimeoutError(GuardCoreApiException):
    """Exception raised for request timeouts."""

    pass


class RequestConnectionError(GuardCoreApiException):
    """Exception raised for connection errors."""

    pass


class RequestResponseError(GuardCoreApiException):
    """Exception raised for invalid responses."""

    pass


class RequestAuthenticationError(GuardCoreApiException):
    """Exception raised for authentication failures."""

    pass
