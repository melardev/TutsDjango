'''
You will need django.contrib.auth and two Middlewares registered in settings.py
AuthenticationMiddleware: associates a request to a user
SessionMiddleware: authentication sessions are handled using sessions.

The authentication contrib app includes many models, views, forms etc, the models are

The models can be checked with a SQLite3 viewer
'''

from django.views.generic import FormView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect


class FormRegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ViewRegister(CreateView):
    success_url = reverse_lazy('auth-status')
    template_name = 'auth/register.html'
    form_class = FormRegisterUser


class ViewRegister2(FormView):
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')
    form_class = FormRegisterUser

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password1"])
        user.save()
        return HttpResponseRedirect(self.success_url)
