from django import forms
from .models import Result


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ["value", "error"]

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data["error"] == "":
            cleaned_data["error"] = None

        value = cleaned_data.get("value")
        error = cleaned_data.get("error")

        if value and error:
            raise forms.ValidationError("Podaj tylko jedną z wartości")
        elif not value and not error:
            raise forms.ValidationError("Nie podano żadnej wartości!")

        return cleaned_data
