from django.db import models

# models for banner
class banner(models.Model):
    banner=models.ImageField(upload_to='banner_images/media')
    caption=models.TextField()
