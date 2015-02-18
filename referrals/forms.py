import autocomplete_light
from .models import Referral, Staff
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button
from crispy_forms.bootstrap import FormActions
# from django.contrib.auth.models import User
from django import forms


class ReferralForm(autocomplete_light.ModelForm):
	reason = forms.ChoiceField(choices=Referral.REASONS_CHOICES,
		widget=forms.RadioSelect)

	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.form_id = 'id-referral'
		self.helper.form_method='post'
		self.helper.form_class='ModelForm'
		self.helper.form_action='referral_new'
		self.helper.add_input(Submit('submit','Submit'))
		self.user = kwargs.pop('user',None)
		super(ReferralForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Referral
		fields = ['scholar','reason','description','consequence']




	