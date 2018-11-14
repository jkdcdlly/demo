from django.contrib import admin

# Register your models here.

from .models import GameInfo


class GameInfoAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'game_img_url')
    search_fields = ['game_name']
    list_filter = ['game_name']


admin.site.register(GameInfo, GameInfoAdmin)
