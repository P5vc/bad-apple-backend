from django.contrib import admin
from django.contrib.auth.models import User , Group
from django.core.exceptions import PermissionDenied
from django.urls import path
from django.conf import settings
from .models import *

class CustomAdminSite(admin.AdminSite):
	site_header = 'Bad Apple Database Management'
	site_title = 'Bad Apple DB'
	index_title = 'Database Contents'



# Use custom, admin site:
customAdminSite = CustomAdminSite(name = 'customAdminSite')
from django.contrib.auth.admin import UserAdmin , GroupAdmin


# Add user administration:
@admin.register(User , site = customAdminSite)
class CustomUserAdmin(UserAdmin):
    pass



# Add group administration:
@admin.register(Group , site = customAdminSite)
class CustomGroupAdmin(GroupAdmin):
    pass



@admin.register(DatabaseManagerPermissions , site = customAdminSite)
class DatabaseManagerPermissionsAdmin(admin.ModelAdmin):
	list_display = ['user' , 'changesThisWeek' , 'changesLastWeek']



@admin.register(PRATemplate , site = customAdminSite)
class PRATemplateAdmin(admin.ModelAdmin):
	list_display = ['subject' , 'state' , 'public' , 'approved']
	exclude = ['createdOn' , 'updatedOn']


	# Custom save behavior:
	def add_view(self, request, form_url='', extra_context=None):
		if (request.method == 'POST'):
			if (request.POST.__contains__('lastChangedBy')):
				request.POST = request.POST.copy()
				request.POST.__setitem__('lastChangedBy' , request.user.username)
				dbManagerObj = DatabaseManagerPermissions.objects.get(user = request.user)
				if (dbManagerObj.changesThisWeek >= settings.WEEKLY_TOUCH_LIMIT):
					raise PermissionDenied
				dbManagerObj.changesThisWeek += 1
				dbManagerObj.save()

				request.POST.__setitem__('daysUntilDeletion' , 30)

		return super().changeform_view(request, None, form_url, extra_context)

	def change_view(self, request, object_id, form_url='', extra_context=None):
		if (request.method == 'POST'):
			if (request.POST.__contains__('lastChangedBy')):
				request.POST = request.POST.copy()
				request.POST.__setitem__('lastChangedBy' , request.user.username)
				dbManagerObj = DatabaseManagerPermissions.objects.get(user = request.user)
				if (dbManagerObj.changesThisWeek >= settings.WEEKLY_TOUCH_LIMIT):
					raise PermissionDenied
				dbManagerObj.changesThisWeek += 1
				dbManagerObj.save()

				request.POST.__setitem__('daysUntilDeletion' , 30)

		return super().changeform_view(request, object_id, form_url, extra_context)



@admin.register(OversightCommission , site = customAdminSite)
class OversightCommissionAdmin(admin.ModelAdmin):
	list_display = ['name' , 'stateProvince' , 'cityTown' , 'public' , 'approved']
	exclude = ['createdOn' , 'updatedOn']


	# Custom save behavior:
	def add_view(self, request, form_url='', extra_context=None):
		if (request.method == 'POST'):
			if (request.POST.__contains__('lastChangedBy')):
				request.POST = request.POST.copy()
				request.POST.__setitem__('lastChangedBy' , request.user.username)
				dbManagerObj = DatabaseManagerPermissions.objects.get(user = request.user)
				if (dbManagerObj.changesThisWeek >= settings.WEEKLY_TOUCH_LIMIT):
					raise PermissionDenied
				dbManagerObj.changesThisWeek += 1
				dbManagerObj.save()

				request.POST.__setitem__('daysUntilDeletion' , 30)

		return super().changeform_view(request, None, form_url, extra_context)

	def change_view(self, request, object_id, form_url='', extra_context=None):
		if (request.method == 'POST'):
			if (request.POST.__contains__('lastChangedBy')):
				request.POST = request.POST.copy()
				request.POST.__setitem__('lastChangedBy' , request.user.username)
				dbManagerObj = DatabaseManagerPermissions.objects.get(user = request.user)
				if (dbManagerObj.changesThisWeek >= settings.WEEKLY_TOUCH_LIMIT):
					raise PermissionDenied
				dbManagerObj.changesThisWeek += 1
				dbManagerObj.save()

				request.POST.__setitem__('daysUntilDeletion' , 30)

		return super().changeform_view(request, object_id, form_url, extra_context)
