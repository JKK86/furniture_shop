from django.core.exceptions import ValidationError
import re


def validate_postal_code(postal_code):
    pattern = r'\d{2}-\d{3}'
    if not re.fullmatch(pattern, postal_code):
        raise ValidationError("Kod pocztowy należy podać w formacie XX-XXX, gdzie X oznacza cyfrę")
