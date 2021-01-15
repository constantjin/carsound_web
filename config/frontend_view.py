import os

from django.conf import settings
from django.shortcuts import render

from utils.vite_loader import vite_loader


def index(request):
    manifest_path = os.path.join(settings.FRONTEND_DIST_PATH, "manifest.json")
    vite_context = vite_loader(manifest_path)

    return render(request, "index.html", {"vite": vite_context})
