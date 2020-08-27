from django.contrib import admin
from privacypolicy.models import PrivacyPolicy

# Register your models here.
class PrivacyPolicyAdmin(admin.ModelAdmin):
    pass

admin.site.register(PrivacyPolicy, PrivacyPolicyAdmin)
