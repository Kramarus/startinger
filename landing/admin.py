from django.contrib import admin
from .models import Applicant, Contact, Newsletter

# Register your models here.
admin.site.register(Applicant)
admin.site.register(Contact)
admin.site.register(Newsletter)