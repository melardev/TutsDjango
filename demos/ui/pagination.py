from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from demos.models import ModelPost


def home(request, *args, **kwargs):
    if 'approach' in request.GET:
        approach = request.GET.get('approach')
        if approach == 'paginator' and 'page_number' in request.GET and 'items_per_page' in request.GET:
            return paginator_demo(request, request.GET['items_per_page'], request.GET.get('page_number'))
        elif approach == 'listview' and 'items_per_page' in request.GET:
            kwargs['items_per_page'] = request.GET['items_per_page']
            return ViewListPosts.as_view()(request, *args, **kwargs)
    return render(request, 'pagination.html')


class ViewListPosts(ListView):
    # model = ModelPost
    queryset = ModelPost.objects.all()
    # paginate_by = 3
    template_name = 'pagination.html'

    def get_paginate_by(self, queryset):
        if 'items_per_page' in self.kwargs:
            return int(self.kwargs['items_per_page'])
        else:
            return 3 # 3 by default, always give a default otherwise crash


def paginator_demo(request, items_per_page, page_number):
    items = ModelPost.objects.all()
    paginator = Paginator(items, items_per_page)

    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # If user supplied page_number that is not an integer, then show first page
        page = paginator.page(1)
    except EmptyPage:
        # If page does not exists ( out of bounds ) then show last
        page = paginator.page(paginator.num_pages)
    context = {'items': page}
    if page.has_next():
        context['next_page_number'] = page.next_page_number()
    if page.has_previous():
        context['previous_page_number'] = page.previous_page_number()
    return render(request, "pagination.html", context)
