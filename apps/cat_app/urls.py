from django.conf.urls import url
from . import views
app_name = 'cat'

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^log_out$', views.log_out, name='log_out'),
    url(r'^add_cat_page$', views.add_cat_page, name='add_cat_page'),
    url(r'^add_cat$', views.add_cat, name='add_cat'),
    url(r'^add_like/(?P<cat_id>\d+)$', views.add_like, name='add_like'),
    url(r'^remove_like/(?P<cat_id>\d+)$', views.remove_like, name='remove_like'),
    url(r'^edit_cat_page/(?P<cat_id>\d+)$', views.edit_cat_page, name='edit_cat_page'),
    url(r'^edit_cat/(?P<cat_id>\d+)$', views.edit_cat, name='edit_cat'),
    url(r'^delete_cat/(?P<cat_id>\d+)$', views.delete_cat, name='delete_cat'),
]
