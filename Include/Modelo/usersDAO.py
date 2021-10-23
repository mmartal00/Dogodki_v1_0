from flask import json
from werkzeug.datastructures import UpdateDictMixin
import Include.conexion as cnx 
from Include.Modelo.usersVO import usersVO

class usersDAO:
    def __init__(self):
        self.__tabla = "usuarios"

    def selectALL(self):
        try:
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            query_select=('SELECT id, username, name, email, password, tipo_usuario FROM '+self.__tabla+'') 
            cursor.execute(query_select)
            data=cursor.fetchall()
            listaVO=[]
            for fila in data:
                vo2 = usersVO(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
                listaVO.append(vo2)
            return listaVO
        except Exception as e:
            return json.dumps({'error':str(e)})
        finally: 
            cursor.close()
            conn.close()

    def findUsername(self, vo):
        try:
            # print(vo.getUsername())
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            query_select=("SELECT * FROM "+self.__tabla+" WHERE username = %s LIMIT 1") 
            # print(query_select)
            values=(vo.getUsername())
            cursor.execute(query_select, values)
            data=cursor.fetchall()
            # print(data[0][0])
            # listaVO=[]
            vo2 = usersVO(data[0][0], data[0][1], data[0][2], data[0][3], data[0][4], data[0][5])
                # listaVO.append(vo)
            # print(vo2)    
            return vo2
        except Exception as e:
            return json.dumps({'error':str(e)})
        finally: 
            cursor.close()
            conn.close()
            
    def insertALL(self, vo):
        try:
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            consulta=('INSERT INTO '+self.__tabla+' (username, name, email, password, tipo_usuario)' "VALUES(%s,%s,%s,%s,%s)")          
            valores=(
            vo.getUsername(),
            vo.getName(),
            vo.getEmail(),
            vo.getPassword(),
            vo.getTipoUsuario()
            )
            cursor.execute(consulta, valores)
            conn.commit()
            print("inserto usr")
            return{
                'message': "insert succesful"
            }
        except Exception as e:
            return json.dumps({'error':str(e)})  
        finally: 
            cursor.close()
            conn.close()    

        # UPDATE

        # DELETE