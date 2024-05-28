import re

def to_table_name(pascal_case_str: str) -> str:
    """Convert ClassNames to table_names."""
    return pluralize(to_snake_case(pascal_case_str))

def to_snake_case(pascal_case_str: str) -> str:
    """convert PascalCase to snake_case."""
    return re.sub(r'(?<=[a-z0-9])(?=[A-Z])', '_', pascal_case_str).lower()

def pluralize(word):
    """Convert a singular word to its plural form."""
    special_cases = {
        'y': _pluralize_y,
        's': _pluralize_s,
    }
    pluralize_func = special_cases.get(word[-1], _pluralize_default)
    return pluralize_func(word)

def _pluralize_y(word):
    return word[:-1] + 'ies'

def _pluralize_s(word):
    return word + 'es'

def _pluralize_default(word):
    return word + 's'
