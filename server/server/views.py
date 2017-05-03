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
        self.valor += "Nombre : " + self.nombre_p
        self.valor += "Version : " + self.version_pro
        self.valor += "Size : " + str(self.tamanio_archivo_KB) + " KB "
        self.valor += "Precio : " + str(self.precio) + " KB "
        self.valor += "Soporte en Sistemas Operativos : "
        self.valor += self.nombre_so + " " + self.version_so + " "
        self.valor += self.arquitectura_so


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

    def desconectar(self):
        self.cursor.close()
        self.coneccion.close()

    def consulta(self, q_sql):
        self.cur.execute("select pg_backend_pid();")
        rows = self.cur.fetchall()

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
        else:
            self.usuario_nominal = None

    def getUsuario(self):
        return self.usuario_nominal

    def permisos(self):
        query = ""
        query += "SELECT * "
        query += 'FROM "Usuario" '
        query += 'INNER JOIN  "User_Rol" ON "Usuario"."id_usuario"="User_Rol"."id_usuario" '# noqa
        query += 'INNER JOIN  "Rol" ON "User_Rol"."id_rol"="Rol"."id_rol" '
        query += 'INNER JOIN  "Rol_Funcion" ON "Rol"."id_rol"="Rol_Funcion"."id_rol" '# noqa
        query += 'INNER JOIN  "Funcion" ON "Rol_Funcion"."id_funcion"="Funcion"."id_funcion" '# noqa
        query += 'INNER JOIN  "Funcion_Interface" ON "Funcion"."id_funcion"="Funcion_Interface"."id_funcion" '# noqa
        query += 'INNER JOIN  "Interface" ON "Funcion_Interface"."id_interface"="Interface"."id_interface" '# noqa
        query += 'INNER JOIN  "Tipo_UI" ON "Interface"."id_tipo_ui"= "Tipo_UI"."id_tipo_ui" '# noqa
        query += 'WHERE "Usuario"."id_usuario" = %d;' % (self.usuario_nominal.getId())# noqa
        rows = self.consulta(query)
        if len(rows) == 1:
            print rows[0]

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

    def comprar(self, productos, id_Ciudad):
        id_Ciudad = int(id_Ciudad)
        fecha = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') #noqa
        for id_producto in productos:
            id_producto = str(id_producto)
            query = ""
            query += 'INSERT INTO "Factura" ('
            query += 'id_producto, fecha, id_ciudad, direccion, id_tarjeta) '
            query += 'VALUES (%s, \'%s\', %d, \'calle libertador 102\', 1);' % (id_producto, fecha, id_Ciudad) #noqa
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
                print "Agregar ciudad", fila[3]
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


class Usuario(View):

    def get(self, request, *args, **kwargs):
        coneccion = getConnecion(request)
        coneccion.permisos()
        productos = coneccion.getProductos()
        paises = coneccion.getCiudades()
        pais = {
            "id_pais": 1,
            "nombre_pai": "Bolivia",
            "ciudades": ["Cbba", "Santa Cruz"]
        }
        context = {
            'saludo': 'Bienvenido Usuario',
            'productos': productos,
            'paises': paises,
            'pais': pais
        }
        return render(request, 'usuario.html', context)


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
    coneccion.desconectar()
    conecciones.remove(coneccion)
    mensaje = 'Ha salido de la  coneccion '
    context = {'saludo': mensaje}
    return render(request, 'index.html', context)


def comprar(request):
    productos = request.POST.getlist('checks')
    coneccion = getConnecion(request)
    id_pais = request.POST['StatesList']
    id_ciudad = request.POST['CitiesList']
    print id_pais, id_ciudad
    coneccion.comprar(productos, id_ciudad)
    mensaje = 'Comprado'
    context = {'saludo': mensaje}
    return render(request, 'index.html', context)


def getConnecion(request):
    res = None
    session = request.session.session_key
    for coneccion in conecciones:
        aux_session = coneccion.secion
        if aux_session == session:
            print "Coneccion Existe"
            res = coneccion
    if res is None:
        print "Coneccion Nueva"
        res = Coneccion()
        res.conectar(session)
        conecciones.append(res)
    return res

conecciones = []
