from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

def index(request):
    return HttpResponse('Welcome to Smoose Portal <a href="/secure">Login To Keycloak</a>')

@login_required
def secure(request):
    #return HttpResponse('Logout from KeyCloak. <a href="/openid/logout">Logout</a>')  
    return render_to_response("demo/home.html", {"userinfo": request.session['userinfo'] if 'userinfo' in request.session.keys() else None})