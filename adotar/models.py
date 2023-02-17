from django.db import models

from divulgar.models import Pet
from django.contrib.auth.models import User

# Create your models here.


class Pedido_Adocao(models.Model):
    status_choices = (

        ('AG', 'Aguardando'),
        ('Ap', 'Aprovado'),
        ('R', 'Recusado')

    )
    pet = models.ForeignKey(Pet, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data = models.DateTimeField()
    status = models.CharField(
        max_length=2, choices=status_choices, default='AG')

    class Meta:
        verbose_name_plural = "Pedidos_Adoção"

    def __str__(self):
        return self.pet.nome
