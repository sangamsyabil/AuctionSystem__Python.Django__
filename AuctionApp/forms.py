from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, Bidder, Seller


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'user_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

#
# class AddProductForm(forms.ModelForm):
#     bid_end_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}))
#
#     class Meta:
#         model = Product
#         fields = ('product_name', 'image', 'category', 'description', 'selling_price', 'bid_end_date')
#
