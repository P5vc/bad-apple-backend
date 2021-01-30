from celery.schedules import crontab
from mainSite.celery import app
from mainSite.models import DatabaseManagerPermissions , PRATemplate , OversightCommission


# Task scheduler:
@app.on_after_finalize.connect
def setup_periodic_tasks(sender , **kwargs):
	sender.add_periodic_task(crontab(minute = 0 , hour = 0) , deleteDatabaseEntries.s())
	sender.add_periodic_task(crontab(minute = 0 , hour = 0 , day_of_week = 'sunday') , databaseManagerRateLimitReset.s())


# Tasks:
@app.task
def deleteDatabaseEntries():
	for dbPRATemplateEntry in PRATemplate.objects.filter(toBeDeleted = True):
		if (dbPRATemplateEntry.daysUntilDeletion <= 0):
			dbPRATemplateEntry.delete()
		else:
			dbPRATemplateEntry.daysUntilDeletion -= 1
			dbPRATemplateEntry.save()

	for dbOversightCommissionEntry in OversightCommission.objects.filter(toBeDeleted = True):
		if (dbOversightCommissionEntry.daysUntilDeletion <= 0):
			dbOversightCommissionEntry.delete()
		else:
			dbOversightCommissionEntry.daysUntilDeletion -= 1
			dbOversightCommissionEntry.save()


@app.task
def databaseManagerRateLimitReset():
	for dbManagerObject in DatabaseManagerPermissions.objects.all():
		dbManagerObject.changesLastWeek = dbManagerObject.changesThisWeek
		dbManagerObject.changesThisWeek = 0
		dbManagerObject.save()
