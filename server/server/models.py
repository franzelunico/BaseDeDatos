from django.db import models
from django.contrib.auth.models import User


class Factura(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)

    id_ciudad = models.ForeignKey('Ciudad', on_delete=models.CASCADE,)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE,)
    id_tarjeta = models.ForeignKey('Tarjeta', on_delete=models.CASCADE)
    correo_e = models.CharField(max_length=255)
    nombre_p = models.CharField(max_length=255)
    precio_p = models.IntegerField()
    valor = models.IntegerField()
    cantidad = models.IntegerField()

    class Meta:
        unique_together = (('fecha', 'id_producto'),)

    def __unicode__(self):
        return self.id_producto.nombre_p


class Tarjeta(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_tar = models.CharField(max_length=255)
    nro_tarjeta = models.CharField(max_length=255)
    cardholder_name = models.CharField(max_length=255)
    fecha_expiracion = models.DateField(null=False)

    def __unicode__(self):
        return self.id_usuario.username + ' - ' + self.nombre_tar


class Ciudad(models.Model):
    id_pais = models.ForeignKey('Pais', on_delete=models.CASCADE,)
    nombre_ciu = models.CharField(max_length=255)
    codigo_postal = models.IntegerField()

    def __unicode__(self):
        return self.nombre_ciu


class Pais(models.Model):
    nombre_pai = models.CharField(max_length=255)
    codigo_pai = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre_pai


class Producto(models.Model):
    nombre_p = models.CharField(max_length=255)
    tamanio_kb = models.IntegerField()
    precio = models.IntegerField()
    porcenta_descuento = models.IntegerField(default=0)
    oferta_inicio = models.DateField(null=True, blank=True)
    oferta_fin = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.nombre_p


class Programa(models.Model):
    producto = models.OneToOneField('Producto', on_delete=models.CASCADE,)
    id_sistema_operativo = models.ForeignKey('Sistema_Operativo',
                                             on_delete=models.CASCADE,)
    fecha_activacion = models.DateField(auto_now_add=True)
    fecha_exipiracion = models.DateField(auto_now_add=True)
    version_pro = models.CharField(max_length=255)
    dominio_32_64 = models.CharField(max_length=5)

    def __unicode__(self):
        so = self.id_sistema_operativo.nombre_so
        return self.producto.nombre_p + " - " + so


class Sistema_Operativo(models.Model):
    nombre_so = models.CharField(max_length=100)
    version_so = models.CharField(max_length=100)
    arquitectura = models.CharField(max_length=2)

    def __unicode__(self):
        ar = self.arquitectura
        return self.nombre_so + ' - ver' + self.version_so + ' - ar' + ar


# Libro
class Libro(models.Model):
    producto = models.OneToOneField('Producto', on_delete=models.CASCADE,)
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE,)
    id_editorial = models.ForeignKey('Editorial', on_delete=models.CASCADE,)
    id_idioma = models.ForeignKey('Idioma', on_delete=models.CASCADE,)

    descripcion = models.CharField(max_length=255)
    isb = models.CharField(max_length=255)
    fecha_publicacion = models.DateField(null=False)

    def __unicode__(self):
        return self.producto.nombre_p


class Categoria(models.Model):
    nombre_cat = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre_cat


class Editorial(models.Model):
    nombre_edi = models.CharField(max_length=255)
    pagina = models.CharField(max_length=255)
    fundacion = models.DateField(null=False)

    def __unicode__(self):
        return self.nombre_edi


class Idioma(models.Model):
    nombre_idio = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre_idio


class Libro_Autor(models.Model):
    id_autor = models.ForeignKey('Autor', on_delete=models.CASCADE,)
    id_producto = models.ForeignKey('Libro', on_delete=models.CASCADE,)

    def __unicode__(self):
        return self.id_autor + " <-> " + self.id_producto


class Autor(models.Model):
    nombres = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    apellido_materno = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombres


# GESTION USUARIOS

class User_Rol(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE,)
    id_rol = models.ForeignKey('Rol', on_delete=models.CASCADE,)
    activo = models.BooleanField(default=False)

    def __unicode__(self):
        usuario = self.id_usuario.username
        rol = " " + self.id_rol.nombre_r
        activo = " Activo: " + str(self.activo)
        return usuario + rol + activo


class Rol_Funcion(models.Model):
    id_rol = models.ForeignKey('Rol', on_delete=models.CASCADE,)
    id_funcion = models.ForeignKey('Funcion', on_delete=models.CASCADE,)
    activo = models.BooleanField(default=False)

    def __unicode__(self):
        return self.id_rol + "-" + self.id_funcion


class Funcion_Interface(models.Model):
    id_funcion = models.ForeignKey('Funcion', on_delete=models.CASCADE,)
    id_interface = models.ForeignKey('Interface', on_delete=models.CASCADE,)

    def __unicode__(self):
        return self.id_funcion + "-" + self.id_interface


class Interface(models.Model):
    nombre = models.CharField(max_length=255)
    id_tipo_ui = models.ForeignKey('Tipo_UI', on_delete=models.CASCADE,)
    nombre_in = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre


class Tipo_UI(models.Model):
    nombre_t_u = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre


class Funcion(models.Model):
    nombre_f = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre_f


class Rol(models.Model):
    nombre_r = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre_r


class Session(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE,)
    pid = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=False)

    def __unicode__(self):
        return self.id_usuario
