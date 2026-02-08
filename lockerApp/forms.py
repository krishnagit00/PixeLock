from django import forms
from .models import LockerUser

# Matches Image 2 (Step 1: Email input)
class LockerLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'you@example.com'}))
    # Note: The "6-Digit Code" input in Image 2 seems to be for creating a *new* locker,
    # while the text says "unlock an existing one using your email and a 6-digit code".
    # This is slightly ambiguous. I will implement the standard flow: Email -> Send Code -> Verify Code.
    # The form in Image 2 looks like it combines registration and login request. Let's assume for now
    # we just ask for email first to send the code.

# Matches Image 2's style for verification (Step 2)
class LockerVerifyForm(forms.Form):
    email = forms.EmailField(widget=forms.HiddenInput())
    code = forms.CharField(min_length=6, max_length=6, widget=forms.TextInput(attrs={'placeholder': 'e.g. 123456'}))
    save_device = forms.BooleanField(required=False)
