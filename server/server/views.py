from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from server.models import Programa, Tarjeta, Producto, Sistema_Operativo
from server.models import Pais, Ciudad, Factura
from server.models import User_Rol
import datetime
import time


class Login(View):

    def get(self, request, *args, **kwargs):
        mensaje = "Get Login"
        context = {'saludo': mensaje}
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        user_nick = request.POST['username']
        user_pass = request.POST['userpass']
        usuario = authenticate(username=user_nick, password=user_pass)
        if usuario is None:
            print "Los datos ingresados no son correctos"
        else:
            user_rol = None
            try:
                user_rol = User_Rol.objects.get(id_usuario=usuario)
            except User_Rol.DoesNotExist:
                user_rol = None
                print "<------USUARIO SIN ROL------>"
            if user_rol is not None:
                if user_rol.activo:
                    login(request, usuario)
                    return redirect('/usuario/')
                else:
                    print "<------ROL INACTIVO------>"

        context = {'user': usuario}
        return render(request, 'index.html', context)


class UserView(View):

    def get(self, request, *args, **kwargs):
        usuario = request.user
        print usuario
        user_rol = User_Rol.objects.get(id_usuario=usuario)
        rol = user_rol.id_rol
        permisos = ""
        context = {}
        if rol.nombre_r == 'administrador':
            permiso = 'producto.html'
            mensaje = 'Abrir coneccion '
            context = {'saludo': mensaje}
            return render(request, permiso, context)
        if rol.nombre_r == 'cliente':
            permisos = "comprar_tarjeta.html"
            programas = Programa.objects.all()
            tarjetas = Tarjeta.objects.filter(id_usuario=usuario)
            lista_tarjetas = []
            for tarj in tarjetas:
                tarjeta = {
                    'cardholder_name': tarj.cardholder_name,
                    'id_tarjeta': tarj.id
                }
                lista_tarjetas.append(tarjeta)
            tarjetas = {'id_usuario': usuario.id, 'tarjetas': lista_tarjetas}

            paises = []
            for pais in Pais.objects.all():
                ciudades = []
                for ciudad in Ciudad.objects.filter(id_pais=pais):
                    ciudad_obj = {
                        "id_ciudad": ciudad.id,
                        "nombre_ciu": ciudad.nombre_ciu
                    }
                    ciudades.append(ciudad_obj)
                pais_obj = {
                    "id_pais": pais.id,
                    "nombre_pai": pais.nombre_pai,
                    "ciudades": ciudades
                }
                paises.append(pais_obj)
            context = {
                'saludo': 'Bienvenido Usuario',
                'programas': programas,
                'u_tarjetas': tarjetas,
                'user': usuario,
                'paises': paises
            }
            return render(request, permisos, context)
        return redirect('/')


def salir(request):
    logout(request)
    return redirect('login')


def programa(request):
    # Producto
    producto = Producto()
    producto.nombre_p = request.POST['nombre_p']
    producto.tamanio_kb = request.POST['tamanio_archivo_KB']
    producto.precio = request.POST['precio']
    producto.save()
    # Programa
    sis_op = Sistema_Operativo.objects.get(pk=1)
    programa = Programa()
    programa.producto = producto
    programa.id_sistema_operativo = sis_op
    programa.version_pro = request.POST['version_pro']
    programa.dominio_32_64 = request.POST['dominio_32_64']
    programa.save()

    mensaje = 'Abrir coneccion '
    context = {'saludo': mensaje}
    return render(request, 'producto.html', context)


def comprar(request):
    id_tarjeta = request.POST['TarjetaList']
    id_ciudad = request.POST['CitiesList']
    correo_e = request.POST['correo_e']
    fecha = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') #noqa
    productos = request.POST.getlist('checks')
    for id_producto in productos:
        print id_producto
        ciudad = Ciudad.objects.get(id=id_ciudad)
        producto = Producto.objects.get(id=id_producto)
        tarjeta = Tarjeta.objects.get(id=id_tarjeta)
        print producto.nombre_p, ciudad.nombre_ciu, tarjeta.nombre_tar
        factura = Factura()
        factura.id_ciudad = ciudad
        factura.id_producto = producto
        factura.id_tarjeta = tarjeta
        factura.correo_e = correo_e
        factura.nombre_p = producto.nombre_p
        factura.precio_p = producto.precio
        factura.cantidad = 1
        factura.valor = factura.cantidad*producto.precio
        factura.fecha = fecha
        factura.save()

    return redirect('/usuario/')


def tarjeta(request):
    tarjeta = Tarjeta()
    tarjeta.id_usuario = request.user
    tarjeta.nombre_tar = request.POST['nombre_tar']
    tarjeta.nro_tarjeta = request.POST['nro_tarjeta']
    tarjeta.cardholder_name = request.POST['cardholder_name']
    tarjeta.fecha_expiracion = request.POST['fecha_expiracion']
    tarjeta.save()
    return redirect('/usuario/')
