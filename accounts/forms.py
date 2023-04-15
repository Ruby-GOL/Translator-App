from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import (UserCreationForm, 
                                        UserChangeForm,
                                        AuthenticationForm,
                                        PasswordResetForm,
                                        SetPasswordForm)
 
User = get_user_model()


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required':'', 
            'name': 'username',
            'id':'username',
            'type':'text', 
            'class':'form-input' ,
            'placeholder':'John Doe', 
            'maxlength':'16',
            'minlength':'4'   
        })
        self.fields['email'].widget.attrs.update({
            'required':'', 'name':"email", 'id':"email", 'type':"email" ,'class':"form-input", 'placeholder':"johndoe@mail.com"
        })
        self.fields['password1'].widget.attrs.update({
            'required':'', 'name':"password1" ,'id':"password1" ,'type':"password", 'class':"form-input",'placeholder':"password" ,'maxlength':"22" ,'minlength':"8"
        })
        self.fields['password2'].widget.attrs.update({
            'required':'', 'name':"password2" ,'id':"password2" ,'type':"password", 'class':"form-input",'placeholder':"password" ,'maxlength':"22" ,'minlength':"8"
        })
    
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('email','username', 'password1', 'password2',)  
        
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user  
        
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-input",
        "type": "text",
        "placeholder": "username"
    }))

    password = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-input",
        "type": "password",
        "placeholder": "password"
    }))


class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-input",
        "type": "email",
        "placeholder": "email"
    }))


class NewPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(NewPasswordForm, self).__init__(*args, **kwargs)

    
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "form-input",
            "type": "password",
            'autocomplete': 'new-password'
    }))

    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': "form-input",
            "type": "password",
            'autocomplete': 'new-password'
    }))

 
class UserChangeForm(UserChangeForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('email',)

class PatientRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'name', 'password']

class DoctorRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'name', 'password']