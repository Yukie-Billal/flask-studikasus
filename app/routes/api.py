from .. import app

@app.route('/api/v1', methods=['GET'])
def index_api() :
	return 'Home API'