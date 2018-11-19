from django.conf.urls import  include, url
from rest_framework.urlpatterns import format_suffix_patterns
from services import views



urlpatterns = [
    url(r'^product/create$', views.product_list, name='product_list'),

]
urlpatterns = format_suffix_patterns(urlpatterns)
