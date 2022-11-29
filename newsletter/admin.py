from django.contrib import admin
from .models import NewsLetter


class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('email', 'timestamp',)


admin.site.register(NewsLetter, NewsLetterAdmin)
