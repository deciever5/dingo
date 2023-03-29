from ..forms import ResultForm
from django.test import TestCase
from ..models import Result


class ResultFormTest(TestCase):

    def test_result_save_correct_data(self):
        data = {"value": 200}
        self.assertEqual(Result.objects.count(), 0)
        form = ResultForm(data=data)
        self.assertTrue(form.is_valid())
        r = form.save()
        self.assertIsInstance(r, Result)
        self.assertEqual(r.value, 200)
        self.assertIsNotNone(r.id)
        self.assertIsNone(r.error)


class Test_Value_And_Error_Validation(TestCase):

    def test_value_and_error_validation(self):
        # Both value and error are provided
        form_data = {'value': 5, 'error': 'Some error'}
        form = ResultForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("Podaj tylko jedną z wartości", form.errors['__all__'])

        # Neither value nor error is provided
        form_data = {'value': None, 'error': ''}
        form = ResultForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("Nie podano żadnej wartości!", form.errors['__all__'])

        # Only value is provided
        form_data = {'value': 5, 'error': ''}
        form = ResultForm(data=form_data)
        self.assertTrue(form.is_valid())

        # Only error is provided
        form_data = {'value': None, 'error': 'Some error'}
        form = ResultForm(data=form_data)
        self.assertTrue(form.is_valid())
