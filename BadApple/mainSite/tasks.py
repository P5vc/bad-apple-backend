from .models import DatabaseManagerPermissions , PRATemplate , OversightCommission
from celery.decorators import periodic_task
from celery.task.schedules import crontab


@periodic_task(run_every = (crontab(minute = 0 , hour = 0)) , name = 'deleteDatabaseEntries' , ignore_result = True)
def deleteDatabaseEntries():
	for dbPRATemplateEntry in PRATemplate.objects.filter(delete = True):
		dbPRATemplateEntry.daysUntilDeletion -= 1
		if (dbPRATemplateEntry.daysUntilDeletion < 0):
			dbPRATemplateEntry.delete()
		else:
			dbPRATemplateEntry.save()

	for dbOversightCommissionEntry in OversightCommission.objects.filter(delete = True):
		dbOversightCommissionEntry.daysUntilDeletion -= 1
		if (dbOversightCommissionEntry.daysUntilDeletion < 0):
			dbOversightCommissionEntry.delete()
		else:
			dbOversightCommissionEntry.save()


@periodic_task(run_every = (crontab(minute = 0 , hour = 0 , day_of_week = 'sunday')) , name = 'databaseManagerRateLimitReset' , ignore_result = True)
def databaseManagerRateLimitReset():
	for dbManagerObject in DatabaseManagerPermissions.objects.all():
		dbManagerObject.changesLastWeek = dbManagerObject.changesThisWeek
		dbManagerObject.changesThisWeek = 0
		dbManagerObject.save()
