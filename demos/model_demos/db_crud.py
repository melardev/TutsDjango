from django.http import HttpResponseRedirect
from demos.models import ModelPost
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

# We will have access to object_list which is usually the items in the query_set
class ViewListPost(ListView):
    queryset = ModelPost.objects.all()

    # model = ModelPost
    # paginate_by = 2
    template_name = 'db_crud/list.html'


class ViewCreatePost(CreateView):
    template_name = 'db_crud/create.html'
    # form_class = FormPost
    model = ModelPost
    fields = '__all__'  # or []

    def form_valid(self, form):
        # Don't call super(..) if you want to process the model further(add timestamp, and other fields, etc)
        # super(ViewCreatePost, self).form_valid(form)
        model = form.save(commit=False)
        model.save()
        return HttpResponseRedirect(reverse('demos-models-dbcrud-list'))
        # You have to either return an HttpResponse(or subclasses), or define get_absolute_url, success_url, etc


class ViewUpdatePost(UpdateView):
    model = ModelPost
    template_name = 'db_crud/update.html'
    fields = ['title', 'body']

    def get_object(self, queryset=None):
        id = self.kwargs['id']
        return self.model.objects.get(id=id)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('demos-models-dbcrud-list'))


class ViewDetailPost(DetailView):
    model = ModelPost
    template_name = 'db_crud/detail.html'

# Display a confirmation warning before deleting, if triggered with GET: it shows the warning(template view)
# If triggered with POST then deletes, the template will receive object, which is the item to be deleted
class ViewDeletePost(DeleteView):
    template_name = 'db_crud/delete.html'
    model = ModelPost
    # Notice get_success_url is defined here and not in the model, because the model will be deleted
    def get_success_url(self):
        return reverse('demos-models-dbcrud-list')

