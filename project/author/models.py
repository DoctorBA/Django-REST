from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True) 
    date_of_death = models.DateField(blank=True, null=True)  
    #photo = models.ImageField(upload_to="authors/", blank=True, default="photo-placeholder.png")

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])