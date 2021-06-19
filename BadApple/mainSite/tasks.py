from celery.schedules import crontab
from mainSite.celery import app
from mainSite.models import DatabaseManagerPermissions , PRATemplate , OversightCommission , Officer , InvestigativeReport , InvestigativeReportFinding , Tip , EncryptedMessage , APIAccount
from gnupg import GPG


# Task scheduler:
@app.on_after_finalize.connect
def setup_periodic_tasks(sender , **kwargs):
	sender.add_periodic_task(crontab(minute = 0 , hour = 0) , deleteDatabaseEntries.s())
	sender.add_periodic_task(crontab(minute = 0 , hour = 0 , day_of_week = 'sunday') , databaseManagerRateLimitReset.s())
	sender.add_periodic_task(crontab(minute = 0 , hour = 0) , archiveTips.s())
	sender.add_periodic_task(crontab(minute = 0 , hour = 0 , day_of_week = 'sunday') , resetWeeklyAPIQueryCounter.s())


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

	for dbOfficerEntry in Officer.objects.filter(toBeDeleted = True):
		if (dbOfficerEntry.daysUntilDeletion <= 0):
			dbOfficerEntry.delete()
		else:
			dbOfficerEntry.daysUntilDeletion -= 1
			dbOfficerEntry.save()

	for dbInvestigativeReportEntry in InvestigativeReport.objects.filter(toBeDeleted = True):
		if (dbInvestigativeReportEntry.daysUntilDeletion <= 0):
			dbInvestigativeReportEntry.delete()
		else:
			dbInvestigativeReportEntry.daysUntilDeletion -= 1
			dbInvestigativeReportEntry.save()

	for dbInvestigativeReportFindingEntry in InvestigativeReportFinding.objects.filter(toBeDeleted = True):
		if (dbInvestigativeReportFindingEntry.daysUntilDeletion <= 0):
			dbInvestigativeReportFindingEntry.delete()
		else:
			dbInvestigativeReportFindingEntry.daysUntilDeletion -= 1
			dbInvestigativeReportFindingEntry.save()

	for tipObject in Tip.objects.filter(processed = True , archive = False):
		if (tipObject.daysUntilDeletion <= 0):
			tipObject.delete()
		else:
			tipObject.daysUntilDeletion -= 1
			tipObject.save()


@app.task
def databaseManagerRateLimitReset():
	for dbManagerObject in DatabaseManagerPermissions.objects.all():
		dbManagerObject.changesLastWeek = dbManagerObject.changesThisWeek
		dbManagerObject.changesThisWeek = 0
		dbManagerObject.save()


@app.task
def archiveTips():
	gpg = GPG(gnupghome = '/home/ubuntu/.gnupg/')
	gpg.encoding = 'utf-8'

	fingerprints = []
	for key in gpg.list_keys():
		fingerprints.append(key['fingerprint'])

	if (len(fingerprints) < 2):
		return

	for tipObject in Tip.objects.filter(archive = True , archived = False):
		for encryptedMessageObject in EncryptedMessage.objects.filter(parentTip = tipObject , messageIsArchived = False):
			if (not(encryptedMessageObject.primaryPubKeyFingerprint in fingerprints)):
				encryptedMessageObject.delete()
				continue

			fingerprints.remove(encryptedMessageObject.primaryPubKeyFingerprint)
			message = encryptedMessageObject.encryptedMessage
			for recipient in fingerprints:
				dualyEncryptedMessage = str(gpg.encrypt(message , recipient , always_trust = True))
				EncryptedMessage.objects.create(parentTip = tipObject , messageIsArchiged = True , primaryPubKeyFingerprint = encryptedMessageObject.primaryPubKeyFingerprint , secondaryPubKeyFingerprint = recipient , encryptedMessage = dualyEncryptedMessage)

			encryptedMessageObject.delete()

		tipObject.archived = True
		tipObject.save()


@app.task
def resetWeeklyAPIQueryCounter():
	for account in APIAccount.objects.filter(approved = True):
		account.currentWeek = 0
		account.save()
