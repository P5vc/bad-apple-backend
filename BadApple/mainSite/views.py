from django.http import JsonResponse as DjangoJsonResponse
from django.utils.translation import gettext as _
from django.shortcuts import redirect , render
from django.forms import TextInput
from mainSite.models import PRATemplate , OversightCommission , Tip , WeeklyStats , Officer , InvestigativeReport , InvestigativeReportFinding , APIAccount
from mainSite.forms import *
import mainSite.extendedModels.modelCodes as modelCodes
from random import choice
from datetime import datetime

# Import and configure BotBlock:
from mainSite import BotBlock
BotBlock.encryptText = True


# Global Variables:

backgroundImages = ['img/andrew-ridley-jR4Zf-riEjI-unsplash.jpg' , 'img/ashkan-forouzani-5nwog4xjpNY-unsplash.jpg' , 'img/billy-huynh-W8KTS-mhFUE-unsplash.jpg' , 'img/bradley-jasper-ybanez-a1xlQq3HoJ0-unsplash.jpg' , 'img/clem-onojeghuo-Ud4GcZW3rOY-unsplash.jpg' , 'img/danist-bviex5lwf3s-unsplash.jpg' , 'img/denise-chan-pXmbsF70ulM-unsplash.jpg' , 'img/derek-thomson-NqJYQ3m_rVA-unsplash.jpg' , 'img/erfan-moradi-wKc-i5zwfok-unsplash.jpg' , 'img/fabio-ballasina-wEL2zPX3jDg-unsplash.jpg' , 'img/genessa-panainte-sBvK15KlpYk-unsplash.jpg' , 'img/henrik-donnestad-V6Qd6zA85ck-unsplash.jpg' , 'img/joel-filipe-WjnF1Tp-p3I-unsplash.jpg' , 'img/jr-korpa-SFT9G3pAxLY-unsplash.jpg' , 'img/kai-dahms-t--2nGjWLXc-unsplash.jpg' , 'img/lucas-benjamin-R79qkPYvrcM-unsplash.jpg' , 'img/lucas-benjamin-wQLAGv4_OYs-unsplash.jpg' , 'img/markus-spiske-Z7n-qSootxg-unsplash.jpg' , 'img/munmun-singh-xRwj5q7vSJ4-unsplash.jpg' , 'img/nareeta-martin-QP24FRmqDEc-unsplash.jpg' , 'img/paola-galimberti-Cawp7im-QMY-unsplash.jpg' , 'img/pawel-czerwinski-8PqU9b_cpbg-unsplash.jpg' , 'img/pawel-czerwinski-l8DUam8vtbc-unsplash.jpg' , 'img/rene-bohmer-YeUVDKZWSZ4-unsplash.jpg' , 'img/robert-katzki-jbtfM0XBeRc-unsplash.jpg' , 'img/rodion-kutsaev-pVoEPpLw818-unsplash.jpg' , 'img/sandro-katalina-k1bO_VTiZSs-unsplash.jpg' , 'img/scott-webb-FEQEQrF5M10-unsplash.jpg' , 'img/scott-webb-INeZJfQxMLE-unsplash.jpg' , 'img/scott-webb-l-TNipQzhRQ-unsplash.jpg' , 'img/scott-webb-lNxbROqJ8zo-unsplash.jpg' , 'img/scott-webb-wqh7V-nzhYo-unsplash.jpg' , 'img/sean-sinclair-C_NJKfnTR5A-unsplash.jpg' , 'img/sean-sinclair-FQ7cRFUU1y0-unsplash.jpg' , 'img/sora-sagano-C8lJ6WE5RNw-unsplash.jpg' , 'img/steve-johnson-ctRJMubyj4o-unsplash.jpg' , 'img/sylvia-szekely-YPW_SVDfJxk-unsplash.jpg' , 'img/thor-alvis-sgrCLKYdw5g-unsplash.jpg' , 'img/vinicius-amnx-amano-OHPdgstNFGs-unsplash.jpg' , 'img/wrongtog-PTIHdN4NDI8-unsplash.jpg' , 'img/zak-7wBFsHWQDlk-unsplash.jpg']


HOME_PAGE_ID              = 0
DOC_PAGE_ID               = 1
PRA_PAGE_ID               = 2
OVERSIGHT_PAGE_ID         = 3
COMMISSION_PAGE_ID        = 4
TIP_PAGE_ID               = 5
BAD_APPLE_PAGE_ID         = 6
PRA_SEARCH_PAGE_ID        = 7
COMMISSION_SEARCH_PAGE_ID = 8
TIP_SUBMISSION_PAGE_ID    = 9
BAD_APPLE_SEARCH_PAGE_ID  = 10
OFFICER_PAGE_ID           = 11
REPORT_PAGE_ID            = 12
API_DOC_PAGE_ID           = 13


# Support Functions:

