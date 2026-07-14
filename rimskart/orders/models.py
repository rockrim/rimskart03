from django.db import models
from customers.models import Customer as cu
from product.models import Product as pu

# Model for order.
class Order(models.Model):  # Fix 1: Capitalised class name
    # If item deleted going to trash
    LIVE = 1
    DELETED = 0
    DELETED_CHOICES = (
        (LIVE, 'live'),
        (DELETED, 'deleted')
    )

    # Order item process
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4  # Fix 2: Fixed spelling typo
    
    STATUS_CHOICE = (
        (CART_STAGE, "cart_stage"),         # Fix 3: Added missing choices
        (ORDER_CONFIRMED, "order_confirmed"), # Fix 3: Added missing choices
        (ORDER_PROCESSED, "order_processed"),
        (ORDER_DELIVERED, "order_delivered"),
        (ORDER_REJECTED, "order_rejected"),
    )
     
    # Fix 4: Allowed null values on ForeignKey since on_delete is SET_NULL
    owner = models.ForeignKey(cu, on_delete=models.SET_NULL, null=True, related_name="orders")
    deleted_status = models.IntegerField(choices=DELETED_CHOICES, default=LIVE)
    order_status = models.IntegerField(choices=STATUS_CHOICE, default=CART_STAGE)
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - Owner: {self.owner}"


class OrderedItem(models.Model):  # Fix 1: Capitalised class name & fixed spelling
    # Item cart product
    product = models.ForeignKey(pu, on_delete=models.SET_NULL, null=True, related_name="ordered_items") # Fix 4 & 5
    quantity = models.PositiveIntegerField(default=1)  # Fix 6: Changed to PositiveIntegerField
    owner = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="ordered_items") # Fix 5

    def __str__(self):
        return f"{self.quantity} x {self.product.name if self.product else 'Deleted Product'}"
