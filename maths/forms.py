from django import forms
from .models import Result

class ResultForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        value = cleaned_data.get('value')
        error = cleaned_data.get('error')

        if all([value, error]):
            raise forms.ValidationError("Podaj tylko jedną z wartości")
        elif not any([value, error]):
            raise forms.ValidationError("Nie podano żadnej wartości!")

    class Meta:
        model = Result
        fields = ["value", "error"]

