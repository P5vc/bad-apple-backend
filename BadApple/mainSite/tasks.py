from celery.schedules import crontab
from .celery import app
from .models import DatabaseManagerPermissions , PRATemplate , OversightCommission


# Task scheduler:
@app.on_after_finalize.connect
def setup_periodic_tasks(sender , **kwargs):
	sender.add_periodic_task(crontab(minute = 0 , hour = 0) , deleteDatabaseEntries.s())
	sender.add_periodic_task(crontab(minute = 0 , hour = 0 , day_of_week = 'sunday') , databaseManagerRateLimitReset.s())


# Tasks:
@app.task
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


@app.task
def databaseManagerRateLimitReset():
	for dbManagerObject in DatabaseManagerPermissions.objects.all():
		dbManagerObject.changesLastWeek = dbManagerObject.changesThisWeek
		dbManagerObject.changesThisWeek = 0
		dbManagerObject.save()
