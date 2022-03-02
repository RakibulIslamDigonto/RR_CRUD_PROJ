from atexit import register
from django.contrib import admin
from ApiCRUDapp.models import PostModel

# Register your models here.

class PostModelAdmin(admin.ModelAdmin):

    list_display = [
        'author',
        'title',
        'description'
    ]
admin.site.register(PostModel, PostModelAdmin)