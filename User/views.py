from django.views.generic import CreateView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import CustomRegisterForm
from .models import CustomUser, Social
from django.contrib.auth import get_user_model
User = get_user_model()

class UserRegisterView(CreateView):
    form_class = CustomRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class UserLoginView(LoginView):
    template_name = 'login.html'
    success_url = '/'


class AboutUsView(ListView):
    template_name = 'about-us.html'
    model = User
    queryset = 'users'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        context['me'] = CustomUser.objects.get(user__username = 'shahan')
        context['socials'] = Social.objects.filter(custom_user__user__username = 'shahan')

        return context