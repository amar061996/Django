from django import forms

from .models import SignUp



class ContactForm(forms.Form):

    fullname=forms.CharField()
    email=forms.EmailField()
    message=forms.CharField()

class SignUpForm(forms.ModelForm):

    class Meta:
        model=SignUp
        fields=["fullname","email"]



    def clean_email(self):

        email=self.cleaned_data.get("email")
        email_base,provider=email.split("@")
        domain,extension=provider.split('.')
        if not "com" in extension:
            raise forms.ValidationError("Error in the email")
        return email


    def clean_fullname(self):

        full_name=self.cleaned_data.get("fullname")
        print full_name
        return full_name