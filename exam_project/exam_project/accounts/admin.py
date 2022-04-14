from django.contrib import admin
from django.contrib.admin.options import get_content_type_for_model
from django.contrib.admin.utils import unquote
from django.contrib.auth import get_user_model

from exam_project.accounts.models import UserProfile

from django.contrib.admin.models import LogEntry

USER = get_user_model()


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(USER)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'last_login', 'is_staff')
