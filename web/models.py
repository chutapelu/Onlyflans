from django.db import models
import uuid
from django.contrib.auth.models import User

class Flan(models.Model):
    flan_uuid=models.UUIDField()
    name= models.CharField(max_length=64)
    description=models.TextField(default='')
    image_url=models.URLField(default='')
    slug=models.SlugField(default='')
    is_private=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField(default='')

    def __str__(self):
        return self.customer_name
    
class Review(models.Model):
    flan = models.ForeignKey(Flan, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Calificación de 1 a 5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.rating} - {self.flan.name}'