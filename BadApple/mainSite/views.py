from django.utils.translation import gettext as _
from django.shortcuts import redirect , render
from django.forms import TextInput
from mainSite.models import PRATemplate , OversightCommission , Tip
from mainSite.forms import PRATemplateForm , OversightCommissionForm , TipForm , TipFormCAPTCHA
from random import choice

# Import and configure BotBlock
from mainSite import BotBlock
BotBlock.encryptText = True


# Global Variables:
backgroundImages = ['img/andrew-ridley-jR4Zf-riEjI-unsplash.jpg' , 'img/ashkan-forouzani-5nwog4xjpNY-unsplash.jpg' , 'img/billy-huynh-W8KTS-mhFUE-unsplash.jpg' , 'img/bradley-jasper-ybanez-a1xlQq3HoJ0-unsplash.jpg' , 'img/clem-onojeghuo-Ud4GcZW3rOY-unsplash.jpg' , 'img/danist-bviex5lwf3s-unsplash.jpg' , 'img/denise-chan-pXmbsF70ulM-unsplash.jpg' , 'img/derek-thomson-NqJYQ3m_rVA-unsplash.jpg' , 'img/erfan-moradi-wKc-i5zwfok-unsplash.jpg' , 'img/fabio-ballasina-wEL2zPX3jDg-unsplash.jpg' , 'img/genessa-panainte-sBvK15KlpYk-unsplash.jpg' , 'img/henrik-donnestad-V6Qd6zA85ck-unsplash.jpg' , 'img/joel-filipe-WjnF1Tp-p3I-unsplash.jpg' , 'img/jr-korpa-SFT9G3pAxLY-unsplash.jpg' , 'img/kai-dahms-t--2nGjWLXc-unsplash.jpg' , 'img/lucas-benjamin-R79qkPYvrcM-unsplash.jpg' , 'img/lucas-benjamin-wQLAGv4_OYs-unsplash.jpg' , 'img/markus-spiske-Z7n-qSootxg-unsplash.jpg' , 'img/munmun-singh-xRwj5q7vSJ4-unsplash.jpg' , 'img/nareeta-martin-QP24FRmqDEc-unsplash.jpg' , 'img/paola-galimberti-Cawp7im-QMY-unsplash.jpg' , 'img/pawel-czerwinski-8PqU9b_cpbg-unsplash.jpg' , 'img/pawel-czerwinski-l8DUam8vtbc-unsplash.jpg' , 'img/rene-bohmer-YeUVDKZWSZ4-unsplash.jpg' , 'img/robert-katzki-jbtfM0XBeRc-unsplash.jpg' , 'img/rodion-kutsaev-pVoEPpLw818-unsplash.jpg' , 'img/sandro-katalina-k1bO_VTiZSs-unsplash.jpg' , 'img/scott-webb-FEQEQrF5M10-unsplash.jpg' , 'img/scott-webb-INeZJfQxMLE-unsplash.jpg' , 'img/scott-webb-l-TNipQzhRQ-unsplash.jpg' , 'img/scott-webb-lNxbROqJ8zo-unsplash.jpg' , 'img/scott-webb-wqh7V-nzhYo-unsplash.jpg' , 'img/sean-sinclair-C_NJKfnTR5A-unsplash.jpg' , 'img/sean-sinclair-FQ7cRFUU1y0-unsplash.jpg' , 'img/sora-sagano-C8lJ6WE5RNw-unsplash.jpg' , 'img/steve-johnson-ctRJMubyj4o-unsplash.jpg' , 'img/sylvia-szekely-YPW_SVDfJxk-unsplash.jpg' , 'img/thor-alvis-sgrCLKYdw5g-unsplash.jpg' , 'img/vinicius-amnx-amano-OHPdgstNFGs-unsplash.jpg' , 'img/wrongtog-PTIHdN4NDI8-unsplash.jpg' , 'img/zak-7wBFsHWQDlk-unsplash.jpg']


def home(request):
	return render(request , 'home.html' , {})


def documentation(request):
	return render(request , 'documentation.html' , {})


def pra(request):
	if (request.method == 'POST'):
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
		praForm = PRATemplateForm()
		return render(request , 'pra.html' , {'praForm' : praForm , 'showResults' : False})


def oversight(request):
	if (request.method == 'POST'):
		oversightForm = OversightCommissionForm(request.POST)

		resultFound = False
		if (oversightForm.is_valid()):
			if (len(oversightForm.cleaned_data['cityTown']) > 0):
				commissionObjects = OversightCommission.objects.filter(stateTerritoryProvince = oversightForm.cleaned_data['stateTerritoryProvince'] , cityTown__icontains = oversightForm.cleaned_data['cityTown'] , completed = True , approved = True , public = True)
			else:
				commissionObjects = OversightCommission.objects.filter(stateTerritoryProvince = oversightForm.cleaned_data['stateTerritoryProvince'] , completed = True , approved = True , public = True)

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
		oversightForm = OversightCommissionForm()
		return render(request , 'oversight.html' , {'oversightForm' : oversightForm , 'showResults' : False})


def commission(request , slug):
	try:
		commissionObject = OversightCommission.objects.get(commissionID = str(slug) , approved = True , public = True)
	except:
		return redirect('oversight')

	return render(request , 'commission.html' , {'image' : choice(backgroundImages) , 'name' : str(commissionObject.name) , 'type' : str(commissionObject.get_type_display()) , 'address1' : str(commissionObject.address1) , 'address2' : str(commissionObject.address2) , 'cityTown' : str(commissionObject.cityTown) , 'stateTerritoryProvince' : str(commissionObject.get_stateTerritoryProvince_display()) , 'email' : str(commissionObject.email) , 'phone' : str(commissionObject.phone) , 'ttdtty' : str(commissionObject.phoneTDD) , 'fax' : str(commissionObject.fax) , 'about' : str(commissionObject.aboutSummary).strip().split('\n') , 'website' : str(commissionObject.website) , 'contactForm' : str(commissionObject.contactForm) , 'pressForm' : str(commissionObject.pressContactForm) , 'complaintInfo1' : str(commissionObject.complaintInfo1) , 'complaintInfo2' : str(commissionObject.complaintInfo2) , 'complaintForm' : str(commissionObject.complaintForm) , 'members' : str(commissionObject.membersPage) , 'faq' : str(commissionObject.faqPage) , 'updated' : str(commissionObject.updatedOn.strftime('%B %d, %Y'))})


def tip(request):
	databaseEntries = Tip.objects.filter(archived = False).count()
	if (databaseEntries >= 100):
		return render(request , 'tip.html' , {'errorMessage' : _('We are unable to accept new tips at the moment, as our tip database is currently full. Please try again soon.') , 'successMessage' : False , 'showForm' : False})

	if (request.method == 'POST'):
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
	return render(request , 'badapple.html' , {})
