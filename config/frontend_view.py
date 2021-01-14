import os
import json

from django.conf import settings
from django.shortcuts import render


def index(request):
    manifest_path = os.path.join(settings.FRONTEND_DIST_PATH, "manifest.json")
    with open(manifest_path) as manifest_file:
        context = {"manifest": json.load(manifest_file)}
        return render(request, "index.html", context)
