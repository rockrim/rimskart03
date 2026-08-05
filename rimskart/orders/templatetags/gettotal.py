from django import template

register = template.Library()   

@register.simple_tag(name='gettotal')
def gettotal(items_queryset):
    total = 0
    
    # Safety guard: return 0 if the data passed from HTML is empty or a string
    if not items_queryset or isinstance(items_queryset, str):
        return total
        
    # Loop over the items directly
    for iteam in items_queryset:
        total += iteam.product.price * iteam.quantity
        
    return total