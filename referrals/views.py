from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from referrals.models import Staff, Scholar, Referral, Advisory
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import autocomplete_light

# Create your views here.
class IndexView(ListView):
	template_name = 'referrals/index.html'
	model = Referral

# class ReferralDetail(DetailView):
# 	model = Referral

	# def get_context_data(self, **kwargs):
	# 	context = super(ReferralDetail, self).get_context_data(**kwargs)
	# 	return context

class ScholarReferrals(ListView):

	template_name = 'referrals/scholar_referrals.html'
	def get_queryset(self):

		self.scholar = get_object_or_404(Scholar, id=self.kwargs['pk'])
		return Referral.objects.filter(scholar=self.scholar)

	def get_context_data(self,**kwargs):
		context = super(ScholarReferrals, self).get_context_data(**kwargs)
		context['scholar'] = self.scholar
		return context

class ReferralCreate(CreateView):
	model = Referral
	fields = ['scholar','staff','reason','description','consequence']
	def __init__(self, *args, **kwargs):
		super(ReferralCreate, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'id-referral'
		self.helper.form_method='post'
		self.helper.form_class='ModelForm'
		self.helper.form_action='submit'

		self.helper.add_input(Submit('submit','Submit'))

# class ReferralList(ListView):
# 	model = Referral

# class ReferralDelete(DeleteView):
# 	model = Referral
# 	success_url = reverse_lazy('index')

class ReferralEdit(UpdateView):
	model = Referral
	fields = ['scholar','staff','reason','description','consequence']

def user_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponse('Account disabled.')
		else:
			return render(request, 'referrals/login.html',{'error':'Invalid login details'})

	else:
		return render(request,'referrals/login.html',{})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')


