from django.shortcuts import render,redirect
from product.models import Product
from django.http import HttpResponse

# View to render the product submission form
def product1(request):
     product=Product.objects.all()
     return render(request, 'products.html',{'data':product})

# View to handle form submission and save product
def product2(request):
        product_name = request.POST.get("product_name")
        product_description = request.POST.get("product_description")
        product_price = request.POST.get("product_price")
        product_category = request.POST.get("product_category")
        product_image = request.FILES.get("product_image")
        
        queryset=Product.objects.all()
        Product.objects.create(product_name=product_name,product_description=product_description,product_price=product_price,product_category=product_category,product_image=product_image)
        return redirect('/product3/')  

# View to display all saved products
def product3(request):
    product = Product.objects.all()
    return render(request,'products3.html',{'data':product}) 

def delete_product(request,id):
     product=Product.objects.get(id=id)
     product.delete()
     product =Product.objects.all()
     return render(request,'products3.html',{'data':product})

def edit_product(request,id):
    product=Product.objects.get( id = id)
    return render(request, 'edit_product.html',{'data':product})

def update_product(request, id):
    product = Product.objects.get(id=id)
    product_name = request.POST.get("product_name")
    product_description = request.POST.get("product_description")
    product_price = request.POST.get("product_price")
    product_category = request.POST.get("product_category")
    product_image = request.FILES.get("product_image")

    # Safety check
    if not all([product_name, product_description, product_price, product_category]):
        return render(request, 'edit_product.html', {
            'data': product,
            'error': 'All fields are required.'
        })

    # Update fields manually
    product.product_name = product_name
    product.product_description = product_description
    product.product_price = product_price
    product.product_category = product_category

    # Update image if a new one is uploaded
    if product_image:
        product.product_image = product_image

    product.save()  # Save changes to DB

    return redirect('/product3/')  # Go to product3 page


def add_to_cart(request, id):
    cart = request.session.get('cart', {})
    cart[str(id)] = cart.get(str(id), 0) + 1  # Add or increment item
    request.session['cart'] = cart
    return redirect('view_cart')




def view_cart(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())

    cart_items = []
    for product in products:
        cart_items.append({
            'product': product,
            'quantity': cart[str(product.id)],
        })

    return render(request, 'cart.html', {'cart_items': cart_items})

def check_out(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())

    cart_items = [
        {
            'product': product,
            'quantity': cart[str(product.id)],
            'item_total': product.product_price * cart[str(product.id)]
        }
        for product in products
    ]

    total = sum(item['item_total'] for item in cart_items)

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total': total,
    })

