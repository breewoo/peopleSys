from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.HOMEPage, name="HOMEPAGE"),
    path('create', views.CREATEPage, name="CREATEPAGE"),
    path('edit/<int:id>', views.EDITPage, name="EDITPAGE"),
    path('update/<int:id>', views.UPDATEPage, name="UPDATEPAGE"),
    re_path(r'^delete/(?P<pk>[0-9]+)/$', views.DELETEPage,name="DELETEPAGE"), 
]