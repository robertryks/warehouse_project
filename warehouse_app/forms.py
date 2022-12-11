from django import forms

from warehouse_app.models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ("tax_id", "name", "users")
        labels = {
            "tax_id": "NIP:",
            "name": "Nazwa:",
            "users": "Użytkownicy:",
        }


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


