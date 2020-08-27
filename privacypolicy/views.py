from django.shortcuts import render
from privacypolicy.models import PrivacyPolicy

# Create your views here.
def privacy_policy_detail(request):
    privacy_policy = PrivacyPolicy.objects.all()
    context = {
        'privacy_policy': privacy_policy,
    }

    return render(request, "privacy_policy_detail.html", context)
