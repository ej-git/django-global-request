from django import template
from app.global_request import get_current_request

register = template.Library()


@register.filter
def test(value):
    return get_current_request().user
