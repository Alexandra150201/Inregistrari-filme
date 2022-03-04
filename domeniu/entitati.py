class Filme(object):
    
    
    def __init__(self, id_film, titlu, descriere, gen):
        self.__id_film = id_film
        self.__titlu = titlu
        self.__descriere = descriere
        self.__gen = gen

    def get_id_film(self):
        return self.__id_film


    def get_titlu(self):
        return self.__titlu


    def get_descriere(self):
        return self.__descriere


    def get_gen(self):
        return self.__gen


    def set_titlu(self, value):
        self.__titlu = value


    def set_descriere(self, value):
        self.__descriere = value


    def set_gen(self, value):
        self.__gen = value
    
    def __str__(self):
        return str(self.__id_film)+","+self.__titlu+","+self.__descriere+","+self.__gen

    def __eq__(self,other):
        return self.__id_film==other.__id_film
    
    



class Clienti(object):
    
    
    def __init__(self, id_client, nume, cnp):
        self.__id_client = id_client
        self.__nume = nume
        self.__cnp = cnp

    def get_id_client(self):
        return self.__id_client


    def get_nume(self):
        return self.__nume


    def get_cnp(self):
        return self.__cnp


    def set_nume(self, value):
        self.__nume = value

    def __str__(self):
        return str(self.__id_client)+","+self.__nume+","+str(self.__cnp)

    def __eq__(self,other):
        return self.__id_client==other.__id_client
    
    



class Inchirieri(object):
    
    
    def __init__(self, id, film, client):
        self.__id = id
        self.__film = film
        self.__client = client

    def set_film(self, value):
        self.__film = value


    def set_client(self, value):
        self.__client = value


    def get_id(self):
        return self.__id


    def get_film(self):
        return self.__film


    def get_client(self):
        return self.__client

    def __str__(self):
        return str(self.__id)+","+str(self.__film)+","+str(self.__client)

    def __eq__(self,other):
        return self.__id==other.__id
    
class ClientDTO(object):
    
    def __init__(self,client):
        self.__client = client

    def get_client(self):
        return self.__client


class FilmDTO(object):
    
    
    def __init__(self, film):
        self.__film = film

    def get_film(self):
        return self.__film

    

class R3DTO(object):
    
    
    def __init__(self, nume, numar_inreg):
        self.__nume = nume
        self.__numar_inreg = numar_inreg

    def get_nume(self):
        return self.__nume

    def get_numar_inreg(self):
        return self.__numar_inreg

    
    
    



