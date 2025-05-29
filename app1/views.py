from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Administrador, Producto, Oferta, MensajeContacto
from django.utils import timezone
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.views.decorators.cache import never_cache


def index(request):
    productos = Producto.objects.all()
    ofertas = Oferta.objects.select_related('producto').all()
    return render(request, 'index.html', {
        'productos': productos,
        'ofertas': ofertas,
    })

def administrador_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            administrador = Administrador.objects.get(email=email)
            # Verificar si el administrador está bloqueado
            if administrador.bloqueado:
                messages.error(request, 'Este usuario está bloqueado. Contacte al administrador.')
                return redirect('administrador_login')
            # Verificar la contraseña
            if check_password(password, administrador.password):
                request.session['administrador_id'] = administrador.id  # Guarda el ID del administrador en la sesión
                return redirect('control')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        except Administrador.DoesNotExist:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'administrador_login.html')

@never_cache
def control(request):
    administrador_id = request.session.get('administrador_id')
    if not administrador_id:
        messages.error(request, 'Por favor, inicie sesión para acceder al panel.')
        return redirect('administrador_login')

    # CRUD para productos y ofertas
    if request.method == 'POST':
        action = request.POST.get('action')
        model_type = request.POST.get('model_type')
        try:
            if action == 'crear':
                if model_type == 'producto':
                    Producto.objects.create(
                        nombre=request.POST.get('nombre'),
                        descripcion=request.POST.get('descripcion'),
                        precio=request.POST.get('precio'),
                        stock=request.POST.get('stock'),
                        imagen=request.FILES.get('imagen')
                    )
                    messages.success(request, 'Producto creado exitosamente')
                elif model_type == 'oferta':
                    Oferta.objects.create(
                        producto_id=request.POST.get('producto_id'),
                        precio_original=request.POST.get('precio_original'),
                        precio_descuento=request.POST.get('precio_descuento'),
                        descripcion=request.POST.get('descripcion'),
                        imagen=request.FILES.get('imagen')
                    )
                    messages.success(request, 'Oferta creada exitosamente')
            elif action == 'eliminar':
                if model_type == 'producto':
                    Producto.objects.get(id=request.POST.get('id')).delete()
                    messages.success(request, 'Producto eliminado exitosamente')
                elif model_type == 'oferta':
                    Oferta.objects.get(id=request.POST.get('id')).delete()
                    messages.success(request, 'Oferta eliminada exitosamente')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')

    productos = Producto.objects.all()
    ofertas = Oferta.objects.select_related('producto').all()
    mensajes = MensajeContacto.objects.all()

    context = {
        'productos': productos,
        'ofertas': ofertas,
        'mensajes': mensajes,
        'active_section': request.POST.get('active_section', 'productos'),
    }
    return render(request, "control.html", context)

def logout(request):
    request.session.flush()  # Eliminar todas las sesiones
    return redirect('index')  # Redirigir a la página de inicio
