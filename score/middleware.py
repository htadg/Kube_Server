from __future__ import unicode_literals


import random


class ScoreMiddleware():

    def generate_key(self):
        seed = random.getrandbits(32)
        while True:
           yield seed
           seed += 1

    def process_request(self, request):
        request.META['Access-Control-Allow-Methods'] = 'GET, POST'
        request.META['Access-Control-Allow-Origin'] = 'http://hitensharma.me'
        request.META['Access-Control-Allow-Credentials'] = False
        if not 'kube-key' in request.session or request.session['kube-key'] == '':
            session_key = next(self.generate_key())
            print "New Session Created"
            request.session['kube-key'] = session_key
        else:
            print "People are returning"

        return request

    def process_response(self, request, response):

        response['Access-Control-Allow-Methods'] = 'GET, POST'
        response['Access-Control-Allow-Origin'] = 'http://hitensharma.me'
        response['Access-Control-Allow-Credentials'] = False

        return response
