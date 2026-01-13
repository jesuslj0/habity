from rest_framework.viewsets import ModelViewSet
from django.views.generic import ListView
from habits.models import Habit
from habits.serializers import HabitSerializer

# Vistas de API
class HabitViewSet(ModelViewSet):
    serializer_class = HabitSerializer

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


# Vistas de Web
class HabitListView(ListView):
    model = Habit
    template_name = 'habits/habit_list.html'

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)