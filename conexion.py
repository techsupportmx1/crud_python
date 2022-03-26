"""
	CRUD con MySQL y Python 3
	Ph.D. Aldo González Vázquez
"""
import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='peliculas')
	print("Conexión correcta")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)
