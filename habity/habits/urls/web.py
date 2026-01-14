from django.urls import path
from habits.views.habits import HabitListView, redirect_to_habit_list, HabitDetailView, HabitCreateView
from habits.views.dashboard import DashboardView

urlpatterns = [
    path("", redirect_to_habit_list, name="home"),
    path("habits/", HabitListView.as_view(), name="habit_list"),
    path("habit/<int:pk>/", HabitDetailView.as_view(), name="habit_detail"),
    path("habit/create/", HabitCreateView.as_view(), name="habit_create"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
]