def incrementStat(originID):
	dateObj = datetime.today().isocalendar()
	statsObj = WeeklyStats.objects.get_or_create(week = dateObj[1] , year = dateObj[0])[0]

	if originID == HOME_PAGE_ID:
		statsObj.homeViews += 1
		statsObj.totalViews += 1
	elif originID == DOC_PAGE_ID:
		statsObj.documentationViews += 1
		statsObj.totalViews += 1
	elif originID == PRA_PAGE_ID:
		statsObj.praViews += 1
		statsObj.totalViews += 1
	elif originID == OVERSIGHT_PAGE_ID:
		statsObj.oversightViews += 1
		statsObj.totalViews += 1
	elif originID == COMMISSION_PAGE_ID:
		statsObj.commissionViews += 1
		statsObj.totalViews += 1
	elif originID == TIP_PAGE_ID:
		statsObj.tipViews += 1
		statsObj.totalViews += 1
	elif originID == BAD_APPLE_PAGE_ID:
		statsObj.badAppleViews += 1
		statsObj.totalViews += 1
	elif originID == PRA_SEARCH_PAGE_ID:
		statsObj.praSearches += 1
		statsObj.totalInteractions += 1
	elif originID == COMMISSION_SEARCH_PAGE_ID:
		statsObj.commissionSearches += 1
		statsObj.totalInteractions += 1
	elif originID == TIP_SUBMISSION_PAGE_ID:
		statsObj.tipSubmissions += 1
		statsObj.totalInteractions += 1
	elif originID == BAD_APPLE_SEARCH_PAGE_ID:
		statsObj.badAppleSearches += 1
		statsObj.totalInteractions += 1
	elif originID == OFFICER_PAGE_ID:
		statsObj.officerViews += 1
		statsObj.totalViews += 1
	elif originID == REPORT_PAGE_ID:
		statsObj.reportViews += 1
		statsObj.totalViews += 1
	elif originID == API_DOC_PAGE_ID:
		statsObj.apiDocumentationViews += 1
		statsObj.totalViews += 1

	statsObj.save()


def JsonResponse(response):
	return DjangoJsonResponse(response, status=response['statusCode'])


# Request Handlers:

def home(request):
	incrementStat(HOME_PAGE_ID)
	return render(request , 'home.html' , {})


def documentation(request):
	incrementStat(DOC_PAGE_ID)
	return render(request , 'documentation.html' , {})


def pra(request):
	if (request.method == 'POST'):
		incrementStat(PRA_SEARCH_PAGE_ID)
		praForm = PRATemplateForm(request.POST)

		resultFound = False
		letterTitle = ''
		letterBody = ''
		if (praForm.is_valid()):
			try:
				STATES_WITH_PRAS = ['USA-AL' , 'USA-AZ' , 'USA-AR' , 'USA-CA' , 'USA-CO' , 'USA-CT' , 'USA-DE' , 'USA-FL' , 'USA-GA' , 'USA-HI' , 'USA-IL' , 'USA-IN' , 'USA-IA' , 'USA-KS' , 'USA-KY' , 'USA-LA' , 'USA-ME' , 'USA-MD' , 'USA-MA' , 'USA-MI' , 'USA-MN' , 'USA-MS' , 'USA-MO' , 'USA-NE' , 'USA-NJ' , 'USA-NM' , 'USA-NY' , 'USA-NC' , 'USA-ND' , 'USA-OH' , 'USA-OK' , 'USA-PA' , 'USA-RI' , 'USA-SC' , 'USA-SD' , 'USA-TN' , 'USA-TX' , 'USA-UT' , 'USA-VT' , 'USA-VA' , 'USA-WA' , 'USA-WV' , 'USA-WI']
				templateObjects = PRATemplate.objects.filter(stateTerritoryProvince = praForm.cleaned_data['stateTerritoryProvince'] , subject = praForm.cleaned_data['subject'] , approved = True , public = True)
				# Look for a specific template:
				if (templateObjects):
					templateObject = templateObjects[0]
					resultFound = True
					letterTitle = str(templateObject.title)
					letterBody = str(templateObject.letterBody)
				# If it doesn't exist, return a generic template (code: USA-00):
				else:
					if (praForm.cleaned_data['stateTerritoryProvince'] in STATES_WITH_PRAS):
						templateObject = PRATemplate.objects.get(stateTerritoryProvince = 'USA-00' , subject = praForm.cleaned_data['subject'] , approved = True , public = True)
						resultFound = True
						letterTitle = str(templateObject.title)
						letterBody = str(templateObject.letterBody)

			except:
				return render(request , 'pra.html' , {'praForm' : praForm , 'showResults' : True , 'resultFound' : False , 'letterTitle' : letterTitle , 'letterBody' : letterBody})

		return render(request , 'pra.html' , {'praForm' : praForm , 'showResults' : True , 'resultFound' : resultFound , 'letterTitle' : letterTitle , 'letterBody' : letterBody})
	else:
		incrementStat(PRA_PAGE_ID)
		praForm = PRATemplateForm()
		return render(request , 'pra.html' , {'praForm' : praForm , 'showResults' : False})


