import base64

from django.core.files import File
from rest_framework import serializers

from .models import Category, Product, ProductImage, Variation, ProductBrand, ProductSeller, ProductVarImage, ProductOccasion, ProductRooms, ProductStyles


class ProductVarImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        f = open(obj.image.path, 'rb')
        image = File(f)
        data = base64.b64encode(image.read())
        f.close()
        return data

    class Meta:
        model = ProductVarImage
        fields = [
            "variation",
            "image",
        ]


class VariationSerializer(serializers.ModelSerializer):
    productvarimage_set = ProductVarImageSerializer(many=True)
    product = serializers.SerializerMethodField()
    class Meta:
        model = Variation
        fields = [
            "id",
            "title",
            "price",
            "sale_price",
            "color",
            "product",
            "productvarimage_set"
        ]

    def get_product(self,obj):
        f = open(obj.product.productimage_set.first().image.path, 'rb')
        image = File(f)
        img_data = base64.b64encode(image.read())
        data = {
            "title":obj.product.title,
            "description":obj.product.description,
            "seller_name":obj.product.seller_id.title,
            "image":img_data
        }
        f.close()
        return  data


class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        f = open(obj.image.path, 'rb')
        image = File(f)
        data = base64.b64encode(image.read())
        f.close()
        return data

    class Meta:
        model = ProductImage
        fields = [
            "product",
            "image",
        ]


class ProductDetailUpdateSerializer(serializers.ModelSerializer):
    variation_set = VariationSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "image",
            "variation_set",
        ]

    def get_image(self, obj):
        f = open(obj.productimage_set.first().image.path, 'rb')
        image = File(f)
        data = base64.b64encode(image.read())
        f.close()
        return data

    def create(self, validated_data):
        title = validated_data["title"]
        Product.objects.get(title=title)
        product = Product.objects.create(**validated_data)
        return product

    def update(self, instance, validated_data):
        instance.title = validated_data["title"]
        instance.save()
        return instance


class ProductDetailSerializer(serializers.ModelSerializer):
    variation_set = VariationSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()
    productimage_set = ProductImageSerializer(many=True)
    similar_product_set = serializers.SerializerMethodField()
    seller_name = serializers.CharField(source='seller_id.title')
    category_name = serializers.CharField(source='default.title')


    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "detail",
            "review",
            "price",
            "brand_id",
            "style_id",
            "occasion_id",
            "room_id",
            "seller_name",
            'category_name',
            "image",
            "variation_set",
            "productimage_set",
            "similar_product_set"
        ]

    def get_image(self, obj):
        f = open(obj.productimage_set.first().image.path, 'rb')
        image = File(f)
        data = base64.b64encode(image.read())
        f.close()
        return data

    def get_similar_product_set(self, obj):

        query_set = Product.objects.get_related(obj)
        serializer = SimilarProduct(query_set, many=True)
        return serializer.data
        # data = serializers.serialize('json', query_set, ensure_ascii=False)
        # data = query_set.get()
        # # data = ProductSerializer(query_set)

class SimilarProduct(serializers.ModelSerializer):
    productimage_set = ProductImageSerializer(many=True)
    img = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'price',
            'img',
            'productimage_set',
        ]

    def get_img(self, obj):
        f = open(obj.productimage_set.first().image.path, 'rb')
        image = File(f)
        data = base64.b64encode(image.read())
        f.close()
        return data


class ProductSerializer(serializers.ModelSerializer):
    variation_set = VariationSerializer(many=True)
    productimage_set = ProductImageSerializer(many=True)
    image = serializers.SerializerMethodField()
    brand_name = serializers.CharField(source='brand_id.title')
    seller_name = serializers.CharField(source='seller_id.title')

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "brand_id",
            "seller_id",
            'description',
            "brand_name",
            "seller_name",
            "image",
            'price',
            "variation_set",
            "productimage_set"
        ]

    def get_image(self, obj):
        f = open(obj.productimage_set.first().image.path, 'rb')
        image = File(f)
        data = base64.b64encode(image.read())
        f.close()
        return data



class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='category_detail_api')
    product_set = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = [
            "url",
            "id",
            "title",
            "description",
            "product_set",
        ]

class ProductOccasionSerializer(serializers.ModelSerializer):
    product_set = ProductSerializer(many=True)
    class Meta:
        model = ProductOccasion
        fields = [
            'id',
            'title',
            'product_set'
        ]

class ProductRoomsSerializer(serializers.ModelSerializer):
    product_set = ProductSerializer(many=True)
    class Meta:
        model = ProductRooms
        fields = [
            'id',
            'title',
            'product_set'
        ]

class ProductStylesSerializer(serializers.ModelSerializer):
    product_set = ProductSerializer(many=True)
    class Meta:
        model = ProductStyles
        fields = [
            'id',
            'title',
            'product_set'
        ]



class BrandSerializer(serializers.ModelSerializer):
    product_set = ProductSerializer(many=True)
    class Meta:
        model = ProductBrand
        fields = [
            "title",
            "id",
            "product_set"
        ]


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSeller
        fields = [
            "title",
            "id",
            "user_id"
        ]