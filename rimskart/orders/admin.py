from django.contrib import admin
from orders.models import Order, OrderedItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Change 'uploaded_at' to 'updated_at' here:
    fields = ('owner', 'deleted_status', 'order_status', 'created_at', 'updated_at', 'get_total_price')
    
    # And change 'uploaded_at' to 'updated_at' here:
    readonly_fields = ('created_at', 'updated_at', 'get_total_price')

    def get_total_price(self, obj):
        if obj.id:
            cart_items = obj.added_items.all()
            cart_subtotal = sum(item.product.price * item.quantity for item in cart_items if item.product)
            return f"${cart_subtotal:.2f}"
        return "$0.00"
    
    get_total_price.short_description = 'Total Price'

admin.site.register(OrderedItem)
