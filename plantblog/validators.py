from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def validate_text_length(value):
    if len(value) < 5:
        raise ValidationError(
            'Minimum 5 characters.'
        )
    elif len(value) > 300:
        raise ValidationError(
            'Maximum 300 characters.'
        )
    else:
        pass


validate_letters = RegexValidator(
    (
        '[^0-9]+'
    )
)
