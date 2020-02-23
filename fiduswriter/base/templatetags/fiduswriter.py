from django import template
from django.conf import settings
from allauth.socialaccount.models import providers

register = template.Library()


@register.inclusion_tag('fiduswriter/config.html', takes_context=True)
def fiduswriter_config_js(context):
    """
    Add Fidus Writer config variables to the window object in JavaScript.
    Usage::
        {% fiduswriter_config_js %}
    """
    socialaccount_providers = []
    for provider in providers.registry.get_list():
        socialaccount_providers.append({
            'id': provider.id,
            'name': provider.name,
            'login_url': provider.get_login_url(context['request'])
        })
    return {
        'language': context['request'].LANGUAGE_CODE,
        'socialaccount_providers': socialaccount_providers
    }
