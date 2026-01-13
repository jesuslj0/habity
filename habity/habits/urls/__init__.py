from django.urls import include, path

urlpatterns = [
    path("", include("habits.urls.web")),
    path("api/", include("habits.urls.api")),
    path("auth/", include("habits.urls.auth")),
]