from django import forms
from .models import ContactForm, Review

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='Correo electrónico')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje')

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

      