def oversight(request):
	if (request.method == 'POST'):
		incrementStat(COMMISSION_SEARCH_PAGE_ID)
		oversightForm = OversightCommissionForm(request.POST)

		resultFound = False
		commissions = []
		if (oversightForm.is_valid()):
			try:
				if (len(oversightForm.cleaned_data['cityTown']) > 0):
					commissionObjects = OversightCommission.objects.filter(stateTerritoryProvince = oversightForm.cleaned_data['stateTerritoryProvince'] , cityTown__icontains = oversightForm.cleaned_data['cityTown'] , completed = True , approved = True , public = True).order_by('cityTown')
				else:
					commissionObjects = OversightCommission.objects.filter(stateTerritoryProvince = oversightForm.cleaned_data['stateTerritoryProvince'] , completed = True , approved = True , public = True).order_by('cityTown')
			except:
				oversightForm = OversightCommissionForm()
				return render(request , 'oversight.html' , {'oversightForm' : oversightForm , 'showResults' : True , 'resultFound' : False , 'commissions' : commissions})

			if (len(commissionObjects) > 0):
				resultFound = True

			for commissionObject in commissionObjects:
				commission = {'image' : choice(backgroundImages) , 'commissionID' : '' , 'cityTown' : '' , 'commissionTitle' : '' , 'aboutText' : '' , 'websiteURL' : '.' , 'modificationDate' : ''}
				commission['commissionID'] = str(commissionObject.commissionID)
				commission['cityTown'] = str(commissionObject.cityTown)
				commission['commissionTitle'] = str(commissionObject.name)
				if (len(str(commissionObject.aboutSummary)) > 200):
					commission['aboutText'] = (str(commissionObject.aboutSummary)[:197] + '...')
				else:
					commission['aboutText'] = str(commissionObject.aboutSummary)
				if (len(commissionObject.website) > 0):
					commission['websiteURL'] = str(commissionObject.website)
				commission['modificationDate'] = str(commissionObject.updatedOn.strftime('%B %d, %Y'))

				commissions.append(commission)

		return render(request , 'oversight.html' , {'oversightForm' : oversightForm , 'showResults' : True , 'resultFound' : resultFound , 'commissions' : commissions})
	else:
		incrementStat(OVERSIGHT_PAGE_ID)
		oversightForm = OversightCommissionForm()
		return render(request , 'oversight.html' , {'oversightForm' : oversightForm , 'showResults' : False})


def commission(request , slug):
	try:
		commissionObject = OversightCommission.objects.get(commissionID = str(slug) , approved = True , public = True)
		incrementStat(COMMISSION_PAGE_ID)
	except:
		return redirect('oversight')

	return render(request , 'commission.html' , {'image' : choice(backgroundImages) , 'name' : str(commissionObject.name) , 'type' : str(commissionObject.get_type_display()) , 'address1' : str(commissionObject.address1) , 'address2' : str(commissionObject.address2) , 'cityTown' : str(commissionObject.cityTown) , 'stateTerritoryProvince' : str(commissionObject.get_stateTerritoryProvince_display()) , 'email' : str(commissionObject.email) , 'phone' : str(commissionObject.phone) , 'ttdtty' : str(commissionObject.phoneTDD) , 'fax' : str(commissionObject.fax) , 'about' : str(commissionObject.aboutSummary).strip().split('\n') , 'website' : str(commissionObject.website) , 'contactForm' : str(commissionObject.contactForm) , 'pressForm' : str(commissionObject.pressContactForm) , 'complaintInfo1' : str(commissionObject.complaintInfo1) , 'complaintInfo2' : str(commissionObject.complaintInfo2) , 'complaintForm' : str(commissionObject.complaintForm) , 'alternateComplaintFormLabel' : str(commissionObject.get_alternateComplaintFormType_display()) , 'alternateComplaintForm' : str(commissionObject.alternateComplaintForm) , 'members' : str(commissionObject.membersPage) , 'faq' : str(commissionObject.faqPage) , 'updated' : str(commissionObject.updatedOn.strftime('%B %d, %Y'))})


