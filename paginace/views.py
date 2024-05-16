from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import *
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Paginator
from django.db.models import  Q

def index(request):
    posts = Post.objects.all().order_by('-published_date')[0:4]
    articulos = Articulo.objects.all().order_by('-published_date')[0:3]
    eventos = Evento.objects.all().order_by('-published_date')[0:2]
    galerias = Galeria.objects.all()
    datoces = Datoce.objects.all()
    relojes = Reloj.objects.all()
    papers = Paper.objects.all().order_by('-id')
    servicios = Servicio.objects.all()
    return render(request, 'index.html', {"posts": posts,"articulos": articulos,"eventos": eventos,"galerias":galerias,
              "datoces":datoces,"relojes":relojes,"papers":papers,"servicios":servicios})

def raiz (request):
    return redirect('/inicio')

def about (request):
    miembros = Miembro.objects.all()
    testimonios = Testimonio.objects.all()
    fotosombras = Fotosombra.objects.all()
    abouts = About.objects.all()
    primeros = Primero.objects.all()
    return render(request, 'about.html' , {"miembros":miembros,"testimonios":testimonios,"fotosombras":fotosombras,"abouts":abouts,"primeros":primeros})

def deportes (request):
    deportes = Deporte.objects.all()
    return render(request, 'copainge.html' , {"deportes":deportes})

def blog (request):
    posts = Post.objects.all().order_by('-published_date')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    paginator_posts = paginator.get_page(page)
    posts = Post.objects.all().order_by('-published_date')[0:6]
    contexto = {"posts_pagin": paginator_posts, "posts": posts}
    return render(request, 'blog.html', contexto)

def single_blog(request, pk):
    post = get_object_or_404(Post, pk=pk)
    posts = Post.objects.all().order_by('-published_date')[0:6]
    contexto = {"post": post, "posts":posts}
    return render(request, 'single_blog.html', contexto)

def course(request):
    articulos = Articulo.objects.all().order_by('-published_date')
    paginator = Paginator(articulos, 6)
    page = request.GET.get('page')
    paginator_articulos = paginator.get_page(page)
    contexto = {"articulos": paginator_articulos}
    return render(request, 'course.html',contexto)

def shop(request):
    articulosis = Articulosi.objects.all().order_by('-published_date')
    paginator = Paginator(articulosis, 6)
    page = request.GET.get('page')
    paginator_articulosis = paginator.get_page(page)
    contexto = {"articulosis": paginator_articulosis}
    return render(request, 'shop.html',contexto)


def eventos(request):
    eventos = Evento.objects.all().order_by('-published_date')
    paginator = Paginator(eventos, 6)
    page = request.GET.get('page')
    paginator_eventos = paginator.get_page(page)
    contexto = {"eventos": paginator_eventos}
    return render(request, 'eventos.html',contexto)

def contact(request):
    return render(request, 'contact.html')

def inscripcion(request):
    return render(request, 'inscripcion.html')

def transparencia(request):
    return render(request, 'transparencia.html')

def feedback(request):
    return render(request, 'feedback.html')

def streaming(request):
    return render(request, 'streaming.html')

def gestion (request):
    gestions = Gestion.objects.all().order_by('-published_date')
    paginator = Paginator(gestions, 30)
    page = request.GET.get('page')
    paginator_posts = paginator.get_page(page)
    gestions = Gestion.objects.all().order_by('-published_date')[0:6]
    contexto = {"posts_pagin": paginator_posts, "gestions": gestions}
    return render(request, 'gestion.html', contexto)

def gestionce(request, pk):
    gestion = get_object_or_404(Gestion, pk=pk)
    gestions = Gestion.objects.all().order_by('-published_date')[0:6]
    contexto = {"gestion": gestion, "gestions": gestions}
    return render(request, 'gestionce.html', contexto)


def crear_correo(request):
    if request.method == "POST":
        emailUsuario = request.POST.get('emailUsuario', None)
        Newsletter_email.objects.create(email = emailUsuario)
        return JsonResponse({"success" : True})

def data_inicial(request):
    posts = serializers.serialize('json', Post.objects.all().order_by('-published_date')[0:2])
    return JsonResponse({"posts": posts})


def crear_contacto(request):
    if request.method == "POST":
        contactoUsuario = request.POST.get('contactoUsuario', None)
        contactoNombre = request.POST.get('contactoNombre', None)
        contactoAsunto = request.POST.get('contactoAsunto', None)
        contactoMen = request.POST.get('contactoMen', None)
        Contacto.objects.create(email = contactoUsuario, nombre = contactoNombre, asunto = contactoAsunto, text = contactoMen)
        return JsonResponse({"success" : True})


