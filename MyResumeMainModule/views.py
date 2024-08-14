from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User
from MyResumeProject.settings import ALLOWED_HOSTS
from django.db.models import Q




def User_index(request, slug=None):

    subdomain = str(request.META.get('HTTP_HOST')).split('.')[0]
    if subdomain in ALLOWED_HOSTS or subdomain == 'localhost:8000':
        subdomain = 'mostafa'
    try:
        subdomainUser = User.objects.get(username__exact=subdomain)
        if slug is None:
            Showing_Main_Skill_user = subdomainUser.UserProfile.Showing_Main_Skill
        elif slug is not None:
            try:
                Showing_Main_Skill_user = subdomainUser.user_skill.get(slug=slug)
            except :
                raise Http404

        contact = {'user': subdomainUser,
                   'user_sub_skills': Showing_Main_Skill_user.user_skills.all(),
                   'user_sub_skills_2': subdomainUser.user_skills.filter(UserSkills=None).all(),
                   'UserAbout': subdomainUser.UserProfile.UserAbout.filter(
                       Q(skill=Showing_Main_Skill_user))[:3],
                   'last_project': Showing_Main_Skill_user.LastProject.all()[:3],
                   'last_projects_posts': Showing_Main_Skill_user.LastProject.all(),
                   # 'last_projects_details': last_projects_details(Showing_Main_Skill_user),
                   'Showing_Main_Skill_user': Showing_Main_Skill_user,
                   'Professional_Skills': subdomainUser.user_Pskills.all()[:4],
                   'work_expts': subdomainUser.work_expts.order_by('-id')[:3],
                   'study_expts': subdomainUser.study_expts.order_by('-id')[:3],

                   }
        return render(request, 'MyResumeMainModuleTemplate/home.html', contact)

    except:
        raise Http404()


def HeaderLayoutPartial(request):
    subdomain = str(request.META.get('HTTP_HOST')).split('.')[0]
    # if subdomain in ALLOWED_HOSTS or subdomain == 'localhost:8000':
    subdomain = 'mostafa'
    try:
        subdomainUser = User.objects.get(username__exact=subdomain)

        return render(request, 'Base/Layouts/HeaderLayout.html',{
            'subdomain': subdomainUser,
        })
    except:
        raise Http404()


def FooterLayoutPartial(request):
    subdomain = str(request.META.get('HTTP_HOST')).split('.')[0]
    # if subdomain in ALLOWED_HOSTS or subdomain == 'localhost:8000':
    subdomain = 'mostafa'
    try:
        subdomainUser = User.objects.get(username__exact=subdomain)
        # print(subdomainUser)
        return render(request, 'Base/Layouts/FooterLayout.html',{
            'subdomain': subdomainUser,
        })
    except:
            raise Http404()
