from django.db import models

class Sport_new(models.Model):
    sport_new_name = models.CharField(max_length=256)

    def __str__(self):
        return str(self.sport_new_name)