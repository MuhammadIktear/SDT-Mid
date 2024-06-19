from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegisterForm, editUserForm
from django.contrib import messages
from django.contrib.auth import logout , update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views import View
from django.urls import reverse_lazy
from Car.models import Order

class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        register_form = RegisterForm()
        return render(request, 'register.html', {'form': register_form, 'type': 'Register'})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
        
        return render(request, 'register.html', {'form': register_form, 'type': 'Register'})


class UserLoginView(LoginView):
    template_name = 'register.html'
    def get_success_url(self):
        return reverse_lazy('home')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context


def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home')

@login_required
def user_profile(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'profile.html', {'orders': orders})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = editUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('user_profile')
    else:
        form = editUserForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})
@login_required
def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password updated successfully')
            update_session_auth_hash(request, form.user)
            return redirect('user_profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change_pass.html', {'form': form})
