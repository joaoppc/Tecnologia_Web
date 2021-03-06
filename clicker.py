# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask import url_for, redirect, request, render_template
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Pergunta(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	pergunta = db.Column(db.String(80), unique=True)
	resposta1 = db.Column(db.String(120), unique=True)
	resposta2 = db.Column(db.String(160), unique=True)
	resposta3 = db.Column(db.String(200), unique=True)
	resposta4 = db.Column(db.String(240), unique=True)
	resposta5 = db.Column(db.String(280), unique=True)
	respostacorreta = db.Column(db.String(280), unique=False)


 
	def __init__(self, pergunta, resposta1,resposta2,resposta3,resposta4,resposta5,respostacorreta):
    	   self.pergunta = pergunta
    	   self.resposta1 = resposta1
    	   self.resposta2 = resposta2
    	   self.resposta3 = resposta3
    	   self.resposta4 = resposta4
    	   self.resposta5 = resposta5
    	   self.respostacorreta = respostacorreta


class Estatistica(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	respesc = db.Column(db.String(80), unique=False)
	

 
	def __init__(self, respesc):
    	   self.respesc = respesc
    	   
@app.route("/")
def root():
    return render_template('index.html')

	

@app.route("/moderador",methods=['GET','POST'])
def moderador():
	if request.method == 'GET':
		return render_template('moderatorfinal.html')
	elif request.method =='POST':
		pergunta = request.form['pergunta']
		resposta1 = request.form['resposta1']
		resposta2 = request.form['resposta2']
		resposta3 = request.form['resposta3']
		resposta4 = request.form['resposta4']
		resposta5 = request.form['resposta5']
		respostacorreta = request.form['respostacorreta']
		clicker = Pergunta(pergunta=pergunta ,resposta1=resposta1,resposta2=resposta2,resposta3=resposta3,resposta4=resposta4,resposta5=resposta5,respostacorreta=respostacorreta)
		db.session.add(clicker)
		db.session.commit()

		return render_template('moderadorcriadofinal.html')
	else:
		return "<h2> Requisição Inválida</h2>"

@app.route("/usuario",methods=['GET','POST'])
def usuario():
	count = 0
	perguntaview = Pergunta.query.all()
	total = len(perguntaview)
	
	if request.method == 'GET':
		return render_template('usuario.html',perguntaview = perguntaview,count=count,total=total)
	if request.method == 'POST':
		for i in range(len(perguntaview)):
			respesc = request.form['group1%s'% perguntaview[i].pergunta]
	
			respostacorreta = perguntaview[i].respostacorreta
			if respesc == respostacorreta:

				count +=1

		clicker2 = Estatistica(respesc=respesc)
		db.session.add(clicker2)
		db.session.commit()	

		return render_template('usuariosubmcorrect.html',count=count,total=total)


@app.route("/estatistica")
def estatistica():
	perguntaview = Pergunta.query.all()
	respostaview = Estatistica.query.all()
	count=0 
	total=0
	for j in range(len(perguntaview)):
		number1 = 0
		number2 = 0
		number3 = 0
		number4 = 0
		number5 = 0
		for i in range(len(respostaview)):
			if respostaview[i].respesc == perguntaview[j].resposta1:
				number1 +=1
			if respostaview[i].respesc == perguntaview[j].resposta2:
				number2 +=1
			if respostaview[i].respesc == perguntaview[j].resposta3:
				number3 +=1
			if respostaview[i].respesc == perguntaview[j].resposta4:
				number4 +=1
			if respostaview[i].respesc == perguntaview[j].resposta5:
				number5 +=1


	total=number1+number2+number3+number4+number5



	return render_template('estatisticafinal.html',perguntaview=perguntaview,number1=number1,number2=number2,number3=number3,number4=number4,number5=number5,total=total)

    
db.create_all()

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
