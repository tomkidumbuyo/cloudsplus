"""cloudsplus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import logout
from django.urls import path, include, re_path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from cloudsplus import settings
from web import views as webviews
from api import views as apiviews
from account import views as accountviews
from administrator import views as adminviews

# Serializers define the API representation.
from web.views import PartialGroupView


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
partial_patterns = ([
    re_path(r'^home', adminviews.PartialGroupView.as_view(template_name='dashboard/home.html'), name='home'),
    re_path(r'^movies', webviews.PartialGroupView.as_view(template_name='dashboard/movies.html'), name='movies'),
    re_path(r'^series', webviews.PartialGroupView.as_view(template_name='dashboard/series.html'), name='series'),
    re_path(r'^live', webviews.PartialGroupView.as_view(template_name='dashboard/live.html'), name='live'),
    re_path(r'^profile', webviews.PartialGroupView.as_view(template_name='dashboard/profile.html'), name='profile'),
    re_path(r'^account', webviews.PartialGroupView.as_view(template_name='dashboard/account.html'), name='account'),
], 'partials')


admin_partial_patterns = ([

    re_path(r'^movies', adminviews.PartialGroupView.as_view(template_name='admin_dashboard/movies.html'), name='movies'),
    re_path(r'^series', adminviews.PartialGroupView.as_view(template_name='admin_dashboard/series.html'), name='series'),
    re_path(r'^payments', adminviews.PartialGroupView.as_view(template_name='admin_dashboard/payments.html'), name='payments'),
    re_path(r'^live', adminviews.PartialGroupView.as_view(template_name='admin_dashboard/live.html'), name='live'),
    re_path(r'^customers', adminviews.PartialGroupView.as_view(template_name='admin_dashboard/customers.html'), name='customers'),
], 'admin_partials')

urlpatterns = [
    #re_path(r'^$', webviews.index , name='index'),
    re_path(r'^$', webviews.home , name='home'),
    re_path(r'^admin/$', adminviews.home , name='admin'),
    re_path(r'^signup/(?P<section>\d+)', accountviews.signup, name='signup'),
    re_path(r'^signup/(?P<section>\d+)/(?P<vars>\d+)/$', accountviews.signup, name='signup'),
    re_path(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('partials/', include(partial_patterns, namespace='partials')),
    path('admin_partials/', include(admin_partial_patterns, namespace='admin_partials')),
    path('django-admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('api/movie_list', apiviews.movieList.as_view(), name = "list"),
    path('api/login', apiviews.login.as_view(), name = "list"),
    path('oauth/', include('social_django.urls', namespace='social')),
]
