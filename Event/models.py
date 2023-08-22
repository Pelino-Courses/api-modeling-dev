from django.db import models

# Create your models here.

class  Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=100)
    is_free = models.BooleanField(default=True)
   
    entry_fee = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0
    )
    
    def __str__(self):
        return self.title
