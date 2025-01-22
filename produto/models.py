from django.db import models

# Create your models here.
class Categoria(models.Model):
    titulo = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.titulo

class Produto(models.Model):
    titulo = models.CharField(max_length=30, unique=True)
    preco_compra = models.DecimalField(max_digits=8, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade = models.DecimalField(max_digits=9, decimal_places=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(upload_to="imagens")

    def __str__(self) -> str:
        return self.titulo

    