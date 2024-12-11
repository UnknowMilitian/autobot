from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(
        self, username, email=None, phone_number=None, password=None, **extra_fields
    ):
        if not username:
            raise ValueError("The Username must be set")
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            phone_number=phone_number,
            password=password,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