def tip(request):
	databaseEntries = Tip.objects.filter(processed = False , archived = False).count()
	if (databaseEntries >= 100):
		return render(request , 'tip.html' , {'errorMessage' : _('We are unable to accept new tips at the moment, as our tip database is currently full. Please try again soon.') , 'successMessage' : False , 'showForm' : False})

	if (request.method == 'POST'):
		incrementStat(TIP_SUBMISSION_PAGE_ID)
		if (databaseEntries >= 10):
			tipForm = TipFormCAPTCHA(request.POST)
			if (not(tipForm.is_valid())):
				captchaData = BotBlock.generate()
				imageData = captchaData['b64Image'].decode()
				newTipForm = TipFormCAPTCHA()
				newTipForm.fields['topic'].initial = tipForm.cleaned_data['topic']
				newTipForm.fields['message'].initial = tipForm.cleaned_data['message']
				newTipForm.fields['verificationText'].initial = captchaData['encryptedText'].decode()
				return render(request , 'tip.html' , {'errorMessage' : _('Form invalid. Please try again.') , 'successMessage' : False , 'showForm' : True , 'tipForm' : newTipForm , 'captcha' : True , 'b64Image' : imageData})

			if (len(tipForm.cleaned_data['topic']) <= 2):
				if (len(str(tipForm.cleaned_data['message'])) <= 10000):
					try:
						if (BotBlock.verify(str(tipForm.cleaned_data['captchaInput']) , str(tipForm.cleaned_data['verificationText']).encode())):
							Tip.objects.create(topic = str(tipForm.cleaned_data['topic']) , message = str(tipForm.cleaned_data['message']))
							return render(request , 'tip.html' , {'errorMessage' : False , 'successMessage' : _('Your tip has been successfully submitted.') , 'showForm' : False})
					except:
						captchaData = BotBlock.generate()
						imageData = captchaData['b64Image'].decode()
						newTipForm = TipFormCAPTCHA()
						newTipForm.fields['topic'].initial = tipForm.cleaned_data['topic']
						newTipForm.fields['message'].initial = tipForm.cleaned_data['message']
						newTipForm.fields['verificationText'].initial = captchaData['encryptedText'].decode()
						return render(request , 'tip.html' , {'errorMessage' : _('An unknown error occurred.') , 'successMessage' : False , 'showForm' : True , 'tipForm' : newTipForm , 'captcha' : True , 'b64Image' : imageData})
					else:
						captchaData = BotBlock.generate()
						imageData = captchaData['b64Image'].decode()
						newTipForm = TipFormCAPTCHA()
						newTipForm.fields['topic'].initial = tipForm.cleaned_data['topic']
						newTipForm.fields['message'].initial = tipForm.cleaned_data['message']
						newTipForm.fields['verificationText'].initial = captchaData['encryptedText'].decode()
						return render(request , 'tip.html' , {'errorMessage' : _('Incorrect CAPTCHA. Please try again.') , 'successMessage' : False , 'showForm' : True , 'tipForm' : newTipForm , 'captcha' : True , 'b64Image' : imageData})
			captchaData = BotBlock.generate()
			imageData = captchaData['b64Image'].decode()
			newTipForm = TipFormCAPTCHA()
			newTipForm.fields['topic'].initial = tipForm.cleaned_data['topic']
			newTipForm.fields['message'].initial = tipForm.cleaned_data['message']
			newTipForm.fields['verificationText'].initial = captchaData['encryptedText'].decode()
			return render(request , 'tip.html' , {'errorMessage' : _('Form invalid. Please try again.') , 'successMessage' : False , 'showForm' : True , 'tipForm' : newTipForm , 'captcha' : True , 'b64Image' : imageData})
		else:
			tipForm = TipForm(request.POST)
			if (not(tipForm.is_valid())):
				return render(request , 'tip.html' , {'errorMessage' : _('Form invalid. Please try again.') , 'successMessage' : False , 'showForm' : True , 'tipForm' : tipForm , 'captcha' : False})

			if (len(tipForm.cleaned_data['topic']) <= 2):
				if (len(str(tipForm.cleaned_data['message'])) <= 10000):
					Tip.objects.create(topic = str(tipForm.cleaned_data['topic']) , message = str(tipForm.cleaned_data['message']))
					return render(request , 'tip.html' , {'errorMessage' : False , 'successMessage' : _('Your tip has been successfully submitted.') , 'showForm' : False})

			return render(request , 'tip.html' , {'errorMessage' : _('Form invalid. Please try again.') , 'successMessage' : False , 'showForm' : True , 'tipForm' : tipForm , 'captcha' : False})

	else:
		incrementStat(TIP_PAGE_ID)
		captchaEnabled = False
		imageData = ''
		tipForm = TipForm()
		if (databaseEntries >= 10):
			captchaData = BotBlock.generate()
			imageData = captchaData['b64Image'].decode()

			tipForm = TipFormCAPTCHA()
			tipForm.fields['verificationText'].initial = captchaData['encryptedText'].decode()
			captchaEnabled = True

		return render(request , 'tip.html' , {'errorMessage' : False , 'successMessage' : False , 'showForm' : True , 'tipForm' : tipForm , 'captcha' : captchaEnabled , 'b64Image' : imageData})


def badApple(request):
	if (request.method == 'POST'):
		incrementStat(BAD_APPLE_SEARCH_PAGE_ID)
		badAppleForm = BadAppleForm(request.POST)

		resultFound = False
		errorMessage = False
		finalResults = []
		if (badAppleForm.is_valid()):
			numberFilled = 0
			for entry in badAppleForm.cleaned_data.values():
				if (entry):
					numberFilled += 1

			if (numberFilled < 2):
				return render(request , 'badapple.html' , {'badAppleForm' : badAppleForm , 'showResults' : resultFound , 'errorMessage' : _('Please fill in at least two fields.') , 'results' : finalResults})

			try:
				applicableOfficers = Officer.objects.filter(firstName__icontains = badAppleForm.cleaned_data['firstName'] , lastName__icontains = badAppleForm.cleaned_data['lastName'] , public = True , approved = True)

				applicableReports = []
				if (badAppleForm.cleaned_data['year']):
					applicableReports = InvestigativeReport.objects.filter(cityTown__icontains = badAppleForm.cleaned_data['cityTownCounty'] , stateTerritoryProvince__icontains = badAppleForm.cleaned_data['stateTerritoryProvince'] , incidentDate__year = int(badAppleForm.cleaned_data['year']) , subjectOfInvestigation__in = applicableOfficers , public = True , approved = True)
				else:
					applicableReports = InvestigativeReport.objects.filter(cityTown__icontains = badAppleForm.cleaned_data['cityTownCounty'] , stateTerritoryProvince__icontains = badAppleForm.cleaned_data['stateTerritoryProvince'] , subjectOfInvestigation__in = applicableOfficers , public = True , approved = True)

				applicableFindings = InvestigativeReportFinding.objects.filter(findingPolicyCategory__icontains = badAppleForm.cleaned_data['policyCategory'] , investigativeReport__in = applicableReports , public = True , approved = True)
			except:
				return render(request , 'badapple.html' , {'badAppleForm' : badAppleForm , 'showResults' : False , 'errorMessage' : _('An error occurred. Please try again.') , 'results' : finalResults})

			officers = set()
			for finding in applicableFindings:
				officers.add(finding.investigativeReport.subjectOfInvestigation)

			for currentOfficer in officers:
				officer = {'officerID' : '' , 'firstName' : '' , 'middleName' : '' , 'lastName' : '' , 'sustainedFindings' : 0 , 'notSustainedFindings' : 0 , 'exoneratedFindings' : 0 , 'unfoundedFindings' : 0 , 'reportLocations' : [] , 'reportDates' : []}

				officer['officerID'] = currentOfficer.officerID
				officer['firstName'] = currentOfficer.firstName
				officer['middleName'] = currentOfficer.middleName
				officer['lastName'] = currentOfficer.lastName

				for officerReport in InvestigativeReport.objects.filter(subjectOfInvestigation = currentOfficer , public = True , approved = True):
					reportLocation = (officerReport.cityTown + ', ' + officerReport.get_stateTerritoryProvince_display())
					officer['reportLocations'].append(reportLocation)
					officer['reportDates'].append(officerReport.reportDate.strftime('%B %d, %Y'))

					for reportFinding in InvestigativeReportFinding.objects.filter(investigativeReport = officerReport , public = True , approved = True):
						if (reportFinding.finding == '0'):
							officer['sustainedFindings'] += 1
						elif(reportFinding.finding == '1'):
							officer['notSustainedFindings'] += 1
						elif(reportFinding.finding == '2'):
							officer['exoneratedFindings'] += 1
						elif(reportFinding.findgin == '3'):
							officer['unfoundedFindings'] += 1

				finalResults.append(officer)

			if (finalResults):
				resultFound = True
			else:
				errorMessage = _('No results found.')

		else:
			errorMessage = _('Form invalid. Please try again.')

		return render(request , 'badapple.html' , {'badAppleForm' : badAppleForm , 'showResults' : resultFound , 'errorMessage' : errorMessage , 'results' : finalResults})
	else:
		incrementStat(BAD_APPLE_PAGE_ID)
		badAppleForm = BadAppleForm()
		return render(request , 'badapple.html' , {'badAppleForm' : badAppleForm , 'showResults' : False , 'errorMessage' : False})


