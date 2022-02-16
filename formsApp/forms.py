from django import forms
from django.core import validators


class UserRegistrationForm(forms.Form):
    GENDER = [('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')]
    firstName = forms.CharField(widget=forms.TextInput, validators=[validators.MaxLengthValidator(20)])
    lastName = forms.CharField(widget=forms.TextInput, validators=[validators.MaxLengthValidator(20)])
    email = forms.EmailField(widget=forms.EmailInput, validators=[validators.MaxLengthValidator(50)])
    gender = forms.CharField(widget=forms.Select(choices=GENDER))
    password = forms.CharField(widget=forms.PasswordInput,
                               validators=[validators.MinLengthValidator(8),
                                           validators.MaxLengthValidator(16)])
    ssn = forms.IntegerField()

    """
    # Custom Single Validation at a time
    def clean(self):
        user_cleaned_data = super().clean()

        input_firstname = self.cleaned_data['firstName']
        if len(input_firstname) > 20:
            raise forms.ValidationError("The max length of first name is 20 characters")

        input_lastname = self.cleaned_data['lastName']
        if len(input_lastname) > 20:
            raise forms.ValidationError("The max length of last name is 20 characters")

        input_email = self.cleaned_data['email']
        if input_email.find("@") == -1:
            raise forms.ValidationError("The email should contain '@'")

    # Custom validation for each input
    def clean_firstName(self):
        input_firstname = self.cleaned_data['firstName']
        if len(input_firstname) > 20:
            raise forms.ValidationError("The max length of first name is 20 characters")
        return input_firstname

    def clean_email(self):
        input_email = self.cleaned_data['email']
        if input_email.find("@") == -1:
            raise forms.ValidationError("The email should contain '@'")
        return input_email
    """
