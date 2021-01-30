from django.shortcuts import render
from mainSite.models import PRATemplate
from mainSite.forms import PRATemplateForm


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
				return render(request , 'praResult.html' , {'praForm' : praForm , 'resultFound' : False , 'letterTitle' : letterTitle , 'letterBody' : letterBody})

		return render(request , 'praResult.html' , {'praForm' : praForm , 'resultFound' : resultFound , 'letterTitle' : letterTitle , 'letterBody' : letterBody})
	else:
		praForm = PRATemplateForm()
		return render(request , 'pra.html' , {'praForm' : praForm})
