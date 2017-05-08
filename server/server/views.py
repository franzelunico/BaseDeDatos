from django.shortcuts import render, redirect
from django.views import View
import psycopg2
import time
import datetime


class Programa(object):
    id_producto = None
    nombre_p = None
    version_pro = None
    tamanio_archivo_KB = None
    nombre_so = None
    version_so = None
    arquitectura = None
    precio = None
    valor = ""
    tipo = "Programa"

    def __init__(self, row):
        self.id_producto = row[0]
        self.nombre_p = row[1]
        self.version_pro = row[2]
        self.tamanio_archivo_KB = row[3]
        self.nombre_so = row[4]
        self.version_so = row[5]
        self.arquitectura_so = row[6]
        self.precio = row[7]
        self.valor += "<Nombre : " + self.nombre_p + '>'
        self.valor += "<Version : " + self.version_pro + '>'
        self.valor += "<Size : " + str(self.tamanio_archivo_KB) + " KB " + '>'
        self.valor += "<Precio : " + str(self.precio) + " Bs " + '>'
        self.valor += "<Soporte en Sistemas Operativos : "
        self.valor += "<Sistema Operativo : " + self.nombre_so + " "
        self.valor += "vesion : " + self.version_so + " "
        self.valor += "Arquitectura : " + self.arquitectura_so + '> >'


class UsuarioNominal(object):
    usuario_Id_Usuario = None
    usuario_nick_name = None
    usuario_password = None

    def __init__(self, u_id, u_nick, u_pass):
        self.usuario_Id_Usuario = u_id
        self.usuario_nick_name = u_nick
        self.usuario_password = u_pass

    def checklogin(self):
        print "checklogin"

    def getId(self):
        return self.usuario_Id_Usuario


