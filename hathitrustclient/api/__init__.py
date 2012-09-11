"""
Contains modules to interact with the various common HathiTrust APIs.

For more information on the various data APIs available through
HathiTrust see the documentatio at http://www.hathitrust.org/data

"""

__author__ = 'Streamweaver'

API_BASEURL = 'http://services.hathitrust.org/htd/'
OAUTH_SERVICE_URI = "/oauth2/token?grant_type=client_credentials"

class APIException(Exception):
    """
    Used to indicate an exception in constructing or using HathiTrust
    API .

    """
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)

class OAuthToken(object):

    def __init__(self, consumer_key, consumer_secret):
        """
        Initializes an OAuth Token from the server and stores it.

        :param consumer_key:  String of HathiTrust API key to use for the connection.
        :param consumer_secret:  String of password or secret phrase for the API Key.

        """
