from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
import datetime


class Categoriacarrera (models.Model):
    nombre = models.CharField(null= False, blank= True, max_length=100)

    def __str__(self):
        return self.nombre


class Categoriaedu (models.Model):
    nombre = models.CharField(null= False, blank= True, max_length=100)

    def __str__(self):
        return self.nombre

class Categoriafcyt (models.Model):
    nombre = models.CharField(null= False, blank= True, max_length=100)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    foto = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    categoriacarrera = models.ForeignKey('Categoriacarrera', on_delete=models.CASCADE,null=True)
    categoriaedu = models.ForeignKey ('Categoriaedu', on_delete=models.CASCADE, null=True)
    categoriafcyt = models.ForeignKey('Categoriafcyt', on_delete=models.CASCADE, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    slug= models.SlugField(null=False, default="#")

    def get_absolute_url(self):
        return reverse('single_blog', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class  Newsletter_email(models.Model):
    email = models.URLField(null=True, blank= True)
    created_at = datetime.date.today()


    def __str__(self):
        return self.email



class Articulo(models.Model):
    foto = models.ImageField(null=False, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    pago = models.URLField(null=False,blank=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title


class Articulosi(models.Model):
    foto = models.ImageField(null=False, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    pago = models.URLField(null=False,blank=False)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title

class Evento(models.Model):
    foto = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    ubicacion = models.TextField()
    red = models.URLField(null=True, blank=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Contacto(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.URLField(null=False, blank= False)
    asunto = models.CharField(max_length=200)
    text = models.TextField()
    created_at = datetime.date.today()


    def __str__(self):
        return self.email


class Galeria(models.Model):
    img_1 = models.ImageField(null=True, blank=True)
    img_2 = models.ImageField(null=True, blank=True)
    img_3 = models.ImageField(null=True, blank=True)
    img_4 = models.ImageField(null=True, blank=True)
    img_5 = models.ImageField(null=True, blank=True)
    img_6 = models.ImageField(null=True, blank=True)
    img_7 = models.ImageField(null=True, blank=True)
    img_8 = models.ImageField(null=True, blank=True)




class Datoce(models.Model):
    anho = models.CharField(max_length= 100)
    miembros = models.CharField(max_length= 100)
    alumnos = models.CharField(max_length= 100)
    actividades = models.CharField(max_length= 100)
    foto  = models.ImageField(null=True, blank=True)



class Reloj(models.Model):
    title = models.CharField(max_length= 500)
    hora = models.CharField(max_length= 300)
    cont = models.CharField(max_length=100, default="#")


class Miembro(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nombre = models.CharField(max_length=300)
    cargo = models.CharField(max_length=300)
    face = models.CharField(max_length=300, default="#")
    twi = models.CharField(max_length=300, default="#")
    ins = models.CharField(max_length=300, default="#")


    def __str__(self):
        return self.nombre


class Testimonio(models.Model):
    foto = models.ImageField(null=True, blank=True)
    texto = models.TextField()
    nombre = models.CharField(max_length=300)
    cargo = models.CharField(max_length=300)


    def __str__(self):
        return self.nombre

class Fotosombra(models.Model):
    img_1 = models.ImageField(null=True, blank=True)
    img_2 = models.ImageField(null=True, blank=True)
    img_3 = models.ImageField(null=True, blank=True)
    img_4 = models.ImageField(null=True, blank=True)
    img_5 = models.ImageField(null=True, blank=True)
    img_6 = models.ImageField(null=True, blank=True)
    img_7 = models.ImageField(null=True, blank=True)
    img_8 = models.ImageField(null=True, blank=True)
    img_9 = models.ImageField(null=True, blank=True)
    img_10 = models.ImageField(null=True, blank=True)
    img_11 = models.ImageField(null=True, blank=True)


class Paper(models.Model):
    titulo = models.CharField(max_length=300)
    subtitulo = models.CharField(max_length=300)
    texto = models.TextField()
    foto = models.ImageField(null=True, blank=True)
    num = models.CharField(max_length=20, default="#")


    def __str__(self):
        return self.titulo

class About(models.Model):
    titulo1 = models.CharField(max_length=100,default="#")
    somos = models.TextField()
    titulo2= models.CharField(max_length=100,default="#")
    historia = models.TextField()
    titulo3 = models.CharField(max_length=100,default="#")
    copainge = models.TextField(default="#")


class Primero(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nombre = models.CharField(max_length=300)
    carrera = models.CharField(max_length=300, default="#")
    cargo = models.CharField(max_length=300)
    face = models.CharField(max_length=300, default="#")
    twi = models.CharField(max_length=300, default="#")
    ins = models.CharField(max_length=300, default="#")


    def __str__(self):
        return self.nombre



class Servicio(models.Model):
    t1 = models.CharField(max_length=100, default="#")
    arte = models.TextField()
    t2 = models.CharField(max_length=100,default="#")
    facil = models.TextField()
    t3 = models.CharField(max_length=100, default="#")
    activ = models.TextField()
    t4 = models.CharField(max_length=100, default="#")
    cualif = models.TextField()
    t5 = models.CharField(max_length=100, default="#")
    hora = models.TextField()
    t6 = models.CharField(max_length=100, default="#")
    lab = models.TextField()
