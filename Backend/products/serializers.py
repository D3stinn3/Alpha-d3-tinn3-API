from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    my_offer = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            "title",
            "content",
            "context",
            "price",
            "sale_price",
            "context_breakdown",
            "my_discount",
            "my_offer",
        ]
        
    def get_my_discount(self, obj):
            return obj.get_discount()
        
    def get_my_offer(self, obj):
            return obj.get_offer()
        
        
class PrimaryProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    my_offer = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            "title",
            "content",
            "context",
            "price",
            "sale_price",
            "context_breakdown",
            "my_discount",
            "my_offer",
        ]
        
        def get_my_discount(self, obj):
            try:
                return obj.get_discount()
            except:
                return None
            
        def get_my_offer(self, obj):
            try:
                return obj.get_offer()
            except:
                return None
