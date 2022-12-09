from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        labels = {
            "username": "Nazwa użytkownika"
        }


# class CompanyForm(forms.ModelForm):
#     class Meta:
#         model = Company
#         fields = ("tax_id", "name", "users")
#         labels = {
#             "tax_id": "NIP:",
#             "name": "Nazwa:",
#             "users": "Użytkownicy:",
#         }
#
#
# class DimensionForm(forms.ModelForm):
#     class Meta:
#         model = Dimension
#         fields = ("size",)
#         labels = {
#             "size": "Średnica w mm"
#         }
#         widgets = {
#             "size": forms.TextInput(
#                 attrs={"placeholder": "0.00"}
#             )
#         }