class Coneccion(object):
    conn = None
    cur = None
    secion = None
    usuario_nominal = None

    def conectar(self, secion):
        self.secion = secion
        conn_string = "host='localhost' "
        conn_string += "dbname='gestion_usuarios' "
        conn_string += "user='franz' "
        conn_string += "password='tbd2017'"
        self.conn = psycopg2.connect(conn_string)
        self.cur = self.conn.cursor()

    def printBackendPID(self, mensaje):
        self.cur.execute("select pg_backend_pid();")
        rows = self.cur.fetchall()
        print mensaje, rows[0]

    def desconectar(self):
        self.cur.close()
        self.conn.close()

    def consulta(self, q_sql):
        self.cur.execute(q_sql)
        rows = self.cur.fetchall()
        return rows

    # debe crearse el usuario recuerda
    def login(self, nick, password):
        query = ""
        query += 'SELECT "id_usuario", "nombre_u", "password" '
        query += 'FROM "Usuario" '
        query += 'WHERE '
        query += '"nombre_u" = \'%s\' and ' % (nick)
        query += '"password" = \'%s\' ' % (password)
        query += ';'
        rows = self.consulta(query)
        if len(rows) == 1:
            u_id, u_nick, u_pass = rows[0]
            self.usuario_nominal = UsuarioNominal(u_id, u_nick, u_pass)
            query = 'insert into "Session"(id_usuario,activo) '
            query += 'values (%s,True);' % (u_id)
            query += ';'
            self.cur.execute(query)
            self.conn.commit()
        else:
            self.usuario_nominal = None

    def getUsuario(self):
        return self.usuario_nominal

    def permisos(self):
        query = ""
        query += "SELECT * "
        query += 'FROM "Usuario" '
        query += 'INNER JOIN  "User_Rol" ON "Usuario"."id_usuario"="User_Rol"."id_usuario" ' # noqa
        query += 'INNER JOIN  "Rol" ON "User_Rol"."id_rol"="Rol"."id_rol" '
        query += 'INNER JOIN  "Rol_Funcion" ON "Rol"."id_rol"="Rol_Funcion"."id_rol" '# noqa
        query += 'INNER JOIN  "Funcion" ON "Rol_Funcion"."id_funcion"="Funcion"."id_funcion" '# noqa
        query += 'INNER JOIN  "Funcion_Interface" ON "Funcion"."id_funcion"="Funcion_Interface"."id_funcion" '# noqa
        query += 'INNER JOIN  "Interface" ON "Funcion_Interface"."id_interface"="Interface"."id_interface" '# noqa
        query += 'INNER JOIN  "Tipo_UI" ON "Interface"."id_tipo_ui"= "Tipo_UI"."id_tipo_ui" '# noqa
        query += 'WHERE "Usuario"."id_usuario" = %d;' % (self.usuario_nominal.getId())# noqa
        rows = self.consulta(query)
        permisos = ""
        for row in rows:
            print row, 'permiso=', row[17]
            if len(permisos) > 0:
                permisos += "_"
            permisos += row[17]
        permisos += ".html"
        return permisos

    def getProductos(self):
        query = ""
        query += "SELECT "
        query += '"Producto".id_producto, '
        query += '"Producto".nombre_p, '
        query += '"Programa".version_pro, '
        query += '"Producto"."tamanio_archivo_KB", '
        query += '"Sistema_Operativo".nombre_so, '
        query += '"Sistema_Operativo".version_so, '
        query += '"Sistema_Operativo".arquitectura, '
        query += '"Sistema_Operativo".arquitectura, '
        query += '"Producto".precio '
        query += 'FROM "Programa" '
        query += 'INNER JOIN "Producto" ON "Programa".id_producto = "Producto".id_producto ' #noqa
        query += 'INNER JOIN "Sistema_Operativo" ON "Programa".id_sistema_operativo = "Sistema_Operativo".id_sistema_operativo;' #noqa
        rows = self.consulta(query)
        productos = []
        for row in rows:
            programa = Programa(row)
            productos.append(programa)
        # Realizar la consulta para los libros y mostrar
        return productos

    # lista de productos seleccionado es productos
    def comprar(self, productos, id_Ciudad, id_tarjetaa, correo_ee):
        fecha = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') #noqa
        cantidad = 1
        for id_producto in productos:
            id_producto = str(id_producto)
            id_ciudad = int(id_Ciudad)
            id_tarjeta = id_tarjetaa
            correo_e = "\'%s\'" % correo_ee
            row = self.getProducto(id_producto)
            nombre_p = "\'%s\'" % (row[0])
            precio_p = row[1]
            print nombre_p, precio_p
            valor = precio_p*cantidad
            query = ""
            query += 'INSERT INTO "Factura" ('
            query += 'id_producto, fecha , id_ciudad, id_tarjeta, correo_e, nombre_p, precio_p, valor, cantidad) ' #noqa
            query += 'VALUES (%s , \'%s\', %s       , \'%s\',%s,%s,%s,%s,%s );' % (id_producto, fecha, id_ciudad, id_tarjeta, correo_e, nombre_p, precio_p, valor, cantidad) #noqa
            self.cur.execute(query)
            self.conn.commit()

    def getCiudades(self):
        print 'GET CIUDADES'
        query = ''
        query += 'select '
        query += '"Pais".id_pais, '
        query += '"Pais".nombre_pai, '
        query += '"Ciudad".id_ciudad, '
        query += '"Ciudad".nombre_ciu '
        query += 'FROM "Ciudad"'
        query += 'INNER JOIN "Pais" ON "Ciudad".id_pais = "Pais".id_pais;'
        tabla = self.consulta(query)
        id_anterior = -1
        paises = []
        ciudades = []
        for fila in tabla:
            if id_anterior == fila[0]:
                ciudad = {
                    "id_ciudad": fila[2],
                    "nombre_ciu": fila[3]
                }
                ciudades.append(ciudad)
            else:
                ciudades = []
                id_anterior = fila[0]
                ciudad = {
                    "id_ciudad": fila[2],
                    "nombre_ciu": fila[3]
                }
                ciudades.append(ciudad)
                pais = {
                    "id_pais": fila[0],
                    "nombre_pai": fila[1],
                    "ciudades": ciudades
                }
                paises.append(pais)
        return paises

    def getTajetas(self):
        id_usuario = self.usuario_nominal.getId()
        query = ""
        query += 'Select "Tarjeta".id_tarjeta, "Tarjeta".cardholder_name '
        query += 'From "Tarjeta" '
        query += 'Where "Tarjeta".id_usuario = %s' % (id_usuario)
        tabla = self.consulta(query)
        tarjetas = []
        for fila in tabla:
            ciudad = {
                "id_tarjeta": fila[0],
                "cardholder_name": fila[1]
            }
            tarjetas.append(ciudad)
        usuario = {
            "id_usuario": id_usuario,
            "tarjetas": tarjetas
        }
        return usuario

    def getProducto(self, id_producto):
        print "GetProducto"
        query = ""
        query += 'select "Producto".nombre_p, "Producto".precio '
        query += 'from "Producto" '
        query += 'where "Producto".id_producto = %s;' % (id_producto)
        rows = self.consulta(query)
        for row in rows:
            print row[0], row[1]
        print rows[0]
        return rows[0]
        print "GetProducto"
        query = ""
        query += 'select "Producto".nombre_p, "Producto".precio '


    def agregarTarjeta(self, nombre_tar, nro_tarjeta, cardholder_name, fecha_expiracion): # noqa
        id_usuario = self.usuario_nominal.getId()
        query = ""
        query += 'insert into "Tarjeta"(id_usuario, nombre_tar, nro_tarjeta, cardholder_name, fecha_expiracion) ' # noqa
        query += 'values (%s, \'%s\', \'%s\', \'%s\', \'%s\');' % (id_usuario, nombre_tar, nro_tarjeta, cardholder_name, fecha_expiracion) # noqa
        self.cur.execute(query)
        self.conn.commit()

    def agregarPrograma(self, nombre_p, tamanio_archivo_KB, precio, version_pro, dominio_32_64): # noqa
        id_usuario = self.usuario_nominal.getId()
        # agregar Producto
        query = ""
        query += 'insert into "Producto"(id_usuario, nombre_p, "tamanio_archivo_KB", precio) ' # noqa
        query += 'values (%s, \'%s\', %s, %s);' % (id_usuario, nombre_p, tamanio_archivo_KB, precio) # noqa
        self.cur.execute(query)
        self.conn.commit()

        query = 'select currval(\'"Producto_id_producto_seq\"\');'
        self.cur.execute(query)
        rows = self.cur.fetchall()
        row = rows[0]
        print int(row[0])

        id_producto = int(row[0])
        id_sistema_operativo = 1
        query = 'insert into "Programa"(id_producto, id_sistema_operativo, version_pro, dominio_32_64) ' # noqa
        query += 'values (%s, %s, %s, %s);' % (id_producto, id_sistema_operativo, version_pro, dominio_32_64) # noqa
        print query
        self.cur.execute(query)
        self.conn.commit()

    def salir(self):
        query = ""
        query += 'select "Session".id_session '
        query += 'from "Session" order by fecha desc limit 1;'
        self.cur.execute(query)
        rows = self.cur.fetchall()
        self.conn.commit()
        id_session = rows[0]
        # session
        query = 'UPDATE "Session" '
        query += 'SET activo=False '
        query += 'WHERE "Session".id_session=%s;' % (id_session)
        self.cur.execute(query)
        self.conn.commit()


