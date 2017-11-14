from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse


def restricted_view_manual(request):
    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL+"?next=" + reverse("restricted1"))
    else:
        return render(request, 'auth/restricted.html', {'approach': 1})

# @login_required(login_url='')
@login_required
def restricted_view_decorator(request):
    return render(request, 'auth/restricted.html', {'approach': 2})


class ViewRestricted(TemplateView):
    template_name = 'auth/restricted.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ViewRestricted, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ViewRestricted, self).get_context_data(**kwargs)
        context['approach'] = 3
        return context


class ViewMixinRestricted(LoginRequiredMixin, TemplateView):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'next'
    template_name = 'auth/restricted.html'

    def get_context_data(self, **kwargs):
        context = super(ViewMixinRestricted, self).get_context_data(**kwargs)
        context['approach'] = 4
        return context

def restricted_from_urls(request):
    return render(request, 'auth/restricted.html', {'approach': 5})

from django.contrib.auth.mixins import UserPassesTestMixin
