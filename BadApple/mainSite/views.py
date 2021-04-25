from django.utils.translation import gettext as _
from django.shortcuts import redirect , render
from django.forms import TextInput
from mainSite.models import PRATemplate , OversightCommission , Tip , WeeklyStats , Officer , InvestigativeReport , InvestigativeReportFinding
from mainSite.forms import *
from random import choice
from datetime import datetime

# Import and configure BotBlock
from mainSite import BotBlock
BotBlock.encryptText = True


# Global Variables:
backgroundImages = ['img/andrew-ridley-jR4Zf-riEjI-unsplash.jpg' , 'img/ashkan-forouzani-5nwog4xjpNY-unsplash.jpg' , 'img/billy-huynh-W8KTS-mhFUE-unsplash.jpg' , 'img/bradley-jasper-ybanez-a1xlQq3HoJ0-unsplash.jpg' , 'img/clem-onojeghuo-Ud4GcZW3rOY-unsplash.jpg' , 'img/danist-bviex5lwf3s-unsplash.jpg' , 'img/denise-chan-pXmbsF70ulM-unsplash.jpg' , 'img/derek-thomson-NqJYQ3m_rVA-unsplash.jpg' , 'img/erfan-moradi-wKc-i5zwfok-unsplash.jpg' , 'img/fabio-ballasina-wEL2zPX3jDg-unsplash.jpg' , 'img/genessa-panainte-sBvK15KlpYk-unsplash.jpg' , 'img/henrik-donnestad-V6Qd6zA85ck-unsplash.jpg' , 'img/joel-filipe-WjnF1Tp-p3I-unsplash.jpg' , 'img/jr-korpa-SFT9G3pAxLY-unsplash.jpg' , 'img/kai-dahms-t--2nGjWLXc-unsplash.jpg' , 'img/lucas-benjamin-R79qkPYvrcM-unsplash.jpg' , 'img/lucas-benjamin-wQLAGv4_OYs-unsplash.jpg' , 'img/markus-spiske-Z7n-qSootxg-unsplash.jpg' , 'img/munmun-singh-xRwj5q7vSJ4-unsplash.jpg' , 'img/nareeta-martin-QP24FRmqDEc-unsplash.jpg' , 'img/paola-galimberti-Cawp7im-QMY-unsplash.jpg' , 'img/pawel-czerwinski-8PqU9b_cpbg-unsplash.jpg' , 'img/pawel-czerwinski-l8DUam8vtbc-unsplash.jpg' , 'img/rene-bohmer-YeUVDKZWSZ4-unsplash.jpg' , 'img/robert-katzki-jbtfM0XBeRc-unsplash.jpg' , 'img/rodion-kutsaev-pVoEPpLw818-unsplash.jpg' , 'img/sandro-katalina-k1bO_VTiZSs-unsplash.jpg' , 'img/scott-webb-FEQEQrF5M10-unsplash.jpg' , 'img/scott-webb-INeZJfQxMLE-unsplash.jpg' , 'img/scott-webb-l-TNipQzhRQ-unsplash.jpg' , 'img/scott-webb-lNxbROqJ8zo-unsplash.jpg' , 'img/scott-webb-wqh7V-nzhYo-unsplash.jpg' , 'img/sean-sinclair-C_NJKfnTR5A-unsplash.jpg' , 'img/sean-sinclair-FQ7cRFUU1y0-unsplash.jpg' , 'img/sora-sagano-C8lJ6WE5RNw-unsplash.jpg' , 'img/steve-johnson-ctRJMubyj4o-unsplash.jpg' , 'img/sylvia-szekely-YPW_SVDfJxk-unsplash.jpg' , 'img/thor-alvis-sgrCLKYdw5g-unsplash.jpg' , 'img/vinicius-amnx-amano-OHPdgstNFGs-unsplash.jpg' , 'img/wrongtog-PTIHdN4NDI8-unsplash.jpg' , 'img/zak-7wBFsHWQDlk-unsplash.jpg']


