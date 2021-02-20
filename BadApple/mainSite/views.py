from django.shortcuts import redirect , render
from mainSite.models import PRATemplate , OversightCommission
from mainSite.forms import PRATemplateForm , OversightCommissionForm
from random import choice


# Global Variables:
backgroundImages = ['img/lucas-benjamin-wQLAGv4_OYs-unsplash.jpg' , 'img/steve-johnson-ctRJMubyj4o-unsplash.jpg' , 'img/joel-filipe-WjnF1Tp-p3I-unsplash.jpg' , 'img/rene-bohmer-YeUVDKZWSZ4-unsplash.jpg' , 'img/jr-korpa-SFT9G3pAxLY-unsplash.jpg' , 'img/rodion-kutsaev-pVoEPpLw818-unsplash.jpg' , 'img/vinicius-amnx-amano-OHPdgstNFGs-unsplash.jpg' , 'img/henrik-donnestad-V6Qd6zA85ck-unsplash.jpg' , 'img/pawel-czerwinski-l8DUam8vtbc-unsplash.jpg' , 'img/denise-chan-pXmbsF70ulM-unsplash.jpg']


def home(request):
	return render(request , 'home.html' , {})


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
				commissionObjects = OversightCommission.objects.filter(stateTerritoryProvince = oversightForm.cleaned_data['stateTerritoryProvince'] , cityTown__icontains = oversightForm.cleaned_data['cityTown'] , approved = True , public = True)
			else:
				commissionObjects = OversightCommission.objects.filter(stateTerritoryProvince = oversightForm.cleaned_data['stateTerritoryProvince'] , approved = True , public = True)

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
