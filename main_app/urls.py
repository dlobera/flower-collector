from django.urls import path
from . import views

urlpatterns = [
  path('', views.home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('flowers/', views.flowers_index, name='flowers_index'),
  path('flowers/<int:flower_id>/', views.flowers_detail, name='flowers_detail'),
  path('flowers/create/', views.FlowerCreate.as_view(), name='flowers_create'),
  path('flowers/<int:pk>/update/', views.FlowerUpdate.as_view(), name='flowers_update'),
  path('flowers/<int:pk>/delete/', views.FlowerDelete.as_view(), name='flowers_delete'),
  path('flowers/<int:flower_id>/add_watering/', views.add_watering, name='add_watering'),
  path('flowers/<int:flower_id>/assoc_vase/<int:vase_id>/', views.assoc_vase, name='assoc_vase'),
  path('vases/create/', views.VaseCreate.as_view(), name='vases_create'),
  path('vases/<int:pk>/', views.VaseDetail.as_view(), name='vases_detail'),
  path('vases/', views.VaseList.as_view(), name='vases_index'),
  path('vases/<int:pk>/update/', views.VaseUpdate.as_view(), name='vases_update'),
  path('vases/<int:pk>/delete/', views.VaseDelete.as_view(), name='vases_delete'),
  path('accounts/signup', views.signup, name='signup'),
]