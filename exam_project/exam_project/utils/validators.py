from django.core.exceptions import ValidationError

LETTERS_VALIDATION_ERROR_MSG = 'Value must contain only letters.'


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError(LETTERS_VALIDATION_ERROR_MSG)


class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def _validation_error_msg(self):
        return "Max file size is %sMB" % str(self.max_size)

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.max_size * 1024 * 1024:
            raise ValidationError(self._validation_error_msg())
