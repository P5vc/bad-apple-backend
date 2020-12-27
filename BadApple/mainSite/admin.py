from django.contrib import admin
from .models import *

@admin.register(PRATemplate)
class AccountContentsAdmin(admin.ModelAdmin):
	list_display = ['public' , 'state' , 'entity' , 'technology' , 'approved']

@admin.register(OversightCommission)
class AccountContentsAdmin(admin.ModelAdmin):
	list_display = ['public' , 'stateProvince' , 'cityTown' , 'approved']
