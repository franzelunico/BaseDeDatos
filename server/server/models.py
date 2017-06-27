from django.db import models


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
        return self.nombre_p


class Tarjeta(models.Model):
    nombre_tar = models.CharField(max_length=255)
    nro_tarjeta = models.CharField(max_length=255)
    cardholder_name = models.CharField(max_length=255)
    fecha_expiracion = models.DateField(null=False)

    def __unicode__(self):
        return self.nombre_tar


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
        return self.version_pro


class Sistema_Operativo(models.Model):
    nombre_so = models.CharField(max_length=100)
    version_so = models.CharField(max_length=100)
    arquitectura = models.CharField(max_length=2)

    def __unicode__(self):
        return self.nombre_so


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
        return self.descripion


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
        return self.nombre_idio
#
#
# class Usuario(models.Model)
#     nombre = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#
#     def __unicode__(self):
#         return self.nombre
