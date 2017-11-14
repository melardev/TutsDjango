from django.shortcuts import render, redirect
from django.views.generic import View
from demos.forms import FormDummy


def home(request):
    if request.method == 'POST':
        form = FormDummy(request.POST)
        # Is this form valid according to the validators and rules set in the form fields?
        # is_valid() will populate cleaned_data dictionary which we can use to get access to the input
        # is_valid() will also populate errors dictionary with error messages
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            gender = form.cleaned_data['gender']
            cv = form.cleaned_data['cv']
            age = form.cleaned_data['age']
            print("%s password: %s ; gender:%s ; cv: %s ; age : %d" % (name, password, gender, cv, age))
            return redirect('home')
    else:
        form = FormDummy()
    return render(request, 'ui/forms_demo.html', {'form': form})

class ViewFormsDemo(View):
    def get(self, request):
        form = FormDummy()
        return render(request, 'ui/forms_demo.html', {'form': form})

    def post(self, request):
        form = FormDummy(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            gender = form.cleaned_data['gender']
            cv = form.cleaned_data['cv']
            age = form.cleaned_data['age']
            print("%s password: %s ; gender:%s ; cv: %s ; age : %d" % (name, password, gender, cv, age))
            return redirect('home')
        return render(request, 'ui/forms_demo.html', {'form': form})
