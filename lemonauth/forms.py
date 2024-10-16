from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


class SignupForm(forms.ModelForm):
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model= CustomUser
        fields =("first_name" , "last_name" , "user_name" , "email")
        widgets= {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

            
    def clean(self):
        cleaned_data = super().clean()
        password1= self.cleaned_data.get('password1')
        password2= self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('passwords not matchingg')
        if password1 :
            if len (password1) <8 :
                raise forms.ValidationError("password must be 8 char. long")
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
           user.save()
        return user


class LoginForm(AuthenticationForm):
    username= forms.CharField(label="Email" ,widget= forms.TextInput(attrs=({'class':'form-control','placeholder': 'email'})))
    password = forms.CharField (widget = forms.PasswordInput(attrs={'class': 'form-control' , 'placeholder': 'password'
    }))

