from django.db import models

class Game_Category(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='categories')
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='games')
    