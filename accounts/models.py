from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ("superadmin", "Super Admin"),
        ("admin", "Admin"),
        ("seller", "Seller"),
        ("buyer", "Buyer"),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
    )
    
    # Extra fields for the marketplace
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    # Clean helper properties for role checking
    @property
    def is_superadmin(self):
        return self.role == "superadmin"

    @property
    def is_admin(self):
        return self.role == "admin"

    @property
    def is_seller(self):
        return self.role == "seller"

    @property
    def is_buyer(self):
        return self.role == "buyer"