from django.contrib.auth.models import UserManager

class CustomUserManager(UserManager):
    def create_user(self, phone_number = None, password = None, **extra_fields):
        if not phone_number:
            raise ValueError("User must have a phone number.")
        user = self.model(phone_number = phone_number, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, phone_number = None, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        return self.create_user(phone_number, password)