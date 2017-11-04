from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


class ViewPasswordChange(TemplateView):
    def get(self, request, *args, **kwargs):
        form = PasswordChangeForm(self.request.user)
        return render(self.request, 'auth/password_change.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(self.request.user, self.request.POST)
        if form.is_valid():
            user_model = form.save()
            # update_session_auth_hash(self.request, user_model)
            return HttpResponseRedirect('')
