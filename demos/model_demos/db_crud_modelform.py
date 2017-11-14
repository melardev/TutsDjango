from django.http import HttpResponseRedirect
from demos.forms import FormPost, FormPostAdmin
from demos.models import ModelPost
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView


# We will have access to object_list which is usually the items in the query_set
class ViewListPost(ListView):
    model = ModelPost
    template_name = 'db_crud_modelform/list.html'


class ViewCreatePost(CreateView):
    template_name = 'db_crud_modelform/create.html'
    form_class = FormPostAdmin

    def form_valid(self, form):
        model = form.save(commit=False)
        model.save()
        return HttpResponseRedirect(reverse('demos-formodels-dbcrud-list'))


class ViewUpdatePost(UpdateView):
    form_class = FormPost
    template_name = 'db_crud_modelform/update.html'

    def get_object(self, queryset=None):
        id = self.kwargs['id']
        return self.form_class.Meta.model.objects.get(id=id)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('demos-formodels-dbcrud-list'))


class ViewDetailPost(DetailView):
    model = ModelPost
    template_name = 'db_crud_modelform/detail.html'


class ViewDeletePost(DeleteView):
    template_name = 'db_crud_modelform/delete.html'
    model = ModelPost

    def get_success_url(self):
        return reverse('demos-formodels-dbcrud-list')
