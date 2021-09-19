from django.http import response
from django.http.response import Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from store.models import Product 

from .basket import Basket

# Create your views here.

def basket_summary(request):
    return render(request, 'store/basket/summary.html')

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        try:
            product = Product.objects.get(id=product_id)
        except:
            raise Http404
        basket.add(product=product)
        response = JsonResponse({'text':'data'})
        return response