def officer(request , slug):
	try:
		officerObject = Officer.objects.get(officerID = str(slug) , approved = True , public = True)
	except:
		return redirect('badApple')

	incrementStat(OFFICER_PAGE_ID)
	reportObjects = InvestigativeReport.objects.filter(subjectOfInvestigation = officerObject , approved = True , public = True)

	reports = []
	earliestReport = 'Unknown'
	latestReport = 'Unknown'
	knownLocations = set()
	knownBadgeNumbers = set()
	sustainedCounter = 0
	notSustainedCounter = 0
	exoneratedCounter = 0
	unfoundedCounter = 0
	lastUpdated = officerObject.updatedOn
	for report in reportObjects:
		if (report.updatedOn > lastUpdated):
			lastUpdated = report.updatedOn
		if (earliestReport == 'Unknown'):
			earliestReport = report.reportDate
			latestReport = report.reportDate
		else:
			if (report.reportDate < earliestReport):
				earliestReport = report.reportDate
			if (report.reportDate > latestReport):
				latestReport = report.reportDate

		reportLocation = (report.cityTown + ', ' + report.get_stateTerritoryProvince_display())
		reportDict = {'reportID' : report.reportID , 'reportType' : report.get_reportType_display() , 'reportLocation' : reportLocation , 'reportDate' : report.reportDate.strftime('%B %d, %Y') , 'sustained' : set() , 'notSustained' : set() , 'exonerated' : set() , 'unfounded' : set()}
		knownLocations.add(reportLocation)
		if (report.officerBadgeNumber):
			knownBadgeNumbers.add(report.officerBadgeNumber)

		findings = InvestigativeReportFinding.objects.filter(investigativeReport = report , approved = True , public = True)
		for finding in findings:
			if (finding.updatedOn > lastUpdated):
				lastUpdated = finding.updatedOn

			if (finding.finding == '0'):
				sustainedCounter += 1
				reportDict['sustained'].add(finding.get_findingPolicyCategory_display())
			elif (finding.finding == '1'):
				notSustainedCounter += 1
				reportDict['notSustained'].add(finding.get_findingPolicyCategory_display())
			elif (finding.finding == '2'):
				exoneratedCounter += 1
				reportDict['exonerated'].add(finding.get_findingPolicyCategory_display())
			elif (finding.finding == '3'):
				unfoundedCounter += 1
				reportDict['unfounded'].add(finding.get_findingPolicyCategory_display())

		reports.append(reportDict)

	if (earliestReport == 'Unknown'):
		earliestReport = _('Unknown')
		latestReport = _('Unknown')
	else:
		earliestReport = earliestReport.strftime('%B %d, %Y')
		latestReport = latestReport.strftime('%B %d, %Y')

	return render(request , 'officer.html' , {'firstName' : officerObject.firstName , 'middleName' : officerObject.middleName , 'lastName' : officerObject.lastName , 'locations' : knownLocations , 'badgeNumbers' : knownBadgeNumbers , 'addedOn' : officerObject.createdOn.strftime('%B %d, %Y') , 'updatedOn' : lastUpdated.strftime('%B %d, %Y') , 'sustained' : sustainedCounter , 'notSustained' : notSustainedCounter , 'exonerated' : exoneratedCounter , 'unfounded' : unfoundedCounter , 'earliestReport' : earliestReport , 'latestReport' : latestReport , 'reports' : reports})


