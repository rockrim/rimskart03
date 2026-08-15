from django.db import models
from customers.models import Customer 
from product.models import Product 


class Order(models.Model): #owner cart single customer 
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
    ORDER_REJECTED = 4  
    
    # giving the strings valus for the variables throgh tuple 
    STATUS_CHOICE = (
        (CART_STAGE, "cart_stage"),        
        (ORDER_CONFIRMED, "order_confirmed"), 
        (ORDER_PROCESSED, "order_processed"),
        (ORDER_DELIVERED, "order_delivered"),
        (ORDER_REJECTED, "order_rejected"),
    )
     
    # creating the fields for spreate cart for every customer
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name="orders")# one customer can have multiple orders
    deleted_status = models.IntegerField(choices=DELETED_CHOICES, default=LIVE)
    order_status = models.IntegerField(choices=STATUS_CHOICE, default=CART_STAGE)
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def save(self, *args, **kwargs):
    # Only calculate if the order already exists in the database
        if self.pk:
            # Assumes your Product model has a field named 'price'
            total = sum(item.quantity * item.product.price for item in self.added_items.all() if item.product)
            self.total_amount = total
        super().save(*args, **kwargs)



    def __str__(self):
        return f"Order {self.id} - Owner: {self.owner}"


class OrderedItem(models.Model):  
    # Items of custormer order cart
    owner = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="added_items")# one customer can have multiple items in cart
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="added_items")#can not create duplicate product in cart for same customer
    quantity = models.PositiveIntegerField(default=1)  
     
    def __str__(self):
        if self.product:
            product_label = getattr(self.product, 'title', 
                            getattr(self.product, 'product_name', 
                            f"Product #{self.product.id}"))
            return f"{self.quantity} x {product_label}"
        return f"{self.quantity} x Deleted Product"
