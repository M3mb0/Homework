"""Exception module store self made exceptions"""


class CrypterBaseException(Exception):
    """Base Crypter Exception"""
    pass


class ArgvException(CrypterBaseException):
    """Exception used when command line arguments are not ok."""
    pass


class NotTextFile(CrypterBaseException):
    """Raised when path does not contain a text file"""
    pass
