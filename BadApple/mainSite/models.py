from django.db import models
from django.conf import settings
from .modelCodes import *



class DatabaseManagerPermissions(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete = models.CASCADE)

	# Limits:
	changesThisWeek = models.IntegerField('Changes Made This Week (max = 10)' , default = 0)
	changesLastWeek = models.IntegerField('Changes Made Last Week (max = 10)' , default = 0)



	# Manage metadata:
	class Meta:
		verbose_name = 'Database Manager Permissions'
		verbose_name_plural = 'Database Manager Permissions'



class PRATemplate(models.Model):
	# Choices:
	SUBJECTS = [
					('0' , 'Body Worn Cameras'),
					('1' , 'Unmanned Aerial Vehicles (Drones)'),
					('2' , 'Facial Recognition'),
					('3' , 'Thermographic Cameras (FLIR)'),
					('4' , 'License Plate Readers'),
					('5' , 'Memoranda of Understanding'),
					('6' , 'Predictive Policing'),
					('7' , 'Gunshot Detection Microphones (ShotSpotter)'),
					('8' , 'Social Media Monitoring'),
					('9' , 'IMSI-Catcher Equipment (Stingray)')
				]

	# Filters:
	country = models.CharField('Country' , max_length = 3 , choices = COUNTRIES , default = 'USA')
	stateTerritoryProvince = models.CharField('State/Territory/Province' , max_length = 6 , choices = STATES_TERRITORIES_PROVINCES , default = 'USA-CA')
	subject = models.CharField('Subject' , max_length = 4 , choices = SUBJECTS , default = '0')

	# Template Contents:
	title = models.CharField('Title' , max_length = 300 , blank = True)
	letterBody = models.TextField('Letter Body' , max_length = 10000 , blank = True)

	# Administrative:
	createdOn = models.DateTimeField('Template Created On (Auto-Filled)' , auto_now_add = True)
	updatedOn = models.DateTimeField('Template Last Updated On (Auto-Filled)' , auto_now = True)
	lastChangedBy = models.CharField('Last Changed By' , max_length = 50 , blank = True)
	delete = models.BooleanField('Delete' , default = False)
	daysUntilDeletion = models.IntegerField('Days Until Deletion (When Marked For Deletion)' , default = 30)

	# Permissions:
	approved = models.BooleanField('Template Approved' , default = False)
	public = models.BooleanField('Template Public' , default = False)



	# Manage metadata:
	class Meta:
		verbose_name = 'PRA Template'
		verbose_name_plural = 'PRA Templates'



class OversightCommission(models.Model):
	# Choices:
	TYPES = [
					('0' , 'Citizen Board/Panel/Commission/Committee'),
					('1' , 'Independent Auditor/Monitor/Agency/Ombudsman'),
					('2' , 'Office/Board/Council/Divison of Elected Officials'),
					('3' , 'Office/Board/Council/Divison of Appointed Officials'),
					('4' , 'Board of Police Commissionors'),
					('5' , 'Interdepartmental Entity (H.R./Office of Complaints)')
			]

	# Profile:
	name = models.CharField('Name' , max_length = 150 , blank = True)
	type = models.CharField('Type' , max_length = 4 , choices = TYPES , default = '0')
	website = models.URLField('Website URL' , max_length = 300 , blank = True)

	# Location:
	country = models.CharField('Country' , max_length = 3 , choices = COUNTRIES , default = 'USA')
	stateTerritoryProvince = models.CharField('State/Territory/Province' , max_length = 6 , choices = STATES_TERRITORIES_PROVINCES , default = 'USA-CA')
	cityTown = models.CharField('City/Town' , max_length = 60 , blank = True)
	postalCode = models.CharField('Postal Code' , max_length = 15 , blank = True)
	address1 = models.CharField('Address (Line 1)' , max_length = 100 , blank = True)
	address2 = models.CharField('Address (Line 2)' , max_length = 100 , blank = True)

	# General Contact Info:
	email = models.EmailField('Email' , blank = True)
	phone = models.CharField('Phone Number (Format: 1-123-555-1234)' , max_length = 18 , blank = True)
	phoneTDD = models.CharField('TTD/TTY Phone Number (Format: 1-123-555-1234)' , max_length = 18 , blank = True)
	fax = models.CharField('Fax Number (Format: 1-123-555-1234)' , max_length = 18 , blank = True)
	contactForm = models.URLField('Contact Form URL' , max_length = 300 , blank = True)

	# Press Contact Info:
	pressEmail = models.EmailField('Press Email' , blank = True)
	pressPhone = models.CharField('Press Phone Number (Format: 1-123-555-1234)' , max_length = 18 , blank = True)
	pressContactForm = models.URLField('Press Contact Form URL' , max_length = 300 , blank = True)

	# Contents:
	aboutSummary = models.TextField('About/Summary' , max_length = 10000 , blank = True)
	complaintInfo1 = models.URLField('Complaint Information (URL 1)' , max_length = 300 , blank = True)
	complaintInfo2 = models.URLField('Complaint Information (URL 2)' , max_length = 300 , blank = True)
	complaintForm = models.URLField('Complaint Form URL' , max_length = 300 , blank = True)
	membersPage = models.URLField('Members Page URL' , max_length = 300 , blank = True)
	faqPage = models.URLField('FAQ Page URL' , max_length = 300 , blank = True)

	# Administrative:
	createdOn = models.DateTimeField('Record Created On' , auto_now_add = True)
	updatedOn = models.DateTimeField('Record Last Updated On' , auto_now = True)
	lastChangedBy = models.CharField('Last Changed By' , max_length = 50 , blank = True)
	delete = models.BooleanField('Delete' , default = False)
	daysUntilDeletion = models.IntegerField('Days Until Deletion' , default = 30)

	# Permissions:
	approved = models.BooleanField('Record Approved' , default = False)
	public = models.BooleanField('Record Public' , default = False)



	# Manage metadata:
	class Meta:
		verbose_name = 'Oversight Commission'
		verbose_name_plural = 'Oversight Commissions'
