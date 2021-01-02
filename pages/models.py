from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title= models.CharField(max_length=50, verbose_name="Título")
    content= RichTextField(verbose_name="Contenido")
    slug= models.CharField(unique=True, max_length=150, verbose_name="URL amigable")#El unique es para que ese campo sea único.
    order= models.IntegerField(default=0, verbose_name="Orden")#Literal solo va a tener un número entero por el tipo de campo.
    visible= models.BooleanField(verbose_name="Visible?")
    create_at= models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at= models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    class Meta():
        verbose_name= "Página"
        verbose_name_plural= "Páginas"

    def __str__(self):
        return self.title#Imprimir el título de cada una de las páginas del panel de administración