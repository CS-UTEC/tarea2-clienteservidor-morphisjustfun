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




if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
