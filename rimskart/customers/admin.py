from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    # This displays the property alongside your database fields
    list_display = ('id', 'username', 'phone', 'deleted_status')

