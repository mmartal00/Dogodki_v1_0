from flask import Flask, app, render_template, json, request, redirect, url_for, session
from flask.helpers import flash
from werkzeug.utils import redirect
from Include.Modelo.usersVO import usersVO
from Include.Modelo.usersDAO import usersDAO
from Include.Modelo.eventosVO import eventosVO
from Include.Modelo.eventosDAO import eventosDAO
# from Include.Modelo.eventos1VO import eventos1VO
# from Include.Modelo.eventos1DAO import eventos1DAO
from werkzeug.security import generate_password_hash, check_password_hash
# app = Flask(__name__, static_url_path='', static_folder='static/')
# app = Flask(__name__, static_url_path='')
# app.static_folder = 'static'
from pprint import pprint
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = 'me gusta_el cafe'
skey = 'fa5d8e166b8444c082e139694ae140b7'
endpoint = 'https://southcentralus.api.cognitive.microsoft.com/'
vision_url = endpoint + "/vision/v3.2/analyze?visualFeatures=Faces"


@app.route("/")
def login():
    return render_template("login.html")

@app.route("/formlogin", methods=['POST', 'GET'])
def formlogin():
    if request.method == 'POST':
        try:
            DAO= usersDAO()  
            data=request.form
            listavo=DAO.selectALL()  
            VO = usersVO(99,data['username'],'','',data['password'],0)
            vo2 = DAO.findUsername(VO)
            #Eventos
            DAO_E= eventosDAO()  
            Datos =DAO_E.selectALL()
            

            if vo2:
                pass_hash=vo2.getPassword()
                # print('lista')
                # print(pass_hash)
                check_password_hash(pass_hash,data['password'])
                session["id"] = vo2.getId()
                session["username"] = vo2.getUsername()
                session["tipo_usuario"] = vo2.getTipoUsuario()
                if 'tipo_usuario' in session:
                    session['tipo_usuario'] = '1'
                    print('jefe')
                    flash("Inició de sesión exitoso")
                    print(Datos)
                    # return render_template('analista.html', User=vo2, users=listavo)
                    return render_template('analista.html', User=session["username"], Datos=Datos, Id= session["id"] )
                else:
                    session['tipo_usuario'] = '2'
                    print('analista')
                    return render_template('analista.html')
            else:
                return render_template("login.html")
        except Exception as e:
            return json.dumps({'error':str(e)})
    else:
        return render_template("login.html")

@app.route("/registrar")
def registrar():
    return render_template("register.html")

@app.route("/formregistrar",methods=["POST"])
def formregistrar():
    try:
        DAO = usersDAO()   
        username = request.form['username']      
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        tipo_usuario = request.form['tipo_usuario']
        hash_pass = generate_password_hash(password)
        # print('campos:')
        # print(username, name, email, hash_pass, tipo_usuario)
        VO = usersVO(id, username, name, email, hash_pass, tipo_usuario)
        DAO.insertALL(VO)
        flash("Se registró correctamente")
        return render_template("login.html")
    except Exception as e:
        return json.dumps({'error':str(e)})


@app.route("/registrareventos")
def registrar_eventos():
    return render_template("registerevento.html", tol_hombres=0, tol_mujeres=0, prom_edad=0)

@app.route("/formregistrareventos",methods=["POST"])
def formregistrareventos():
    try:
        if request.files:
            image = request.files["image"]
            print(image)

            documents ={
                "url": "https://www.nombres.pro/wp-content/uploads/2015/10/Nombre-para-grupos-de-amigos.jpg"
            }
            _headers = {"Ocp-Apim-Subscription-Key": skey}
            _response=requests.post(vision_url, headers=_headers, json=documents)
            rostros = _response.json()

            print(rostros)    


        print("registra eventos init")
        DAO = eventosDAO()
        numberh = request.form['numberh']         
        numberm = request.form['numberm']
        age = request.form['age']
        event = request.form['event']
        user = session["id"]
        # nombre_event = request.form['nombre_evento']   
        
        VO = eventosVO(id, numberh, numberm, age, event, user )
        DAO.insertALL(VO)
        flash("Se registró correctamente")
        if 'tipo_usuario' in session:
            session['tipo_usuario'] = '1'
            print('jefe')
            flash("Inició de sesión exitoso")

            DAO_E= eventosDAO()  
            Datos =DAO_E.selectALL()
            return render_template('analista.html', Datos = Datos , User=session["username"],  Id= session["id"] )
        else:
            session['tipo_usuario'] = '2'
            print('analista')
            return render_template('analista.html')
    except Exception as e:
        return json.dumps({'error':str(e)})


