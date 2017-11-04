from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View


class ViewViewDemo(View):
    def get(self, request, *args, **kwargs):
        # This method has to return an HttpResponse object
        return render(request, 'view_view.html', {'title': 'generic View usage', 'header_form': 'Login'})

    def post(self, request, *args, **kwargs):
        pass
