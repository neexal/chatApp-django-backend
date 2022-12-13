from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    

# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# class UserManager(BaseUserManager):
#   def create_user(self, username, password=None):
#     if not username:
#       raise ValueError('Users must have a username')
#     user = self.model(username=username)
#     user.set_password(password)
#     user.save(using=self._db)
#     return user

#   def create_superuser(self, username, password):
#     user = self.create_user(username, password)
#     user.is_admin = True
#     user.save(using=self._db)
#     return user

# class User(AbstractBaseUser):
#   username = models.CharField(max_length=255, unique=True)
#   is_active = models.BooleanField(default=True)
#   is_admin = models.BooleanField(default=False)

#   objects = UserManager()

#   USERNAME_FIELD = 'username'

#   def __str__(self):
#     return self.username

#   def has_perm(self, perm, obj=None):
#     return True

#   def has_module_perms(self, app_label):
#     return True
