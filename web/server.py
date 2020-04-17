from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json
import time

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)
@app.route('/espar/<numero>')
def espar(numero):
    num = int(numero)
    if num%2 ==0:
        return "Es par"
    else:
        return "Es impar"
@app.route('/esprimo/<numero>')
def esprimo(numero):
    num = int(numero)
    condicion  = 0
    if num<0:
        return "El numero no es positivo, prueba con otro"
    if num==1:
        condicion=2
    for i in range(2,num):
        if num%i == 0:
            condicion = 1
    if num==0:
        condicion = 1
    if condicion==1:
        return "El numero no es primo"
    elif condicion ==2:
        return "El numero no es primo ni compuesto"
    else:
        return "El numero es primo"

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)




if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
