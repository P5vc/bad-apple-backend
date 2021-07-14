from django.conf import settings
from django.db import models



class DatabaseManagerPermissions(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete = models.CASCADE)

	# Limits:
	changesThisWeek = models.IntegerField('Changes Made This Week (max = 10)' , default = 0)
	changesLastWeek = models.IntegerField('Changes Made Last Week (max = 10)' , default = 0)



	# Manage metadata:
	class Meta:
		verbose_name = 'Database Manager Permissions'
		verbose_name_plural = 'Database Manager Permissions'



class WeeklyStats(models.Model):
	# Identifiers:
	week = models.IntegerField('Week')
	year = models.IntegerField('Year')

	# Page View Stats:
	totalViews = models.IntegerField('Total Views' , default = 0)
	homeViews = models.IntegerField('Home Page Views' , default = 0)
	documentationViews = models.IntegerField('Learn More Page Views' , default = 0)
	praViews = models.IntegerField('PRA Templates Page Views' , default = 0)
	oversightViews = models.IntegerField('Oversight Lookup Page Views' , default = 0)
	commissionViews = models.IntegerField('Commission Page Views' , default = 0)
	tipViews = models.IntegerField('Tip Page Views' , default = 0)
	badAppleViews = models.IntegerField('Bad Apple Database Page Views' , default = 0)
	officerViews = models.IntegerField('Officer Page Views' , default = 0)
	reportViews = models.IntegerField('Report Page Views' , default = 0)
	apiDocumentationViews = models.IntegerField('API Documentation Page Views' , default = 0)

	# Action Stats:
	totalInteractions = models.IntegerField('Total Interactions' , default = 0)
	praSearches = models.IntegerField('PRA Template Searches' , default = 0)
	commissionSearches = models.IntegerField('Oversight Commission Searches' , default = 0)
	tipSubmissions = models.IntegerField('Tip Submissions' , default = 0)
	badAppleSearches = models.IntegerField('Bad Apple Database Searches' , default = 0)



	# Manage metadata:
	class Meta:
		verbose_name = 'Weekly Statistics'
		verbose_name_plural = 'Weekly Statistics'



class DatabaseDump(models.Model):
	# Choices:
	DATA_CATEGORIES = [
					('0' , 'Police Oversight Commissions')
			]

	# Parameters:
	dataCategory = models.CharField('Data to Dump' , max_length = 2 , choices = DATA_CATEGORIES , default = '0')



	# Manage metadata:
	class Meta:
		verbose_name = 'Database Dump'
		verbose_name_plural = 'Database Dump'



	# Override default save behavior, to ensure that the database is never touched:
	def save(self , *args , **kwargs):
		pass
