from django.contrib import admin
from django.contrib.auth.models import User , Group
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.utils.html import mark_safe
from django.urls import path , reverse
from django.conf import settings
from mainSite.models import *
from io import BytesIO
from os import remove
import time

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



@admin.register(WeeklyStats , site = customAdminSite)
class WeeklyStatsAdmin(admin.ModelAdmin):
	list_display = ['week' , 'year']
	readonly_fields = ['week' , 'year' , 'homeViews' , 'documentationViews' , 'praViews' , 'oversightViews' , 'commissionViews' , 'tipViews' , 'badAppleViews' , 'praSearches' , 'commissionSearches' , 'tipSubmissions']



@admin.register(Tip , site = customAdminSite)
class TipAdmin(admin.ModelAdmin):
	list_display = ['id' , 'topic' , 'viewed' , 'processed' , 'archived']
	readonly_fields = ['topic' , 'message' , 'daysUntilDeletion' , 'archived' , 'encrypted']



@admin.register(EncryptedMessage , site = customAdminSite)
class EncryptedMessageAdmin(admin.ModelAdmin):
	list_display = ['id' , 'primaryPubKeyFingerprint' , 'secondaryPubKeyFingerprint' , 'messageIsArchived']
	readonly_fields = ['parentTipURL' , 'parentTip' , 'messageIsArchived' , 'primaryPubKeyFingerprint' , 'secondaryPubKeyFingerprint' , 'encryptedMessage']



	def parentTipURL(self , object):
		parentTipLink = reverse('admin:mainSite_tip_change' , args = [object.parentTip.id])
		return mark_safe('<a href="' + parentTipLink + '">Modify Tip</a>')


	parentTipURL.short_description = 'Parent Tip URL'



# Custom save behavior for managed models:
def customSaveBehavior(request):
	if (request.method == 'POST'):
		if (request.POST.__contains__('lastChangedBy')):
			request.POST = request.POST.copy()
			dbManagerObj = DatabaseManagerPermissions.objects.get(user = request.user)
			if (dbManagerObj.changesThisWeek >= settings.WEEKLY_TOUCH_LIMIT):
				raise PermissionDenied
			dbManagerObj.changesThisWeek += 1
			dbManagerObj.save()

			# Set/reset administrative values:
			request.POST.__setitem__('lastChangedBy' , request.user.username)
			request.POST.__setitem__('daysUntilDeletion' , 30)
			if (not(request.user.groups.filter(name = 'Database Admins').exists())):
				request.POST.__setitem__('approved' , False)
				request.POST.__setitem__('public' , False)

	return request



@admin.register(PRATemplate , site = customAdminSite)
class PRATemplateAdmin(admin.ModelAdmin):
	list_display = ['subject' , 'stateTerritoryProvince' , 'public' , 'approved']
	readonly_fields = ['createdOn' , 'updatedOn' , 'daysUntilDeletion']


	# Override save behavior:
	def add_view(self , request , form_url = '' , extra_context = None):
		return super().changeform_view(customSaveBehavior(request) , None , form_url , extra_context)


	def change_view(self , request , object_id , form_url = '' , extra_context = None):
		return super().changeform_view(customSaveBehavior(request) , object_id , form_url , extra_context)



@admin.register(OversightCommission , site = customAdminSite)
class OversightCommissionAdmin(admin.ModelAdmin):
	list_display = ['name' , 'stateTerritoryProvince' , 'cityTown' , 'public' , 'approved' , 'completed']
	readonly_fields = ['createdOn' , 'updatedOn' , 'daysUntilDeletion' , 'commissionID']


	# Override save behavior:
	def add_view(self , request , form_url = '' , extra_context = None):
		return super().changeform_view(customSaveBehavior(request) , None , form_url , extra_context)


	def change_view(self , request , object_id , form_url = '' , extra_context = None):
		return super().changeform_view(customSaveBehavior(request) , object_id , form_url , extra_context)



@admin.register(Officer , site = customAdminSite)
class OfficerAdmin(admin.ModelAdmin):
	list_display = ['firstName' , 'lastName']
	readonly_fields = ['createdOn' , 'updatedOn' , 'daysUntilDeletion' , 'officerID']


	# Override save behavior:
	def add_view(self , request , form_url = '' , extra_context = None):
		return super().changeform_view(customSaveBehavior(request) , None , form_url , extra_context)


	def change_view(self , request , object_id , form_url = '' , extra_context = None):
		return super().changeform_view(customSaveBehavior(request) , object_id , form_url , extra_context)



