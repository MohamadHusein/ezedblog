from django import forms
from django.core.validators import ValidationError
from .models import Massage




class ContactUsForm(forms.Form):
    BIRTH_YEAR_CHOICES = ['2000' , '2001' , '2002' , '2003' , '2004' , '2005' , '2006' , '2007' , '2008']
    FAVORITE_COLOR_CHOICES = [

        ('red', 'Red'),
        ('black', 'Black'),
        ('white', 'White'),

    ]



    name = forms.CharField(max_length=10 , label='your name' , required=False)
    text = forms.CharField(max_length=10 , label='your message')
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES , attrs={'class':'form-control'}))
    colors = forms.ChoiceField(choices=FAVORITE_COLOR_CHOICES , widget=forms.RadioSelect())


    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if name == text:
            raise ValidationError('name and text are same' , code='name_text_same')








class MassageForm(forms.ModelForm):
    class Meta:
        model = Massage
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'enter your title' , 'style':'max-width:300px'}),
            'text': forms.Textarea(attrs={'class':'form-control' , 'placeholder':'enter your message'}),
            'email': forms.EmailInput(attrs={'class':'form-control' , 'placeholder':'enter your email'}),
            'age': forms.NumberInput(attrs={'class':'form-control'}),
        }















