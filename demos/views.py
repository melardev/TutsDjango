from django.shortcuts import render, redirect



# Create your views here.
def home(request):
    return render(request, 'index.html', {'demo_title': 'Wello world', 'name': 'melardev'})


def template_demo(request):
    return render(request, 'ui/template_example.html', {'demo_title': 'templates Demo'})