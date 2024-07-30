from django import forms
from .models import Todo


class MyForm(forms.ModelForm):
    class Meta:
        model = Todo  
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
        }

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'priority', 'complete']
        widgets = {
            'title': forms.TextInput (attrs={
                'class': 'form-control',
                'placeholder': 'enter todo item',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'enter description of todo item'  
            }),
            'priority': forms.Select(attrs={
                'class': 'form-control', 
            }),
            'complete': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'password'  
            })
        }

