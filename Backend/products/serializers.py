from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    discount_yangu = serializers.SerializerMethodField(read_only=True)
    offer_yangu = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            "title",
            "content",
            "context",
            "price",
            "sale_price",
            "context_breakdown",
            "discount_yangu",
            "offer_yangu",
        ]
        
        def get_discount_yangu(self, obj):
            return obj.get_discount()
        
        def get_offer_yangu(self, obj):
            return obj.get_offer()
        
        
class PrimaryProductSerializer(serializers.ModelSerializer):
    discount_yangu = serializers.SerializerMethodField(read_only=True)
    offer_yangu = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            "title",
            "content",
            "context",
            "price",
            "sale_price",
            "context_breakdown",
            "discount_yangu",
            "offer_yangu",
        ]
        
        def get_discount_yangu(self, obj):
            try:
                return obj.get_discount()
            except:
                return None
            
        def get_offer_yangu(self, obj):
            try:
                return obj.get_offer()
            except:
                return None
