from django import forms

class MyForm(forms.Form):
    name = forms.CharField(
        label='Name', 
        max_length=100, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name',
            'id': 'exampleFormControlInput1'
        })
    )
    email = forms.EmailField(
        label='Email address', 
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'name@example.com',
            'id': 'exampleFormControlInput2'
        })
    )
    password = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'inputPassword6',
            'aria-describedby': 'passwordHelpInline'
        })
    )