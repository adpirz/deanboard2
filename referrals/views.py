from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Staff, Scholar, Referral, Advisory
from .forms import ReferralForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required



# Create your views here.

class IndexView(ListView):
	template_name = 'referrals/index.html'
	model = Referral

# def ReferralCreate(request):
# 	if request.method == 'POST':
# 		form = ReferralForm(request.POST)

# 		if form.is_valid():
# 			form.save(commit=True)
# 			return HttpResponseRedirect('index')

# 		else:
# 			print form.errors
# 	else:
# 		form = ReferralForm()

# 	return render(request,'referrals/referral_form.html',{'form':form})

class ReferralCreate(CreateView):
	form_class=ReferralForm
	model = Referral

class ReferralList(ListView):
	model = Referral

class ReferralDelete(DeleteView):
	model = Referral
	success_url = reverse_lazy('index')

class ReferralEdit(UpdateView):
	form_class=ReferralForm
	model = Referral

class ScholarReferrals(ListView):

	template_name = 'referrals/scholar_referrals.html'
	def get_queryset(self):

		self.scholar = get_object_or_404(Scholar, id=self.kwargs['pk'])
		return Referral.objects.filter(scholar=self.scholar)

	def get_context_data(self,**kwargs):
		context = super(ScholarReferrals, self).get_context_data(**kwargs)
		context['scholar'] = self.scholar
		return context

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


