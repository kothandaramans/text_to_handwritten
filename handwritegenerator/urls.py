from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name='index'),
    path('txt/upload',views.txt_upload, name='txtupload'),
    path('txt/generator',views.txt_upload, name='txtgenerator'),
]