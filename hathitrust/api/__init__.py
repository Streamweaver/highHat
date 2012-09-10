"""
Contains modules to interact with the various common HathiTrust APIs.

For more information on the various data APIs available through
HathiTrust see the documentatio at http://www.hathitrust.org/data

"""

__author__ = 'Streamweaver'

API_BASEURL = 'http://services.hathitrust.org/htd/'

class APIException(Exception):
    """
    Used to indicate an exception in constructing or using HathiTrust
    API .

    """
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)