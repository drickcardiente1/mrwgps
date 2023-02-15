from django.db import models
from api.models import User
from .managers import *
from django.utils.text import gettext_lazy as _

class client(User):
    class Meta :
        proxy = True
        verbose_name = _("Renters")
        verbose_name_plural = _("Renters")
    objects = ClientManager()
    def save(self , *args , **kwargs):
        self.is_client = True
        self.is_admin = False
        self.is_staff = False
        self.is_superuser = False
        return super().save(*args , **kwargs)