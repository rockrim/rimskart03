from django.db import models

# model for product.
class Product(models.Model):
    #if iteam deleted going to trash
    live=1
    deleted=0
    deleted_choices=((live,'live'),(deleted,'deleted'))

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='product_images/media')
    priority=models.IntegerField(default=0) 
    deleted_status=models.IntegerField(choices=deleted_choices,default=live)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
