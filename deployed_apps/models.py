from django.db import models
from django.conf import settings
import uuid


class DeployedApp(models.Model):
    app_id = models.CharField(max_length=64, unique=True, editable=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='apps'
    )
    active = models.BooleanField(default=True)


    async def asave(self, *args, **kwargs):
        if not self.app_id:
            self.app_id = f'app_{uuid.uuid4().hex[:8]}'
        await super().asave(*args, **kwargs)


    def __str__(self):
        return f'{self.app_id} ({self.owner.username})'
