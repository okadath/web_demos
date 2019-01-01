
**Iniciar server**

	export FLASK_APP=my_server.py
	export FLASK_ENV=development
	flask run

usaremos jupyter para el analisis de datos, es mas facil desplegar graficos, aunque es un fastidio 

desde el servidor en flask inyectamos las variables para el js:
	
	@app.route("/", methods=['POST', 'GET'])
	def index():
	    return render_template('index.html',var_js = var_python,...)