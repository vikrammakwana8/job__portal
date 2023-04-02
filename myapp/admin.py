from django.contrib import admin
from .models import User,Company,Job,Employe,Appointment

# Register your models here.
admin.site.register(User)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Employe)
admin.site.register(Appointment)
	