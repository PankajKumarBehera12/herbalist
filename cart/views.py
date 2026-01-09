from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from cart.cart import Cart
from products.models import Product


@csrf_exempt        # TEMPORARY: for debugging
@require_POST
def cart_add(request):
    try:
        product_id = request.POST.get('product_id')

        if not product_id:
            return JsonResponse({'error': 'Product ID missing'}, status=400)

        product = Product.objects.get(id=product_id)

        cart = Cart(request)
        cart.add(product=product)

        cart_quantity = cart.__len__()



        return JsonResponse({
            'Product name:' : product.name,
            'qty': cart_quantity,
            'success': True,
            'cart_count': len(cart.cart)
        })

    except Product.DoesNotExist:
        return JsonResponse({'error': 'Invalid product'}, status=404)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prod()
    return render(request, 'cart_summary.html', {"cart_products": cart_products})

def cart_delete(request):
    pass
def cart_update(request):
    pass 