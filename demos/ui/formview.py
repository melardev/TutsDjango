from django.views.generic import FormView
from django.core.mail import send_mail
from demos.forms import FormDummy, FormUserDummy
from django.core.urlresolvers import reverse_lazy, reverse

'''
FormView abstracts away from you the boilerplate code which we have seen in tutorial about forms
where we checked if request is get or post. if post call is_valid and if correct redirect user, otherwise show again the form .
If GET then also show the form. This is always the same, so instead of rewriting it each and every time, we can use FormView
Which does that for us without writing that boilerplate code. BUT, FormView does not work on models, it just deals with forms
'''


class ViewFormView(FormView):
    form_class = FormDummy
    template_name = 'ui/formview_demo.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # now form is valid, do something, if form_class is ModelForm you could call save()
        send_mail('User submited the form', 'User filled the form, he is a good boy', ['admin@admin.com']
                  , ['managers@department.com'])
        super(ViewFormView, self).form_valid(form)


class ViewFormViewEx(FormView):
    form_class = FormDummy
    template_name = 'ui/formview_demo.html'

    def get_initial(self):
        initial_data = super(ViewFormViewEx, self).get_initial()
        initial_data['name'] = "This is the begin value"
        return initial_data

    def form_valid(self, form):
        send_mail('User submited the form', 'User filled the form, he is a good boy', ['admin@admin.com']
                  , ['managers@department.com'])

    def form_invalid(self, form):
        if '\'' in form.data['name'] or 'union' in form.data['name'].lower():
            print('SQL injection attempt!')
        return super(ViewFormViewEx, self).form_invalid(form)

    def get_success_url(self):
        return reverse('home')


class ViewModelForm(FormView):
    form_class = FormDummy
    template_name = 'ui/formview_demo.html'
    success_url = '/'
