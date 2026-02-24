from django.urls import path

from home_pages.apps import HomePagesConfig
from home_pages.views import (
    HomeView,
)

app_name = HomePagesConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
