from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name = 'index'),
    path('register', views.register, name = 'register'),
    path('login', views.login,  name = 'login'),
    path('shop', views.shop, name='shop'),
    path('products/<int:id>/', views.shop_detail, name="shop_detail"),
     path('add-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
      path('update/<int:product_id>/', views.update_cart, name='update_cart'),
    path('cart/', views.cart, name="cart"),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
 path('clear/', views.clear_cart, name='clear_cart'),
   
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)