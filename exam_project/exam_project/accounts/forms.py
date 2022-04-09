from django import forms
from django.contrib.auth import forms as auth_forms

from exam_project.accounts.models import UserProfile, ProjectUser

USER = ProjectUser
PROFILE = UserProfile

ALIAS_VALIDATOR_ERROR_MSG = 'Such alias already exists.'
DESCRIPTION_TEXT_FIELD_ROW_NUMBER = 5


class CreateProfileForm(auth_forms.UserCreationForm):
    alias = forms.CharField(
        max_length=PROFILE.ALIAS_MAX_LEN,
    )

    first_name = forms.CharField(
        max_length=PROFILE.FIRST_NAME_MAX_LEN,
    )

    last_name = forms.CharField(
        max_length=PROFILE.LAST_NAME_MAX_LEN,
    )

    picture = forms.ImageField(
        required=False,
    )

    date_of_birth = forms.DateField(
        required=False,
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': DESCRIPTION_TEXT_FIELD_ROW_NUMBER}),
        required=False,
    )

    gender = forms.ChoiceField(
        choices=PROFILE.GENDERS,
    )

    def save(self, commit=True):
        user = super().save(commit=True)

        profile = PROFILE(
            alias=self.cleaned_data['alias'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            description=self.cleaned_data['description'],
            gender=self.cleaned_data['gender'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = USER
        fields = ('email', 'password1', 'password2')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = PROFILE
        fields = (
            'alias',
            'first_name',
            'last_name',
            'picture',
            'date_of_birth',
            'description',
            'gender',
        )


