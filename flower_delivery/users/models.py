# users/models.py
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass  # Настройка дополнительных полей для пользователя при необходимости
