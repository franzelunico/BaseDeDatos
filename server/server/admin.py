from django.contrib import admin
from .models import Factura, Tarjeta, Ciudad, Pais, Producto
from .models import Programa, Sistema_Operativo, Libro, Categoria, Editorial
from .models import Idioma, Libro_Autor, Autor
from .models import User_Rol, Rol_Funcion, Funcion_Interface, Interface
from .models import Tipo_UI, Funcion, Rol, Session


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
admin.site.register(User_Rol)
admin.site.register(Rol_Funcion)
admin.site.register(Funcion_Interface)
admin.site.register(Interface)
admin.site.register(Tipo_UI)
admin.site.register(Funcion)
admin.site.register(Rol)
admin.site.register(Session)
