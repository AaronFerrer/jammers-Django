from django.contrib import admin

# Register your models here.

from .models import Surgeon, Deformity, Patient, RxInstance

#admin.site.register(Surgeon)
admin.site.register(Deformity)
#admin.site.register(PrescriptionInstance)
#admin.site.register(Patient)

class SurgeonAdmin(admin.ModelAdmin):
	list_display = ['last_name', 'first_name']

# Associate admin with this model
admin.site.register(Surgeon, SurgeonAdmin)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
	list_display =  ['last_name', 'first_name', 'date_of_birth']

# Register the Admin classes for BookInstance using the decorator
@admin.register(RxInstance)
class RxInstanceAdmin(admin.ModelAdmin):
	pass

