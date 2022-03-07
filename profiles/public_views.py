from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponse

#PLY:
from dynapages import models as dynapages
import ply
from ply.toolkit import vhosts,profiles
from gallery.uploader import upload_plugins_builder
from profiles.models import Profile
from group.models import Group,GroupMember,GroupTitle
from stats.models import BaseStat,ProfileStat
# Create your views here.

# Render the User Dashboard Home page:
def profile_view(request,profile_id):
    vhost = request.META["HTTP_HOST"].split(":")[0];
    community = (vhosts.get_vhost_community(hostname=vhost))
    profile = Profile.objects.get(profile_id=profile_id)
    if request.user.is_authenticated:
        current_profile = profiles.get_active_profile(request)
        all_profiles = profiles.get_all_profiles(request)
    try:
        groups = GroupMember.objects.get(profile=profile)
        primaryGroup = GroupMember.objects.get(profile=profile,primary=True)
    except GroupMember.DoesNotExist:
        groups = []
        primaryGroup = False

    widgets = dynapages.PageWidget.objects.order_by('order').filter(page=profile.dynapage)
    stats = ProfileStat.objects.filter(profile=profile)
    context = {'community':community,'vhost':vhost,'profile':profile,'widgets':widgets,'groups':groups,'primaryGroup':primaryGroup,"av_path":ply.settings.PLY_AVATAR_FILE_URL_BASE_URL,"stats":stats,'template':profile.dynapage.template.filename,'current_profile':current_profile,'profiles':all_profiles}
    return render(request,'profile_dashboard_dynapage_wrapper.html',context)
