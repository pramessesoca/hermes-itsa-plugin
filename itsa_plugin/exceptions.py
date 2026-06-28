"""Custom exceptions for the ITSA plugin."""


class ITSAPluginError(Exception):
    """Base exception for the plugin."""


class ConfigurationError(ITSAPluginError):
    """Raised when required configuration is missing or invalid."""


class DataValidationError(ITSAPluginError):
    """Raised when incoming data does not match the expected schema."""


class DataNotLoadedError(ITSAPluginError):
    """Raised when a provider is asked for data before loading."""
