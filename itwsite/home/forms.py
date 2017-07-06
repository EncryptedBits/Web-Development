from django import forms


class Usr(forms.Form):
    roll_no = forms.CharField(max_length=10)
    #user_email = forms.EmailField()
    user_password = forms.CharField(widget = forms.PasswordInput())
    #user_password2 = forms.CharField(widget = forms.PasswordInput())
