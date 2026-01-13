from django.contrib.auth.views import LoginView,LogoutView
from habits.forms.auth import CustomRegisterForm, CustomLoginForm
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login

class RegisterView(FormView):
    form_class = CustomRegisterForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('habit_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    

class LoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = 'auth/login.html'
    redirect_authenticated_user = True


class LogoutView(LogoutView):
    next_page = reverse_lazy('login')