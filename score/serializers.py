from __future__ import unicode_literals

from rest_framework import serializers

from .models import LeaderBoard


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaderBoard
        fields = ('name', 'score')
