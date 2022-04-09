from django import forms


class CustomDateInput(forms.DateInput):
    def __init__(self, *args, **kwargs):
        kwargs.update({'attrs': {'type': 'date'}})
        super(CustomDateInput, self).__init__(*args, **kwargs)


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField(widget=forms.Textarea())
    phone_number = forms.IntegerField()
    contact_at = forms.DateField(widget=CustomDateInput())
