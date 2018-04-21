from django.conf.urls import url
from .import views

urlpatterns = [
       # url(r'^$',views.homepage,name='home'),
       url(r'^$',views.all_users),
       url(r'^(?P<user_id>[0-9]+)/$',views.view_user,name = 'view_user'),
        ]
