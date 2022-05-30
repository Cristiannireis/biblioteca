from django.db import models

# Create your models here.
class Books(models.Model):
    id_book = models.CharField(max_length=10)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo