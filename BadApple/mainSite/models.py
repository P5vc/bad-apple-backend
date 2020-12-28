from django.db import models
from django.conf import settings

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
	ENTITIES = [
				('PD' , 'Police Department'),
				('SD' , 'Sheriff\'s Department')
				]
	SUBJECTS = [
					('0' , 'Body Cameras'),
					('1' , 'Drones'),
					('2' , 'Facial Recognition'),
					('3' , 'Thermographic Cameras'),
					('4' , 'License Plate Readers'),
					('5' , 'Memorandas of Understanding'),
					('6' , 'Predictive Policing'),
					('7' , 'ShotSpotter'),
					('8' , 'Social Media Monitoring'),
					('9' , 'Stingray')
					]

	# Filters:
	state = models.CharField('State' , max_length = 30)
	entity = models.CharField('Entity' , max_length = 2 , choices = ENTITIES , default = 'PD')
	subject = models.CharField('Subject' , max_length = 4 , choices = SUBJECTS , default = '0')

	# Template Contents:
	letterBody = models.TextField('Letter Body' , max_length = 10000 , blank = True)

	# Administrative:
	createdOn = models.DateTimeField('Template Created On (Auto-Filled)' , auto_now_add = True)
	updatedOn = models.DateTimeField('Template Last Updated On (Auto-Filled)' , auto_now = True)
	lastChangedBy = models.CharField('Last Changed By' , max_length = 50 , blank = True)
	delete = models.BooleanField('Delete' , default = False)
	daysUntilDeletion = models.IntegerField('Days Until Deletion' , default = 30)

	# Permissions:
	approved = models.BooleanField('Template Approved' , default = False)
	public = models.BooleanField('Template Public' , default = False)



	# Manage metadata:
	class Meta:
		verbose_name = 'PRA Template'
		verbose_name_plural = 'PRA Templates'



class OversightCommission(models.Model):
	# Profile:
	name = models.CharField('Name' , max_length = 60 , blank = True)
	type = models.CharField('Type' , max_length = 60 , blank = True)
	website = models.URLField('Website URL' , max_length = 250 , blank = True)

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
