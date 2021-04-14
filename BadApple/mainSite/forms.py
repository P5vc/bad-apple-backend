from django.utils.translation import gettext_lazy as _
from django.forms import Form , ModelForm , Select , TextInput , CharField , IntegerField , ChoiceField , Textarea
from mainSite.models import PRATemplate , OversightCommission , Tip
import mainSite.extendedModels.modelCodes as choices



class PRATemplateForm(ModelForm):
	class Meta:
		model = PRATemplate
		fields = ['stateTerritoryProvince' , 'subject']
		widgets = {'stateTerritoryProvince' : Select(attrs = {'class' : 'form-control'}) , 'subject' : Select(attrs = {'class' : 'form-control'})}



class OversightCommissionForm(ModelForm):
	class Meta:
		model = OversightCommission
		fields = ['stateTerritoryProvince' , 'cityTown']
		widgets = {'stateTerritoryProvince' : Select(attrs = {'class' : 'form-control'}) , 'cityTown' : TextInput(attrs = {'class' : 'form-control' , 'placeholder' : _('City or Town (Optional)')})}



class TipForm(ModelForm):
	class Meta:
		model = Tip
		fields = ['topic' , 'message']
		widgets = {'topic' : Select(attrs = {'class' : 'form-control'}) , 'message' : Textarea(attrs = {'class' : 'form-control' , 'rows' : '8' , 'placeholder' : _('Enter your message here...')})}



class TipFormCAPTCHA(ModelForm):
	captchaInput = CharField(max_length = 6 , widget = TextInput(attrs = {'class' : 'form-control' , 'placeholder' : _('Enter CAPTCHA text here...')}))
	verificationText = CharField(max_length = 1000)

	class Meta:
		model = Tip
		fields = ['topic' , 'message']
		widgets = {'topic' : Select(attrs = {'class' : 'form-control'}) , 'message' : Textarea(attrs = {'class' : 'form-control' , 'rows' : '8' , 'placeholder' : _('Enter your message here...')})}



class BadAppleForm(Form):
	firstName = CharField(max_length = 150 , required = False , widget = TextInput(attrs = {'class' : 'form-control' , 'placeholder' : _('First Name')}))
	lastName = CharField(max_length = 150 , required = False , widget = TextInput(attrs = {'class' : 'form-control' , 'placeholder' : _('Last Name')}))
	cityTownCounty = CharField(max_length = 150 , required = False , widget = TextInput(attrs = {'class' : 'form-control' , 'placeholder' : _('City, Town, or County')}))
	stateTerritoryProvince = ChoiceField(choices = ([('' , _('Any'))] + choices.STATES_TERRITORIES_PROVINCES) , required = False , widget = Select(attrs = {'class' : 'form-control'}))
	year = IntegerField(max_value = 3000 , min_value = 1000 , required = False , widget = TextInput(attrs = {'class' : 'form-control' , 'placeholder' : _('Year of Incident')}))
	policyCategory = ChoiceField(choices = ([('' , _('Any'))] + choices.POLICY_CATEGORIES) , required = False , widget = Select(attrs = {'class' : 'form-control'}))
