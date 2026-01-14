from rest_framework.viewsets import ModelViewSet
from django.views.generic import ListView, DetailView, FormView
from habits.models import Habit
from habits.serializers import HabitSerializer
from django.shortcuts import redirect
from django.urls import reverse_lazy
from habits.forms.habits import HabitForm

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
    
def redirect_to_habit_list(request):
    return redirect('habit_list')

class HabitDetailView(DetailView):
    model = Habit
    template_name = 'habits/habit_detail.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
class HabitCreateView(FormView):
    template_name = 'habits/habit_create.html'
    form_class = HabitForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('habit_list')