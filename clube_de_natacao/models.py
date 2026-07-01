from django.db import models

# Create your models here.

class Treinador (models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Nadador (models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class EstiloDeTreino (models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class Treino (models.Model):
    nome = models.CharField(max_length=50)
    hora = models.TimeField()
    treinador = models.ForeignKey(Treinador, on_delete=models.CASCADE, related_name="treinos")
    estilo = models.ManyToManyField(EstiloDeTreino, related_name="treinos")
    nadadores = models.ManyToManyField(Nadador, related_name="treinos")

    def __str__(self):
        return f'{self.nome}-{self.hora}'