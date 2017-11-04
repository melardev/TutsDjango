"""TutsDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from demos.views import home, template_demo
from demos.cookie_sessions.cookies import cookies_demo

from demos.ui.view import ViewViewDemo
from demos.cookie_sessions.sessions import session_demo
from demos.model_demos import db_crud
from demos.ui import pagination
from demos.templatetags import custom_filter_tags
from demos.ui import create_view
from demos.net.mail_simple import ViewSendEmail

from demos.auth.login_manual import ViewLoginManual
from demos.auth.auth_status import ViewAuthStatus
from demos.auth import register, edit_profile
from demos.auth import password_change
from demos.auth import auth_social

from django.contrib.auth.views import login, logout, logout_then_login
from django.contrib.auth.views import password_change_done
from django.contrib.auth.views import password_reset, password_reset_confirm, password_reset_complete, \
    password_reset_done

from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    # admin contrib app urls
    url(r'^admin/', admin.site.urls),

    # auth contrib app urls
    url(r'^login/?$', login, {'template_name': 'auth/login.html'}, name='login'),
    url(r'^logout/?$', logout, {'template_name': 'auth/logged_out.html'}, name='logout'),
    url(r'^logout_then_login/?$', logout_then_login, name='logout_then_login'),

    url(r'^auth-social/', include('social_django.urls', namespace='social')),

    url(r'^password_change/?$', password_change.ViewPasswordChange.as_view(), name='password_change'),
    url(r'^password_change_done/?$', password_change_done, {'template_name': 'auth/password_change_done.html'},
        name='password_change_done'),
    url(r'^password_reset/?$', password_reset, {'template_name': 'auth/password_reset.html'
        , 'email_template_name': 'auth/password_reset_email.html', 'from_email': 'melardev@django.com'},
        name='password-reset'),
    url(r'^password_reset_confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/?$', password_reset_confirm,
        {'template_name': 'auth/password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^password_reset_complete/?$', password_reset_complete, {'template_name': 'auth/password_reset_complete.html'},
        name='password_reset_complete'),
    url(r'^password_reset_done/?$', password_reset_done, {'template_name': 'auth/password_reset_done.html'},
        name='password_reset_done'),

    url(r'^$', home, name='home'),
    url(r'^demos/templates/?$', template_demo, name='templates-home'),
    url(r'demos/home', home, name='demos-home'),
    url(r'^demos/cookies/?$', cookies_demo, name='demos-cookies'),
    url(r'^demos/ui/view', ViewViewDemo.as_view(), name='demos-ui-view'),
    url(r'^demos/sessions/?$', session_demo, name='demos-sessions'),
    url(r'^demos/db_crud/?$', db_crud.ViewListPost.as_view(), name='demos-models-dbcrud-list'),
    url(r'^demos/db_crud/detail/(?P<pk>\d+)/$', db_crud.ViewDetailPost.as_view(), name='demos-models-dbcrud-detail'),
    url(r'^demos/db_crud/update/(?P<id>\d+)/$', db_crud.ViewUpdatePost.as_view(), name='demos-models-dbcrud-update'),
    url(r'^demos/db_crud/create/$', db_crud.ViewCreatePost.as_view(), name='demos-models-dbcrud-create'),
    url(r'^demos/db_crud/delete/(?P<pk>\d+)/$', db_crud.ViewDeletePost.as_view(), name='demos-models-dbcrud-delete'),
    url(r'^demos/pagination/?$', pagination.home, name='demos-ui-pagination'),
    url(r'^demos/filter_tags/?$', custom_filter_tags.home, name='demos-ui-filter_tag'),
    url(r'^demos/ui/createview/?$', create_view.home, name='demos-ui-createview'),
    url(r'^demos/email_simple', ViewSendEmail.as_view(), name='demos-email-simple'),

    url(r'^auth/login/manual/?$', ViewLoginManual.as_view(), name='login-manual'),
    url(r'^auth/status/?$', ViewAuthStatus.as_view(), name='auth-status'),
    url(r'^auth/social', auth_social.home, name='auth-social'),
    url(r'^register/?$', register.ViewRegister.as_view(), name='auth-register'),
    url(r'^register2/?$', register.ViewRegister2.as_view(), name='auth-register2'),
    url(r'^profile/edit/(?P<pk>\d+)/?$', edit_profile.ViewUpdateProfile.as_view(), name='auth-update-profile'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
