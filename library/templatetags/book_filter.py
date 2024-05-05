from django import template

register = template.Library()

@register.filter(name='get_human_readable_language')
def get_language_name(language_code):
    LANGUAGES = {
        'en': 'English',
        'ar': 'Arabic',
    }
    return LANGUAGES.get(language_code, language_code)