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
    return render_template('index.html')
@app.route("/moderador",methods=['GET','POST'])
def moderador():
	if request.method == 'GET':
		return render_template('moderator2.html')
	elif request.method =='POST':
		pergunta = request.form['pergunta']
		resposta = request.form['resposta']
		clicker = Pergunta(pergunta=pergunta ,resposta=resposta)
		db.session.add(clicker)
		db.session.commit()

		return render_template('moderadorcriado.html')
	else:
		return "<h2> Requisição Inválida</h2>"

@app.route("/usuario",methods=['GET','POST'])
def usuario():
	perguntaview = Pergunta.query.filter_by(pergunta=pergunta).first()

	if request.method == 'GET':
		return render_template('usuario.html',perguntaview = perguntaview)
	if request.method == 'POST':
		respostaesc = request.form['group1']
		return render_template('usuariosubm.html')
    
db.create_all()

if __name__ == "__main__":
    app.run()
