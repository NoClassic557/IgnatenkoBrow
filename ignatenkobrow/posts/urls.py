from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('price', views.ServiceList.as_view(), name="price123"),
    path('price_change/<pk>', views.ServiceChange.as_view(), name='price-change'),
    path('price_change', views.ServiceCreate.as_view(), name='price-create'),
    path('add', views.ServiceCreate.as_view(), name='add'),
    path('group', views.CreatGroup.as_view(), name='group'),
    path('blog', views.BlogList.as_view(), name='blog'),
    path('blog_creat', views.BlogCreate.as_view(), name='blog_creat')
    ]
