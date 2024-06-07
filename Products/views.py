from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Product
from .models import Category
from .models import Cart
from django.http import JsonResponse
from .models import CartItem
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from mytask.cart import Carts


# Create your views here


def index(request):
    
    features = Product.objects.filter(is_feature = True)
    organics = Product.objects.filter( is_organic= True)
    inorganics = Product.objects.filter( is_inorganic=False)
    
    categorys = Category.objects.all()
    
   
    bestsellers = Product.objects.filter(is_bestseller=True)
    
    
    # allfeatures = Product.objects.filter(is_allfeatures=True)
    

    
    return render(request, 'index.html', {'features':features, 'categorys':categorys, 'bestsellers':bestsellers, 'organics':organics, 'inorganics':inorganics})


def shop(request):
    features = Product.objects.filter(is_feature = True)

    
    categorys = Category.objects.all()
    
    allProducts = Category.objects.all()
    
    featureall = Product.objects.filter(is_feature=True)
    
    allproduct = Product.objects.all()
    
   
    return render(request, 'shop.html', {'features':features, 'categorys':categorys, 'allproducts':allProducts, 'featureall':featureall, 'allproduct':allproduct})


# def details_view(request, pk):
#     products = get_object_or_404(Product, pk=pk)
#     products = Product.objects.filter(pk=pk)
#     # products = Product.objects.get(pk=pk)
    
#     return render(request, 'details_view.html', {'products':products})




def shop_detail(request, id):
    products = get_object_or_404(Product, id=id)
    products = Product.objects.filter(id=id)
    
    featureall = Product.objects.filter(is_feature=True)
   
    
    return render(request, 'shop_detail.html', {'products': products, 'featureall':featureall,})




def cart_add(request):
    
    cart = Carts(request)
    
    if request.POST.get('action') == 'post':
        
        product_id = int(request.POST.get('product_id'))
        
        product = get_object_or_404(Product, id=product_id)
        
        cart.add(product=product)
        
        
        response = JsonResponse({'Product Name': product_id})
        
        context = {'response':response}
        
        return render(request, 'cart_add.html', context) 

 

# trial version



def add_to_cart(user, product_id, quantity=1):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=user)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
        
    cart_item.save()
    return cart_item
    

# ends here


@login_required
def add_product_to_cart(request, product_id):
    if request.method == "POST":
        quantity = int(request.POST.get('quantity', 1))
        add_to_cart(request, product_id, quantity)
        return redirect(reverse('cart_detail'))


@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart_detail.html', {'cart': cart, 'created':created} )

# END TRIALS

# def addtocart(request):
#     if request.method == "POST":
#         if request.user.is_authenticated:
#             prod_id = int(request.POST.get('product_id'))
#             try:
#                 product_check = Product.objects.get(id=prod_id)
#             except Product.DoesNotExist:
#                 return JsonResponse({'status': 'No such product found'})

#             if Cart.objects.filter(user=request.user, product_id=prod_id).exists():
#                 return JsonResponse({'status': 'Product already in cart'})
#             else:
#                 prod_qty = int(request.POST.get('product_qty'))

#                 if product_check.quantity >= prod_qty:
#                     Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
#                     return JsonResponse({'status': 'Product added successfully'})
#                 else:
#                     return JsonResponse({'status': f'Only {product_check.quantity} quantity available'})
#         else:
#             return JsonResponse({'status': 'Login to continue'})

#     return redirect('addtocart')





# def cart(request, pk):
#     cart_p={}
#     cart_p[str(request.GET['id'])]={
#         'title':request.GET['title'],
#         'qty':request.GET['qty'],
#         'price':request.GET['price']
#     }
    
    
    
    
#     if 'cartdata' in request.session:
    
#        if str(request.GET['id']) in request.session['cartdata']:
#           cart_data=request.session['cartdata']
#           cart_data[str(request.GET['id'])]['qty']+=1
#           cart_data.update(cart_data)
#           request.session['cartdata']=cart_data
#        else:
#            cart_data=request.session['cartdata']
#            cart_data.update(cart_data)
#            request.session['cart_data']-cart_data
#     else:
#          request.session['cartdata']=cart_p   
    
    
#     return JsonResponse({'data':request.session['cartdata']})     
    
#     return render(request, 'cart.html', context)






# FOR FORMS

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        # email = request.POST.get['email']
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








# def index(request):
    
#     feature1 = Feature()
#     feature1.id = 0
#     feature1.name = 'apple'
#     feature1.desc = 'is very sweet papa'
#     feature1.price = '$4352'
#     feature1.is_true = 'False'
    
#     feature2 = Feature()
#     feature2.id = 1
#     feature2.name = 'pineaple'
#     feature2.desc = 'taste great'
#     feature2.price = '$5687'
#     feature1.is_true = 'True'
    
#     feature3 = Feature()
#     feature3.id = 2
#     feature3.name = 'watermelon'
#     feature3.desc = 'good for blood circulation'
#     feature3.price = '$9352'
#     feature1.is_true = 'True'
    
    
#     feature4 = Feature()
#     feature4.id = 3
#     feature4.name = 'banana'
#     feature4.desc = 'digest food quick'
#     feature4.price = '$2008'
    
    
  

#     return render(request, 'index.html', {'feature': feature1, 'features': feature2, 'featuress': feature3, 'featuresss':feature4 })
