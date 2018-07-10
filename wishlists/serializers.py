from rest_framework import serializers
from .models import Wishlist, WishlistItem
from product.models import Variation
from product.serializers import VariationSerializer
<<<<<<< HEAD

=======
>>>>>>> e5c2f4d56cb9064404831271c81324e10cf7dd2b

from django.conf import settings

#For each
class WishlistItemList(serializers.RelatedField):
    def to_representation(self, value):

        return {
            "id": value.id,
            "wishlist": value.wishlist.id,
            "product": value.product.title,
            "product_id": value.product.id,
            "price": value.product.sale_price,
            "quantity": value.quantity
        }


class WishlistSerializer(serializers.ModelSerializer):
    wishlist_items = WishlistItemList(many=True, read_only=True)
    class Meta:
        model = Wishlist
        fields = ('id', 'user', 'wishlist_items')

class WishlistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistItem
        fields = ('id', 'wishlist', 'product',
            'quantity', 'date_added'
        )

class GetWishListItemsSerializer(serializers.ModelSerializer):
    variation_set = serializers.SerializerMethodField()
    class Meta:
        model = WishlistItem
        fields = ('id', 'wishlist', 'variation_set',
            'quantity', 'date_added'
        )

    def get_variation_set(self, obj):
        query_set = Variation.objects.filter(id=obj.product.id)
        serializers =VariationSerializer(query_set, many=True)
<<<<<<< HEAD
        return serializers.data
=======
        return serializers.data
>>>>>>> e5c2f4d56cb9064404831271c81324e10cf7dd2b
