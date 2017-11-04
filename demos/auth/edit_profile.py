from django.contrib.auth.models import User
from django.views.generic import UpdateView

class ViewUpdateProfile(UpdateView):
    model = User
    fields = ['username', 'email']
    template_name = 'auth/profile_edit.html'
