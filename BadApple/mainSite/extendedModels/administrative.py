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
	def save(self, *args, **kwargs):
		pass
