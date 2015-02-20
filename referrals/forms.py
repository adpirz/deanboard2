import autocomplete_light
from .models import Referral, Staff
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button, ButtonHolder, Div
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
		# self.helper.add_input(Submit('submit','Submit', css_class='btn-block btn-lg'))
		self.helper.layout = Layout (
			Div(
				'scholar',
				Div('reason', css_id='reason-list'),
				'description',
				'consequence',
				FormActions(
					Submit('submit','Submit',css_class='btn-block btn-lg')),
				css_class='well col-md-6 col-lg-6 col-md-offset-3 col-lg-offset-3'
				)
			)
		self.user = kwargs.pop('user',None)
		super(ReferralForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Referral
		fields = ['scholar','reason','description','consequence']




	