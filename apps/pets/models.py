from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from apps.users.models import User
import uuid

# Create your models here.


class Pet(models.Model):
    name = models.CharField(max_length=45)
    type_pet = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    size = models.CharField(max_length=45)
    description = models.TextField()
    image_pet = models.ImageField(upload_to='static/images/pets', height_field=None,
                                  width_field=None, max_length=None, default='static/images/pet_null.jpg')
    rescuer = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=45)
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          primary_key=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pets'
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'
