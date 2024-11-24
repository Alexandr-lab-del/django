from django import forms
from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    prohibited_words = [
        'казино', 'криптовалюта', 'крипта', 'биржа',
        'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'placeholder': f'Введите {field_name}'})

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        self.check_prohibited_words(name)
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        self.check_prohibited_words(description)
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price

    def check_prohibited_words(self, text):
        text_lower = text.lower()
        for word in self.prohibited_words:
            if word in text_lower:
                raise forms.ValidationError(f"Запрещено использование слова: {word}")
