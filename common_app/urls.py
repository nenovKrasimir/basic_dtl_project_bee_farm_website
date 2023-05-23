from django.urls import path
from basic_dtl_project_bee_farm_website.common_app import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('bee_farm/', views.bee_farm, name='bee-farm')
]