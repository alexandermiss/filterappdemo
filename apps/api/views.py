from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from apps.api.serializers import ProductSerializer

from apps.catalog.models import Product


class ProductListApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_fields = ('name',)
