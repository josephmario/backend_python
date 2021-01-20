from django.db import models

# Create your models here.
class InfoCustomer(models.Model):
	lastname                  = models.CharField(max_length=100, blank=False, null=False)
	firstname                 = models.CharField(max_length=100, blank=False, null=False)
	middlename                = models.CharField(max_length=100, blank=True, null=True)
	tel_cellphone_num         = models.CharField(max_length=12)
	house_num                 = models.CharField(max_length=100, blank=False, null=False)
	street                    = models.CharField(max_length=100, blank=False, null=False)
	building_subdivision_name = models.CharField(max_length=100, blank=True, null=True)
	barangay                  = models.CharField(max_length=100, blank=False, null=False)
	city                      = models.CharField(max_length=100, blank=False, null=False)
	country                   = models.CharField(max_length=100, blank=False, null=False)
	postal_code               = models.CharField(max_length=100, blank=False, null=False)
	email                     = models.EmailField(max_length=100, blank=True, null=True)
	temperature               = models.DecimalField(default=0.0, decimal_places=1, max_digits=5, blank=False, null=False)
	fever                     = models.BooleanField()
	travel                    = models.BooleanField()
	date                      = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.lastname