from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    phone_number = forms.IntegerField()
    contact_at = forms.DateField()
