from django.utils.translation import gettext_lazy as _
from django.forms import Form , ModelForm , Select , TextInput , CharField , IntegerField , ChoiceField , Textarea
from mainSite.models import PRATemplate , OversightCommission , Tip , InvestigativeReportFinding
import mainSite.extendedModels.modelCodes as choices


# Generate a form-friendly policy category list (in order from most to least common, then alphabetized):
policyCategories = [('' , _('Any'))]
usedPolicyCategories = []
unusedPolicyCategories = []
for category in choices.POLICY_CATEGORIES:
	numTimesUsed = InvestigativeReportFinding.objects.filter(findingPolicyCategory = category[0] , public = True , approved = True).count()
	if (numTimesUsed):
		usedPolicyCategories.append([numTimesUsed , category])
	else:
		unusedPolicyCategories.append([category[1] , category[0]])

usedPolicyCategories.sort()
usedPolicyCategories.reverse()
unusedPolicyCategories.sort()
for category in usedPolicyCategories:
	policyCategories.append(category[1])
for category in unusedPolicyCategories:
	policyCategories.append((category[1] , category[0]))



class PRATemplateForm(ModelForm):
	class Meta:
		model = PRATemplate
		fields = ['stateTerritoryProvince' , 'subject']
		widgets = {'stateTerritoryProvince' : Select(attrs = {'class' : 'form-control bg-white'}) , 'subject' : Select(attrs = {'class' : 'form-control bg-white'})}



class OversightCommissionForm(ModelForm):
	class Meta:
		model = OversightCommission
		fields = ['stateTerritoryProvince' , 'cityTown']
		widgets = {'stateTerritoryProvince' : Select(attrs = {'class' : 'form-control bg-white'}) , 'cityTown' : TextInput(attrs = {'class' : 'form-control' , 'placeholder' : _('City or Town (Optional)')})}



class TipForm(ModelForm):
	class Meta:
		model = Tip
		fields = ['topic' , 'message']
		widgets = {'topic' : Select(attrs = {'class' : 'form-control bg-white'}) , 'message' : Textarea(attrs = {'class' : 'form-control' , 'rows' : '8' , 'placeholder' : _('Enter your message here...')})}



class TipFormCAPTCHA(ModelForm):
	captchaInput = CharField(max_length = 6 , widget = TextInput(attrs = {'class' : 'form-control' , 'placeholder' : _('Enter CAPTCHA text here...')}))
	verificationText = CharField(max_length = 1000)

	class Meta:
		model = Tip
		fields = ['topic' , 'message']
		widgets = {'topic' : Select(attrs = {'class' : 'form-control bg-white'}) , 'message' : Textarea(attrs = {'class' : 'form-control' , 'rows' : '8' , 'placeholder' : _('Enter your message here...')})}



class BadAppleForm(Form):
	firstName = CharField(max_length = 150 , min_length = 2 , required = False , widget = TextInput(attrs = {'class' : 'form-control' , 'placeholder' : _('First Name')}))
	lastName = CharField(max_length = 150 , min_length = 2 , required = False , widget = TextInput(attrs = {'class' : 'form-control' , 'placeholder' : _('Last Name')}))
	cityTownCounty = CharField(max_length = 150 , min_length = 2 , required = False , widget = TextInput(attrs = {'class' : 'form-control' , 'placeholder' : _('City, Town, or County')}))
	stateTerritoryProvince = ChoiceField(choices = ([('' , _('Any'))] + choices.STATES_TERRITORIES_PROVINCES) , required = False , widget = Select(attrs = {'class' : 'form-control bg-white'}))
	year = IntegerField(max_value = 3000 , min_value = 1000 , required = False , widget = TextInput(attrs = {'class' : 'form-control' , 'placeholder' : _('Year of Incident')}))
	policyCategory = ChoiceField(choices = policyCategories , required = False , widget = Select(attrs = {'class' : 'form-control bg-white'}))
