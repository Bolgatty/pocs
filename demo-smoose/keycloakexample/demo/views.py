from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse('Welcome to Smoose Portal <a href="/secure">Login To Keycloak</a>')

@login_required
def secure(request):
    return HttpResponse('Logout from KeyCloak. <a href="/openid/logout">Logout</a>')  
