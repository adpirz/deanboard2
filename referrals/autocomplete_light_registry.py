import autocomplete_light
from models import Referral, Scholar, Staff

autocomplete_light.register(Scholar,
	search_fields=['first_name','last_name'])

autocomplete_light.register(Referral,
	search_fields=['scholar','staff'])

# autocomplete_light.register(autocomplete_light.AutocompleteListBase, name='ReasonsAutoComplete',
# 	choices=Referral.REASONS_CHOICES)

