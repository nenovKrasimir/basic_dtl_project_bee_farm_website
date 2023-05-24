from django.urls import path
from basic_dtl_project_bee_farm_website.products import views

urlpatterns = [
    path('', views.all_products, name='all-products'),
    path('buy/', views.buy_product, name='buy_product')
]