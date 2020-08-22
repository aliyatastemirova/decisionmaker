from django.urls import path
from .views import HomeView, ResultView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("result/", ResultView.as_view(), name="result")
]
