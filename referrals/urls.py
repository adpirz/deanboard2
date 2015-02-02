from django.conf.urls import patterns, url
from referrals.views import ReferralCreate, ReferralEdit, user_login, ScholarReferrals
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from referrals.models import Staff, Scholar, Referral, Advisory


urlpatterns = patterns('',
	url(r'^$', ListView.as_view(
		model=Referral, 
		template_name = 'referrals/index.html'), 
		name='index'),
	url(r'^referral/(?P<pk>\d+)$', DetailView.as_view(model=Referral), name = 'referral'),
	url(r'^referral/(?P<pk>\d+)/delete/$', DeleteView.as_view(
		model=Referral,
		success_url = '/'), 
		name = 'referral_delete'),
	url(r'^referral/(?P<pk>\d+)/edit/$', ReferralEdit.as_view(), name = 'referral_edit'),
	url(r'^new/$', ReferralCreate.as_view(), name='referral_new'),
	url(r'^all/$', ListView.as_view(model=Referral), name='referral_list'),
	url(r'^login/$',user_login, name='user_login'),
	url(r'^scholar/(?P<pk>\d+)$',ScholarReferrals.as_view(), name='scholar'),

	)

