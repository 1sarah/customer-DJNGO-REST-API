from django.test import TestCase
from ordercust.models import Customer, Order
# Create your tests here.

class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(name="bat",code="1234")
        Customer.objects.create(name="hat",code="5678")

    def test_customer_code(self):
            # test customer with a particular code
        bat=Customer.objects.get(name="bat")
        hat=Customer.objects.get(name="hat")
        self.assertEquals(bat.code,1234)
        self.assertEquals(hat.code,5678)

    def test_details(self):
         # Issue a GET request.
        response = self.client.get('/customer/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
