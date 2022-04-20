from django import template
register = template.Library()
@register.filter
def my_create_cookie(data):
    if 'user' in data:
        value = data["user"]
        if value == 'Tutor':
            return 1
        elif value == 'Student':
            return 2
        elif value == 'no_auth':
            return 3
        else:
            return 0
    else:
        return -1