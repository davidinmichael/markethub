from django.db import models
from django.utils.translation import gettext_lazy as _

class Gender(models.TextChoices):
    FEMALE = "female", _("Female")
    MALE = "male", _("Male")
    OTHER = "other", _("Other")
