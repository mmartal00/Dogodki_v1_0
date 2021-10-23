class eventosVO:

    def __init__(self, id, numberh, numberm, age, event, id_usuario):
        self.__id = id
        self.__numberh = numberh
        self.__numberm = numberm
        self.__age = age        
        self.__event = event
        # self.__nombre_evento = nombre_evento  
        self.__id_usuario = id_usuario      

    #METODOS
    def setId(self, n):
        self.__id = n

    def getId(self):
        return self.__id

    def setNumberh(self, n):
        self.__numberh = n

    def getNumberh(self):
        return self.__numberh

    def setNumberm(self, n):
        self.__numberm = n

    def getNumberm(self):
        return self.__numberm

    def setAge(self, n):
        self.__age = n

    def getAge(self):
        return self.__age          

    def setEvent(self, n):
        self.__event = n

    def getEvent(self):
        return self.__event

    def setId_usuario(self, n):
        self.__id_usuario = n

    def getId_usuario(self):
        return self.__id_usuario

    # def setNombre_evento(self, n):
    #     self.__nombre_evento = n

    # def getNombre_evento(self):
    #     return self.__nombre_evento
        