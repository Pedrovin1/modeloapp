from .models import Produtos
from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Produtos
        fields = '__all__'