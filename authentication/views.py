from django.shortcuts import render, redirect
from .forms import UserCreationFormReformed
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.views import View
from django.views.generic.base import ContextMixin
from django.urls import reverse_lazy


class LoginAuthView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True


class RegistrationView(ContextMixin, View):
    template_name = 'register.html'
    success_url = 'loginMe'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(form=UserCreationFormReformed())
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UserCreationFormReformed(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'pass_change.html'
    success_url = reverse_lazy('index', urlconf='mainApp.urls')


class ForgetPasswordView(PasswordResetView):
    template_name = 'forgotten.html'
    success_url = reverse_lazy('password_done')
    email_template_name = 'password_reset_email.txt'
    subject_template_name = 'subject.txt'
    from_email = 'admin@mysite.com'


def pass_reset_done(request):
    return render(request, 'pass_reset_done.html')


class SetNewPassword(PasswordResetConfirmView):
    template_name = 'set_password.html'
    success_url = reverse_lazy('loginMe')


def logoutMe(request):
    logout(request)
    return render(request, 'logout.html')
