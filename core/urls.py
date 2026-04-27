from django.urls import path
from . import views

urlpatterns = [
    # add your urls here
    path("", views.index, name="homePage"),
    path("tasks/", views.TaskView.as_view(), name="tasks"),
    path("tasks/add/", views.TaskView.as_view(), name="task-add"),
    path("tasks/delete/", views.TaskView.as_view(), name="task-delete"),
    ]
    
