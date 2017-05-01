import psycopg2


class Coneccion(object):
    conn = None
    cur = None
    secion = None

    def conectar(self, secion):
        print secion
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
        self.cur.execute(q_sql)
        rows = self.cur.fetchall()
        for row in rows:
            print "   ", row[0]

# coneccion_1 = Coneccion()
# coneccion_1.conectar("seccion_1")
# coneccion_1.consulta("select pg_backend_pid();")
#
# coneccion_2 = Coneccion()
# coneccion_2.conectar("seccion_2")
# coneccion_2.consulta("select pg_backend_pid();")
