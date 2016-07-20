from django.contrib import admin

from .models import LeaderBoard


class LeaderBoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'score',)
    search_fields = ('name',)
    ordering = ('-score',)
    fields = ('name', 'score',)

admin.site.register(LeaderBoard, LeaderBoardAdmin)
