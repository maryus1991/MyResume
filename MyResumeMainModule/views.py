from django.contrib.auth.models import User
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from .forms import Contactus_form
from MyResumeProject.settings import ALLOWED_HOSTS

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def User_index(request, slug=None):

    subdomain = str(request.META.get('HTTP_HOST')).split('.')[0]
    if subdomain in ALLOWED_HOSTS or subdomain == 'localhost:8000':
        subdomain = 'mostafa'
    try:
        subdomainUser = User.objects.filter(username__exact=subdomain, is_active=True).first()
        subdomainUser.UserViews.create(ip=get_client_ip(request)).save()
        if slug is None:
            if subdomainUser.UserProfile.is_active and not subdomainUser.UserProfile.is_deleted :
                Showing_Main_Skill_user = subdomainUser.UserProfile.Showing_Main_Skill
            else:
                raise Http404()
        elif slug is not None:
            try:
                Showing_Main_Skill_user = subdomainUser.user_skill.filter(slug=slug, is_active=True, is_deleted=False).first()
            except:
                raise Http404
        if request.method == 'POST':
            form = Contactus_form(request.POST or None)
            if form.is_valid():
                form.instance.Profile = subdomainUser.UserProfile
                form.instance.skill = Showing_Main_Skill_user.title
                form.save()

        contact = {'user': subdomainUser,
                   'user_sub_skills': Showing_Main_Skill_user.user_skills.filter(is_deleted=False, is_active=True).all(),
                   'user_sub_skills_2': subdomainUser.user_skills.filter(UserSkills=None,is_deleted=False, is_active=True).all(),
                   'UserAbout': subdomainUser.UserProfile.UserAbout.filter(
                       Q(skill=Showing_Main_Skill_user), Q(is_deleted=False, is_active=True))[:3],
                   'last_project': Showing_Main_Skill_user.LastProject.filter(is_deleted=False, is_active=True).all()[:3],
                   'last_projects_posts': Showing_Main_Skill_user.LastProject.filter(is_deleted=False, is_active=True).all(),
                   # 'last_projects_details': last_projects_details(Showing_Main_Skill_user),
                   'Showing_Main_Skill_user': Showing_Main_Skill_user,
                   'Professional_Skills': subdomainUser.user_Pskills.filter(is_deleted=False, is_active=True).all()[:4],
                   'work_expts': subdomainUser.work_expts.filter(is_deleted=False, is_active=True).order_by('-id')[:3],
                   'study_expts': subdomainUser.study_expts.filter(is_deleted=False, is_active=True).order_by('-id')[:3],

}
        return render(request, 'MyResumeMainModuleTemplate/home.html', contact)

    except:
        raise Http404()


def mh_about_tag_partial(request, **kwargs):
    lproject = kwargs['last_projects_post']
    UserSubSkill = lproject.UserSubSkill.filter(is_deleted=False, is_active=True).all()
    return render(request, 'MyResumeRenderPartial/mh_about_tag_partial.html', {
        'UserSubSkill': UserSubSkill
    })


def mh_portfolio_modal_img(request, **kwargs):
    lproject = kwargs['last_projects_post']
    LastProjectGallerys = lproject.LastProjectGallery.filter(is_deleted=False, is_active=True).all()
    return render(request, 'MyResumeRenderPartial/mh_portfolio_modal_img.html', {
        'LastProjectGallerys': LastProjectGallerys
    })


def HeaderLayoutPartial(request, **kwargs):
    user = kwargs['user']
    try:
        return render(request, 'Base/Layouts/HeaderLayout.html', {
            'subdomain': user,
        })
    except:
        raise Http404()


def FooterLayoutPartial(request, **kwargs):
    user = kwargs['user']
    try:
        # print(subdomainUser)
        return render(request, 'Base/Layouts/FooterLayout.html', {
            'subdomain': user,
            'Contactus_form': Contactus_form(request.POST or None)
        })
    except:
        raise Http404()
