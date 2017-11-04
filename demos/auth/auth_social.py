'''
Steps:
pip install python-social-auth (deprecated, don't use it) instead use:
1. Install : pip install social-auth-app-django
2. Add social_django in INSTALLED_APPS in settings
3. Create databases python.py manage.py migrate
then go ahead and add the corresponding AUTHENTICATION_BACKENDS into settings.py
This is the list of supported authentication_backends
https://python-social-auth.readthedocs.io/en/latest/backends/index.html#supported-backends
'''
from django.shortcuts import render


def home(request, *args, **kwargs):
    return render(request, 'auth/auth_social.html')
