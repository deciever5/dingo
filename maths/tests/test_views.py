from django.test import TestCase, Client
from dingo.maths.models import Math, Result

class MathViewsTest(TestCase):

    def setUp(self):
        result = Result.objects.create(value=10)
        Math.objects.create(operation="add", a=5, b=5, result=result)
        self.client = Client()

    def test_math_view(self):
        response = self.client.get("/maths/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Tu będzie matma", response.content.decode())

    def test_add_view(self):
        response = self.client.get("/maths/add/3/4")
        self.assertEqual(response.status_code, 200)
        self.assertIn("operacja: +", response.content.decode())
        self.assertIn("wynik: 7", response.content.decode())

    def test_sub_view(self):
        response = self.client.get("/maths/sub/7/3")
        self.assertEqual(response.status_code, 200)
        self.assertIn("operacja: -", response.content.decode())
        self.assertIn("wynik: 4", response.content.decode())

    def test_mul_view(self):
        response = self.client.get("/maths/mul/2/3")
        self.assertEqual(response.status_code, 200)
        self.assertIn("operacja: *", response.content.decode())
        self.assertIn("wynik: 6", response.content.decode())

    def test_div_view(self):
        response = self.client.get("/maths/div/8/2")
        self.assertEqual(response.status_code, 200)
        self.assertIn("operacja: /", response.content.decode())
        self.assertIn("wynik: 4.0", response.content.decode())

    def test_div_view_zero_division(self):
        response = self.client.get("/maths/div/8/0")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Error", response.content.decode())

    def test_maths_list(self):
        response = self.client.get("/maths/histories/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["maths"]), 1)
        self.assertIn('<li><a href="/maths/histories/1">id:1, a=5, b=5, op=add</a></li>', response.content.decode())

    def test_math_details(self):
        response = self.client.get("/maths/histories/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("id:1, a=5, b=5, op=add", response.content.decode())
