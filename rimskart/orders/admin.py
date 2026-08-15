from django.contrib import admin
from orders.models import Order, OrderedItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ('owner', 'deleted_status', 'order_status', 'created_at', 'updated_at', 'get_total_price')
    readonly_fields = ('created_at', 'updated_at', 'get_total_price')
    list_filter=['order_status','deleted_status']
    search_fields=['owner__user__username','owner__user__email']

    def get_total_price(self, obj):
        if obj.id:
            cart_items = obj.added_items.all()
            cart_subtotal = sum(item.product.price * item.quantity for item in cart_items if item.product)
            return f"₹{cart_subtotal:.2f}"
        return "₹0.00"
    
    get_total_price.short_description = 'Total Price' #changing name of the field in admin panel

admin.site.register(OrderedItem)
 