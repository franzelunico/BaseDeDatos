from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Factura, Tarjeta, Ciudad, Pais, Producto
from .models import Programa, Sistema_Operativo, Libro, Categoria, Editorial
from .models import Idioma, Libro_Autor, Autor


admin.site.register(Factura)
admin.site.register(Tarjeta)
admin.site.register(Ciudad)
admin.site.register(Pais)
admin.site.register(Producto)
admin.site.register(Programa)
admin.site.register(Sistema_Operativo)
admin.site.register(Libro)
admin.site.register(Categoria)
admin.site.register(Editorial)
admin.site.register(Idioma)
admin.site.register(Libro_Autor)
admin.site.register(Autor)
