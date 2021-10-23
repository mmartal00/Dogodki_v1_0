class usersVO:

    def __init__(self, id, username, name, email, password, tipo_usuario):
        self.__id = id
        self.__username = username
        self.__name = name
        self.__email = email        
        self.__password = password        
        self.__tipo_usuario = tipo_usuario

    #METODOS
    def setId(self, n):
        self.__id = n

    def getId(self):
        return self.__id

    def setUsername(self, n):
        self.__username = n

    def getUsername(self):
        return self.__username

    def setName(self, n):
        self.__name = n

    def getName(self):
        return self.__name

    def setEmail(self, n):
        self.__email = n

    def getEmail(self):
        return self.__email          

    def setPassword(self, n):
        self.__password = n

    def getPassword(self):
        return self.__password        

    def setTipoUsuario(self, n):
        self.__tipo_usuario = n

    def getTipoUsuario(self):
        return self.__tipo_usuario