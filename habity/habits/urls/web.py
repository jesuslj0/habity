from django.urls import path
from habits.views.habits import HabitListView
from habits.views.dashboard import DashboardView

urlpatterns = [
    path("habits/", HabitListView.as_view(), name="habit_list"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
]
