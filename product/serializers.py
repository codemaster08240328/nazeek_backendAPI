import base64

from django.core.files import File
from rest_framework import serializers

from .models import Category, Product, ProductImage, Variation, ProductBrand, ProductSeller, ProductVarImage, ProductOccasion, ProductRooms, ProductStyles, ProductDesigner, ProductTable, ProductChair, ProductSofa



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
            'product',
            "id",
            "title",
            "price",
            "sale_price",
            "color",
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

class SearchVariationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Variation
        fields = [
            "id",
            "title",
            "price",
            "sale_price",
            "color",
        ]


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

class SearchProductSerializer(serializers.ModelSerializer):
    variation_set = SearchVariationSerializer(many=True)
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
            'arab'
            "description",
            "product_set",
        ]

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'arab',
            'description'
        ]

class ProductOccasionSerializer(serializers.ModelSerializer):
    product_set = ProductSerializer(many=True)
    class Meta:
        model = ProductOccasion
        fields = [
            'id',
            'title',
            'arab',
            'product_set'
        ]

class ProductDesignerSerializer(serializers.ModelSerializer):
    product_set = ProductSerializer(many=True)
    class Meta:
        model = ProductDesigner
        fields = [
            'id',
            'title',
            'product_set'
        ]

class ProductTableSerializer(serializers.ModelSerializer):
    product_set = ProductSerializer(many=True)
    class Meta:
        model = ProductTable
        fields = [
            'id',
            'title',
            'product_set'
        ]

class ProductChairSerializer(serializers.ModelSerializer):
    product_set = ProductSerializer(many=True)
    class Meta:
        model = ProductChair
        fields = [
            'id',
            'title',
            'product_set'
        ]

class ProductSofaSerializer(serializers.ModelSerializer):
    product_set = ProductSerializer(many=True)
    class Meta:
        model = ProductSofa
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
            'arab',
            'product_set'
        ]

class ProductStylesSerializer(serializers.ModelSerializer):
    product_set = ProductSerializer(many=True)
    class Meta:
        model = ProductStyles
        fields = [
            'id',
            'title',
            'arab',
            'product_set'
        ]
# class ListFilter(Filter):
#     def filter(self, qs, value):
#         value_list = value.split(u',')
#         return super(ListFilter, self).filter(qs, Lookup(value_list, 'in'))
#
# class ProductStylesSerializer(filters.Filterset):
#     styles = ListFilter(name='categories__slug')
#     class Meta:
#         model = ProductStyles
#         fields = [
#             'id',
#             'title',
#             'product_set'
#         ]


    # class Meta:
    #     model = ProductStyles
    #     fields = ['category']

class BrandSerializer(serializers.ModelSerializer):
    product_set = ProductSerializer(many=True)
    class Meta:
        model = ProductBrand
        fields = [
            "title",
            'arab',
            "id",
            "product_set"
        ]
class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBrand
        fields = [
            "title",
            'arab',
            "id"
        ]
class OccasionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOccasion
        fields = [
            'id',
            'title',
            "arab"
        ]

class DesignerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDesigner
        fields = [
            'id',
            'title'
        ]

class TableListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTable
        fields = [
            'id',
            'title',        ]

class ChairListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductChair
        fields = [
            'id',
            'title'
        ]

class SofaListSerializer(serializers.ModelSerializer):
    product_set = ProductSerializer(many=True)
    class Meta:
        model = ProductSofa
        fields = [
            'id'
            'title',
        ]

class RoomsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRooms
        fields = [
            'id',
            'title',
            "arab",
        ]

class StylesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductStyles
        fields = [
            'id',
            'title',
            "arab"
        ]

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSeller
        fields = [
            "title",
            "id",
            "user_id"
        ]
