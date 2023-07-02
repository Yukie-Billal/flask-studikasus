from .. import app
from ..controllers import auth_controller

@app.route('/')
def index() :
	return auth_controller.index()