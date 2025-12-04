from django.db import models

# Create your models here.
import uuid
from django.db import models
from accounts.models import Customuser


class Customer(models.Model):
    customer_id = models.CharField(
        max_length=36,
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        
    )

    custom_user = models.ForeignKey(
        Customuser,
        on_delete=models.CASCADE,
        related_name="customer_profiles",
        db_column='custom_user_id'
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "customer"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
