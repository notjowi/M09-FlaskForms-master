import mysql.connector
#Nos conectamos a la base de datos
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="emaildb"
)

mycursor = mydb.cursor()
       
#CONSTANTS pel resultat de les fucions
NOTROBAT = "NOTROBAT"
AFEGIT = "AFEGIT"
MODIFICAT = "MODIFICAT"
JAEXISTEIX = "JAEXISTEIX"
#Esta funcion compara con la base de datos mysql con el usuario y contraseña que le entran como parametros 
def sqlgetuserdata(name,password):
    #sqlname = "SELECT name FROM tienda WHERE name ='%s'"
    #sqlpassword = "SELECT password FROM tienda WHERE password ='%s'"
    sql = "SELECT name, password FROM tienda WHERE name = %s AND password = %s"
    mycursor.execute(sql, (name,password,))
    myresult = mycursor.fetchone()
    if myresult:
        return JAEXISTEIX
    return NOTROBAT
#Esta funcion hace una consulta a la base de datos para comprobar si el usuario pertenece o no a la misma
def sqlgetname(name):
    sql = "SELECT name FROM tienda WHERE name =%s"
    mycursor.execute(sql, (name,))
    myresult = mycursor.fetchall()
    if myresult is not None:
        return JAEXISTEIX
    else:
        return NOTROBAT
#Esta funcion añade usuarios mediante una consula de mysql
def sqladdUser(name,password):
    oldname = sqlgetname(name)
    sqlinsert = "INSERT INTO tienda (name, password) VALUES (%s, %s)"
    val = (name, password)
    if oldname == NOTROBAT:
        mycursor.execute(sqlinsert, val)
        mydb.commit()
        return AFEGIT
    else:
        return JAEXISTEIX
#Esta funcion modifica un usuario ya existente en la base de datos mediante una query    
def sqlmodUser(updatedname,updatedpassword,name):
    oldname = sqlgetname(name)
    sqlupdate = "UPDATE tienda SET name = (%s), password = (%s) WHERE name = (%s)"
    val = (updatedname,updatedpassword,name)
    if (oldname == JAEXISTEIX):
        mycursor.execute(sqlupdate, val)
        return MODIFICAT
    mydb.commit()