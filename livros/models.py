from django.db import models

# criar dados
class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    descrição = models.TextField(max_length=300)

    def __str__(self):
        return self.titulo



