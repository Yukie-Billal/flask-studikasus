from flask import render_template
from app.models.user import User as user_model
from app import db

def index() :
	# user = db.session.execute(db.select(user_model).order_by(user_model.nama)).scalars()
	user = user_model.query.all()
	return render_template('app.html', users=user)

def add(data) :
	nama = data['nama']
	email = data['email']
	print(nama, email)
	db.session.add(user_model(nama=nama, email=email))
	db.session.commit()

def edit(data) :
	id = data['id']
	nama = data['nama']
	email = data['email']
	print(nama, email, id)
	# user = db.get_or_404(user_model, id)
	user = user_model.query.filter_by(id=id).first()
	user.nama = nama
	user.email = email
	db.session.commit()
	return 'success'

def delete(id) :
	user = user_model.query.filter_by(id=id).first()
	db.session.delete(user)
	db.session.commit()