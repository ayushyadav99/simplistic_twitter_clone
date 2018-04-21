"""howler URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from howler_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^homepage/$',views.homepage,name='homepage'),
    url(r'^add_howl/$',views.add_howl,name = 'add_howl'),
    url(r'^login/$', auth_views.login),
    url(r'^logout/$',auth_views.logout),
    url(r'^profile/$',views.user_profile),
    url(r'^search/$',views.search),
    url(r'users/',include('howler_app.urls'),name = 'users'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^add/$',views.add_follower),
    url(r'^following/$',views.my_followers),
    url(r'^howls/$',views.all_howls),
	url(r'^$',views.index),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
