'''
login handles login process
logout logs out the user
logout_then_login logs out the user and redirects him to the login page
'''

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
# It will redirect the user to settings.LOGIN_REQUIRED?next=current_url
@login_required
def restricted_area(request, *args, **kwargs):
    return render(request, 'auth/restricted_area.html')


'''PermissionRequiredMixin is build'''
class MyView(LoginRequiredMixin, CreateView):
    permission_required = 'polls.can_vote'
    # Or multiple of permissions:
    model = ModelBlogPost

