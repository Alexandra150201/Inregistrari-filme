from infrastructura.repo import Repository_filme,Repository_clienti,Repository_inchirieri
from domeniu.entitati import Filme,Clienti,Inchirieri


class ClientRepositoryFile(Repository_clienti):
    """
      Responsible with the load/store of clients from/into a text file
      Include different version of:
           reading from the file
           accessing base class attributes (fields/methods)
      
    """
    def __init__(self,fileName):
        Repository_clienti.__init__(self)
        self.__fileName = fileName
        #incarca clienti din fisier
        self.__incarca_din_fisier()
        
    def __creeaza_client(self, line):
        """
        Transforma o linie din fisier intr un client
        Returneaza clientul
        """
        campuri = line.split(",")
        client = Clienti(int(campuri[0]),str(campuri[1]),int(campuri[2]))
        return client



    def __incarca_din_fisier(self):
        """
          incarca clientii din fisier
          procesul e linie dupa linie
        """
        fh = open(self.__fileName)
        for line in fh:
            if line.strip()!="":
                client = self.__creeaza_client(line)
                Repository_clienti.adauga(self, client)
        fh.close()
        

    def __adauga_in_fisier(self,client):
        """
        Adauga o noua linie in fisier reprezentand clientul client
        """
        fh = open(self.__fileName,"a")
        line = str(client)
        fh.write("\n")
        fh.write(line)
        fh.close()
    
    def __rescrie_fisier(self):
        """
        Rescrie fisierul cu lista din memorie actuala la momentul apelarii
        """
        with open(self.__fileName,"w") as fh:
            for client in self._elems:
                self.__adauga_in_fisier(client)
                
    def store(self,client):
        """
    Aceasta functie adauga un client primit in lista
        """
        Repository_clienti.adauga(self, client)
        self.__adauga_in_fisier(client)
        
            
    def returneaza_clienti(self):
        """
        returneaza lista cu clienti din memorie
        """
        self._elems=[]
        self.__incarca_din_fisier()
        return Repository_clienti.get_all(self)
        
    def cauta_dupa_id(self, id_client):
        """
    Aceasta functie retuneaza clientii cu idul primit
        """
        return Repository_clienti.cauta_dupa_id(self, id_client)
    
    
    def sterge_dupa_id(self, id_client):
        """
    Aceasta functie sterge un client din lista dupa idul primit
        """
        self._elems=[]
        self.__incarca_din_fisier()
        Repository_clienti.sterge_dupa_id(self, id_client)
        self.__rescrie_fisier()
        
    def modifica(self,client):
        """
    Aceasta functie modifica un client cu cel primit
        """
        Repository_clienti.modifica(self,client)
        self.__rescrie_fisier()
    
    
    
class FilmRepositoryFile(Repository_filme):
    """
      Responsible with the load/store of movies from/into a text file
      Include different version of:
           reading from the file
           accessing base class attributes (fields/methods)
      
    """
    def __init__(self,fileName):
        Repository_filme.__init__(self)
        self.__fileName = fileName
        #incarca filme din fisier
        self.__incarca_din_fisier2()
        
    def __creeaza_film(self, line):
        """
        Transforma o linie din fisier intr un film
        Returneaza filmul
        """
        campuri = line.split(",")
        film = Filme(int(campuri[0]),str(campuri[1]),str(campuri[2]),str(campuri[3]))
        return film



    def __incarca_din_fisier2(self):
        """
          incarca filmele din fisier
          procesul e linie dupa linie
        """
        with open(self.__fileName,"r") as fh:
            lines=fh.readlines()
            for line in lines:
                if line.strip()!="":
                    film = self.__creeaza_film(line)
                    Repository_filme.adauga(self, film)
        

    def __adauga_in_fisier(self,film):
        """
        Adauga o noua linie in fisier reprezentand filmul film
        """
        fh = open(self.__fileName,"a")
        line = str(film)
        fh.write("\n")
        fh.write(line)
        fh.close()
    
    def __rescrie_fisier(self):
        """
        Rescrie fisierul cu lista din memorie actuala la momentul apelarii
        """
        with open(self.__fileName,"w") as fh:
            for film in self._elems:
                self.__adauga_in_fisier(film)
                
    def store(self,film):
        """
    Aceasta functie adauga un film primit in lista
        """
        Repository_filme.adauga(self, film)
        self.__adauga_in_fisier(film)
        
            
    def returneaza_filme(self):
        """
        returneaza lista cu filme din memorie
        """
        return Repository_filme.get_all(self)
        
    def cauta_dupa_id(self, id_film):
        """
    Aceasta functie retuneaza filmele cu idul primit
        """
        return Repository_filme.cauta_dupa_id(self, id_film)
    
    
    def sterge_dupa_id(self, id_film):
        """
    Aceasta functie sterge un film din lista dupa idul primit
        """
        Repository_filme.sterge_dupa_id(self, id_film)
        self.__rescrie_fisier()
        
    def modifica(self,film):
        """
    Aceasta functie modifica un film cu cel primit
        """
        Repository_filme.modifica(self,film)
        self.__rescrie_fisier()
    
    


