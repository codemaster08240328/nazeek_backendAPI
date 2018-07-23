from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from cart.views import (
    CartAPIView,
    CheckoutAPIView,
    CheckoutFinalizeAPIView, CheckoutFinalView, ItemCountView, CartItemDeleteAPIView
# ,CartAPIView_GetItem
)
from dummy_pages.views import DummyListAPIView
from order.views import (OrderListAPIView, OrderRetrieveAPIView, UserAddressCreateAPIView, UserAddressListAPIView,
                         UserCheckoutAPI, UserGetID)
from product.views import (APIHomeView, BrandListAPIView, CategoryListAPIView, CategoryRetrieveAPIView,
                           ProductListAPIView, ProductRetrieveAPIView, SellerListAPIView, SearchListAPIView,
                           FilteredListAPIView, StyleRetrieveAPIView, RoomRetrieveAPIView, OccasionRetrieveAPIView, BrandRetrieveAPIView, DesignerRetrieveAPIView,TableRetrieveAPIView,ChairRetrieveAPIView,SofaRetrieveAPIView
                           )
from user_profile.views import (UserViewSet)
from social import views
from rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)
router = routers.DefaultRouter()
router.register(r'user', UserViewSet, )

urlpatterns = [
    # router.urls,
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('wishlists.urls')),
    url(r'^api/', include('product_review.urls')),
    url(r'^api/newsletter/', include('newsletter.api.urls')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

    url(r'^rest-auth/social/facebook/$', views.FacebookLogin.as_view(), name='fb_login'),
    url(r'^rest-auth/social/twitter/$', views.TwitterLogin.as_view(), name='twitter_login'),
    url(r'^rest-auth/social/google/$', views.GoogleLogin.as_view(), name='google_login'),

    url(r'^rest-auth/facebook/connect/$', views.FacebookConnect.as_view(), name='fb_connect'),
    url(r'^rest-auth/google/connect/$', views.GoogleConnect.as_view(), name='google_connect'),
    url(r'^rest-auth/twitter/connect/$', views.TwitterConnect.as_view(), name='twitter_connect'),

    url(r'^socialaccounts/$', SocialAccountListView.as_view(), name='social_account_list'),
    url(r'^socialaccounts/(?P<pk>\d+)/disconnect/$', SocialAccountDisconnectView.as_view(), name='social_account_disconnect'),

    url(r'^account/', include('allauth.urls')),
    url(r'^api/$', APIHomeView.as_view(), name='home_api'),
    url(r'^api/products/$', ProductListAPIView.as_view(), name='products_api'),
    url(r'^api/sellers/$', SellerListAPIView.as_view(), name='sellers_api'),
    url(r'^api/brand/$', BrandListAPIView.as_view(), name='brands_api'),
    url(r'^api/dummy/$', DummyListAPIView.as_view(), name='dummy_api'),
    url(r'^api/categories/$', CategoryListAPIView.as_view(), name='categories_api'),
    url(r'^api/categories/(?P<pk>\d+)/$', CategoryRetrieveAPIView.as_view(), name='category_detail_api'),
    url(r'^api/products/(?P<pk>\d+)/$', ProductRetrieveAPIView.as_view(), name='products_detail_api'),
    url(r'^api/searchlist/$', SearchListAPIView.as_view(), name='search_list_api'),
    url(r'^api/filtered/$', FilteredListAPIView.as_view(), name='filtered_result_api'),
    url(r'^api/style/(?P<pk>\d+)/$', StyleRetrieveAPIView.as_view(), name='style_item_api'),
    url(r'^api/room/(?P<pk>\d+)/$', RoomRetrieveAPIView.as_view(), name='room_item_api'),
    url(r'^api/occasion/(?P<pk>\d+)/$', OccasionRetrieveAPIView.as_view(), name='occasion_item_api'),
    url(r'^api/brand/(?P<pk>\d+)/$', BrandRetrieveAPIView.as_view(), name='brand_item_api'),
    url(r'^api/designer/(?P<pk>\d+)/$', DesignerRetrieveAPIView.as_view(), name='designer_item_api'),
    url(r'^api/table/(?P<pk>\d+)/$', TableRetrieveAPIView.as_view(), name='table_item_api'),
    url(r'^api/chair/(?P<pk>\d+)/$', ChairRetrieveAPIView.as_view(), name='chair_item_api'),
    url(r'^api/sofa/(?P<pk>\d+)/$', SofaRetrieveAPIView.as_view(), name='sofa_item_api'),
    url(r'^api/orders/$', OrderListAPIView.as_view(), name='orders_api'),
    url(r'^api/orders/(?P<pk>\d+)/$', OrderRetrieveAPIView.as_view(), name='order_detail_api'),
    url(r'^api/cart/$', CartAPIView.as_view(), name='cart_api'),
    url(r'^api/cartdelete/(?P<cart_pk>[0-9]+)/(?P<item_pk>[0-9]+)/$',
        CartItemDeleteAPIView.as_view(), name='cart_delete'),
    url(r'^cart/count/$', ItemCountView.as_view(), name='item_count'),
    url(r'^checkout/final/$', CheckoutFinalView.as_view(), name='checkout_final'),
    url(r'^api/checkout/$', CheckoutAPIView.as_view(), name='checkout_api'),
    url(r'^api/checkout/finalize/$', CheckoutFinalizeAPIView.as_view(), name='checkout_finalize_api'),
    url(r'^api/auth/token/$', obtain_jwt_token, name='auth_login_api'),
    url(r'^api/auth/token/refresh/$', refresh_jwt_token, name='refresh_token_api'),
    url(r'^api/user/address/$', UserAddressListAPIView.as_view(), name='user_address_list_api'),
    url(r'^api/user/get/$', UserGetID.as_view(), name='user_token_list_api'),
    url(r'^api/user/address/create/$', UserAddressCreateAPIView.as_view(), name='user_address_create_api'),
    url(r'^api/user/checkout/$', UserCheckoutAPI.as_view(), name='user_checkout_api'),
    url(r'^api/categories/$', CategoryListAPIView.as_view(), name='categories_api'),
    url(r'^api/categories/(?P<pk>\d+)/$', CategoryRetrieveAPIView.as_view(), name='category_detail_api'),
    url(r'^api/orders/$', OrderListAPIView.as_view(), name='orders_api'),
    url(r'^api/orders/(?P<pk>\d+)/$', OrderRetrieveAPIView.as_view(), name='order_detail_api'),

]
