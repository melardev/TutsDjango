from django.views.generic import TemplateView


class ViewAuthStatus(TemplateView):
    template_name = 'auth/auth_status.html'

    def get_context_data(self, **kwargs):
        context = super(ViewAuthStatus, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            try:
                twitter = self.request.user.userextended.twitter_handle
                context['twitter'] = twitter
            except Exception as e:
                print(e)
        return context
