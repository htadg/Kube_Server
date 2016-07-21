from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import LeaderBoard
from .serializers import ScoreSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        kwargs['headers'] = {'Access-Control-Allow-Origin': 'http://hitensharma.me',
        'Access-Control-Allow-Methods': 'GET, POST',
        'Access-Control-Allow-Credentials': False}
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def get_score(request):
    if request.method == 'GET':
        leaders = LeaderBoard.objects.order_by('-score')
        serializer = ScoreSerializer(leaders[:10], many=True)
        return JSONResponse(serializer.data)
    else:
        data = {'error': 'Bad Request Method'}
        return JSONResponse(data)
