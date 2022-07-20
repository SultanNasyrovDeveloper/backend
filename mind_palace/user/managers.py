from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email: str, password: str):

        if not email:
            raise ValueError('Users must have email')

        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email: str, password: str):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )
        user.set_password(password)
        user.save()
        return user
