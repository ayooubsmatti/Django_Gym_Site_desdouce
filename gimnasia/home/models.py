from django.db import models


class Entrenador(models.Model):
    entrenador_nombre = models.CharField(max_length=200)
    entrenador_descripcion = models.CharField(max_length=1000)
    entrenador_url_img = models.CharField(max_length=2083)
    def __str__(self):
        return self.entrenador_nombre

class Milestone(models.Model):
    milestone_nombre=models.CharField(max_length=200)
    milestone_numero =models.IntegerField(default=0)
    def __str__(self):
        return self.milestone_nombre