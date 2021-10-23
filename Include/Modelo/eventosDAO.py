from flask import json
from werkzeug.datastructures import UpdateDictMixin
import Include.conexion as cnx 
from Include.Modelo.eventosVO import eventosVO

class eventosDAO:
    def __init__(self):
        self.__tabla = "eventos"

    def selectALL(self):
        try:
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            query_select=('SELECT id, numberh, numberm, age, event, id_usuario FROM '+self.__tabla) 
            cursor.execute(query_select)
            data=cursor.fetchall()
            listaVO=[]
            for fila in data:
                vo2 = eventosVO(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
                listaVO.append(vo2)
            return listaVO
        except Exception as e:
            return json.dumps({'error':str(e)})
        finally: 
            cursor.close()
            conn.close()

    
    def findEvent(self, vo):
        try:
            # print(vo.getUsername())
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            query_select=("SELECT * FROM "+self.__tabla+" WHERE event = %s LIMIT 1") 
            # print(query_select)
            values=(vo.getEvent())
            cursor.execute(query_select, values)
            data=cursor.fetchall()
            # print(data[0][0])
            # listaVO=[]
            vo2 = eventosVO(data[0][0], data[0][1], data[0][2], data[0][3], data[0][4], data[0][5])
                # listaVO.append(vo)
            # print(vo2)    
            return vo2
        except Exception as e:
            return json.dumps({'error':str(e)})
        finally: 
            cursor.close()
            conn.close()

    # def findId_evento(self, vo3):
    #     try:
    #         conn=cnx.mysql.connect()
    #         cursor=conn.cursor()
    #         query_select=("SELECT * FROM "+self.__tabla+" WHERE id_evento = %s LIMIT 1") 
    #         print(query_select)
    #         values=() 
    #         cursor.execute(query_select, values)
    #         data=cursor.fetchall()
    #         # formVO=[]
    #         # for fila in data:
    #         vo3 = eventosVO(data[0][0], data[0][1], data[0][2], data[0][3], data[0][4], data[0][5])
    #             # formVO.append(vo)
    #         return vo3
    #     except Exception as e:
    #         return json.dumps({'error':str(e)})
    #     finally:
    #         cursor.close()
    #         conn.close()

    # def selectId_evento(self, event):
    #     try:
    #         print(event)
    #         conn=cnx.mysql.connect()
    #         cursor=conn.cursor()
    #         query_select=('SELECT id, numberh, numberm, age, event, id_evento FROM '+self.__tabla+' WHERE id_evento = %s') 
    #         values=(event) 
    #         cursor.execute(query_select, values)
    #         data=cursor.fetchall()
    #         formVO=[]
    #         for fila in data:
    #             vo = eventosVO(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
    #             formVO.append(vo)
    #         return formVO
    #     except Exception as e:
    #         return json.dumps({'error':str(e)})
    #     finally: 
    #         cursor.close()
    #         conn.close()
            
    def insertALL(self, vo):
        try:
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            consulta=("INSERT INTO "+self.__tabla+" (numberh, numberm, age, event, id_usuario)" "VALUES(%s,%s,%s,%s,%s)")          
            valores=(
            vo.getNumberh(),
            vo.getNumberm(),
            vo.getAge(),
            vo.getEvent(),
            vo.getId_usuario()           
            )
             # vo.getNombre_evento()
            cursor.execute(consulta, valores)
            conn.commit()
            print("inserto evento")
            return{
                'message': "insert succesful"
            }
        except Exception as e:
            return json.dumps({'error':str(e)})  
        finally: 
            cursor.close()
            conn.close()

        # UPDATE
