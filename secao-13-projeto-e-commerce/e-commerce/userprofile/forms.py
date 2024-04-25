from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"
        exclude = ("user",)


class UserForm(forms.ModelForm):
    password = forms.CharField(
        required=False, widget=forms.PasswordInput(), label="Senha"
    )

    password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label="Confirmação da senha",
    )

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "password2",
        )

    def clean(self, *args, **kwargs):
        cleaned = self.cleaned_data
        validation_error_msg = {}

        user_data = cleaned.get("username")
        password_data = cleaned.get("password")
        password2_data = cleaned.get("password2")
        email_data = cleaned.get("email")

        user_db = User.objects.filter(username=user_data).first()
        email_db = User.objects.filter(email=email_data).first()

        error_msg_user_exists = "Usuário já existe."
        error_msg_email_exists = "E-mail já existe."
        error_msg_password_match = "Senhas não conferem."
        error_msg_password_short = (
            "Sua senha precisa de pelo menos 6 caracteres."
        )

        if self.user:
            if user_db:
                if user_data != user_db.username:
                    validation_error_msg["username"] = error_msg_user_exists

            if email_data != email_db.email:  # type: ignore
                if email_db:
                    validation_error_msg["email"] = error_msg_email_exists

            if password_data:
                if password_data != password2_data:
                    validation_error_msg["password"] = error_msg_password_match
                    validation_error_msg["password2"] = (
                        error_msg_password_match
                    )
                if len(password_data) < 6:
                    validation_error_msg["password"] = error_msg_password_short
        else:
            pass

        if validation_error_msg:
            raise forms.ValidationError(validation_error_msg)