@app.route("/formregistrareventos_info",methods=["POST"])
def formregistrareventos_info():
    try:
        if request.files:
            image = request.files["image"]
            #Guardar imagen dentro de carpeta
            #Recuperar url de la imagen
            print(image)

            documents ={
                #regresar url
                "url": "{ image }"
            }
            _headers = {"Ocp-Apim-Subscription-Key": skey}
            _response=requests.post(vision_url, headers=_headers, json=documents)
            rostros = _response.json()

            print(rostros)
            tot_hombres = 0
            tot_mujeres = 0

            tot_edad = 0

            for rostro in rostros['faces']:
                rostro['gender']
                rostro['age']

                if (rostro['gender'] == 'Male'):
                    tot_hombres += 1
                else:
                    tot_mujeres += 1

            print(tot_hombres)
            print(tot_mujeres)

            for rostro in rostros['faces']:
                tot_edad = tot_edad + rostro['age']

            prom_edad = tot_edad / len(rostros['faces'])

            print(int(prom_edad))
            return render_template("registerevento.html", tol_hombres=tot_hombres, tol_mujeres=tot_mujeres, prom_edad= int(prom_edad))




        print("registra eventos init")
        DAO = eventosDAO()
        numberh = request.form['numberh']         
        numberm = request.form['numberm']
        age = request.form['age']
        event = request.form['event']
        user = session["id"]
        # nombre_event = request.form['nombre_evento']   
        
        VO = eventosVO(id, numberh, numberm, age, event, user )
        DAO.insertALL(VO)
        flash("Se registró correctamente")
        if 'tipo_usuario' in session:
            session['tipo_usuario'] = '1'
            print('jefe')
            flash("Inició de sesión exitoso")

            DAO_E= eventosDAO()  
            Datos =DAO_E.selectALL()
            return render_template('analista.html', Datos = Datos , User=session["username"],  Id= session["id"] )
        else:
            session['tipo_usuario'] = '2'
            print('analista')
            return render_template('analista.html')
    except Exception as e:
        return json.dumps({'error':str(e)})



# @app.route("/registroevento")
# def registroevento():
#     return render_template("formevento.html")

# @app.route("/formevento",methods=["POST"])
# def formevento():
#     try:
#         DAO = eventosDAO()
#         formvo=DAO.selectALL()
#         print(formvo)
#         numberh = request.form['numberh']         
#         numberm = request.form['numberm']
#         age = request.form['age']
#         event = request.form['event']
#         id_evento = ''
#         print('campos:')
#         print(numberh, numberm, age, event, id_evento)
#         VO = eventosVO(id, numberh, numberm, age, event, id_evento)
#         DAO.insertALL(VO)
#         flash("Se guardaron los datos del evento")
#         vo3 = DAO.selectId_evento(VO)
#         print(vo3)
#         return render_template("analista.html", dato=vo3, Datos=formvo)
#     except Exception as e:
#         return json.dumps({'error':str(e)})

# @app.route("/crearevento")
# def crearevento():
#     return render_template("crearevento.html")

# @app.route("/formevento1",methods=["POST"])
# def formevento1():
#     try:
#         DAO = eventos1DAO()   
#         evento = request.form['evento']  
#         form1vo=DAO.selectALL()
#         # print('campos:')
#         # print(evento)
#         VO = eventos1VO(id, evento)
#         DAO.insertALL(VO)
#         flash("Se creó un evento con éxito")
#         vo4 = DAO.selectEvento(VO)
#         return render_template("analista.html", evento=vo4, Eventos=form1vo)
#     except Exception as e:
#         return json.dumps({'error':str(e)})

@app.route("/borrarevento", methods=["POST"])
def borrarevento():
    # evento = request.form['id']
    return redirect("/analista")

@app.route("/editardatos")
def editardatos():
        return render_template('formevento.html')  

@app.route("/borrardatos")
def borrardatos():
        return redirect('analista')

@app.route("/jefe")
def jefe():
        return render_template('jefe.html')  

@app.route("/analista")
def analista():
        return render_template('analista.html')  

@app.route("/recuperar")
def recuperar():
        return render_template('password.html')  

@app.route("/tabla")
def tabla():
    return render_template('tables.html')

@app.route("/error")
def error():
    return render_template('404.html')

@app.route("/salir")
def salir():
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))



if __name__ == "__main__":
    app.run()