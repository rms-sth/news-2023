from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from newspaper.models import Category, Comment, Contact, Newsletter, Post, Tag

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(Newsletter)
admin.site.register(Comment)


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)


admin.site.register(Post, PostAdmin)
