from django import forms
from .models import todo

class MyForm(forms.ModelForm):
    class Meta:
        model = todo  
        fields = ['name', 'email', 'password'] 
        widgets = {  
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
                'id': 'exampleFormControlInput1'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'name@example.com',
                'id': 'exampleFormControlInput2'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'id': 'inputPassword6',
                'aria-describedby': 'passwordHelpInline'
            }),
        }