def report(request , slug):
	try:
		reportObject = InvestigativeReport.objects.get(reportID = str(slug) , approved = True , public = True)

	except:
		return redirect('badApple')

	incrementStat(REPORT_PAGE_ID)
	sustainedFindings = []
	notSustainedFindings = []
	exoneratedFindings = []
	unfoundedFindings = []
	for finding in InvestigativeReportFinding.objects.filter(investigativeReport = reportObject , approved = True , public = True):
		if (finding.finding == '0'):
			sustainedFindings.append({'category' : finding.get_findingPolicyCategory_display() , 'policy' : finding.findingBasis , 'summary' : str(finding.findingSummary).strip().split('\n')})
		elif (finding.finding == '1'):
			notSustainedFindings.append({'category' : finding.get_findingPolicyCategory_display() , 'policy' : finding.findingBasis , 'summary' : str(finding.findingSummary).strip().split('\n')})
		elif (finding.finding == '2'):
			exoneratedFindings.append({'category' : finding.get_findingPolicyCategory_display() , 'policy' : finding.findingBasis , 'summary' : str(finding.findingSummary).strip().split('\n')})
		elif (finding.finding == '3'):
			unfoundedFindings.append({'category' : finding.get_findingPolicyCategory_display() , 'policy' : finding.findingBasis , 'summary' : str(finding.findingSummary).strip().split('\n')})


	reportLocation = (reportObject.cityTown + ', ' + reportObject.get_stateTerritoryProvince_display())
	subjectOfInvestigation = (reportObject.subjectOfInvestigation.firstName + ' ' + reportObject.subjectOfInvestigation.middleName + ' ' + reportObject.subjectOfInvestigation.lastName).strip()

	return render(request , 'report.html' , {'reportType' : reportObject.get_reportType_display() , 'investigationID' : reportObject.investigationID , 'location' : reportLocation , 'subject' : subjectOfInvestigation , 'officerID' : reportObject.subjectOfInvestigation.officerID , 'reportDate' : reportObject.reportDate.strftime('%B %d, %Y') , 'client' : reportObject.client , 'incidentDate' : reportObject.incidentDate.strftime('%B %d, %Y') , 'investigator' : reportObject.investigator , 'license' : reportObject.license , 'employer' : reportObject.investigatorEmployer , 'summary' : str(reportObject.findingsSummary).strip().split('\n') , 'conclusion' : str(reportObject.conclusion).strip().split('\n') , 'reportURL' : reportObject.fullReportURL , 'archiveURL' : reportObject.fullArchiveURL , 'praURL' : reportObject.praURL , 'source' : reportObject.sourceURL , 'added' : reportObject.createdOn.strftime('%B %d, %Y') , 'sustained' : sustainedFindings , 'notSustained' : notSustainedFindings , 'exonerated' : exoneratedFindings , 'unfounded' : unfoundedFindings})


def apiDocumentation(request):
	incrementStat(API_DOC_PAGE_ID)
	return render(request , 'api.html' , {})


