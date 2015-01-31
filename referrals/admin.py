from django.contrib import admin
from referrals.models import Staff, Scholar, Advisory, Referral
# Register your models here.

class ScholarInline(admin.TabularInline):
	model=Scholar
	def has_add_permission(self,request):
		return False
	def has_delete_permission(self,request, obj=None):
		return False

class StaffInline(admin.TabularInline):
	model=Staff
	fields = ('user','advisory')
	def has_add_permission(self,request):
		return False
	def has_delete_permission(self,request, obj=None):
		return False

class ReferralInline(admin.TabularInline):

	model = Referral
	extra = 0


class AdvisoryAdmin(admin.ModelAdmin):
	inlines = [ScholarInline, StaffInline]

class StaffAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'advisory')

	inlines = [ReferralInline]

class ScholarAdmin(admin.ModelAdmin):
	inlines = [ReferralInline]

class ReferralAdmin(admin.ModelAdmin):
	list_display = ('__unicode__','datetime','scholar','staff')

admin.site.register(Staff, StaffAdmin)
admin.site.register(Scholar, ScholarAdmin)
admin.site.register(Advisory, AdvisoryAdmin)
admin.site.register(Referral, ReferralAdmin)