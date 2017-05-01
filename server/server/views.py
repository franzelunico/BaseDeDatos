from django.shortcuts import render, redirect
from django.views import View
import psycopg2


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
        print "pg_backend_pid ", rows[0]

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
        print query
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


class Usuario(View):

    def get(self, request, *args, **kwargs):
        coneccion = getConnecion(request)
        coneccion.permisos()
        context = {'saludo': 'Bienvenido Usuario'}
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
