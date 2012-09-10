"""
Contains classes and functions for querying the HathiTrust Data
API.  For more information see the documetation at
"""

__author__ = 'Streamweaver'

import urllib, urllib2

from hathitrust.api import API_BASEURL, APIException

class HtResource(object):

    def __init__(self, id):
        """
        Creates a python class around a HathiTrust Data API resource of `id`.

        :param id: String for HathiTrust resource Persistant Identifier

        """
        self.id = id

    def _resource_url(self, resource, params=None):
        """
        Constructs a URL for the desired HathiTrust Data API service.  See
        documentation at http://www.hathitrust.org/data_api#URI_scheme for
        more information on the URI Schema.

        :param resource: String of pre-defined API object resource to call.
        :param params:  Dict of additional params to pass for API call.

        """
        url = "".join([API_BASEURL, resource, "/", self.id])
        if params:
            url = url + "?" + urllib.urlencode(params)
        return url

    def meta(self, segment=None, json=False):
        """
        Calls the meta resource for this HathiTrust Object.  By default
        it returns parsed eTree of the XML return from the API but may
        optionally return the a pythonic representation of the object
        loaded from the JSON return.

        :param segment: Int of page segment to return specific data for.
        :param json: Boolean to load JSON return into a pythonic object.

        """

    def structure(self):
        # TODO: Someone implement me.
        return None

    def aggregate(self):
        # TODO: Someone implement me.
        return None

    def pageimage(self):
        # TODO: Someone implement me.
        return None

    def pageocr(self):
        # TODO: someone implement me.
        return None

    def pagecoordocr(self):
        # TODO: someone implement me.
        return None

    def pagemeta(self):
        # TODO: someone implement me.
        return None