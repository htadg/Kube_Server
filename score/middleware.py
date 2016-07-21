from __future__ import unicode_literals

import random
from django import http

try:
    import Kube_Server.settings as settings
    XS_SHARING_ALLOWED_ORIGINS = settings.XS_SHARING_ALLOWED_ORIGINS
    XS_SHARING_ALLOWED_METHODS = settings.XS_SHARING_ALLOWED_METHODS
    XS_SHARING_ALLOWED_CREDENTIALS = settings.XS_SHARING_ALLOWED_CREDENTIALS
except:
    XS_SHARING_ALLOWED_ORIGINS = '*'
    XS_SHARING_ALLOWED_METHODS = ['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE']
    XS_SHARING_ALLOWED_CREDENTIALS = False


class ScoreMiddleware():

    def generate_key(self):
        seed = random.getrandbits(32)
        while True:
           yield seed
           seed += 1

    def process_request(self, request):
        if not 'kube-key' in request.session or request.session['kube-key'] == '':
            session_key = next(self.generate_key())
            print "New Session Created"
            request.session['kube-key'] = session_key
        else:
            print "People are returning"


class XsSharing(object):
    """
        This middleware allows cross-domain XHR using the html5 postMessage API.

        Access-Control-Allow-Origin: http://foo.example
        Access-Control-Allow-Methods: POST, GET, OPTIONS, PUT, DELETE
    """
    def process_request(self, request):

        # if 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
        if request.method in XS_SHARING_ALLOWED_METHODS:
            response = http.HttpResponse()
            response['Access-Control-Allow-Origin'] = XS_SHARING_ALLOWED_ORIGINS
            response['Access-Control-Allow-Methods'] = ",".join(XS_SHARING_ALLOWED_METHODS)
            response['Access-Control-Allow-Credentials'] = XS_SHARING_ALLOWED_CREDENTIALS

            return response

        return None

    def process_response(self, request, response):
        # Avoid unnecessary work
        if response.has_header('Access-Control-Allow-Origin'):
            return response

        response['Access-Control-Allow-Origin'] = XS_SHARING_ALLOWED_ORIGINS
        response['Access-Control-Allow-Methods'] = ",".join(XS_SHARING_ALLOWED_METHODS)
        response['Access-Control-Allow-Credentials'] = XS_SHARING_ALLOWED_CREDENTIALS

        return response