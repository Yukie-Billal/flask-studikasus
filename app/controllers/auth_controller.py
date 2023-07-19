from flask import render_template
from app.models.user import User as user_model
from app import db

def index() :
	user = db.session.execute(db.select(user_model).order_by(user_model.nama)).scalars()
	user = user_model.query.all()
	return render_template('app.html')

def add(data) :
	nama = data['nama']
	email = data['email']

	db.session.add(user_model(nama=nama, email=email))
	user_model.add(nama,email)
	db.session.commit()
	# Coba dua akun di local git. biar santai push tanpa masalah

def edit(data) :
	id = data['id']
	nama = data['nama']
	email = data['email']
	
	user = user_model.query.filter_by(id=id).first()
	user_model.update(nama,email)
	user_model.save()
	return 'success'

def delete(id) :
	user = user_model.query.filter_by(id=id).first()
	user_model.delete(user)
	user_model.save()