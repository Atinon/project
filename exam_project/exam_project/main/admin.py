from django.contrib import admin

from exam_project.comments.models import ProfileComments


@admin.register(ProfileComments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'author', 'receiver')
