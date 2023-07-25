from django.db import models

# Create your models here.
class Player_category(models.Model):
    category = models.CharField(max_length=128)

    def __str__(self):
        return str(self.category)

class Player(models.Model):
    player_name = models.CharField(max_length=50)
    player_age = models.IntegerField()
    player_club = models.CharField(max_length=100)
    player_position = models.CharField(max_length=50)
    contract_per = models.DateTimeField()
    player_price = models.IntegerField()
    player_category = models.ForeignKey(Player_category, on_delete=models.CASCADE)
    added_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.player_name)