import json
from django.conf import settings


def vite_loader(manifest_path):
    with open(manifest_path) as manifest_file:
        manifest_dict = json.load(manifest_file)

        manifest_css = []
        manifest_js = []

        for name, path_dict in manifest_dict.items():
            if name.endswith(".css"):
                manifest_css.append(settings.STATIC_URL + path_dict["file"])
            elif name.endswith(".js"):
                manifest_js.append(settings.STATIC_URL + path_dict["file"])

        vite_context = {}
        vite_context["css"] = manifest_css
        vite_context["js"] = manifest_js

        return vite_context
