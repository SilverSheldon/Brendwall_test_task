from django.urls import path
from rest_framework import routers

from .views import ProductViewSet, AddProductView

app_name = 'shop'

router = routers.SimpleRouter()
router.register(prefix=r'products', viewset=ProductViewSet)

urlpatterns = [
    path('add_product/', AddProductView.as_view(), name='add_product')
]

urlpatterns += router.urls
print(urlpatterns)