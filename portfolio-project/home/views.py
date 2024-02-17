from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    CreateView,
    UpdateView,
)
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView, PasswordChangeView
from django.shortcuts import render, redirect
from jobs.models import Job
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.urls import reverse_lazy



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')

            # Check if a user with this email already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already in use.', extra_tags='email_error')
                return render(request, 'home/signup.html', {'form': form})
            
            # Create a new user since one doesn't exist
            user = form.save(commit=False)
            user.username = email.split('@')[0]  # Adjust username logic as necessary
            user.email = email  # Make sure to set the email
            user.set_password(raw_password)  # Ensure password is hashed
            user.save()

            # Specify the backend and log in the newly created user
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            messages.success(request, 'Your account has been created successfully!')
            return redirect('home')
        else:
            # Form is not valid, show form with errors
            messages.error(request, 'Please correct the error below.')
    else:
        form = SignUpForm()

    return render(request, 'home/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect()


class LogoutInterfaceView(LogoutView):
    template_name = "home/logout.html"

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'home/login.html'  # Specify the path to your login template
    success_url = reverse_lazy('home')  # Redirect to a success page after login

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        # Attempt to authenticate the user using the provided email and password
        user = authenticate(self.request, email=email, password=password)

        if user is not None:
            # User is authenticated, now log them in
            login(self.request, user)
            return super().form_valid(form)
        else:
            # Authentication failed
            messages.error(self.request, "Invalid email or password.")
            return self.form_invalid(form)


class HomeView(TemplateView):
    template_name = "home/welcome.html"
    
    
class ForgotPasswordView(PasswordChangeView):
    template_name = "home/forgot-password.html"
    success_url = "home"
    
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["jobs"] = Job.objects.all()
        return context
