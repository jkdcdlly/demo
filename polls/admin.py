from django.contrib import admin

# Register your models here.

from .models import Question, Choice, Trade, GameInfo


# admin.site.register(Question)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    search_fields = ['question_text']


class GameInfoAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'game_img_url')
    search_fields = ['game_name']
    list_filter = ['game_name']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Trade)
admin.site.register(GameInfo, GameInfoAdmin)
