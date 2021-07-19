from django.contrib import admin
from django import forms
from .models import *
from django.utils.safestring import mark_safe


class SmartphoneAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if not instance.sd:
            self.fields['sd_volume_max'].widget.attrs.update({
                'readonly': True,
                'style': 'background: lightgray;'
            })

    def clean(self):
        if not self.cleaned_data['sd']:
            self.cleaned_data['sd_volume_max'] = None

        return self.cleaned_data


class LaptopAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return forms.ModelChoiceField(Category.objects.filter(slug='laptops'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartphoneAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'
    form = SmartphoneAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return forms.ModelChoiceField(Category.objects.filter(slug='smartphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Customer)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Order)
admin.site.register(Comment)
