import autocomplete_light
from .models import Referral
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button
from crispy_forms.bootstrap import FormActions
from django.contrib.auth.models import User
from django import forms


class ReferralForm(autocomplete_light.ModelForm):
	reason = forms.ChoiceField(choices=Referral.REASONS_CHOICES,
		widget=forms.RadioSelect)

	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.form_id = 'id-referral'
		self.helper.form_method='post'
		self.helper.form_class='ModelForm'
		self.helper.form_action='index'
		self.helper.add_input(Submit('submit','Submit'))
		super(ReferralForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Referral
		fields = ['scholar','staff','reason','description','consequence']