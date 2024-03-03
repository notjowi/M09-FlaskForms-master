from flask import Flask, request, render_template_string, render_template, redirect, url_for
import maildb

app = Flask(__name__)

#Cuando alguien busca la raiz de la pagina web le redirije al home
@app.route("/")
def inici():
    return redirect(url_for('home'))
#abre el archivo home.html cuando alguien busca dominio/home
@app.route('/home')
def home():
   return render_template('home.html')
#Esta funcion se encarga del proceso de login tanto el formulario de login como una vez hecho el login
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      result=True
      nom = request.form['name']
      password = request.form['password']
      data = maildb.sqlgetuserdata(nom,password)
      return render_template('formlogin.html',nom=nom,data=data,result=result)
   else:
      result=False
      return render_template('formlogin.html',result=result)
#Esta funcion se encarga del proceso de registro tanto el formulario como una vez registrado
@app.route('/register',methods = ['POST', 'GET'])
def register():
   if request.method == 'POST':
      nom = request.form['name'] 
      password = request.form['password']
      result_msg = maildb.sqladdUser(nom,password)
      return render_template('resultadoregister.html',nom=nom,result_msg=result_msg)
   else:
      return render_template('formregister.html')
#Esta funcion abre el aboutme.html al redirigirse a la url /aboutme
@app.route('/aboutme')
def aboutme():
   return render_template('aboutme.html')