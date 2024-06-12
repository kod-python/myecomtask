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
from .models import Order, OrderItem ,Carts
import uuid
from .forms import CheckoutForm


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


def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    cart = Cart(request)
    
    return render(request, 'order_confirmation.html', {'order': order, 'cart':cart})



def proceed_checkout(request):
    cart = Cart(request)
    if not cart:
        messages.error(request, "Your cart is empty")
        return redirect('cart')
    

    messages.success(request, "Proceeding to checkout")
    return redirect('checkout')












# def checkout(request):
    
#    product = Product.objects.all()
#    cart = Cart(request)
#    product_count = cart.get_product_count()
    
#    if request.method == 'POST':
#         form = CheckoutForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             company_name = form.cleaned_data['company_name']
#             address = form.cleaned_data['address']
#             house_number_street_name = form.cleaned_data['house_number_street_name']
#             town_city = form.cleaned_data['town_city']
#             country = form.cleaned_data['country']
#             postcode_zip = form.cleaned_data['postcode_zip']
#             mobile = form.cleaned_data['mobile']
#             email_address = form.cleaned_data['email_address']
#             create_account = form.cleaned_data['create_account']
#             ship_to_different_address = form.cleaned_data['ship_to_different_address']
#             payment_method = form.cleaned_data['payment_method']

#             cart = get_object_or_404(Carts, user=request.user)
#             cart_items = OrderItem.objects.filter(cart=cart)

          
#             total_price = 0
#             for item in cart_items:
#                 item.sub_total = item.product.price * item.quantity
#                 total_price += item.sub_total

          
#             order = Order.objects.create(
#                 user=request.user,
#                 first_name=first_name,
#                 last_name=last_name,
#                 company_name=company_name,
#                 address=address,
#                 house_number_street_name=house_number_street_name,
#                 town_city=town_city,
#                 country=country,
#                 postcode_zip=postcode_zip,
#                 mobile=mobile,
#                 email_address=email_address,
#                 total_price=total_price,
#                 payment_method=','.join(payment_method)  
#             )

          
#             if ship_to_different_address:
              
#                 pass

          
#             cart_items.delete()

#             return redirect('order_confirmation', order_id=order.id)
#    else:
#         form = CheckoutForm()
    

#         cart = get_object_or_404(Carts, user=request.user)
#         cart_items = OrderItem.objects.filter(cart=cart)
    
   
#         for item in cart_items:
#             item.sub_total = item.product.price * item.quantity
    
#    return render(request, 'checkout.html',{'cart':cart, 'form':form, 'product':product, 'product_count':product_count})























def checkout(request):
    product = Product.objects.all()
    cart = Cart(request)
    product_count = cart.get_product_count()
    
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            company_name = form.cleaned_data['company_name']
            address = form.cleaned_data['address']
            house_number_street_name = form.cleaned_data['house_number_street_name']
            town_city = form.cleaned_data['town_city']
            country = form.cleaned_data['country']
            postcode_zip = form.cleaned_data['postcode_zip']
            mobile = form.cleaned_data['mobile']
            email_address = form.cleaned_data['email_address']
            create_account = form.cleaned_data['create_account']
            ship_to_different_address = form.cleaned_data['ship_to_different_address']
            payment_method = form.cleaned_data['payment_method']
          
            cart = get_object_or_404(Carts, user=request.user)
            cart_items = OrderItem.objects.filter(cart=cart)

        
            total_price = sum(item.product.price * item.quantity for item in cart_items)

            order = Order.objects.create(
               user=request.user,
                first_name=first_name,
                last_name=last_name,
                company_name=company_name,
                address=address,
                house_number_street_name=house_number_street_name,
                town_city=town_city,
                country=country,
                postcode_zip=postcode_zip,
                mobile=mobile,
                email_address=email_address,
                total_price=total_price,
                payment_method=','.join(payment_method)  
            )

         
            cart_items.delete()

            return redirect('order_confirmation', order_id=order.id)
    else:
        form = CheckoutForm()
    
    return render(request, 'checkout.html',{'cart':cart, 'form':form, 'product':product, 'product_count':product_count})




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









def testimonial(request):
    
    return render(request, 'testimonial.html')




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








