
from django.test import TestCase, Client
from ..models import Math, Result
import re

class MathViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        result = Result.objects.create(value=10)
        Math.objects.create(operation="add", a=5, b=5, result=result)
        cls.client = Client()

    def test_math_view(self):
        response = self.client.get("/maths/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Tu będzie matma", response.content.decode())

    def test_add_view(self):
        response = self.client.get("/maths/add/3/4")
        content = response.content.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn("+", content)
        self.assertIn("7", content)

        # Sprawdź, czy obiekt Result został utworzony
        result = Result.objects.filter(value=7).first()
        self.assertIsNotNone(result)

        # Sprawdź, czy obiekt Math został utworzony
        math = Math.objects.filter(operation='add', a=3, b=4, result=result).first()
        self.assertIsNotNone(math)

    def test_sub_view(self):
        response = self.client.get("/maths/sub/6/3")
        content = response.content.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn("-", content)
        self.assertIn("3", content)

        # Sprawdź, czy obiekt Result został utworzony
        result = Result.objects.filter(value=3).first()
        self.assertIsNotNone(result)

        # Sprawdź, czy obiekt Math został utworzony
        math = Math.objects.filter(operation='sub', a=6, b=3, result=result).first()
        self.assertIsNotNone(math)

    def test_mul_view(self):
        response = self.client.get("/maths/mul/2/3")
        content = response.content.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn('*', response.content.decode())
        self.assertIn('Wynik', content)
        self.assertIn('6', content)

        # Sprawdź, czy obiekt Result został utworzony
        result = Result.objects.filter(value=6).first()
        self.assertIsNotNone(result)

        # Sprawdź, czy obiekt Math został utworzony
        math = Math.objects.filter(operation='mul', a=2, b=3, result=result).first()
        self.assertIsNotNone(math)

    def test_div_view(self):
        response = self.client.get("/maths/div/8/2")
        content = response.content.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn("/", content)
        self.assertIn("4.0", content)

        # Sprawdź, czy obiekt Result został utworzony
        result = Result.objects.filter(value=4.0).first()
        self.assertIsNotNone(result)

        # Sprawdź, czy obiekt Math został utworzony
        math = Math.objects.filter(operation='div', a=8, b=2, result=result).first()
        self.assertIsNotNone(math)

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
        content = response.content.decode()
        patterns = [r'1', r'5', r'5', r'add']
        matches = [re.search(pattern, content) for pattern in patterns]
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(all(matches))


class MathViewsPaginationTest(TestCase):
    fixtures = ['math_fixture']

    def setUp(self):
        self.client = Client()

    def test_get_first_5(self):
        response = self.client.get("/maths/histories/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["maths"]), 5)

    def test_get_last_page(self):
        response = self.client.get("/maths/histories/?page=3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["maths"]), 4)
