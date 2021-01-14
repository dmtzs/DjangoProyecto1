from django.db import models
#from ckeditor.fields import RichTextField
import ckeditor.fields as ck
from django.contrib.auth.models import User#Para lo de foreignkey debajo, es para el modelo de usuarios que viene por default por parte de django

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=100, verbose_name="Nombre")
    description= models.CharField(max_length=255, verbose_name="Descripción")
    created_at= models.DateTimeField(auto_now_add=True, verbose_name="Creado el")

    class Meta():
        verbose_name= "Categoría"
        verbose_name_plural= "Categorías"

    def __str__(self):
        return self.name

class Article(models.Model):
    title= models.CharField(max_length=150, verbose_name="Título")
    content= ck.RichTextField(verbose_name="Contenido")
    image= models.ImageField(default="null", verbose_name="Imagen")
    public= models.BooleanField(verbose_name="Publicado?")
    #**************************************************************************************Relaciones, son las cosas nuevas lo que está encerrado aquí**************************************************************************************
    user= models.ForeignKey(User, verbose_name="Usuario", on_delete= models.CASCADE)#Esto lo que guardara el ID del usuario que ha creado el artículo, la parte de models.CASCADE si borro un usuario que tiene articulos se borraran todos los mismos que creo.
    categories= models.ManyToManyField(Category, verbose_name="Categorías", null=True, blank=True)#Muchos articulos pueden tener muchas categorias en este caso por ejemplo. Los True que ahí se ponen es para indicar que no nos interesa que este o no lleno.
    #***************************************************************************************************************************************************************************************************************************************
    created_at= models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at= models.DateTimeField(auto_now=True, verbose_name="Editado el")

    class Meta():
        verbose_name= "Artículo"
        verbose_name_plural= "Artículos"

    def __str__(self):
        return self.title