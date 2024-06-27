from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Django docs highly recommend creating a custom user model.
    See https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
    """
    pass
