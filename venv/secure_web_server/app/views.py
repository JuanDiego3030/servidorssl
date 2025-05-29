from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

def home(request):
    return HttpResponse("Welcome to the secure web server!")

@login_required
@require_http_methods(["GET"])
def sensitive_data(request):
    return HttpResponse("This is sensitive data, accessible only to authenticated users.")