from django import forms
from rango.models import Referral, Scholar, Staff
import datetime

class ReferralForm (forms.ModelForm):
	staff = forms.ModelChoiceField(queryset=Staff.objects.all())
	scholar = forms.ModelChoiceField(queryset=Scholar.objects.all())
	datetime = forms.DateTimeField(default=datetime.now())
	reason = forms.ChoiceField(choices=REASONS_CHOICES)
	description = forms.CharField(max_length=300)
	in_dos = forms.BooleanField(default=False)
	consequence = forms.ChoiceField(choices=CONSEQUENCE_CHOICES)

	class Meta:
		model = Referral
		fields = ('staff', 'scholar', 'datetime', 'reason', 'description', 'in_dos', 'consequence')

