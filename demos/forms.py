from django import forms
from demos.models import ModelPost, ModelDummyUser
from django.core.validators import MaxValueValidator, MinValueValidator


class FormPost(forms.Form):
    class Meta:
        model = ModelPost


class FormUserDummy(forms.ModelForm):
    class Meta:
        model = ModelDummyUser
        fields = ['first_name', 'last_name', 'age']


class FormUserDummyRaw(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    age = forms.IntegerField(validators=[MaxValueValidator(100), MaxValueValidator(0)])
    password = forms.CharField(widget=forms.PasswordInput)
    created_at = forms.DateField()
    created_at3 = forms.DateInput()
    created_at2 = forms.DateTimeField()
    created_at4 = forms.DateTimeInput()

    class Meta:
        model = FormUserDummy

class FormEmailSend(forms.Form):
    to_email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email(s) to send to', 'class': 'form-control'}))
    subject = forms.CharField(required=False,
                              widget=forms.TextInput(attrs={'placeholder': 'subject', 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Email body', 'class': 'form-control'}))
    from_email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))


