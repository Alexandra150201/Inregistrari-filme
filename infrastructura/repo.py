from erori.exceptii import RepoError
class Repository_filme(object):
    
    
    def __init__(self):
        self._elems=[]
    
    def __len__(self):
        return len(self._elems)

    
    def adauga(self, film):
        """
    Aceasta functie adauga un film primit in lista
        """
        if film in self._elems:
            raise RepoError("element existent\n")
        self._elems.append(film)

    def cauta_dupa_id(self, id_film):
        """
    Aceasta functie retuneaza filmele cu idul primit
        """
        for el in self._elems:
            if el.get_id_film()==id_film:
                return el
        raise RepoError("element inexistent\n")
    

    
    def modifica(self, film_nou):
        """
    Aceasta functie modifica un film cu cel primit
        """
        if film_nou not in self._elems:
            raise RepoError("element inexistent\n")
        for i in range(len(self._elems)):
            if self._elems[i]==film_nou:
                self._elems[i]=film_nou
                return

    
    def get_all(self):
        """
    Aceasta functie returneaza lista filmelor
        """
        return self._elems[:]

    
    def sterge_dupa_id(self, id_film):
        """
    Aceasta functie sterge un film din lista dupa idul primit
        """
        for i in range(len(self._elems)):
            if self._elems[i].get_id_film()==id_film:
                del self._elems[i]
                return
        raise RepoError("element inexistent\n")

    



class Repository_clienti(object):

    
    def __init__(self):
        self._elems=[]
    
    def __len__(self):
        return len(self._elems)

    
    def adauga(self, client):
        """
    Aceasta functie adauga un client primit in lista
        """
        if client in self._elems:
            raise RepoError("element existent\n")
        self._elems.append(client)

    
    def cauta_dupa_id(self, id_client):
        """
    Aceasta functie retuneaza clientii cu idul primit
        """
        for el in self._elems:
            if el.get_id_client()==id_client:
                return el
        raise RepoError("element inexistent\n")

    
    def modifica(self, client_nou):
        """
    Aceasta functie modifica un client cu cel primit
        """
        if client_nou not in self._elems:
            raise RepoError("element inexistent\n")
        for i in range(len(self._elems)):
            if self._elems[i]==client_nou:
                self._elems[i]=client_nou
                self._elems[i].set_nume(client_nou.get_nume())
                
                return

    
    def get_all(self):
        """
    Aceasta functie returneaza lista clientilor
        """
        return self._elems[:]

    
    def sterge_dupa_id(self, id_client):
        """
    Aceasta functie sterge un client din lista dupa idul primit
        """
        for i in range(len(self._elems)):
            if self._elems[i].get_id_client()==id_client:
                del self._elems[i]
                return
        raise RepoError("element inexistent\n")

    
    


class Repository_inchirieri(object):
    
    
    def __init__(self):
        self._elems=[]
    
    def __len__(self):
        return len(self._elems)
    

    def get_all(self):
        """
    Aceasta functie returneaza lista inchirierilor
        """
        return self._elems[:]
    
    def adauga_inchiriere(self, inchiriat):
        """
    Aceasta functie adauga o inchiriere primita in lista
        """
        if inchiriat in self._elems:
            raise RepoError("element existent\n")
        self._elems.append(inchiriat)
        
    def returneaza_dupa_id(self, id_inchiriat):
        """
    Aceasta functie returneaza un film inchiriat
        """
        for i in range(len(self._elems)):
            if self._elems[i].get_id()==id_inchiriat:
                del self._elems[i]
                return
        raise RepoError("element inexistent\n")
    
    def cauta_dupa_id_client(self, id_client):
        """
    Aceasta functie retuneaza idul inchirierii in functie de idul clientului
        """
        for el in self._elems:
            client=el.get_client()
            if client.get_id_client()==id_client:
                return el.get_id()
        raise RepoError("element inexistent\n")
    
    def cauta_dupa_id_film(self, id_film):
        """
    Aceasta functie retuneaza idul inchirierii in functie de idul filmului
        """
        for el in self._elems:
            film=el.get_film()
            if film.get_id_film()==id_film:
                return el.get_id()
        raise RepoError("element inexistent\n")
    
   
    
    



