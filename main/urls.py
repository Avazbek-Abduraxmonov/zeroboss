from django.urls import path
from .views import IndexView, TodoActionView, withdraw


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<int:todo_id>/<str:action>/action/", TodoActionView.as_view(), name="action"),
    path("withdraw/", withdraw, name="withdraw")
]