class Usuario(View):

    def get(self, request, *args, **kwargs):
        print "GET Usuario print permisos"
        coneccion = getConnecion(request)
        permisos = coneccion.permisos()
        productos = coneccion.getProductos()
        paises = coneccion.getCiudades()
        tarjetas = coneccion.getTajetas()
        context = {
            'saludo': 'Bienvenido Usuario',
            'productos': productos,
            'paises': paises,
            'u_tarjetas': tarjetas
        }
        return render(request, permisos, context)


class Login(View):
    coneccion = None

    def get(self, request, *args, **kwargs):
        getConnecion(request)
        mensaje = "Get Login"
        context = {'saludo': mensaje}
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        user_nick = request.POST['username']
        user_pass = request.POST['userpass']
        coneccion = getConnecion(request)
        coneccion.login(user_nick, user_pass)
        usuario = coneccion.getUsuario()
        if usuario is None:
            print "Los datos ingresados no son correctos"
        else:
            return redirect('/usuario/')

        coneccion.consulta("select pg_backend_pid();")
        mensaje = 'Abrir coneccion '
        context = {'saludo': mensaje}
        return render(request, 'index.html', context)


def salir(request):
    request.session.flush()
    coneccion = getConnecion(request)
    coneccion.salir()
    coneccion.desconectar()
    conecciones.remove(coneccion)
    coneccion = getConnecion(request)
    return redirect('login')


def comprar(request):
    productos = request.POST.getlist('checks')
    print "Lista de productos"
    print productos
    print "-------------------"
    coneccion = getConnecion(request)
    id_pais = request.POST['StatesList']
    id_ciudad = request.POST['CitiesList']
    id_tarjeta = request.POST['TarjetaList']
    correo_ee = request.POST['correo_e']
    print id_pais, id_ciudad, id_tarjeta
    coneccion.comprar(productos, id_ciudad, id_tarjeta, correo_ee)
    return redirect('/usuario/')


def tarjeta(request):
    nombre_tar = request.POST['nombre_tar']
    nro_tarjeta = request.POST['nro_tarjeta']
    cardholder_name = request.POST['cardholder_name']
    fecha_expiracion = request.POST['fecha_expiracion']
    coneccion = getConnecion(request)
    coneccion.agregarTarjeta(nombre_tar, nro_tarjeta, cardholder_name, fecha_expiracion) # noqa
    return redirect('/usuario/')


def programa(request):
    coneccion = getConnecion(request)
    permisos = coneccion.permisos()
    a = request.POST['nombre_p']
    b = request.POST['tamanio_archivo_KB']
    c = request.POST['precio']
    d = request.POST['version_pro']
    e = request.POST['dominio_32_64']
    coneccion.agregarPrograma(a, b, c, d, e)
    return render(request, permisos)


def getConnecion(request):
    res = None
    session = request.session.session_key
    mensaje = ""
    for coneccion in conecciones:
        aux_session = coneccion.secion
        if aux_session == session:
            mensaje = "Coneccion Existe"
            res = coneccion
    if res is None:
        mensaje = "Coneccion Nueva"
        res = Coneccion()
        res.conectar(session)
        conecciones.append(res)
    res.printBackendPID(mensaje)
    return res

conecciones = []
