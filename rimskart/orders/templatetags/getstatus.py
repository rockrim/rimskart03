from django import template

register = template.Library()   

@register.simple_tag(name='getstatus')
def getstatus(status):
    status=status-1
    status_array=['ORDER_CONFIRMED','ORDER_PROCESSED','ORDER_DELIVERED','ORDER_REJECTED']
    return status_array[status]

