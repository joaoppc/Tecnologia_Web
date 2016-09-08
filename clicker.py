# -*- coding: utf-8 -*-

from flask import Flask
from flask import url_for, redirect, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Pergunta(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	pergunta = db.Column(db.String(80), unique=True)
	resposta = db.Column(db.String(120), unique=True)
 
	def __init__(self, pergunta, resposta):
    	   self.pergunta = pergunta
    	   self.resposta = resposta

@app.route("/")
def root():
    return """<!DOCTYPE html>
				<html>

				<head>
					<h1>Bem vindo ao Insper Clicker</h1>
				</head>

				<body>
					<a href="""+ url_for('moderador')+""">Moderador</a>
					<a href="http://www.w3schools.com/html/">Usuario</a>
				</body>

				</html>"""
@app.route("/moderador",methods=['GET','POST'])
def moderador():
	if request.method == 'GET':
		return render_template('moderator2.html')
	elif request.method =='POST':
		pergunta1 = request.form['pergunta']
		resposta1 = request.form['resposta']
		clicker = Pergunta(pergunta=pergunta1 ,resposta=resposta1)
		db.session.add(clicker)

		return render_template('moderadorcriado.html')
	else:
		return "<h2> Requisição Inválida</h2>"


    
db.create_all()

if __name__ == "__main__":
    app.run()
