from django import forms
from core.models import User

class RegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['email','name','password','confirm_password']


        def clean(self):
            cleaned_date=super().clean()
            password=cleaned_date.get('password')
            confirm_password=cleaned_date.get('confirm_password')

            if password != confirm_password:
                self.add_error('confirm_password','Password and confirm password do not match.')
            return cleaned_date
        
        def clean_email(self):
            email=self.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('A user with this email already exists.')
            return email
        

class PasswordResetForm(forms.Form):
    email=forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={'placeholder':'you@example.com'})

    )

    def clean_email(self):
        email=self.cleaned_data.get('email')

        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                ('No account is associated with this email address.')
            )
        return email