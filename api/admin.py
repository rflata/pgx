from django.contrib import admin
from .models import *

# Models for admin site
admin.site.register(Activity)
admin.site.register(Drug)
admin.site.register(Gene)
admin.site.register(Recommendation)
admin.site.register(Patient)
admin.site.register(PatientGenetics)
admin.site.register(Prescriber)
admin.site.register(Prescription)
