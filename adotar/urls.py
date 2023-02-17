from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.listar_pets, name='listar_pets'),
    path('ver_pedido_adocao/<int:id>', views.pedido_adocao, name='pedido_adocao'),
   
] 
