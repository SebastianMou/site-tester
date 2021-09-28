from store.models import Product
from decimal import Decimal

class Basket():
    """"
    a base basket class,providing some default behaviors that
    can be inherited or overridad, as necessary
    """

    ## __init__ integer constructor
    def __init__(self, request):
        self.session = request.session          ## assign self to request session(grabing info inside request/ grabing session data)
        basket = self.session.get('skey')       ## get session key
        if 'skey' not in request.session:       ## if no session key
            basket = self.session['skey'] = {}  ## set up new session
        self.basket = basket                    ## contaning new session or old session

    def add(self, product, qty):
        """
        adding and updating the user basket session data
        """
        product_id = product.id                                                             ## save product_id in product.id

        ## the self.basket wich can acces the info and the basket can have informacion about the users session
        if product_id not in self.basket:                                                   ## if product_iud is not in the basket
            self.basket[product_id] = {'price': str(product.price), 'qty': int(qty)}        ## is no session id exist it will create session

        self.session.modified = True                                                        ## telling django that we have modified the session

    def __iter__(self):
        """
        collect the product in the session data to query database and return products
        """
        product_ids = self.basket.keys()                        ## collect ALL the keys/products
        products = Product.products.filter(id__in=product_ids) 
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

        

    def __len__(self):
        """
        get the basket data and count the qty of items
        """
        return sum(item['qty'] for item in self.basket.values())

