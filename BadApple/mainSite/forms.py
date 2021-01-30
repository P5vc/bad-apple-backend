from django.forms import ModelForm , Select
from mainSite.models import PRATemplate



class PRATemplateForm(ModelForm):
	class Meta:
		model = PRATemplate
		fields = ['stateTerritoryProvince' , 'subject']
		widgets = {'stateTerritoryProvince' : Select(attrs = {'class' : 'form-control'}) , 'subject' : Select(attrs = {'class' : 'form-control'})}
