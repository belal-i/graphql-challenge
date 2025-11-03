from django.db import models
from django.conf import settings


class DeployedApp(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='apps'
    )
    active = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.id} ({self.owner.username})'
