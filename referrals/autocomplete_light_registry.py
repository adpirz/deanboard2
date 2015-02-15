from referrals.models import Scholar
import autocomplete_light

class ScholarAutocomplete(autocomplete_light.AutocompleteModelBase):
	search_fields = ['first_name', 'last_name']

autocomplete_light.register(Scholar, ScholarAutocomplete)