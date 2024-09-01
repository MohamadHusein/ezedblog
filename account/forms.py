from django import forms
from django.contrib.auth import authenticate
from django.forms import ValidationError




class LoginForm(forms.Form):
    username = forms.CharField(max_length=50 , widget=forms.TextInput(attrs={'class':'input100' , 'placeholder':'Enter your Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100' , 'placeholder':'Enter your Password'}))





    def clean_password(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is not None:
            return self.cleaned_data.get('password')
        raise ValidationError('Incorrect Username or Password' , code='invalid_info')