class InchirieriRepositoryFile(Repository_inchirieri):
    """
      Responsible with the load/store of registrations from/into a text file
      Include different version of:
           reading from the file
           accessing base class attributes (fields/methods)
      
    """
    def __init__(self,fileName):
        Repository_inchirieri.__init__(self)
        self.__fileName = fileName
        #incarca inregistrarii din fisier
        self.__incarca_din_fisier()
        
    def __creeaza_inchiriere(self, line):
        """
        Transforma o linie din fisier intr o inchiriere
        Returneaza inchirierea
        """
        campuri = line.split(",")
        film = Filme(int(campuri[1]),str(campuri[2]),str(campuri[3]),str(campuri[4]))
        client = Clienti(int(campuri[5]),str(campuri[6]),int(campuri[7]))
        inchiriere = Inchirieri(int(campuri[0]),film,client)
        return inchiriere



    def __incarca_din_fisier(self):
        """
          incarca inchirierile din fisier
          procesul e linie dupa linie
        """
        fh = open(self.__fileName)
        for line in fh:
            if line.strip()!="":
                inchiriere = self.__creeaza_inchiriere(line)
                Repository_inchirieri.adauga_inchiriere(self, inchiriere)
        fh.close()
        

    def __adauga_in_fisier(self,inchiriere):
        """
        Adauga o noua linie in fisier reprezentand inchirierea primita
        """
        fh = open(self.__fileName,"a")
        line = str(inchiriere)
        fh.write("\n")
        fh.write(line)
        fh.close()
    
    def _rescrie_fisier(self):
        """
        Rescrie fisierul cu lista din memorie actuala la momentul apelarii
        """
        with open(self.__fileName,"w") as fh:
            for inchiriere in self._elems:
                self.__adauga_in_fisier(inchiriere)
                
    def store(self,inchiriere):
        """
    Aceasta functie adauga o inchiriere primita in lista
        """
        Repository_inchirieri.adauga_inchiriere(self, inchiriere)
        self.__adauga_in_fisier(inchiriere)
        
            
    def returneaza_inchirieri(self):
        """
        returneaza lista cu inchirierile din memorie
        """
        return Repository_inchirieri.get_all(self)
        
    def cauta_dupa_id_client(self, id_client):
        """
    Aceasta functie retuneaza idul inch dupa idul clientului primit
        """
        return Repository_inchirieri.cauta_dupa_id_client(self, id_client)
    
    def cauta_dupa_id_film(self, id_film):
        """
    Aceasta functie retuneaza idul inch dupa idul filmului primit
        """
        return Repository_inchirieri.cauta_dupa_id_film(self, id_film)
    
    def returneaza_dupa_id(self, id):
        """
    Aceasta functie sterge o inchiriere din lista dupa idul primit
        """
        Repository_inchirieri.returneaza_dupa_id(self, id)
        self._rescrie_fisier()
        
    
    


