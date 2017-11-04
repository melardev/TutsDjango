'''
authenticate() will iterate through settings.AUTHENTICATION_BACKENDS and try to
authenticate against each one, if one of them returns a user then we
can authenticate, for that matter we call login()
'''
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.shortcuts import reverse

class FormLogin(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ViewLoginManual(TemplateView):
    def get(self, *args, **kwargs):
        form = FormLogin()
        return render(self.request, 'auth/login_manual.html', {'form': form})

    def post(self, *args, **kwargs):
        form = FormLogin(self.request.POST)
        # check if username and password are not empty(by default required=True)
        if form.is_valid():
            # check if credentials are valid
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(self.request, user)
                    return HttpResponseRedirect(reverse('auth-status'))
            else:
                return render(self.request, 'auth/login_manual.html', {
                    'error_message': 'invalid credentials',
                    'form': form
                })
        return render(self.request, 'auth/login_manual.html')
