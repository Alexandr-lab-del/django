from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.views import LoginView


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:product_list')
    template_name = 'users/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user_email = form.cleaned_data['email']
        send_mail(
            'Привет',
            'СПС за регистрацию',
            settings.DEFAULT_FROM_EMAIL,
            [user_email],
            fail_silently=False,
        )
        return response


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
