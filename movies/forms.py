from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

from movies.models import Movie, Actor, Director, Profile


class DatePickerDateInput(forms.DateInput):
    def __init__(self, *args, **kwargs):
        kwargs.update({'attrs': {'type': 'date'}})
        super(DatePickerDateInput, self).__init__(*args, **kwargs)


class DateFieldSevenDaysFromNow(forms.DateField):
    widget = DatePickerDateInput

    def validate(self, value):
        super(DateFieldSevenDaysFromNow, self).validate(value)
        if value < timezone.now().date() + timedelta(days=7):
            raise ValidationError('Cannot create contact at earlier that 7 days from now')


def contact_name_is_not_david(value):
    if 'david' in value.lower():
        raise ValidationError('David cannot create contact')


class ContactForm(forms.Form):
    name = forms.CharField(validators=[contact_name_is_not_david, ])
    email = forms.EmailField()
    subject = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    phone_number = forms.IntegerField()
    age = forms.IntegerField(min_value=1, max_value=99)
    contact_at = DateFieldSevenDaysFromNow()
    subscribe = forms.BooleanField()

    def clean_name(self):
        return self.data.get('name').lower()


class MovieForm(forms.ModelForm):
    released = forms.DateField(widget=DatePickerDateInput())

    class Meta:
        model = Movie
        fields = '__all__'
        exclude = ['likes', ]


class ActorForm(forms.ModelForm):
    born_at = forms.DateField(widget=DatePickerDateInput())
    movies = forms.ModelMultipleChoiceField(queryset=Movie.objects.all())

    class Meta:
        model = Actor
        fields = '__all__'

    def save(self, commit=True):
        actor = super(ActorForm, self).save(commit=commit)
        actor.movies.add(*self.cleaned_data.get('movies'))
        return actor


class DirectorForm(forms.ModelForm):
    born_at = forms.DateField(widget=DatePickerDateInput())

    class Meta:
        model = Director
        fields = '__all__'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user', )

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(ProfileForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.user = self.request.user
        return super(ProfileForm, self).save(commit=commit)


class SearchForm(forms.Form):
    query = forms.CharField()

