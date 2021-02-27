from django.forms import ModelForm , Select , TextInput
from mainSite.models import PRATemplate , OversightCommission



class PRATemplateForm(ModelForm):
	class Meta:
		model = PRATemplate
		fields = ['stateTerritoryProvince' , 'subject']
		widgets = {'stateTerritoryProvince' : Select(attrs = {'class' : 'form-control'}) , 'subject' : Select(attrs = {'class' : 'form-control'})}



class OversightCommissionForm(ModelForm):
	class Meta:
		model = OversightCommission
		fields = ['stateTerritoryProvince' , 'cityTown']
		widgets = {'stateTerritoryProvince' : Select(attrs = {'class' : 'form-control'}) , 'cityTown' : TextInput(attrs = {'class' : 'form-control' , 'placeholder' : 'City or Town'})}
