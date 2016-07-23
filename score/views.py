from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import LeaderBoard
from .serializers import ScoreSerializer


class PlayerList(APIView):
    """
    List the Score Board or add a new Score
    """
    def get(self, request, format=None):
        scoreboard = LeaderBoard.objects.order_by('-score')[:10]
        scoreboard = scoreboard.extra(select={'score': 'CAST(result AS INTEGER)'}).extra(order_by=['-score'])
        serializer = ScoreSerializer(scoreboard, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
