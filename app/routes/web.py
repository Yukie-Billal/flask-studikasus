from flask import request, redirect
from .. import app
from ..controllers import auth_controller

@app.route('/')
def index() :
	return auth_controller.index()

@app.route('/users', methods=['POST'])
def user_add() :
	if request.method == 'POST':
		auth_controller.add(request.form)
		return redirect('/')

@app.route('/users/edit', methods=['POST'])
def user_edit() :
	user = auth_controller.edit(request.form)
	return redirect('/')

@app.route('/users/delete/<int:id>')
def user_delete(id) :
	auth_controller.delete(id)
	return redirect('/')