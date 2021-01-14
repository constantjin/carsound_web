from django.urls import path, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

from maintenance_mode.core import set_maintenance_mode


@staff_member_required
def on_maintenance(request):
    set_maintenance_mode(True)
    messages.info(request, "Maintenance mode ON!")
    return HttpResponseRedirect(reverse("admin:index"))


@staff_member_required
def off_maintenance(request):
    set_maintenance_mode(False)
    messages.info(request, "Maintenance mode OFF!")
    return HttpResponseRedirect(reverse("admin:index"))


app_name = "maintenance"
urlpatterns = [
    path(
        # {% url 'maintenance:on' %}
        route="on/",
        view=on_maintenance,
        name="on",
    ),
    path(
        # {% url 'maintenance:off' %}
        route="off/",
        view=off_maintenance,
        name="off",
    ),
]
