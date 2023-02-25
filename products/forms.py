from django import forms
from products.models import Product, Version


class ProductForm(forms.ModelForm):
    black_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):

        name = self.cleaned_data['name']
        if name in self.black_list:
            raise forms.ValidationError('Содержит запрещенное слово в названии')
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        if description in self.black_list:
            raise forms.ValidationError('Содержит запрещенное слово в описании')
        return description


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'