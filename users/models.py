from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    user_id = models.CharField(max_length=64, unique=True, editable=False)
    PLAN_CHOICES = [
        ('HOBBY', 'Hobby'),
        ('PRO', 'Pro'),
    ]
    plan = models.CharField(max_length=5, choices=PLAN_CHOICES, default='HOBBY')


    def save(self, *args, **kwargs):
        if not self.user_id:
            # Use u_<8_hex_chars> for user_id
            self.user_id = f'u_{uuid.uuid4().hex[:8]}'
        super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.username} ({self.plan})'