# Support Functions:
def incrementStat(originID):
	dateObj = datetime.today().isocalendar()
	statsObj = WeeklyStats.objects.get_or_create(week = dateObj[1] , year = dateObj[0])[0]

	if (originID == 0):
		statsObj.homeViews += 1
	elif (originID == 1):
		statsObj.documentationViews += 1
	elif (originID == 2):
		statsObj.praViews += 1
	elif (originID == 3):
		statsObj.oversightViews += 1
	elif (originID == 4):
		statsObj.commissionViews += 1
	elif (originID == 5):
		statsObj.tipViews += 1
	elif (originID == 6):
		statsObj.badAppleViews += 1
	elif (originID == 7):
		statsObj.praSearches += 1
	elif (originID == 8):
		statsObj.commissionSearches += 1
	elif (originID == 9):
		statsObj.tipSubmissions += 1
	elif (originID == 10):
		statsObj.badAppleSearches += 1
	elif (originID == 11):
		statsObj.officerViews += 1
	elif (originID == 12):
		statsObj.reportViews += 1

	statsObj.save()


# Request Handlers:

def home(request):
	incrementStat(0)
	return render(request , 'home.html' , {})


def documentation(request):
	incrementStat(1)
	return render(request , 'documentation.html' , {})


def pra(request):
	if (request.method == 'POST'):
		incrementStat(7)
		praForm = PRATemplateForm(request.POST)

		resultFound = False
		letterTitle = ''
		letterBody = ''
		if (praForm.is_valid()):
			try:
				templateObject = PRATemplate.objects.get(stateTerritoryProvince = praForm.cleaned_data['stateTerritoryProvince'] , subject = praForm.cleaned_data['subject'] , approved = True , public = True)
				resultFound = True
				letterTitle = str(templateObject.title)
				letterBody = str(templateObject.letterBody)
			except:
				return render(request , 'pra.html' , {'praForm' : praForm , 'showResults' : True , 'resultFound' : False , 'letterTitle' : letterTitle , 'letterBody' : letterBody})

		return render(request , 'pra.html' , {'praForm' : praForm , 'showResults' : True , 'resultFound' : resultFound , 'letterTitle' : letterTitle , 'letterBody' : letterBody})
	else:
		incrementStat(2)
		praForm = PRATemplateForm()
		return render(request , 'pra.html' , {'praForm' : praForm , 'showResults' : False})


def oversight(request):
	if (request.method == 'POST'):
		incrementStat(8)
		oversightForm = OversightCommissionForm(request.POST)

		resultFound = False
		if (oversightForm.is_valid()):
			if (len(oversightForm.cleaned_data['cityTown']) > 0):
				commissionObjects = OversightCommission.objects.filter(stateTerritoryProvince = oversightForm.cleaned_data['stateTerritoryProvince'] , cityTown__icontains = oversightForm.cleaned_data['cityTown'] , completed = True , approved = True , public = True).order_by('cityTown')
			else:
				commissionObjects = OversightCommission.objects.filter(stateTerritoryProvince = oversightForm.cleaned_data['stateTerritoryProvince'] , completed = True , approved = True , public = True).order_by('cityTown')

			if (len(commissionObjects) > 0):
				resultFound = True

			commissions = []
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
		incrementStat(3)
		oversightForm = OversightCommissionForm()
		return render(request , 'oversight.html' , {'oversightForm' : oversightForm , 'showResults' : False})


