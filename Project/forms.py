from django import forms

class MyForm(forms.Form):
    # Define your form fields here
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    # Add more fields as needed
