from django import forms
from demos.models import ModelPost, ModelDummyUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import MinValueValidator, MaxValueValidator

class FormPost(forms.ModelForm):
    class Meta:
        model = ModelPost
        fields = ['title', 'body']


class FormPostAdmin(forms.ModelForm):
    class Meta:
        model = ModelPost
        fields = '__all__'


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



class FormDummy(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your name', 'class': 'form-control'}),
                           label="Your Name", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    gender = forms.ChoiceField(choices=((1, 'Male'), (2, 'Female')), required=True)
    curriculum_vitae = forms.CharField(widget=forms.Textarea(), label="CV")
    age = forms.IntegerField(validators=[MinValueValidator(5), MaxValueValidator(100)])
    agree = forms.BooleanField(required=False, label="Checking this box means you agree with the license terms")
