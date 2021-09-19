

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

    def add(self, product):
        """
        adding and updating the user basket session data
        """
        product_id = product.id

        if product_id not in self.basket:
            self.basket[product_id] = {'price': str(product.price)}

        self.session.modified = True
