from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name = 'index'),
    path('register', views.register, name = 'register'),
    path('login', views.login,  name = 'login'),
    path('shop', views.shop, name='shop'),
    # path('products/<int:pk>/', views.details_view, name="details_view"),
    path('products/<int:id>/', views.shop_detail, name="shop_detail"),
    # path('cart/', views.cart_view, name='cart_view'),
    # path('cart/<int:id>/', views.cart, name='cart'),
    
    # path('cart/<int:pk>/', views.cart, name="cart"),
    # path('addtocart', views.addtocart, name="addtocart")
    path('cart/', views.cart_detail, name='cart_detail'),
    # path('add_to_cart', views.add_to_cart, name="add_to_cart"),
    path('cart/add/<int:product_id>/', views.add_product_to_cart, name='cart_add'),
    
    path('add/', views.cart_add, name="cart_add")
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)