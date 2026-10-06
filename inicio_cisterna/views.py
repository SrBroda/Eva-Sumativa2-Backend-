from django.http import Http404
from django.shortcuts import render

TEMAS = [
    {
        'slug': 'tema-1',
        'titulo': 'Tema 1',
        'descripcion': 'Imágenes de Civilization VI y Minecraft.',
        'imagen_principal': 'inicio_cisterna/images/Captura de pantalla 2026-10-06 012609.png',
        'imagenes': [
            'inicio_cisterna/images/Captura de pantalla 2026-10-06 012609.png',
            'inicio_cisterna/images/videojuegos-minecraft.png',
        ],
    },
    {
        'slug': 'tema-2',
        'titulo': 'Tema 2',
        'descripcion': 'Imágenes de Pink Floyd y Soundgarden.',
        'imagen_principal': 'inicio_cisterna/images/musica-pink-floyd.png',
        'imagenes': [
            'inicio_cisterna/images/musica-pink-floyd.png',
            'inicio_cisterna/images/musica-soundgarden.png',
        ],
    },
]


def inicio(request):
    context = {
        'nombre': 'Benjamin Cisterna',
        'apellido': 'Cisterna',
        'temas': TEMAS,
    }
    return render(request, 'inicio_cisterna/inicio.html', context)


def tema_detalle(request, slug):
    tema = next((item for item in TEMAS if item['slug'] == slug), None)
    if tema is None:
        raise Http404('Tema no encontrado.')

    context = {
        'apellido': 'Cisterna',
        'tema': tema,
        'temas': TEMAS,
    }
    return render(request, 'inicio_cisterna/tema_detalle.html', context)
