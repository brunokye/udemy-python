from django import forms
from django.core.exceptions import ValidationError
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "phone", "email")

    def clean(self):
        self.add_error(
            None, ValidationError("Mensagem de erro", code="invalid")
        )
        self.add_error(
            None, ValidationError("Mensagem de erro 2", code="invalid")
        )
        return super().clean()