@admin.register(InvestigativeReport , site = customAdminSite)
class InvestigativeReportAdmin(admin.ModelAdmin):
	list_display = ['client' , 'date']
	readonly_fields = ['createdOn' , 'updatedOn' , 'daysUntilDeletion' , 'reportID']


	# Override save behavior:
	def add_view(self , request , form_url = '' , extra_context = None):
		return super().changeform_view(customSaveBehavior(request) , None , form_url , extra_context)


	def change_view(self , request , object_id , form_url = '' , extra_context = None):
		return super().changeform_view(customSaveBehavior(request) , object_id , form_url , extra_context)



@admin.register(InvestigativeReportFinding , site = customAdminSite)
class InvestigativeReportFindingAdmin(admin.ModelAdmin):
	list_display = ['finding' , 'findingBasis']
	readonly_fields = ['createdOn' , 'updatedOn' , 'daysUntilDeletion']


	# Override save behavior:
	def add_view(self , request , form_url = '' , extra_context = None):
		return super().changeform_view(customSaveBehavior(request) , None , form_url , extra_context)


	def change_view(self , request , object_id , form_url = '' , extra_context = None):
		return super().changeform_view(customSaveBehavior(request) , object_id , form_url , extra_context)



@admin.register(DatabaseDump , site = customAdminSite)
class DatabaseDumpAdmin(admin.ModelAdmin):
	# Custom save behavior to generate and return the database dump:
	def add_view(self , request , form_url = '' , extra_context = None):
		if (request.POST.__contains__('dataCategory')):
			if (request.POST['dataCategory'] == '0'):
				filepath = ('/tmp/' + str(time.time()) + '.html')
				with open(filepath , 'w') as mainFile:
					headers = ('<h1 style="text-align:center">Bad Apple</h1>\n<h2 style="text-align:center">Police Oversight Commissions</h2>\n<h3 style="text-align:center">' + str(time.ctime()) + '</h3>\n\n')
					mainFile.write(headers)

				with open((filepath + '.toc') , 'w') as tableOfContentsFile:
					tableOfContentsHeader = ('<h1><u>Table of Contents</u></h1>\n<ul>\n\t<li>')
					tableOfContentsFile.write(tableOfContentsHeader)

				country = ''
				stateTerritoryProvince = ''
				previousCountry = ''
				previousStateTerritoryProvince = ''
				firstIteration = True
				countrySameAsBefore = False
				stateTerritoryProvinceSameAsBefore = False
				for entry in OversightCommission.objects.order_by('country' , 'stateTerritoryProvince' , 'name'):
					if (firstIteration):
						country = str(entry.get_country_display())
						stateTerritoryProvince = str(entry.get_stateTerritoryProvince_display())
						previousCountry = country
						previousStateTerritoryProvince = stateTerritoryProvince
					else:
						previousCountry = country
						previousStateTerritoryProvince = stateTerritoryProvince
						country = str(entry.get_country_display())
						stateTerritoryProvince = str(entry.get_stateTerritoryProvince_display())
						if (previousCountry == country):
							countrySameAsBefore = True
						else:
							countrySameAsBefore = False
						if (previousStateTerritoryProvince == stateTerritoryProvince):
							stateTerritoryProvinceSameAsBefore = True
						else:
							stateTerritoryProvinceSameAsBefore = False

					if (not(countrySameAsBefore)):
						if (firstIteration):
							countryLine = ('<h2><a href="#' + str(entry.country) + '">' + country + '</a></h2>\n\t<ul>')
							firstIteration = False
						else:
							countryLine = ('\n\t</ul>\n\t</li>\n\t<li><h2><a href="#' + str(entry.country) + '">' + country + '</a></h2></li>')

						with open((filepath + '.toc') , 'a') as tableOfContentsFile:
							tableOfContentsFile.write(countryLine)

					if (not(stateTerritoryProvinceSameAsBefore)):
						stateTerritoryProvinceHeader = ('\n\t\t<li><h3><a href="#' + str(entry.stateTerritoryProvince) + '">' + stateTerritoryProvince + '</a></h3></li>')
						with open((filepath + '.toc') , 'a') as tableOfContentsFile:
							tableOfContentsFile.write(stateTerritoryProvinceHeader)

					# Individual Entries:
					if (not(countrySameAsBefore)):
						countryDeclaration = ('<h1 id="' + str(entry.country) + '">' + country + '</h1>\n')
						with open((filepath + '.entries') , 'a') as entriesFile:
							entriesFile.write(countryDeclaration)

					entryString = ''

					if (not(stateTerritoryProvinceSameAsBefore)):
						entryString += ('<h2 id="' + str(entry.stateTerritoryProvince) + '">' + stateTerritoryProvince + '</h2>\n')

					entryString += ('<h3>' + str(entry.cityTown) + '</h3>\n<p><strong>Name:</strong> ' + str(entry.name) + '</p>\n<p><strong>Type:</strong> ' + str(entry.get_type_display()) + '</p>\n<p><strong>Website URL:</strong> ' + str(entry.website) + '</p>\n<p><strong>Address (Line 1):</strong> ' + str(entry.address1) + '</p>\n<p><strong>Address (Line 2):</strong> ' + str(entry.address2) + '</p>\n<p><strong>Email Address:</strong> ' + str(entry.email) + '</p>\n<p><strong>Phone Number:</strong> ' + str(entry.phone) + '</p>\n<p><strong>TTD/TTY Phone Number:</strong> ' + str(entry.phoneTDD) + '</p>\n<p><strong>Fax Number:</strong> ' + str(entry.fax) + '</p>\n<p><strong>Contact Form URL:</strong> ' + str(entry.contactForm) + '</p>\n<p><strong>Press Email Address:</strong> ' + str(entry.pressEmail) + '</p>\n<p><strong>Press Phone Number:</strong> ' + str(entry.pressPhone) + '</p>\n<p><strong>Press Contact Form URL:</strong> ' + str(entry.pressContactForm) + '</p>\n<p><strong>About/Summary:</strong> ' + str(entry.aboutSummary) + '</p>\n<p><strong>Complaint Information (URL 1):</strong> ' + str(entry.complaintInfo1) + '</p>\n<p><strong>Complaint Information (URL 2):</strong> ' + str(entry.complaintInfo2) + '</p>\n<p><strong>Complaint Form URL:</strong> ' + str(entry.complaintForm) + '</p>\n<p><strong>Members Page URL:</strong> ' + str(entry.membersPage) + '</p>\n<p><strong>FAQ Page URL:</strong> ' + str(entry.faqPage) + '</p>\n<p><strong>Record Created On:</strong> ' + str(entry.createdOn) + '</p>\n<p><strong>Record Last Updated On:</strong> ' + str(entry.updatedOn) + '</p>\n<p><strong>Record Approved:</strong> ' + str(entry.approved) + '</p>\n<p><strong>Record Public:</strong> ' + str(entry.public) + '</p>\n<p>&nbsp;</p>\n\n')
					with open((filepath + '.entries') , 'a') as entriesFile:
						entriesFile.write(entryString)


				tableOfContentsCleanup = '\n\t</ul>\n\t</li>\n</ul>\n<p>&nbsp;</p>\n\n<h1><u>Entries</u></h1>\n'
				with open((filepath + '.toc') , 'a') as tableOfContentsFile:
					tableOfContentsFile.write(tableOfContentsCleanup)

				# Combine the individual files into one:
				with open(filepath , 'a') as mainFile:
					with open((filepath + '.toc') , 'r') as tableOfContentsFile:
						mainFile.write(tableOfContentsFile.read())
					with open((filepath + '.entries') , 'r') as entriesFile:
						mainFile.write(entriesFile.read())

				# Read the file in, to a BytesIO object, so that it may be returned for downloading:
				ioObj = BytesIO()
				with open(filepath , 'rb') as mainFile:
					ioObj.write(mainFile.read())

				# Remove the old files:
				remove((filepath + '.toc'))
				remove((filepath + '.entries'))
				remove(filepath)

				response = HttpResponse(ioObj.getvalue() , content_type = 'application/xml')
				response['Content-Disposition'] = ('attachment; filename=OversightCommissionsDatabaseDump.html')

				return response

		return super().changeform_view(request , None , form_url , extra_context)
