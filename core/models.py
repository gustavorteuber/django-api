from django.contrib.auth.models import AbstractUser
from django.db import models
from uploader.models import Image

class Usuario(AbstractUser):
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default="",
    )


class Dolar(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default="",
    )
    foto2 = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default="",
    )
    foto3 = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default="",
    )
    link = models.TextField()
    curso = models.TextField()


    def __str__(self):
        return self.titulo


class Indice(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default="",
    )
    foto2 = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default="",
    )
    foto3 = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default="",
    )
    link = models.TextField()
    curso = models.TextField()


    def __str__(self):
        return self.titulo

class acoes(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default="",
    )
    foto2 = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default="",
    )
    foto3 = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default="",
    )
    link = models.TextField()
    curso = models.TextField()

    def __str__(self):
        return self.titulo


class Contatos(models.Model):  

    link = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.youtube

class Banner(models.Model):
     foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

class saq(models.Model):
    topico = models.CharField(max_length=100, default="")
    pergunta = models.CharField(max_length=100, default="")
    texto = models.TextField()
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.pergunta