def apiQuery(request , slug):
	response = {'statusCode' : 403}

	if (request.method == 'GET'):
		if (not(slug in ['PRA' , 'Oversight' , 'BA'])):
			response['statusCode'] = 404
			return JsonResponse(response)

		if 'API-Key' not in request.headers.keys():
			response['statusCode'] = 423
			return JsonResponse(response)
		else:
			providedAPIKey = str(request.headers['API-Key'])
			if (len(providedAPIKey) == 36):
				try:
					correspondingAccount = APIAccount.objects.get(apiKey = providedAPIKey , approved = True)
					if (slug == 'BA'):
						if ((correspondingAccount.currentWeek + 2) >= correspondingAccount.weeklyQueryLimit):
							response['statusCode'] = 429
							response['statusMessage'] = 'You have reached your weekly query limit.'
							return JsonResponse(response)
						correspondingAccount.currentWeek += 3
						correspondingAccount.totalQueries += 3
					else:
						if (correspondingAccount.currentWeek >= correspondingAccount.weeklyQueryLimit):
							response['statusCode'] = 429
							response['statusMessage'] = 'You have reached your weekly query limit.'
							return JsonResponse(response)
						correspondingAccount.currentWeek += 1
						correspondingAccount.totalQueries += 1
					correspondingAccount.save()
				except:
					return JsonResponse(response)

				response['statusMessage'] = ''
				response['results'] = []
				response['remainingQueries'] = (correspondingAccount.weeklyQueryLimit - correspondingAccount.currentWeek)

				for item in request.headers.items():
					if (len(item[1]) > 100):
						response['statusCode'] = 400
						response['statusMessage'] = 'Invalid header: too long'
						return JsonResponse(response)
					elif (len(item[1]) <= 0):
						if ((not(item[0] == 'Content-Type')) and (not(item[0] == 'Content-Length'))):
							response['statusCode'] = 400
							response['statusMessage'] = 'Invalid header: too short'
							return JsonResponse(response)

				if (slug == 'PRA'):
					if (('State' in request.headers.keys()) and ('Subject' in request.headers.keys())):
						state = str(request.headers['State'])
						subject = str(request.headers['Subject'])
						stateFound = False
						for stateCode in modelCodes.STATES_TERRITORIES_PROVINCES:
							if (state == stateCode[0]):
								stateFound = True
								break
						subjectFound = False
						for subjectCode in modelCodes.PRA_SUBJECTS:
							if (subject == subjectCode[0]):
								subjectFound = True
								break
						if ((stateFound) and (subjectFound)):
							praTemplateObjects = PRATemplate.objects.filter(stateTerritoryProvince = state , subject = subject , approved = True , public = True)
							if (not(praTemplateObjects)):
								STATES_WITH_PRAS = ['USA-AL' , 'USA-AZ' , 'USA-AR' , 'USA-CA' , 'USA-CO' , 'USA-CT' , 'USA-DE' , 'USA-FL' , 'USA-GA' , 'USA-HI' , 'USA-IL' , 'USA-IN' , 'USA-IA' , 'USA-KS' , 'USA-KY' , 'USA-LA' , 'USA-ME' , 'USA-MD' , 'USA-MA' , 'USA-MI' , 'USA-MN' , 'USA-MS' , 'USA-MO' , 'USA-NE' , 'USA-NJ' , 'USA-NM' , 'USA-NY' , 'USA-NC' , 'USA-ND' , 'USA-OH' , 'USA-OK' , 'USA-PA' , 'USA-RI' , 'USA-SC' , 'USA-SD' , 'USA-TN' , 'USA-TX' , 'USA-UT' , 'USA-VT' , 'USA-VA' , 'USA-WA' , 'USA-WV' , 'USA-WI']
								if (state in STATES_WITH_PRAS):
									praTemplateObjects = PRATemplate.objects.filter(stateTerritoryProvince = 'USA-00' , subject = subject , approved = True , public = True)
								else:
									praTemplateObjects = []
							for praTemplate in praTemplateObjects:
								tempItem = {}
								tempItem['country'] = praTemplate.get_country_display()
								tempItem['stateTerritoryProvince'] = praTemplate.get_stateTerritoryProvince_display()
								tempItem['subject'] = praTemplate.get_subject_display()
								tempItem['title'] = praTemplate.title
								tempItem['letterBody'] = praTemplate.letterBody
								tempItem['createdOn'] = str(praTemplate.createdOn)
								tempItem['updatedOn'] = str(praTemplate.updatedOn)
								response['results'].append(tempItem)
							response['statusCode'] = 200
							response['statusMessage'] = 'Success'
							return JsonResponse(response)
						else:
							response['statusCode'] = 400
							response['statusMessage'] = 'The provided "State" and "Subject" filters are invalid.'
							return JsonResponse(response)
					else:
						response['statusCode'] = 400
						response['statusMessage'] = 'This resource requires the use of "State" and "Subject" filters.'
						return JsonResponse(response)
				elif (slug == 'Oversight'):
					if ('State' in request.headers.keys()):
						state = str(request.headers['State'])
						stateFound = False
						for stateCode in modelCodes.STATES_TERRITORIES_PROVINCES:
							if (state == stateCode[0]):
								stateFound = True
								break
						if (stateFound):
							if ('City' in request.headers.keys()):
								city = str(request.headers['City'])
								if (len(city) < 2):
									response['statusCode'] = 400
									response['statusMessage'] = 'The provided "City" filter is invalid.'
									return JsonResponse(response)
								commissionObjects = OversightCommission.objects.filter(stateTerritoryProvince = state , cityTown__icontains = city , approved = True , public = True)
							else:
								commissionObjects = OversightCommission.objects.filter(stateTerritoryProvince = state , approved = True , public = True)
							for commission in commissionObjects:
								tempItem = {}
								tempItem['name'] = commission.name
								tempItem['type'] = commission.get_type_display()
								tempItem['website'] = commission.website
								tempItem['country'] = commission.get_country_display()
								tempItem['stateTerritoryProvince'] = commission.get_stateTerritoryProvince_display()
								tempItem['cityTown'] = commission.cityTown
								tempItem['postalCode'] = commission.postalCode
								tempItem['address1'] = commission.address1
								tempItem['address2'] = commission.address2
								tempItem['email'] = commission.email
								tempItem['phone'] = commission.phone
								tempItem['phoneTDD'] = commission.phoneTDD
								tempItem['fax'] = commission.fax
								tempItem['contactForm'] = commission.contactForm
								tempItem['pressEmail'] = commission.pressEmail
								tempItem['pressPhone'] = commission.pressPhone
								tempItem['pressContactForm'] = commission.pressContactForm
								tempItem['aboutSummary'] = commission.aboutSummary
								tempItem['complaintInfo1'] = commission.complaintInfo1
								tempItem['complaintInfo2'] = commission.complaintInfo2
								tempItem['complaintForm'] = commission.complaintForm
								tempItem['alternateComplaintFormType'] = commission.get_alternateComplaintFormType_display()
								tempItem['alternateComplaintForm'] = commission.alternateComplaintForm
								tempItem['membersPage'] = commission.membersPage
								tempItem['faqPage'] = commission.faqPage
								tempItem['commissionID'] = commission.commissionID
								tempItem['createdOn'] = str(commission.createdOn)
								tempItem['updatedOn'] = str(commission.updatedOn)
								response['results'].append(tempItem)
							response['statusCode'] = 200
							response['statusMessage'] = 'Success'
							return JsonResponse(response)
						else:
							response['statusCode'] = 400
							response['statusMessage'] = 'The provided "State" filter is invalid.'
							return JsonResponse(response)
					else:
						response['statusCode'] = 400
						response['statusMessage'] = 'This resource requires the use of the "State" filter.'
						return JsonResponse(response)
				elif (slug == 'BA'):
					if ('First' in request.headers.keys()):
						firstName = request.headers['First']
						if (not(len(firstName) >= 2)):
							response['statusCode'] = 400
							response['statusMessage'] = 'The provided "First" filter is invalid.'
							return JsonResponse(response)
					else:
						firstName = ''

					if ('Last' in request.headers.keys()):
						lastName = request.headers['Last']
						if (not(len(lastName) >= 2)):
							response['statusCode'] = 400
							response['statusMessage'] = 'The provided "Last" filter is invalid.'
							return JsonResponse(response)
					else:
						lastName = ''

					if ('City' in request.headers.keys()):
						city = request.headers['City']
						if (not(len(city) >= 2)):
							response['statusCode'] = 400
							response['statusMessage'] = 'The provided "City" filter is invalid.'
							return JsonResponse(response)
					else:
						city = ''

					if ('State' in request.headers.keys()):
						state = str(request.headers['State'])
						stateFound = False
						for stateCode in modelCodes.STATES_TERRITORIES_PROVINCES:
							if (state == stateCode[0]):
								stateFound = True
								break
						if (not(stateFound)):
							response['statusCode'] = 400
							response['statusMessage'] = 'The provided "State" filter is invalid.'
							return JsonResponse(response)
					else:
						state = ''

					if ('Incident-Year' in request.headers.keys()):
						try:
							incidentYear = int(request.headers['Incident-Year'])
							if (not((incidentYear > 1800) and (incidentYear < 2100))):
								response['statusCode'] = 400
								response['statusMessage'] = 'The provided "Incident-Year" filter is invalid.'
								return JsonResponse(response)
						except:
							response['statusCode'] = 400
							response['statusMessage'] = 'The provided "Incident-Year" filter is invalid.'
							return JsonResponse(response)
					else:
						incidentYear = False

					if ('Policy' in request.headers.keys()):
						policy = str(request.headers['Policy'])
						policyFound = False
						for policyCode in modelCodes.POLICY_CATEGORIES:
							if (policy == policyCode[0]):
								policyFound = True
								break
						if (not(policyFound)):
							response['statusCode'] = 400
							response['statusMessage'] = 'The provided "Policy" filter is invalid.'
							return JsonResponse(response)
					else:
						policy = ''

					if ('Report-ID' in request.headers.keys()):
						reportID = request.headers['Report-ID']
						if (len(reportID) != 36):
							response['statusCode'] = 400
							response['statusMessage'] = 'The provided "Report-ID" filter is invalid.'
							return JsonResponse(response)
					else:
						reportID = ''

					try:
						applicableOfficers = Officer.objects.filter(firstName__icontains = firstName , lastName__icontains = lastName , public = True , approved = True)

						applicableReports = []
						if (incidentYear):
							applicableReports = InvestigativeReport.objects.filter(cityTown__icontains = city , stateTerritoryProvince__icontains = state , reportID__icontains = reportID , incidentDate__year = incidentYear , subjectOfInvestigation__in = applicableOfficers , public = True , approved = True)
						else:
							applicableReports = InvestigativeReport.objects.filter(cityTown__icontains = city , stateTerritoryProvince__icontains = state , reportID__icontains = reportID , subjectOfInvestigation__in = applicableOfficers , public = True , approved = True)

						applicableFindings = InvestigativeReportFinding.objects.filter(findingPolicyCategory__icontains = policy , investigativeReport__in = applicableReports , public = True , approved = True)
					except:
						response['statusCode'] = 400
						response['statusMessage'] = 'The query could not be completed.'
						return JsonResponse(response)

					reports = set()
					for finding in applicableFindings:
						reports.add(finding.investigativeReport)

					for report in reports:
						tempResult = {}
						tempResult['officerFirstName'] = report.subjectOfInvestigation.firstName
						tempResult['officerMiddleName'] = report.subjectOfInvestigation.middleName
						tempResult['officerLastName'] = report.subjectOfInvestigation.lastName
						tempResult['officerID'] = report.subjectOfInvestigation.officerID
						tempResult['country'] = report.get_country_display()
						tempResult['state'] = report.get_stateTerritoryProvince_display()
						tempResult['city'] = report.cityTown
						tempResult['investigator'] = report.investigator
						tempResult['investigatorLicense'] = report.license
						tempResult['investigatorEmployer'] = report.investigatorEmployer
						tempResult['reportType'] = report.get_reportType_display()
						tempResult['investigationID'] = report.investigationID
						tempResult['officerBadgeNumber'] = report.officerBadgeNumber
						tempResult['incidentDate'] = str(report.incidentDate)
						tempResult['reportDate'] = str(report.reportDate)
						tempResult['findingsSummary'] = report.findingsSummary
						tempResult['conclusion'] = report.conclusion
						tempResult['fullReportURL'] = report.fullReportURL
						tempResult['fullArchiveURL'] = report.fullArchiveURL
						tempResult['sourceURL'] = report.sourceURL
						tempResult['praURL'] = report.praURL
						tempResult['reportID'] = report.reportID
						tempResult['createdOn'] = str(report.createdOn)
						tempResult['updatedOn'] = str(report.updatedOn)
						tempResult['findings'] = []
						for finding in InvestigativeReportFinding.objects.filter(investigativeReport = report , public = True , approved = True):
							tempFinding = {}
							tempFinding['findingPolicyCategory'] = finding.get_findingPolicyCategory_display()
							tempFinding['findingSummary'] = finding.findingSummary
							tempFinding['findingBasis'] = finding.findingBasis
							tempFinding['finding'] = finding.get_finding_display()
							tempFinding['createdOn'] = str(finding.createdOn)
							tempFinding['updatedOn'] = str(finding.updatedOn)
							tempResult['findings'].append(tempFinding)
						response['results'].append(tempResult)

					response['statusCode'] = 200
					response['statusMessage'] = 'Success'
					return JsonResponse(response)
				else:
					response['statusCode'] = 404
					return JsonResponse(response)
			else:
				response['statusCode'] = 400
				return JsonResponse(response)
	else:
		response['statusCode'] = 405
		return JsonResponse(response)
