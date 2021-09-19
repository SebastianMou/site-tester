from .basket import Basket

"""
passing the request data in to the Basket class
"""
def basket(request):                   ## get request
    return {'basket': Basket(request)} ## sending the request to Basket