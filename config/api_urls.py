from django.urls import path

from subjects.api import views as subjects_views

from sounds.api import views as sounds_views

from ratings.api import views as ratings_view

app_name = "api"
urlpatterns = [
    path(
        # {% url 'api:register' %}
        route="register/",
        view=subjects_views.SubjectCreateAPIView.as_view(),
        name="register",
    ),
    path(
        # {% url 'api:get-run/<uuid>' %}
        route="get-run/<uuid:subject_pk>",
        view=sounds_views.GetRunSound.as_view(),
        name="get-run",
    ),
    path(
        # {% url 'api:get-emotional/<uuid>/<pk>' %}
        route="get-emotional/<uuid:subject_pk>/<int:run_pk>",
        view=sounds_views.GetEmotionalSound.as_view(),
        name="get-emotional",
    ),
    path(
        # {% url 'api:ratings' %}
        route="ratings/",
        view=ratings_view.RatingCreateAPIView.as_view(),
        name="ratings",
    ),
]
