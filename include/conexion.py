from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

##debug es una propiedad de la aplicacion, el sabor es Flask

app.config["DEBUG"] = True
app.config["MYSQL_DATABASE_USER"] = 'sepherot_DemoAdmin'
app.config["MYSQL_DATABASE_PASSWORD"] = 'Pa73UiXbWG'
app.config["MYSQL_DATABASE_DB"] = 'sepherot_DemoDB'
app.config["MYSQL_DATABASE_HOST"] = 'nemonico.com.mx'  


##conexion a la base de datos sql

mysql = MySQL(app)