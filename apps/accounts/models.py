from django.db import models

# Create your models here.
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone



class Customuser(AbstractUser):
    custom_user_id = models.CharField(
        max_length=36,
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        
    )

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    last_login = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    # Your requested field
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "phone_number"]

    

    class Meta:
        db_table = "customuser"

    def __str__(self):
        return self.username
