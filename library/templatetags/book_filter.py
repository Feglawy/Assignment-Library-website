from django import template
from django.templatetags.static import static
register = template.Library()

@register.filter(name='get_human_readable_language')
def get_language_name(language_code):
    LANGUAGES = {
        'en': 'English',
        'ar': 'Arabic',
    }
    return LANGUAGES.get(language_code, language_code)


@register.filter(name='get_item_from_dict')
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter(name='get_url_if_found_else')
def get_url_otherwise(url, default_path):
    if not url:
        return static(default_path)
    return url
