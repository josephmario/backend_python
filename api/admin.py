from django.contrib import admin
from .models import	InfoCustomer
# Register your models here.

# admin.site.register(InfoCustomer)

@admin.register(InfoCustomer)
class InfoCustomerAdmin(admin.ModelAdmin):
	list_filter = ('lastname', 'temperature', 'fever', 'travel')
	list_display = ('lastname', 'city', 'temperature', 'fever', 'travel')