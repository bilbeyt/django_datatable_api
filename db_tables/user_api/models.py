from django.db import models
import uuid


class CustomUser(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=25)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    user_code = models.UUIDField(editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " " + self.surname

