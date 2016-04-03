from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.views import UserDetailView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SistemaDiscusiones.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('apps.home.urls')),
    # url(r'^', include('apps.users.urls', namespace='users')),

    # Python social auth
    url('', include('social.apps.django_app.urls',namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^usuario/(?P<slug>[-\w]+)/', UserDetailView.as_view(), name='user_detail'),
)
