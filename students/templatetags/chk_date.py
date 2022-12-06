from django import template
register = template.Library()

@register.simple_tag()
def have_time(date, *args, **kwargs):
    # you would need to do any localization of the result here
    print(date,"************************")
    return True