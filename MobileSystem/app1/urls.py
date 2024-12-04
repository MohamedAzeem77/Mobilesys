from .views import MobileCreateViews,MobileListViews
from django.urls import path

urlpatterns=[
    path('mobile/',MobileCreateViews.as_view(),name='Mobile-Create'),
    path('mobile/<int:pk>',MobileListViews.as_view(),name='Mobile-list'),

]