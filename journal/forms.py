from django import forms


class ContactUsForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'First name',
    }))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'Last name',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'www.example.com',
    }))
    message = forms.CharField(required=True, widget=forms.Textarea)

