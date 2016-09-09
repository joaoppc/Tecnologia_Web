# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Pessoas(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(120), unique=True)
	pessoas_ = db.relationship('Respostas', backref='pessoas',lazy='dynamic')
 	#tipo = db.Column(d
	def __init__(self, username, email):
    	   self.username = username
    	   self.email = email

class Perguntas(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	pergunta = db.Column(db.String(2000), unique=True)
	resp1=db.Column(db.String(2000))
	resp2=db.Column(db.String(2000))
	resp3=db.Column(db.String(2000))
	resp4=db.Column(db.String(2000))
	resp5=db.Column(db.String(2000))
	resp_certa=db.Column(db.Integer)
	perguntas_ = db.relationship('Respostas', backref='perguntas',lazy='dynamic')

	def __init__(self, username, email,resp1,resp2,resp3,resp4,resp5,resp_certa):
    	   self.pergunta=pergunta
    	   self.resp1=resp1
    	   self.resp2=resp2
    	   self.resp3=resp3
    	   self.resp4=resp4
    	   self.resp5=resp5
    	   self.resp_certa=resp_certa

class Respostas(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	pessoas_id = db.Column(db.Integer, db.ForeignKey('Pessoas.id'))
	resp_user=db.Column(db.Integer)
	pergunta_id=db.Column(db.Integer,db.ForeignKey('pergunta.id'))
	def __init__(self, pessoas_id):
		self.resp_user=resp_user
		self.pergunta_id=pergunta_id
		self.pessoas_id=pessoas_id
    	  


db.create_all()
 
if __name__ == "__main__":
	app.run()