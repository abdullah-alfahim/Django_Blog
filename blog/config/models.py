from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog')
    heading = models.CharField(max_length=50)
    keywords = models.CharField(max_length=50)
    image = models.ImageField( blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.username + " | " + self.heading 