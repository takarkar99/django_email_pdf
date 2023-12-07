from django import forms
from django.contrib.auth.forms import UserCreationForm
from CustomUser.models import CustomUser  # Import your CustomUser model

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'password1', 'password2')  # Include the necessary fields for user creation

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already in use.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
