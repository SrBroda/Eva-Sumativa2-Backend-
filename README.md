# Evaluacion Sumativa 2 Backend

Este sitio corresponde a la Evaluación Sumativa 2 de Backend. Tiene una página de inicio y dos temas; cada tema cuenta con una galería de dos imágenes.

## Integrante
- Nombre completo: Benjamin Cisterna
- Correo institucional: benjamin.cisterna03@inacapmail.cl

## Requisitos
- Python 3.12 o superior
- Git

Las dependencias de Python están declaradas en `requirements.txt`. Bootstrap y Bootstrap Icons se cargan desde CDN.

## Instalación en Windows (PowerShell)
```powershell
git clone https://github.com/SrBroda/Eva-Sumativa2-Backend-.git
cd Eva-Sumativa2-Backend-
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abrir `http://127.0.0.1:8000/` en el navegador.

## Pruebas
```powershell
python manage.py check
python manage.py test
```

## Estructura
- `cisterna/`: configuración del proyecto Django.
- `inicio_cisterna/`: vistas, rutas y pruebas de la aplicación.
- `templates/inicio_cisterna/`: templates compartidos, inicio y detalle de temas.
- `static/inicio_cisterna/css/`: estilos propios.
- `static/inicio_cisterna/images/`: imágenes de los carruseles.
- `manage.py`: comandos de administración de Django.

## Temas e imágenes
La vista entrega los datos de los temas a los templates. Cada detalle muestra su descripción y un carrusel con dos imágenes. Los archivos se sirven desde `static/inicio_cisterna/images/`.
