from django.contrib import admin

# Register your models here.
from .models import Dimension, Grade, Heat, Certificate, Supply, SupplyItem, Issue, IssueItem, Company


class SupplyItemInlineSupply(admin.TabularInline):
    model = SupplyItem


class SupplyAdmin(admin.ModelAdmin):
    inlines = [SupplyItemInlineSupply]


class IssueItemInlineSupply(admin.TabularInline):
    model = IssueItem


class IssueAdmin(admin.ModelAdmin):
    inlines = [IssueItemInlineSupply]


admin.site.register(Company)
admin.site.register(Dimension)
admin.site.register(Grade)
admin.site.register(Heat)
admin.site.register(Certificate)
admin.site.register(Supply, SupplyAdmin)
admin.site.register(Issue, IssueAdmin)

