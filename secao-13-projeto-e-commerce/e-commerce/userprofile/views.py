# from django.shortcuts import render
from . import forms
from django.views import View
from django.shortcuts import render


class BaseProfile(View):
    template_name = "userprofile/create.html"

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        if self.request.user.is_authenticated:
            self.context = {
                "userform": forms.UserForm(
                    data=self.request.POST or None,
                    user=self.request.user,
                    instance=self.request.user,
                ),
                "profileform": forms.ProfileForm(
                    data=self.request.POST or None
                ),
            }
            self.render = render(
                self.request, self.template_name, self.context
            )
        else:
            self.context = {
                "userform": forms.UserForm(data=self.request.POST or None),
                "profileform": forms.ProfileForm(
                    data=self.request.POST or None
                ),
            }
            self.render = render(
                self.request, self.template_name, self.context
            )

    def get(self, *args, **kwargs):
        return self.render


class Create(BaseProfile):
    def post(self, *args, **kwargs):
        userform = self.context["userform"]
        profileform = self.context["profileform"]

        if not userform.is_valid() or not profileform.is_valid():
            return self.render

        user = userform.save(commit=False)
        user.set_password(userform.cleaned_data["password"])
        user.save()

        profile = profileform.save(commit=False)
        profile.user = user
        profile.save()

        return render(self.request, "userprofile/create.html")


class Update(View):
    pass


class Login(View):
    pass


class Logout(View):
    pass