def commission(request , slug):
	try:
		commissionObject = OversightCommission.objects.get(commissionID = str(slug) , approved = True , public = True)
		incrementStat(4)
	except:
		return redirect('oversight')

	return render(request , 'commission.html' , {'image' : choice(backgroundImages) , 'name' : str(commissionObject.name) , 'type' : str(commissionObject.get_type_display()) , 'address1' : str(commissionObject.address1) , 'address2' : str(commissionObject.address2) , 'cityTown' : str(commissionObject.cityTown) , 'stateTerritoryProvince' : str(commissionObject.get_stateTerritoryProvince_display()) , 'email' : str(commissionObject.email) , 'phone' : str(commissionObject.phone) , 'ttdtty' : str(commissionObject.phoneTDD) , 'fax' : str(commissionObject.fax) , 'about' : str(commissionObject.aboutSummary).strip().split('\n') , 'website' : str(commissionObject.website) , 'contactForm' : str(commissionObject.contactForm) , 'pressForm' : str(commissionObject.pressContactForm) , 'complaintInfo1' : str(commissionObject.complaintInfo1) , 'complaintInfo2' : str(commissionObject.complaintInfo2) , 'complaintForm' : str(commissionObject.complaintForm) , 'alternateComplaintFormLabel' : str(commissionObject.get_alternateComplaintFormType_display()) , 'alternateComplaintForm' : str(commissionObject.alternateComplaintForm) , 'members' : str(commissionObject.membersPage) , 'faq' : str(commissionObject.faqPage) , 'updated' : str(commissionObject.updatedOn.strftime('%B %d, %Y'))})


def tip(request):
	databaseEntries = Tip.objects.filter(archived = False).count()
	if (databaseEntries >= 100):
		return render(request , 'tip.html' , {'errorMessage' : _('We are unable to accept new tips at the moment, as our tip database is currently full. Please try again soon.') , 'successMessage' : False , 'showForm' : False})

	if (request.method == 'POST'):
		incrementStat(9)
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
		incrementStat(5)
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
		incrementStat(10)
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
		incrementStat(6)
		badAppleForm = BadAppleForm()
		return render(request , 'badapple.html' , {'badAppleForm' : badAppleForm , 'showResults' : False , 'errorMessage' : False})


def officer(request , slug):
	try:
		officerObject = Officer.objects.get(officerID = str(slug) , approved = True , public = True)
		incrementStat(11)
	except:
		return redirect('badApple')

	reportObjects = InvestigativeReport.objects.filter(subjectOfInvestigation = officerObject , approved = True , public = True)

	reports = []
	sustainedFindings = []
	notSustainedFindings = []
	exoneratedFindings = []
	unfoundedFindings = []
	for report in reportObjects:
		reportDate = report.reportDate.strftime('%B %d, %Y')
		reports.append({'reportID' : report.reportID , 'reportDate' : reportDate})

		reportLocation = (report.cityTown + ', ' + report.get_stateTerritoryProvince_display())
		findings = InvestigativeReportFinding.objects.filter(investigativeReport = report , approved = True , public = True)
		for finding in findings:
			if (finding.finding == '0'):
				sustainedFindings.append({'category' : finding.get_findingPolicyCategory_display() , 'policy' : finding.findingBasis , 'location' : reportLocation , 'date' : reportDate , 'reportID' : report.reportID})
			elif (finding.finding == '1'):
				notSustainedFindings.append({'category' : finding.get_findingPolicyCategory_display() , 'policy' : finding.findingBasis , 'location' : reportLocation , 'date' : reportDate , 'reportID' : report.reportID})
			elif (finding.finding == '2'):
				exoneratedFindings.append({'category' : finding.get_findingPolicyCategory_display() , 'policy' : finding.findingBasis , 'location' : reportLocation , 'date' : reportDate , 'reportID' : report.reportID})
			elif (finding.finding == '3'):
				unfoundedFindings.append({'category' : finding.get_findingPolicyCategory_display() , 'policy' : finding.findingBasis , 'location' : reportLocation , 'date' : reportDate , 'reportID' : report.reportID})


	return render(request , 'officer.html' , {'firstName' : officerObject.firstName , 'middleName' : officerObject.middleName , 'lastName' : officerObject.lastName , 'reports' : reports , 'sustained' : sustainedFindings , 'notSustained' : notSustainedFindings , 'exonerated' : exoneratedFindings , 'unfounded' : unfoundedFindings , 'addedOn' : officerObject.createdOn.strftime('%B %d, %Y') , 'updatedOn' : officerObject.updatedOn.strftime('%B %d, %Y')})
