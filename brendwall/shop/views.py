from django.views.generic import CreateView
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .forms import AddProductForm
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AddProductView(CreateView):
    form_class = AddProductForm
    template_name = 'shop/add_product.html'
    extra_context = {
        'head_title': "Добавить продукт",
        'legend': 'Добавьте продукт',
    }
