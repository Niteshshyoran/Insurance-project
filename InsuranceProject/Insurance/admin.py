from django.contrib import admin
from .models import Company,Policy,Claim,Payment
# Register your models here.


admin.site.register(Company)
admin.site.register(Policy)
admin.site.register(Claim)
admin.site.register(Payment)
