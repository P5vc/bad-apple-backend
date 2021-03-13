from django.forms import ModelForm , Select , TextInput
from mainSite.models import PRATemplate , OversightCommission , Tip



class PRATemplateForm(ModelForm):
	class Meta:
		model = PRATemplate
		fields = ['stateTerritoryProvince' , 'subject']
		widgets = {'stateTerritoryProvince' : Select(attrs = {'class' : 'form-control'}) , 'subject' : Select(attrs = {'class' : 'form-control'})}



class OversightCommissionForm(ModelForm):
	class Meta:
		model = OversightCommission
		fields = ['stateTerritoryProvince' , 'cityTown']
		widgets = {'stateTerritoryProvince' : Select(attrs = {'class' : 'form-control'}) , 'cityTown' : TextInput(attrs = {'class' : 'form-control' , 'placeholder' : 'City or Town (Optional)'})}



class TipForm(ModelForm):
	class Meta:
		model = Tip
		fields = ['topic' , 'message']
		widgets = {'topic' : Select(attrs = {'class' : 'form-control'}) , 'message' : TextInput(attrs = {'class' : 'form-control' , 'placeholder' : 'Enter your message here...'})}
