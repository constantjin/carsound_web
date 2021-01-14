import os
import glob

from django.http import HttpResponseRedirect
from django.contrib import admin
from django.urls import path
from django.conf import settings

from .models import RunSound, EmotionalSound


@admin.register(RunSound)
class RunSoundAdmin(admin.ModelAdmin):
    change_list_template = "runsound_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("add_runsound/", self.add_runsound),
        ]
        return my_urls + urls

    def add_runsound(self, request):
        self.model.objects.all().delete()
        sound_paths = glob.glob(
            os.path.join(settings.SOUNDS_ROOT, "run", "*.wav"), recursive=True
        )
        for sound_path in sound_paths:
            sound_with_ext = os.path.basename(sound_path)
            sound_name = os.path.splitext(sound_with_ext)[0]
            sound_url = settings.DOMAIN + settings.SOUNDS_URL + "run/" + sound_with_ext
            self.model.objects.create(name=sound_name, url=sound_url)

        self.model.objects.create(name="base", url="")  # Base run

        self.message_user(request, "Previous Run sounds removed and newly added")
        return HttpResponseRedirect("../")


@admin.register(EmotionalSound)
class EmotionalSoundAdmin(admin.ModelAdmin):
    change_list_template = "emotionalsound_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("add_emotionalsound/", self.add_emotionalsound),
        ]
        return my_urls + urls

    def add_emotionalsound(self, request):
        self.model.objects.all().delete()
        sound_paths = glob.glob(
            os.path.join(settings.SOUNDS_ROOT, "emotional", "*.wav"), recursive=True
        )
        for sound_path in sound_paths:
            sound_with_ext = os.path.basename(sound_path)
            sound_name = os.path.splitext(sound_with_ext)[0]
            sound_url = (
                settings.DOMAIN + settings.SOUNDS_URL + "emotional/" + sound_with_ext
            )
            self.model.objects.create(name=sound_name, url=sound_url)
        self.message_user(request, "Previous Emotional sounds removed and newly added")
        return HttpResponseRedirect("../")
