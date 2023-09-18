from django.db import models

# Create your models here.

class Speaker(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150)
    biography = models.TextField()
    photo = models.URLField(null=True, blank=True)
    email = models.EmailField()
    phone_number = models.IntegerField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name