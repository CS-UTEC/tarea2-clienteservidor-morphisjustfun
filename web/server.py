from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json
import time

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/palindrome/<palabra>')
def palindrome(palabra):
    i =int(len(palabra)/2)
    condition = 1
    for x in range(0,i):
        if palabra[x]!=palabra[len(palabra)-1-x]:
            condition = 0
    if condition ==1:
        return ("Es palindromo")
    else:
        return ("No es palindromo")
@app.route('/multiplo/<numero1>/<numero2>')
def esmultiplo(numero1,numero2):
    num1 = int(numero1)
    num2 = int(numero2)
    if num1 % num2 ==0:
        final = numero1 + " es multiplo de " + numero2
        return (final)
    else:
        final = numero1 +" no es multiplo de " + numero2
        return (final)

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)

@app.route('/create_user/<nombre>/<apellido>/<passwd>/<nick>')
def create_user(nombre,apellido,passwd,nick):
    #crear un objeto (instancia de una clase)
    user = entities.User(
        name = nombre,
        fullname = apellido,
        password = passwd,
        username = nick
    )

    #Guardar el objeto en la capa decreate_user persistencia
    db_session = db.getSession(engine)
    db_session.add(user)
    db_session.commit()
    return "User created!"

@app.route('/read_user')
def read_users():
    db_session = db.getSession(engine)
    respuesta = db_session.query(entities.User)
    users = respuesta[:]
    i = 0
    final = ""
    for user in users:
        if (i==0):
            final = final + str(i) + " Nombre: " + user.name + " Apellido: " + user.fullname + " Pass: " + user.password + " Username: " + user.username
        else:
            final = final + "<br/>" +str(i) + " Nombre: " + user.name + " Apellido: " + user.fullname + " Pass: " + user.password + " Username: " + user.username
        i+=1
    return final


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
