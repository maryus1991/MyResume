from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User
from MyResumeProject.settings import ALLOWED_HOSTS


# Create your views here.


# def index(request):
#     # subdomain = str(request.META.get('HTTP_HOST')).split('.')[0]
#     return render(request, 'MyResumeMainModuleTemplate/home.html')


def User_index(request):
    subdomain = str(request.META.get('HTTP_HOST')).split('.')[0]
    if subdomain in ALLOWED_HOSTS or subdomain == 'localhost:8000':
        subdomain = 'mostafa'
    try:
        subdomainUser = User.objects.get(username__exact=subdomain)
        return render(request, 'MyResumeMainModuleTemplate/home.html', {'user': subdomainUser})

    except:
        raise Http404()


def HeaderLayoutPartial(request):
    return render(request, 'Base/Layouts/HeaderLayout.html')


def FooterLayoutPartial(request):
    return render(request, 'Base/Layouts/FooterLayout.html')
