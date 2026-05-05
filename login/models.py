from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import RegexValidator

class MyUserManager(BaseUserManager):
    def create_user(self, phone_number, first_name, last_name, password=None):

        if not phone_number:
            raise ValueError("Users must have a phone number")

        user = self.model(
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, first_name, last_name, password=None):

        user = self.create_user(
            phone_number,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    name_validator = RegexValidator(
        regex=r'^[А-ЯЁ][а-яё]+(?:-[А-ЯЁ][а-яё]+)?$',
        message='Имя должно начинаться с заглавной буквы и содержать только буквы',
        code='invalid_name'
    )
    phone_validator = RegexValidator(
        regex=r'^\+7\d{10}$',
        message='Номер телефона должен быть в формате 10 цифр после +7',
        code='invalid_phone'
    )


    phone_number = models.CharField(
        verbose_name="phone number",
        max_length=15,
        unique=True,
        validators=[phone_validator]
    )
    first_name = models.CharField(max_length=30, validators=[name_validator])
    last_name = models.CharField(max_length=30, validators=[name_validator])
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.phone_number})"

    def has_perm(self, perm, obj=None):

        return True

    def has_module_perms(self, app_label):

        return True

    @property
    def is_staff(self):
        return self.is_admin
