from django.core import validators as django_validators
from django.db import models
from django.contrib.auth import models as auth_models

from exam_project.accounts.managers import ProjectUserManager
from exam_project.utils import validators as custom_validators


class ProjectUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    EMAIL_MAX_LENGTH = 254
    EMAIL_MIN_LENGTH = 3

    email = models.EmailField(
        max_length=EMAIL_MAX_LENGTH,
        validators=(
            django_validators.MinLengthValidator(EMAIL_MIN_LENGTH),
        ),
        unique=True,
        null=False,
        blank=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'

    objects = ProjectUserManager()

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    ALIAS_MAX_LEN = 25
    ALIAS_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 25
    FIRST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 25
    LAST_NAME_MIN_LEN = 2

    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'
    DO_NOT_SHOW = 'Do not show'
    GENDERS = [(x, x) for x in (MALE, FEMALE, OTHER, DO_NOT_SHOW)]

    alias = models.CharField(
        null=True,
        blank=True,
        # unique=True,  # probably wont work
        max_length=ALIAS_MAX_LEN,
        validators=(
            django_validators.MinLengthValidator(ALIAS_MIN_LEN),
            # whitespace validator?
        )
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            django_validators.MinLengthValidator(FIRST_NAME_MIN_LEN),
            custom_validators.validate_only_letters,
        ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            django_validators.MinLengthValidator(LAST_NAME_MIN_LEN),
            custom_validators.validate_only_letters,
        ),
    )

    picture = models.ImageField(
        null=True,
        blank=True,
        validators=(
            custom_validators.MaxFileSizeInMbValidator,
        )
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        default=DO_NOT_SHOW,
    )

    user = models.OneToOneField(
        ProjectUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.user.email
