from django import forms
from django.core.exceptions import ValidationError
from .models import Product, Tag


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'slug', 'description', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

        def clean_slug(self):
            new_slug = self.cleaned_data['slug'].lower()

            if new_slug == 'create':
                raise ValidationError('слаг не может быть create')
            return new_slug


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('слаг не может быть create')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('слаг \'{}\' уже есть'.format(new_slug))
        return new_slug
