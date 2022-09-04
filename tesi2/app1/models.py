from django.db import models
from stdimage import StdImageField

# Create your models here.



class Contato(models.Model):
    def __str__(self):
        return "{}".format(self.telefone)
    telefone = models.CharField('Telefone', max_length=13)

class Cliente(models.Model):
    def __str__(self):
        return "{} {}".format(self.nome, self.sobrenome)
    contato = models.OneToOneField(Contato, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.CharField('Email', max_length=150)

class Produto(models.Model):
    def __str__(self):
        return "{}".format(self.nome)
    imagem = StdImageField('imagem', upload_to='produtos', variations={'thumb': (90,90)})
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

class Pedido(models.Model):
    def __str__(self):
        return "{}: {}".format(self.cliente.nome, self.pk)
    produto = models.ManyToManyField(Produto)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


