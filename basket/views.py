from django.http import response
from django.http.response import Http404, JsonResponse
from django.shortcuts import render

from store.models import Product 

from .basket import Basket

# Create your views here.
def basket_summary(request):
    basket = Basket(request)
    return render(request, 'store/basket/summary.html', {'basket': basket})


def basket_add(request):
    """
    colect data that was sent from js/ajaxs/ detail.html
    """
    basket = Basket(request)                                ## grab the session data
    if request.POST.get('action') == 'post':                ## seeing if the request is a post request
        product_id = int(request.POST.get('productid'))     ## get product id
        ##product_qty = int(request.POST.get('productqty'))   ## get product qty
        try:                                                ## exeption 
            product = Product.objects.get(id=product_id)    ## get product_id
        except:
            raise Http404
        basket.add(product=product, qty=1)                  ## save to session
        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})           ## make jasonresponse / to see in console
        return response
