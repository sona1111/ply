from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from communities.preferences.models import Preferences
from core.dynapages.models import Page, PageWidget

# Create your views here.
# PLY:
from ply import settings
from ply.toolkit import vhosts, profiles, contexts, dynapages as dp_tools
from dashboard.navigation import SideBarBuilder_dynamic
from communities.community.models import CommunityStaff, CommunityRegistryPageView
from communities.group.models import GroupMember
from core.dynapages import models as dynapages
from communities.profiles.models import ProfilePageNode
from roleplaying.stats.models import ProfileStat
from roleplaying.exp.models import ProfileExperience


# Render the Staff Dashboard Home page:
@login_required
def dashboard_home(request):
    #  Ignore port:
    context, vhost, community, profile = contexts.default_context(request)
    if community is None:
        return render(request, "error-no_vhost_configured.html", {})
    else:
        request.session["community"] = str(community.uuid)
    profile = profiles.get_active_profile(request)
    is_staff = CommunityStaff.objects.filter(
        community=community, profile=profile, active=True
    )
    if len(is_staff) < 1:
        return render(request, "error-access-denied.html", {})
    sideBar = SideBarBuilder_dynamic(community=community, application_mode="staff")
    sidebar_modules = sideBar.get_dynamic_sidebar(community, "staff")
    dashboard = CommunityRegistryPageView.objects.get(
        community=community, grouping_key="community_appmode_dashboards",key="__dashboard-landingPage-staff"
    )
    dynapage = Page.objects.get(pk=dashboard.page_id)
    prefs = Preferences.objects.get_or_create(user=request.user)[0]
    widgets = PageWidget.objects.filter(page=dynapage)
    context.update(
        {"sidebar": sidebar_modules.values(), "dashboard_name": "Event Staff","widgets":widgets,"dynapage":dynapage,"preferences":prefs}
    )

    return render(request, "dashboard/community_admin/dashboard/index.html", context)


@login_required
def dashboard_panel_home(request):
    context, vhost, community, profile = contexts.default_context(request)

    return render(
        request, "dashboard/community_admin/dashboard/panel_home.html", context
    )
