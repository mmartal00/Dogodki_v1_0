from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config["DEBUG"]=True

app.config['MYSQL_DATABASE_USER']='sepherot_marinam'
app.config['MYSQL_DATABASE_PASSWORD']='B}M&JG[wmR[g'
app.config['MYSQL_DATABASE_DB']='sepherot_marinamBD'
app.config['MYSQL_DATABASE_HOST']='nemonico.com.mx'

mysql=MySQL(app)