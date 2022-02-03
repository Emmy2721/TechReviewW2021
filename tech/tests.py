from django.test import TestCase
from django.config.models import User
from .models import TechType, Product, Review
import datetime
from .forms import ProductForm
from django.urls import revers_lazy, reverse

# Create your tests here.
class TechTypeTest(TestCase):

    def setUp(self):
        self.type=TechType(typename='Lenovo Laptop')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Lenovo Laptop')

    def test_tablename(self):
        self.assertEqual(str(TechType._meta.db_table), 'techtype')

class ProductTest(TestCase):
    def setUp(self):
        self.type=TechType(typename='Laptop')
        self.user=User(username= 'user1')
        self.product= Product(productname= 'Lenovo',producttype=self.type, user=self.user, dateentered=datetime.date('2021,1,10'),price=1200.99, producturl='http://www.lenovo.com', description="lenovo laptop")

    def test_string(self):
            self.assertEqual(str(self.product), 'Lenovo')

    def test_discount(self):
        disc = self.product.price * .05
        self.assertEqual(self.product.discountAmount()disc,)

    def test_discountAmount(self):
        disc=self.product.pric * (1 - .05)
        self.assertEqual(self.product.discountprice(),disc)

    class NewProductForm(TestCase):
        #valid form data
        def test_productform(self):
            data={
                {'productname'='surface',
                 'producttype' :'laptop', 
                 'user' :'steve', 
                 'dateentered': '2021-1-5',
                 'price': '1200',
                 'producturl': 'http://www.microsoft.com',
                 'discription': 'half laptop half tablet'
                }

            
        from=productform (data)
        self.assertfalset(form.is_valid)

        data={
                {'productname'='surface',
                 'producttype' :'laptop', 
                 'user' :'steve', 
                 'dateentered': '2021-1-5',
                 'producturl': 'http://www.microsoft.com',
                 'discription': 'half laptop half tablet'
                }
class New_Product_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=user.objects.creat_user(username='testuser1', password='p@ssw0rd1')
        self.type=TechType.object.create(typename='laptop')
        self.product=Product.objects.create(Productname='Lenovo',self.type, user=self.user, dateentered=datetime.date('2021,1,10'),price=1200.99, producturl='http://www.lenovo.com', description="lenovo laptop"))

    def test_redirect_if_not logged_in(self):
        response=self.client.get(reverse('newproduct'))
        self.assertRedirects(response, 'accounts/login/?next=tech/newproduct/')

  

