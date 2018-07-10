from rest_framework import filters, generics
from rest_framework.response import Response
from rest_framework.reverse import reverse as api_reverse
from rest_framework.views import APIView
import requests
import json

# Create your views here.
from .models import Category, Product, ProductSeller, ProductBrand, ProductStyles, ProductRooms, ProductOccasion
from .pagination import CategoryPagination
from .serializers import (CategorySerializer, ProductDetailSerializer, ProductSerializer, BrandSerializer, ProductOccasionSerializer, ProductRoomsSerializer, ProductStylesSerializer,
                          SellerSerializer)
from project.settings import PROJECT_URL

class APIHomeView(APIView):
    def get(self, request, format=None):
        data = {

            "address": {
                "url": api_reverse("user_address_list_api", request=request),
                "create": api_reverse("user_address_create_api", request=request),
            },
            "checkout": {
                "cart": api_reverse("cart_api", request=request),
                "checkout": api_reverse("checkout_api", request=request),
                "finalize": api_reverse("checkout_finalize_api", request=request),
            },
            "products": {
                "count": Product.objects.all().count(),
                "url": api_reverse("products_api", request=request)
            },

            "sellers": {
                "count": ProductSeller.objects.all().count(),
                "url": api_reverse("sellers_api", request=request)
            },
            "brands": {
                "count": ProductBrand.objects.all().count(),
                "url": api_reverse("brands_api", request=request)
            },
            "dummy_pages": {
                "url": api_reverse("dummy_api", request=request)
            },
            "categories": {
                "count": Category.objects.all().count(),
                "url": api_reverse("categories_api", request=request)
            },
            "orders": {
                "url": api_reverse("orders_api", request=request),
            }
        }
        return Response(data)


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SearchListAPIView(APIView):

    def get(self, request, format=None):
        queryset = ProductOccasion.objects.all()
        occasion_items = ProductOccasionSerializer(queryset, many=True)
        queryset = ProductStyles.objects.all()
        style_item = ProductStylesSerializer(queryset, many=True)
        queryset = ProductBrand.objects.all()
        brand_item = BrandSerializer(queryset, many=True)
        queryset = ProductRooms.objects.all()
        room_item = ProductRoomsSerializer(queryset, many=True)
        data = {
            'occasions' : occasion_items.data,
            'rooms' : room_item.data,
            'styles' : style_item.data,
            'brands' : brand_item.data
        }
        return Response(data)

class FilteredListAPIView(APIView):

    def post(self, request, format=None):
        searchItem = self.request.POST.get('search_item');
        itemId = self.request.POST.get('item_id');

        if searchItem == "occasions":
            data = requests.get(PROJECT_URL + '/api/occasion/' + itemId)
        elif searchItem == 'styles':
            data = requests.get(PROJECT_URL + '/api/style/' + itemId)
        elif searchItem == 'rooms':
            data = requests.get(PROJECT_URL + '/api/room/' + itemId)
        elif searchItem == 'brands':
            data = requests.get(PROJECT_URL + "/api/brand/" + itemId)

        data = json.loads(data.text)
        return Response(data)

class StyleListAPIView(generics.ListAPIView):
    queryset = ProductStyles.objects.all()
    serializer_class = ProductStylesSerializer



class StyleRetrieveAPIView(generics.RetrieveAPIView):
    queryset = ProductStyles.objects.all()
    serializer_class = ProductStylesSerializer

class RoomListAPIView(generics.ListAPIView):
    queryset = ProductRooms.objects.all()
    serializer_class = ProductRoomsSerializer



class RoomRetrieveAPIView(generics.RetrieveAPIView):
    queryset = ProductRooms.objects.all()
    serializer_class = ProductRoomsSerializer

class OccasionListAPIView(generics.ListAPIView):
    queryset = ProductOccasion.objects.all()
    serializer_class = ProductOccasionSerializer



class OccasionRetrieveAPIView(generics.RetrieveAPIView):
    queryset = ProductOccasion.objects.all()
    serializer_class = ProductOccasionSerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["title", "description"]
    ordering_fields = ["title", "id", 'price', 'modified_date', 'created_date']


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class SellerListAPIView(generics.ListAPIView):
    queryset = ProductSeller.objects.all()
    serializer_class = SellerSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["title"]
    ordering_fields = ["title", "id"]


class BrandListAPIView(generics.ListAPIView):
    queryset = ProductBrand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["title"]
    ordering_fields = ["title", "id"]

class BrandRetrieveAPIView(generics.RetrieveAPIView):
    queryset = ProductBrand.objects.all()
    serializer_class = BrandSerializer