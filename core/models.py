
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


from django.contrib.auth.hashers import make_password


class BaseUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        extra_fields.setdefault('password', make_password(password))  # Hash the password
        user = self.model(email=email, **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    
    
class BaseUser(AbstractUser):

    USERNAME_FIELD = 'username'
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STUDENT = "STUDENT", "Student"
        TEACHER = "TEACHER", "Teacher"
        PARENT = "PARENT",'Parent'
        STAFF = "STAFF",'Staff'

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    objects = BaseUserManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            self.set_password(self.password)  # Hash the password before saving
        return super().save(*args, **kwargs)
    
    
class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=BaseUser.Role.STUDENT)
    
class TeacherManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=BaseUser.Role.TEACHER)
    
class ParentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=BaseUser.Role.PARENT)
    
class StaffManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=BaseUser.Role.STAFF)