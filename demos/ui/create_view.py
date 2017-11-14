from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views.generic.edit import CreateView

from demos.forms import *

'''
CreateView works with models, you tell which model class to be used either
model= MyModel or
queryset = MyModel.objects.first() the class of the returned object will be used
the get_object() the class of the returned object will eb used 
'''


def home(request, *args, **kwargs):
    if 'approach' in request.GET:
        approach = int(request.GET.get('approach'))
        if approach == 1:
            return ViewDummyUserCreate.as_view()(request, *args, **kwargs)
        elif approach == 2:
            return ViewDummyUserCreate2.as_view()(request, *args, **kwargs)
        elif approach == 3:
            return ViewDummyUserCreate3.as_view()(request, *args, **kwargs)
        elif approach == 4:
            return ViewDummyUserCreate4.as_view()(request, *args, **kwargs)
    return render(request, 'ui/create.html')


class ViewDummyUserCreate(CreateView):
    template_name = 'ui/create.html'
    model = ModelDummyUser
    #fields = ('first_name', 'last_name')
    fields = '__all__'


class ViewDummyUserCreate2(CreateView):
    form_class = FormUserDummy
    template_name = 'ui/create.html'
    # must be lazy loading because urls are not loaded yet, otherwise crash!
    success_url = reverse_lazy('demos-ui-createview')

    def form_valid(self, form):
        model = form.save(commit=False)
        print(type(model))
        return super(ViewDummyUserCreate2, self).form_valid(form)


class ViewDummyUserCreate3(CreateView):
    form_class = FormUserDummy
    http_method_names = ('post', 'get')
    template_name = 'ui/create.html'

    '''
    get_initial method, which we also used in 
    NewCommentView previously. In Django, each form can have some initial data. This 
    is data that is shown when the form is Unbound. The boundness of a form is an 
    important concept. It took me a while to wrap my head around it, but it is quite 
    simple. In Django, a form has essentially two functions. It can be displayed in the 
    HTML code for a web page or it can validate some data.
    '''

    def get_initial(self):
        initial_data = super(ViewDummyUserCreate3, self).get_initial()
        initial_data['first_name'] = 'from initial data'
        return initial_data
        # now the form will be shown with the link_pk bound to a value

    def get_context_data(self, **kwargs):
        ctx = super(ViewDummyUserCreate3, self).get_context_data(**kwargs)
        ctx['from_context'] = '<b>This is my value</b>'
        return ctx


class ViewDummyUserCreate4(CreateView):
    # make a form based on this model
    model = ModelDummyUser
    # if we only want to edit these two fields
    # fields = ('first_name', 'last_name')
    fields = '__all__'

    # render this html file, pass a form object to that file
    template_name = 'ui/create.html'

    def form_valid(self, form):
        # don't call super because it will call save() which tries to save into db
        # throwing an exception because submitted_by should not be null and it is not filled yet
        model = form.save(commit=False)
        model.submitted_by = self.request.user
        model.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('demos-ui-createview')


''' if you want to allow only authenticated users, (I will explain this in a separate tutorial)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ViewCreateDummyUser, self).dispatch(*args, **kwargs)
'''
