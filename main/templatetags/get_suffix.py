from django import template
register = template.Library()


@register.simple_tag
def get_suffix(path):
    return path.split('/')[-1]
