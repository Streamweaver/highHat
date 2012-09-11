"""
Contains classes and functions for querying the HathiTrust Data
API.  For more information see the documetation at
"""

__author__ = 'Streamweaver'

import urllib, urllib2, json, os
from xml.etree import ElementTree

from hathitrustclient.api import API_BASEURL, APIException

NS_HTD = {"http://schemas.hathitrust.org/htd/2009"}

class HtResource(object):

    def __init__(self, id):
        """
        Creates a python class around a HathiTrust Data API resource of `id`.

        :param id: String for HathiTrust resource Persistant Identifier

        """
        self.id = id

    def _resource_url(self, resource, segment=None, params=None):
        """
        Constructs a URL for the desired HathiTrust Data API service.  See
        documentation at http://www.hathitrustclient.org/data_api#URI_scheme for
        more information on the URI Schema.

        :param resource: String of pre-defined API object resource to call.
        :param params:  Dict of additional params to pass for API call.

        """
        url = "".join([API_BASEURL, resource, "/", self.id])
        if segment:
            url = url + "/" + segment
        if params:
            url = url + "?" + urllib.urlencode(params)
        return url

    def _get_metadata_resource(self, resource, segment=None, json=False):
        """
        Calls the named resource for this HathiTrust Object.  By default
        it returns parsed eTree of the XML return from the API but may
        optionally return the a pythonic representation of the object
        loaded from the JSON return.

        :param segment: Int of page segment to return specific data for.
        :param json: Boolean to load JSON return into a pythonic object.

        """
        if segment:
            segment = "%s" % segment
        if json:
            return self._get_metadata_resource_json(resource, segment)

        url = self._resource_url(resource, segment)
        tree = ElementTree.parse(urllib.urlopen(url))
        return tree.getroot()

    def _get_metadata_resource_json(self, resource, segment):
        """
        Calls the JSON return for a HathiTrust Resource and returns
        the parsed pythonic object.

        :params resource:  String of resource to be called.
        :params segment:  Segment of object to call for individual page metadata.
        """
        url = self._resource_url(resource, segment, params={'alt': 'json'})
        request = urllib2.urlopen(url)
        return json.loads(request.read())

    def _get_binary_resource(self, resource, location, filename, chunk=16384):
        """
        Takes a binary file download and writes it to `filename` to `location`.

        :param resoruce: String of resource to request from HathiTrust Data API.
        :param location: String of path to save the resultant download to.
        :param fielname: String of filename to write file as.
        :param chunk: Int of bytes to read the download file in.
        """
        location = self._check_path(location)
        url = self._resource_url(resource)
        request = urllib2.urlopen(url)
        with file("%s/%s" % (location, filename), 'wb') as f:
            while True:
                buffer = request.read(chunk)
                if not buffer:
                    break
                f.write(buffer)
            f.close()

    def _check_path(self, location):
        """
        Checks to ensure location is a valid location on the filesystem and
        normalizes it into a path object.

        :param location:  String of path.
        """
        if not os.path.exists(location):
            raise IOError("Location %s does not exist on the filesystem!")
        return os.path.normpath(location)

    def meta(self, segment=None, json=False):
        """Calls the meta resource."""
        return self._get_metadata_resource('meta', segment, json)

    def structure(self, json=False):
        """Calls the structure resource."""
        return self._get_metadata_resource('structure', None, json)

    def aggregate(self, location, filename=None):
        """
        Saves the aggregate resource return to location.  By default the filename
        will be <Item ID>.zip but an optional filename may be supplied.

        :param location:  String of path to write file to.
        :param filename:  Sting of filename to use instead of default <ID>.zip

        """
        if not filename:
            filename = "%s.zip" % self.id
        self._get_binary_resource('aggregate', location, filename)

    def pageimage(self):
        # TODO: Someone implement me.
        return None

    def pageocr(self):
        # TODO: someone implement me.
        return None

    def pagecoordocr(self):
        # TODO: someone implement me.
        return None

    def pagemeta(self, segment, json=False):
        """Calls the pagemeta resource."""
        return self._get_metadata_resource('pagemeta', segment, json)