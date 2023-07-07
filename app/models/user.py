from app import db

class User(db.Model) : 
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	nama = db.Column(db.String(40), nullable=False)
	email = db.Column(db.String(30), nullable=False)

	# def __repr__(self) :
	# 	return '<User = {}>'.format(self.name)
	def delete(user:object) -> bool:
		db.session.delete(user)

	def save() :
		db.session.commit()

	def update(self, nama, email) :
		self.nama = nama
		self.email = email
	
	def add(self,nama:str,email:str) :
		db.session.add(self(nama=nama,email=email))