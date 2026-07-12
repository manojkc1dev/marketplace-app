# BAD: Don't do this
from .models import User 

# GOOD: Do this instead
from django.contrib.auth import get_user_model
User = get_user_model()