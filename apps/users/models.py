from django.db import models
from django.db.models.fields import CharField, EmailField
from django.db.models.fields.files import ImageField
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=CASCADE)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.EmailField(max_length=45)
    image_user = models.ImageField(upload_to='static/images/users', height_field=None,
                                   width_field=None, max_length=None, blank=True, null=True, default='static/images/user_null.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
