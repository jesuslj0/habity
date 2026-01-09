from rest_framework.viewsets import ModelViewSet
from .models import Habit
from .serializers import HabitSerializer


class HabitViewSet(ModelViewSet):
    serializer_class = HabitSerializer

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
