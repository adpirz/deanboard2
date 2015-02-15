from django.conf.urls import patterns, url, include
from referrals.views import ReferralCreate, ReferralEdit, user_login, ScholarReferrals, IndexView, user_logout
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from referrals.models import Staff, Scholar, Referral, Advisory


urlpatterns = patterns('',
	url(r'^$', IndexView.as_view(), name='index'),
	url(r'^referral/(?P<pk>\d+)$', DetailView.as_view(model=Referral), name = 'referral'),
	url(r'^referral/(?P<pk>\d+)/delete/$', DeleteView.as_view(
		model=Referral,
		success_url = '/'), 
		name = 'referral_delete'),
	url(r'^referral/(?P<pk>\d+)/edit/$', ReferralEdit.as_view(), name = 'referral_edit'),
	url(r'^new/$', ReferralCreate.as_view(), name='referral_new'),
	url(r'^all/$', ListView.as_view(model=Referral), name='referral_list'),
	url(r'^login/$',user_login, name='user_login'),
	url(r'^logout/$',user_logout, name='user_logout'),
	url(r'^scholar/(?P<pk>\d+)$',ScholarReferrals.as_view(), name='scholar'),
	url(r'^autocomplete/', include('autocomplete_light.urls')),

	)