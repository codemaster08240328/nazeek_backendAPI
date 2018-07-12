from django.contrib import admin

from .models import Category, Product, ProductImage, Variation, ProductBrand, ProductSeller, ProductVarImage, ProductOccasion, ProductStyles, ProductRooms, ProductDesigner, ProductTable, ProductChair, ProductSofa


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    max_num = 10


class VariationInline(admin.TabularInline):
    model = Variation
    extra = 0
    max_num = 10


class ImagesInline(admin.TabularInline):
    model = ProductVarImage
    extra = 0
    max_num = 10


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price']
    inlines = [
        ProductImageInline,
        VariationInline,
    ]

    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(seller_id__user_id=request.user)
        else:
            return qs

    class Meta:
        model = Product


class VariationAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'color', 'price']
    inlines = [
        ImagesInline,
    ]

    def get_queryset(self, request):
        qs = super(VariationAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(product__seller_id__user_id=request.user)
        else:
            return qs

    class Meta:
        model = Variation


class BrandAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    def get_queryset(self, request):
        qs = super(BrandAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(seller_id__user_id=request.user)
        else:
            return qs
    class Meta:
        model = ProductBrand


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['__str__']

    def get_queryset(self, request):
        qs = super(ProductImageAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(product__seller_id__user_id=request.user)
        else:
            return qs

    class Meta:
        model = ProductImage


class ProductVarImageAdmin(admin.ModelAdmin):
    list_display = ['__str__']

    def get_queryset(self, request):
        qs = super(ProductVarImageAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(variation__product__seller_id__user_id=request.user)
        else:
            return qs

    class Meta:
        model = ProductVarImage

class ProductStylesAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    def get_queryset(self, request):
        qs = super(ProductStylesAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(seller_id__user_id=request.user)
        else:
            return qs
    class Meta:
        model = ProductStyles

class ProductOccasionAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    def get_queryset(self, request):
        qs = super(ProductOccasionAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(seller_id__user_id=request.user)
        else:
            return qs
    class Meta:
        model = ProductOccasion

class ProductRoomsAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    def get_queryset(self, request):
        qs = super(ProductRoomsAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(seller_id__user_id=request.user)
        else:
            return qs
    class Meta:
        model = ProductRooms

class ProductDesignerAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    def get_queryset(self, request):
        qs = super(ProductDesignerAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(seller_id__user_id=request.user)
        else:
            return qs
    class Meta:
        model = ProductDesigner

class ProductTableAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    def get_queryset(self, request):
        qs = super(ProductTableAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(seller_id__user_id=request.user)
        else:
            return qs
    class Meta:
        model = ProductTable

class ProductChairAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    def get_queryset(self, request):
        qs = super(ProductChairAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(seller_id__user_id=request.user)
        else:
            return qs
    class Meta:
        model = ProductChair
class ProductSofaAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    def get_queryset(self, request):
        qs = super(ProductSofaAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(seller_id__user_id=request.user)
        else:
            return qs
    class Meta:
        model = ProductSofa

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductVarImage, ProductVarImageAdmin)
admin.site.register(Category)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ProductBrand, BrandAdmin)
admin.site.register(ProductSeller)
admin.site.register(ProductRooms, ProductRoomsAdmin)
admin.site.register(ProductOccasion, ProductOccasionAdmin)
admin.site.register(ProductStyles, ProductStylesAdmin)
admin.site.register(ProductDesigner, ProductDesignerAdmin)
admin.site.register(ProductTable, ProductTableAdmin)
admin.site.register(ProductChair, ProductChairAdmin)
admin.site.register(ProductSofa, ProductSofaAdmin)
