from django.conf.urls import url
from machine_module import views

app_name = 'maintainer'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'machine_module/',views.dataInputRequest,name='form'),
    url(r'^machine_module_predict/',views.analyser,name='titanic_predict'),

]
