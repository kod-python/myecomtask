from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Product
from .models import Category
from .cart import Cart
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# from .models import Order, OrderItem 
import uuid


# Create your views here


def index(request):
    
    features = Product.objects.filter(is_feature = True)
    organics = Product.objects.filter( is_organic= True)
    inorganics = Product.objects.filter( is_inorganic=False)
    
    categorys = Category.objects.all()
    cart = Cart(request)
   
    bestsellers = Product.objects.filter(is_bestseller=True)
    
    
    # allfeatures = Product.objects.filter(is_allfeatures=True)
    
    product_count = cart.get_product_count()
    
    return render(request, 'index.html', {'features':features, 'categorys':categorys, 'bestsellers':bestsellers, 'organics':organics, 'inorganics':inorganics, 'product_count':product_count})


def shop(request):
    features = Product.objects.filter(is_feature = True)

    
    categorys = Category.objects.all()
    
    allProducts = Category.objects.all()
    
    featureall = Product.objects.filter(is_feature=True)
    
    allproduct = Product.objects.all()
    cart = Cart(request)
    product_count = cart.get_product_count()
   
    return render(request, 'shop.html', {'features':features, 'categorys':categorys, 'allproducts':allProducts, 'featureall':featureall, 'allproduct':allproduct, 'product_count':product_count})




def shop_detail(request, id):
    products = get_object_or_404(Product, id=id)
    products = Product.objects.filter(id=id)
    
    featureall = Product.objects.filter(is_feature=True)
    cart = Cart(request)
    product_count = cart.get_product_count()
    
    return render(request, 'shop_detail.html', {'products': products, 'featureall':featureall,'product_count':product_count})


def chackout(request):
    
    product = Product.objects.all()
    cart = Cart(request)
    product_count = cart.get_product_count()
    return render(request, 'chackout.html', {'cart':cart, 'product':product, 'product_count':product_count})




def cart(request):
    
    product = Product.objects.all()
    cart = Cart(request)
    # carts = Cart(request)
   
    product_count = cart.get_product_count()
    return render(request, 'cart.html', {'cart':cart, 'product':product, 'product_count':product_count})





def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    quantity = int(request.POST.get('quantity', 1))
    
    cart = Cart(request)
    cart.add(product_id=product.id, quantity=quantity)
    
    messages.success(request, "Product added to cart successfully")
    return redirect('cart')





# def proceed_checkout(request):
#     cart = Cart(request)
#     if not cart:
#         messages.error(request, "Your cart is empty")
#         return redirect('cart')
    
   
#     total = sum(item['price'] * item['quantity'] for item in cart)
    
  
#     order = Order.objects.create(
#         user=request.user,
#         total=total,
#         order_number=str(uuid.uuid4())
#     )
    
  
#     for item in cart:
#         OrderItem.objects.create(
#             order=order,
#             product=item['product'],
#             quantity=item['quantity'],
#             price=item['price']
#         )
    
  
#     cart.clear()

#     messages.success(request, "Order placed successfully")
#     return redirect('order_confirmation', order_id=order.id) 










def proceed_checkout(request):
    cart = Cart(request)
    if not cart:
        messages.error(request, "Your cart is empty")
        return redirect('cart')
    

    messages.success(request, "Proceeding to checkout")
    return redirect('chackout')








def update_cart(request, product_id):
    cart = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    quantity = int(request.POST.get('quantity', 1))
    cart.update_quantity(product_id, quantity)
    messages.success(request, "Cart updated successfully")
    return redirect('cart')    
    
    
    
def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    messages.success(request, "Product removed from cart successfully")
    return redirect('cart')


    
    
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    messages.success(request, "Cart cleared successfully")
    return redirect('cart')
    
    
    
    
    


# FOR FORMS

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        
        password = request.POST['password']
        password2 = request.POST['password2']
        
        
        if password == password2:
            # if User.objects.filter(email=email).exists():
            #     messages.info(request, 'email already exists')
            #     return redirect('register')
            
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return redirect('register')
            
            else:
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'Registration successful. Please login.')
                # User.save()
                return redirect('login')
        else:
            messages.error(request, 'passowrd not matched')
     
            return redirect('register')
        
    else:    
      return render(request, 'register.html')





def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            
            return redirect('/')
        else:
            messages.info(request, 'credentials are incorrect')
            return redirect('login')
    else:       
      return render(request, 'login.html')








