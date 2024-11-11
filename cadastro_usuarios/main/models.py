from django.db import models

# Create your models here.
class Config(models.Model):
    Nome = models.CharField('Nome Integração', max_length=100)
    url = models.CharField('URL', max_length=300)
    typeauth = models.CharField('Type Auth', max_length=100)

    def __str__(self):
        return self.Nome

def retentidades():
    return [ ('1','Produto'), ('2','Estoque'), ('3','Preco'), ('4','Status')]

def tipocpo():
    return [ ('1','Caracter'), ('2','Numerico'), ('3','Logico'), ('4','Objeto')]

class LayoutJson(models.Model):
    Filial = models.CharField('Filial', max_length=4)
    Codigo = models.IntegerField(editable=False, unique=True)
    Entidade = models.CharField('Entidade', max_length=20, choices=retentidades)
    Campo_API = models.CharField('Campo API', max_length=50)
    Tipo_Cpo = models.CharField('Tipo Campo', max_length=10, choices=tipocpo)
    #Cpo_Objeto 

    def __str__(self):
        return self.Entidade