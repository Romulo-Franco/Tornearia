from django.db import models

# Create your models here.
class Servico(models.Model):
    titulo = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
