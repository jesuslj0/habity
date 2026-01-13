from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from habits.models import Habit


class DashboardView(ListView, LoginRequiredMixin):
    template_name = 'habits/dashboard.html'

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)