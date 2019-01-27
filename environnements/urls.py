from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from environnements import views

urlpatterns = [

    path('types/', views.TypeList.as_view(), name='type-list'),
    path('types/<int:pk>/', views.TypeDetail.as_view(), name='type-detail'),
    path('environnements/', views.EnvironnementList.as_view(), name='environnement-list'),
    path('environnements/<int:pk>/', views.EnvironnementDetail.as_view(), name='environnement-detail'),

    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)