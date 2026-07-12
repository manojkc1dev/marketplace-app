from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'role') 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # 1. Map custom placeholders to each field
        placeholders = {
            'username': 'Enter your username',
            'email': 'Enter your email address',
            'password1': 'Enter a strong password',
            'password2': 'Confirm your password',
        }
        
        # 2. Loop through all fields to apply placeholders and Tailwind styles
        for field_name, field in self.fields.items():
            # Apply placeholders if they exist in our map
            if field_name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[field_name]
            
            # Apply styling to give fields high visibility, borders, and padding
            field.widget.attrs.update({
                'class': 'w-full py-4 px-5 text-lg border border-gray-300 rounded-xl focus:border-teal-500 focus:ring-2 focus:ring-teal-200 outline-none bg-gray-50/50 transition duration-200'
            })
        
        # 3. Secure and clean up the role dropdown options
        self.fields['role'].choices = [
            ('', 'Select your role'), 
            ('buyer', 'Buyer'),
            ('seller', 'Seller'),
        ]