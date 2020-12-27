from django.db import models

class PRATemplate(models.Model):
	# Filters:
	state = models.CharField('State' , max_length = 30)
	entity = models.CharField('Entity' , max_length = 50 , default = 'Police')
	technology = models.CharField('Technology' , max_length = 50 , blank = True)

	# Template Contents:
	letterBody = models.TextField('Letter Body' , max_length = 10000 , blank = True)

	# Administrative:
	createdOn = models.DateTimeField('Template Created On (Auto-Filled)' , auto_now_add = True)
	updatedOn = models.DateTimeField('Template Last Updated On (Auto-Filled)' , auto_now = True)

	# Permissions:
	approved = models.BooleanField('Template Approved' , default = False)
	public = models.BooleanField('Template Public' , default = False)



class OversightCommission(models.Model):
	# Profile:
	name = models.CharField('Name' , max_length = 60 , blank = True)
	type = models.CharField('Type' , max_length = 60 , blank = True)
	website = models.URLField('Website URL' , max_length = 250)

	# Location:
	country = models.CharField('Country' , max_length = 60 , blank = True , default = 'United States of America')
	stateProvince = models.CharField('State/Province' , max_length = 60 , blank = True)
	cityTown = models.CharField('City/Town' , max_length = 60 , blank = True)
	postalCode = models.CharField('Postal Code' , max_length = 15 , blank = True)

	# Contact Info:
	email = models.EmailField('Email' , blank = True)
	phone = models.CharField('Phone Number' , max_length = 15 , blank = True)

	# Administrative:
	createdOn = models.DateTimeField('Record Created On (Auto-Filled)' , auto_now_add = True)
	updatedOn = models.DateTimeField('Record Last Updated On (Auto-Filled)' , auto_now = True)

	# Permissions:
	approved = models.BooleanField('Record Approved' , default = False)
	public = models.BooleanField('Record Public' , default = False)
