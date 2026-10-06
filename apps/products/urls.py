from django.urls import path, include
from . import views
from rest_framework import routers

from django.conf.urls.static import static
from django.conf import settings

app_name = 'products'

router = routers.SimpleRouter()
router.register('', views.ProductViewSet, basename='produtos')


urlpatterns = [
# - = - = - = - = - = - MVT - = - = - = - = - = -
    path('listar/', views.list_products, name='list_products'),
    path('adicionar/', views.add_product, name='add_product'),
    path('editar/<int:id_product>/', views.edit_product, name='edit_product'),
    path('excluir/<int:id_product>/', views.delete_product, name='delete_product'),

# - = - = - = - = - = - REST - = - = - = - = - = -
    path('', include(router.urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)