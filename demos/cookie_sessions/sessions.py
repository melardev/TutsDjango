'''
Prerequesites
To enable sessions we have to have the SessionMiddleware up and running as well as
django.contrib.sessions in INSTALLED APPS
INSTALLED_APPS
    django.contrib.sessions
MIDDLEWARE
    django.contrib.sessions.middleware.SessionMiddleware

Django saves the sessions in a database called django_session(table if RDMS, or collection if NoSQL)
The first time you may need to run python manage.py migrate
because the sessions contrib app creates a table, and tables creation in Django has to be done through migrations
Once you do that you will see the output:
Applying sessions.0001_initial... OK
'''

from django import forms
from django.shortcuts import render, redirect


class FormLogin(forms.Form):
    username = forms.CharField(label=("Username"), required=True)
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput, required=True)


def session_demo(request):
    username = None  # default value
    form_login = FormLogin()
    if request.method == 'GET':

        if 'action' in request.GET:
            action = request.GET.get('action')
            if action == 'logout':
                if request.session.has_key('username'):
                    request.session.flush()
                return redirect('demos-sessions')

        if 'username' in request.session:
            username = request.session['username']
            print(request.session.get_expiry_age())  # session lifetime in seconds(from now)
            print(
                request.session.get_expiry_date())  # datetime.datetime object which represents the moment in time at which the session will expire

    elif request.method == 'POST':
        form_login = FormLogin(request.POST)
        if form_login.is_valid():
            username = form_login.cleaned_data['username']
            password = form_login.cleaned_data['password']
            if username.strip() == 'youtuber' and password.strip() == 'secret':
                request.session['username'] = username
            else:
                username = None

    return render(request, 'sessions.html', {
        'demo_title': 'Sessions in Django',
        'form': form_login,
        'username': username,
    })
