from django.core.exceptions import ValidationError

LETTERS_VALIDATION_ERROR_MSG = 'Value must contain only letters.'


def validate_only_letters(value):
    for ch in value:
        if not ch.is_alpha():
            raise ValidationError(LETTERS_VALIDATION_ERROR_MSG)
