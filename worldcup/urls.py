from django.urls import path
from . import views

urlpatterns = [
    path("find_result/<int:id>", views.team_result, name="find-result"),
    path("all_countries", views.index, name="index"),
    path("input", views.input),
    path("insert", views.insert)
]
