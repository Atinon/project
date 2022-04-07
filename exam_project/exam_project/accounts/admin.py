from django.contrib import admin

from exam_project.accounts.models import UserProfile


@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    pass
