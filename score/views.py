from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import LeaderBoard
from .serializers import ScoreSerializer


domain_list = ['hitensharma.me', 'htadg.github.io', 'vigneshm.com', 'vigzmv.github.io', '127.0.0.1', 'localhost']


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def get_score(request):
    if request.META['REMOTE_ADDR'] in domain_list:
        if request.method == 'GET':
            leaders = LeaderBoard.objects.order_by('-score')
            serializer = ScoreSerializer(leaders[:10], many=True)
            return JSONResponse(serializer.data)
        else:
            data = {'status': 'Bad Request Method'}
            return JSONResponse(data)
    else:
        return JSONResponse({'status': 'Client Address Error'})
