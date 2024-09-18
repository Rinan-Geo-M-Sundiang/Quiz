from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



User = get_user_model()

class RegisterForm(UserCreationForm):
    is_superuser = forms.BooleanField(required=False, label="Register as superuser")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_superuser')

class SuperUserCreationForm(UserCreationForm):
    is_superuser = forms.BooleanField(required=False, label="Register as superuser")

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('is_superuser',)


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'weight', 'height', 'region', 'province', 'municipality', 'blood_type',
                  'availability']

    def clean(self):
        cleaned_data = super().clean()
        availability = cleaned_data.get("availability")
        blood_type = cleaned_data.get("blood_type")

        # Add any custom validation logic here if needed
        # For example, ensure a valid blood type is selected
        if blood_type not in ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']:
            self.add_error('blood_type', 'Invalid blood type selected')

        return cleaned_data