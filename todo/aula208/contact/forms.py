from django import forms
from django.core.exceptions import ValidationError
from .models import Contact


class ContactForm(forms.ModelForm):
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "classe-a classe-b",
    #             "placeholder": "Digite seu nome",
    #         }
    #     ),
    #     label="Nome",
    #     help_text="Digite seu nome",
    # )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields["first_name"].widget.attrs.update(
        #     {
        #         "class": "classe-a classe-b",
        #         "placeholder": "Digite seu nome",
        #     }
        # )

    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "phone")
        # widgets = {
        #     "first_name": forms.TextInput(
        #         attrs={
        #             "class": "classe-a classe-b",
        #             "placeholder": "Digite seu nome",
        #         }
        #     )
        # }

    def clean(self):
        self.add_error(
            None, ValidationError("Mensagem de erro", code="invalid")
        )
        self.add_error(
            None, ValidationError("Mensagem de erro 2", code="invalid")
        )
        return super().clean()
