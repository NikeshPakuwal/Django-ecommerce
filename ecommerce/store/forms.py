from django import forms
from django.forms import ModelForm
from .models import Category, SubCategory, Product

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#admin panel features
class AuthUser(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(AuthUser, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    

#registration process
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ecommerceCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ecommerceCategory, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ecommerceSubCategory(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['title', 'slug', 'category']
        
    
    def __init__(self, *args, **kwargs):
        super(ecommerceSubCategory, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select"
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    

class ecommerceProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(ecommerceProduct, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select"
        self.fields['subcategory'].empty_label = "Select"
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
