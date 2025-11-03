from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    PLAN_CHOICES = [
        ('HOBBY', 'Hobby'),
        ('PRO', 'Pro'),
    ]
    plan = models.CharField(
        max_length=5,
        choices=PLAN_CHOICES,
        default='HOBBY'
    )


    def __str__(self):
        return f'{self.username} ({self.plan})'
