from django.db import models
from django.contrib.auth.models import User

# model for customer.
class Customer(models.Model):
    #if iteam deleted going to trash
    live=1
    deleted=0
    deleted_choices=((live,'live'),(deleted,'deleted'))

    username = models.CharField(max_length=200)
    address = models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="customer_profile")
    phone=models.CharField(max_length=15)
    deleted_status=models.IntegerField(choices=deleted_choices,default=live)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