def busqueda(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.all().order_by('-published_date')
    if queryset:
        posts=Post.objects.filter(
            Q(title__icontains=queryset)|
            Q(text__icontains=queryset)
        ).distinct().order_by('-published_date')
    paginator = Paginator(posts, 20)
    page = request.GET.get('page')
    paginator_busquedas = paginator.get_page(page)
    contexto = {"busqueda": paginator_busquedas, "posts": posts}
    return render(request,'busqueda.html',contexto)




def tag1 (request):
    posts = Post.objects.filter(
        categoriacarrera = Categoriacarrera.objects.get(nombre = 'Desarrollo')
    ).order_by('-published_date')
    paginator = Paginator(posts, 20)
    page = request.GET.get('page')
    paginator_tags = paginator.get_page(page)
    contexto = {"tag": paginator_tags, "posts": posts}
    return render(request, 'tag.html', contexto)


def tag2(request):
    posts = Post.objects.filter(
        categoriacarrera = Categoriacarrera.objects.get(nombre = 'Proyectos')
    ).order_by('-published_date')
    paginator = Paginator(posts, 20)
    page = request.GET.get('page')
    paginator_tags = paginator.get_page(page)
    contexto = {"tag": paginator_tags, "posts": posts}
    return render(request, 'tag.html', contexto)

def tag3(request):
    posts = Post.objects.filter(
        categoriacarrera = Categoriacarrera.objects.get(nombre = 'Democracia')
    ).order_by('-published_date')
    paginator = Paginator(posts, 20)
    page = request.GET.get('page')
    paginator_tags = paginator.get_page(page)
    contexto = {"tag": paginator_tags, "posts": posts}
    return render(request, 'tag.html', contexto)

def tag4(request):
    posts = Post.objects.filter(
        categoriacarrera = Categoriacarrera.objects.get(nombre = 'Construcción')
    ).order_by('-published_date')
    paginator = Paginator(posts, 20)
    page = request.GET.get('page')
    paginator_tags = paginator.get_page(page)
    contexto = {"tag": paginator_tags, "posts": posts}
    return render(request, 'tag.html', contexto)

def tag5(request):
    posts = Post.objects.filter(
        categoriacarrera = Categoriacarrera.objects.get(nombre = 'Informática')
    ).order_by('-published_date')
    paginator = Paginator(posts, 20)
    page = request.GET.get('page')
    paginator_tags = paginator.get_page(page)
    contexto = {"tag": paginator_tags, "posts": posts}
    return render(request, 'tag.html', contexto)

def tag6(request):
    posts = Post.objects.filter(
        categoriacarrera = Categoriacarrera.objects.get(nombre = 'Electricidad')
    ).order_by('-published_date')
    paginator = Paginator(posts, 20)
    page = request.GET.get('page')
    paginator_tags = paginator.get_page(page)
    contexto = {"tag": paginator_tags, "posts": posts}
    return render(request, 'tag.html', contexto)

def tag7(request):
    posts = Post.objects.filter(
        categoriacarrera = Categoriacarrera.objects.get(nombre = 'Electronica')
    ).order_by('-published_date')
    paginator = Paginator(posts, 20)
    page = request.GET.get('page')
    paginator_tags = paginator.get_page(page)
    contexto = {"tag": paginator_tags, "posts": posts}
    return render(request, 'tag.html', contexto)

def tag8(request):
    posts = Post.objects.filter(
        categoriaedu = Categoriaedu.objects.get(nombre = 'Deportes')
    ).order_by('-published_date')
    paginator = Paginator(posts, 20)
    page = request.GET.get('page')
    paginator_tags = paginator.get_page(page)
    contexto = {"tag": paginator_tags, "posts": posts}
    return render(request, 'tag.html', contexto)

def tag9(request):
    posts = Post.objects.filter(
        categoriaedu = Categoriaedu.objects.get(nombre = 'Medio Ambiente')
    ).order_by('-published_date')
    paginator = Paginator(posts, 20)
    page = request.GET.get('page')
    paginator_tags = paginator.get_page(page)
    contexto = {"tag": paginator_tags, "posts": posts}
    return render(request, 'tag.html', contexto)

def tag10(request):
    posts = Post.objects.filter(
        categoriaedu = Categoriaedu.objects.get(nombre = 'Educación')
    ).order_by('-published_date')
    paginator = Paginator(posts, 20)
    page = request.GET.get('page')
    paginator_tags = paginator.get_page(page)
    contexto = {"tag": paginator_tags, "posts": posts}
    return render(request, 'tag.html', contexto)

def tag11(request):
    posts = Post.objects.filter(
        categoriafcyt = Categoriafcyt.objects.get(nombre = 'FCyT')
    ).order_by('-published_date')
    paginator = Paginator(posts, 20)
    page = request.GET.get('page')
    paginator_tags = paginator.get_page(page)
    contexto = {"tag": paginator_tags, "posts": posts}
    return render(request, 'tag.html', contexto)

def tag12(request):
    posts = Post.objects.filter(
        categoriafcyt = Categoriafcyt.objects.get(nombre = 'Paraguay')
    ).order_by('-published_date')
    paginator = Paginator(posts, 20)
    page = request.GET.get('page')
    paginator_tags = paginator.get_page(page)
    contexto = {"tag": paginator_tags, "posts": posts}
    return render(request, 'tag.html', contexto)


def search(request):
    searchText = request.POST.get('searchText', None)
    print("searchText")
    print(searchText)
    posts = serializers.serialize('json', Post.objects.filter(text__contains=searchText) )
    return JsonResponse({"success": True, "posts": posts})