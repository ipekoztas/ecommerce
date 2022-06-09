from django import forms
from .models import Product, Comment


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'size', 'brand', 'dis', 'price', 'description']

        CHOICES = (('Option 1', 'XS'), ('Option 2', 'S'), ('Option 3', 'M'), ('Option 4', 'L'), ('Option 5', 'XL'),)

        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.Select(choices=CHOICES),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'dis': forms.CheckboxInput(attrs={'class': 'form-control'}),
            #'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Enter Product Name:',
            'image': 'Select an Image: ',
            'size': 'Enter Size: ',
            'brand': 'Enter Brand: ',
            'dis': 'Check if Product has Discount: ',
            'price': 'Enter a price: ',
            'description': 'Enter a Description: ',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body',)
        widgets = {
            'comment_body': forms.Textarea(attrs={'class': 'form-control'}),
        }