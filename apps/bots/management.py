from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):

    def create_user(self, username, phone_number=None, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username must be set")
        if not phone_number:
            raise ValueError(
                "The phone_number must be set"
            )  # Enforce phone_number presence

        user = self.model(username=username, phone_number=phone_number, **extra_fields)

        # Hash the password if provided
        if password:
            user.set_password(password)
        else:
            user.set_password(self.make_random_password())

        user.save(using=self._db)
        return user

    def create_superuser(
        self, username, password=None, phone_number=None, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        # Provide a default phone_number if none is provided
        if phone_number is None:
            phone_number = "+0000000000"  # Use a placeholder or dummy value

        return self.create_user(
            username=username,
            password=password,
            phone_number=phone_number,
            **extra_fields
        )
