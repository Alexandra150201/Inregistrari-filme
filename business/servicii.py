from domeniu.entitati import Filme,Clienti,Inchirieri,ClientDTO,FilmDTO,R3DTO
from erori.exceptii import RepoError
from sortari import insertSort, bingoSort
class ServiceFilme(object):
    
    
    def __init__(self, valid, repo):
        self.__valid = valid
        self.__repo = repo

    
    def adauga_film(self, id_film,titlu,descriere,gen):
        """
    Aceasta functie valideaza un film creeat prin datele primite si il adauga in lista, prin atribuirea lui repository
        """
        film=Filme(id_film,titlu,descriere,gen)
        self.__valid.valideaza(film)
        self.__repo.store(film)
    
    def get_filme(self):
        """
    Aceasta functie returneaza lista filmelor
        """
        return self.__repo.returneaza_filme()
    
    def cauta(self,id_film):
        """
    Aceasta functie cauta dupa id si returneaza un film
        """
        return self.__repo.cauta_dupa_id(id_film)
    
    def sterge_film(self,id_film):
        """
    Aceasta functie primeste un id si sterge filmul cu idul respectiv
        """
        self.__repo.sterge_dupa_id(id_film)
    
    def modifica_film(self,id_film, titlu, descriere, gen):
        """
    Aceasta functie creeaza un film cu datele primite si l valideaza dupa care il modifica in lista
        """
        film=Filme(id_film,titlu, descriere, gen)
        self.__valid.valideaza(film)
        self.__repo.modifica(film)
        

class ServiceClienti(object):
    
    
    def __init__(self, val, rep):
        self.__val = val
        self.__rep = rep
    
    def adauga_client(self, id_client, nume,cnp):
        """
    Aceasta functie valideaza un client creat prin datele primite si il adauga in lista, prin atribuirea lui repository
        """
        client=Clienti(id_client, nume,cnp)
        self.__val.valideaza(client)
        self.__rep.store(client)
    
    def get_clienti(self):
        """
    Aceasta functie returneaza lista clientilor
        """
        return self.__rep.returneaza_clienti()
    
    def cauta(self,id_client):
        """
    Aceasta functie cauta dupa id si returneaza un client
        """
        return self.__rep.cauta_dupa_id(id_client)
    
    def sterge_client(self,id_client):
        """
    Aceasta functie primeste un id si sterge clientul cu idul respectiv
        """
        self.__rep.sterge_dupa_id(id_client)
        
    
    def modifica_client(self,id_client, nume,cnp):
        """
    Aceasta functie creeaza un client cu datele primite si l valideaza dupa care il modifica in lista
        """
        client=Clienti(id_client, nume,cnp)
        self.__val.valideaza(client)
        self.__rep.modifica(client)
        
class ServiceInchirieri(object):
    
    def __init__(self, vali, repos,repo,rep):
        self.__vali = vali
        self.__repos = repos
        self.__repo = repo
        self.__rep = rep
        
    
    def inchiriere(self,id,id_film,id_client):
        """
        Aceasta functie valideaza si adauga o inchiriere de film
        """
        film=self.__repo.cauta_dupa_id(id_film)
        client=self.__rep.cauta_dupa_id(id_client)
        inchiriat=Inchirieri(id,film,client)
        self.__vali.valideaza(inchiriat)
        self.__repos.store(inchiriat)
        
    def returnare(self,id):
        """
    Aceasta functie primeste un id si sterge inchirierea cu idul respectiv
        """
        self.__repos.returneaza_dupa_id(id)
        
    def get_inchirieri(self):
        """
    Aceasta functie returneaza lista inchirierilor
        """
        return self.__repos.returneaza_inchirieri()
    
    def cauta_dupa_id_client(self,id):
        """
        Aceasta functie returneaza idul inchirierii
        """
        try:
            return self.__repos.cauta_dupa_id_client(id)
        except RepoError:
            pass
        
    def returnare_id_c(self,id_client):
        """
        Aceasta functie returneaza toate inchirierile dupa idul clientului primit
        """
        while True:
            try:
                id= self.__repos.cauta_dupa_id_client(id_client)
                self.__repos.returneaza_dupa_id(id)
            except RepoError:
                return

    def returnare_id_f(self,id_film):
        """
        Aceasta functie returneaza toate inchirierile dupa idul filmului primit
        """
        while True:
            try:
                id= self.__repos.cauta_dupa_id_film(id_film)
                self.__repos.returneaza_dupa_id(id)
            except RepoError:
                return
            
    def modifica_dupa_client(self,client):
        """
        Aceasta functie modifica toate inchirierile dupa clientul nou primit
        """
        try:
            inchirieri=self.__repos.returneaza_inchirieri()
            for inchiriat in inchirieri:
                if inchiriat.get_client()==client:
                    inchiriat.set_client(client)
            self.__repos._rescrie_fisier()
        except RepoError:
            pass
        
    def modifica_dupa_film(self,film):
        """
        Aceasta functie modifica toate inchirierile dupa filmul nou primit
        """
        try:
            inchirieri=self.__repos.returneaza_inchirieri()
            for inchiriat in inchirieri:
                if inchiriat.get_film()==film:
                    inchiriat.set_film(film)
            self.__repos._rescrie_fisier()
            
        except RepoError:
            pass


def adaugare_lista(nume,lista,l):
    """
    functie recursiva ce adauga clientii cu numele nume si inchirieri in lista lista, in l
    """
    if lista==[]:
        return l
    client=lista[0].get_client()
    if client.get_nume()==nume:
        if client not in l:
            l.append(ClientDTO(client).get_client())
    return adaugare_lista(nume,lista[1:],l)
    

def adauga_lista_2(i, dic, inchirieri,lista_clienti):
    if dic==[]:
        return lista_clienti
    el=dic[0]
    if el[1]==i:
        for elem in inchirieri:
            client=elem.get_client()
            id=client.get_id_client()
            if id==el[0]:
                if client not in lista_clienti:
                    lista_clienti.append(ClientDTO(client).get_client())
    return adauga_lista_2(i, dic[1:], inchirieri, lista_clienti)


class ServiciiRapoarte(object):
    
    
    def __init__(self, repos):
        self.__repos = repos
        
    def R1_nume(self):
        """
        Aceasta functie returneaza o lista cu clienti cu filme inchiriate ordonata dupa nume
        """
        lista_nume=[]
        lista_clienti=[]
        inchirieri=self.__repos.returneaza_inchirieri()
        for el in inchirieri:
            client=el.get_client()
            nume=client.get_nume()
            if nume not in lista_nume:
                lista_nume.append(nume)
        lista=insertSort(lista_clienti)
        lista_nume_sortata=[]
        lista_nume_sortata=insertSort(lista_nume)
        #lista_nume_sortata=sorted(lista_nume)
        lista=[]
        for nume in lista_nume_sortata:
            lista=adaugare_lista(nume, inchirieri, lista)
            """for el in inchirieri:
                client=el.get_client()
                if client.get_nume()==nume:
                    if client not in lista:
                        lista.append(ClientDTO(client).get_client())"""
        return lista
            
            
        
        
    def R1_numar(self):
        """
        Aceasta functie returneaza o lista cu clienti cu filme inchiriate ordonata dupa numarul de inchirieri
        """
        lista_id=[]
        for el in self.__repos.returneaza_inchirieri():
            client=el.get_client()
            id=client.get_id_client()
            lista_id.append(id)
        lista_id_sortata=[]
        #lista_id_sortata=sorted(lista_id)
        lista_id_sortata=bingoSort(lista_id)
        dic=[]
        nr=1
        maxx=1
        for i in range(0,len(lista_id_sortata)-1):
            if lista_id_sortata[i]==lista_id_sortata[i+1]:
                nr+=1
                if nr>maxx:
                    maxx=nr
            else:
                lista=[lista_id_sortata[i],nr]
                dic.append(lista)
                nr=1
        
        if len(lista_id_sortata)>0:
            lista1=[lista_id_sortata[len(lista_id_sortata)-1],nr]
            dic.append(lista1)
        
        inchirieri=self.__repos.get_all()
        lista_clienti=[]
        for i in range(maxx,0,-1):
            lista_clienti=adauga_lista_2(i,dic,inchirieri,lista_clienti)
            """for el in dic:
                if el[1]==i:
                    for elem in inchirieri:
                        client=elem.get_client()
                        id=client.get_id_client()
                        if id==el[0]:
                            if client not in lista_clienti:
                                lista_clienti.append(ClientDTO(client).get_client())"""
    
        return lista_clienti            
            
    def R2(self):
        """
        Aceasta functie returneaza o lista cu cu primele 5 cele mai inchiriate filme
        """
        lista_id_film=[]
        for el in self.__repos.returneaza_inchirieri():
            film=el.get_film()
            id=film.get_id_film()
            lista_id_film.append(id)
        lista_id_sortata=sorted(lista_id_film)
        dic=[]
        nr=1
        maxx=1
        for i in range(0,len(lista_id_sortata)-1):
            if lista_id_sortata[i]==lista_id_sortata[i+1]:
                nr+=1
                if nr>maxx:
                    maxx=nr
            else:
                lista=[lista_id_sortata[i],nr]
                dic.append(lista)
                nr=1
        
        if len(lista_id_sortata)>0:
            lista1=[lista_id_sortata[len(lista_id_sortata)-1],nr]
            dic.append(lista1)
            
       
        lista_filme=[]
        for i in range(maxx,maxx-5,-1):
            for el in dic:
                if el[1]==i:
                    for elem in self.__repos.get_all():
                        film=elem.get_film()
                        if film.get_id_film()==el[0]:
                            if film not in lista_filme:
                                lista_filme.append(FilmDTO(film).get_film())
       
        return lista_filme
        
    def R3(self):
        """
        Aceasta functie returneaza o lista cu primii 30% clienti cu filme inchiriate ordonata dupa numarul de inchirieri
        """
        lista_id=[]
        for el in self.__repos.returneaza_inchirieri():
            client=el.get_client()
            id=client.get_id_client()
            lista_id.append(id)
        lista_id_sortata=[]
        lista_id_sortata=sorted(lista_id)
        dic=[]
        nr=1
        maxx=1
        for i in range(0,len(lista_id_sortata)-1):
            if lista_id_sortata[i]==lista_id_sortata[i+1]:
                nr+=1
                if nr>maxx:
                    maxx=nr
            else:
                lista=[lista_id_sortata[i],nr]
                dic.append(lista)
                nr=1
        
        if len(lista_id_sortata)>0:
            lista1=[lista_id_sortata[len(lista_id_sortata)-1],nr]
            dic.append(lista1)
        
        p=int(len(dic)*3//10)
        lista_clienti=[]
        clienti=[]
        for i in range(maxx,0,-1):
            for el in dic:
                if el[1]==i:
                    for elem in self.__repos.get_all():
                        client=elem.get_client()
                        if client.get_id_client()==el[0]:
                            if client not in clienti:
                                clienti.append(client)
                                
        for i in range(maxx,0,-1):
            for el in dic:
                if el[1]==i:
                    for client in clienti:
                        if client.get_id_client()==el[0]:
                            nume=client.get_nume()
                            if p>0:
                                lista_clienti.append([R3DTO(nume,el[1]).get_nume(),R3DTO(nume,el[1]).get_numar_inreg()])
                                p-=1                
        return lista_clienti
    
    def R4(self,a,b):
        """
        Aceasta functie primeste 2 numere ce constituie intervalul in care se va returna lista de clienti cu acel numar incadrat de inchirieri
        """
        lista_id=[]
        inchirieri=self.__repos.returneaza_inchirieri()
        for el in inchirieri:
            client=el.get_client()
            id=client.get_id_client()
            lista_id.append(id)
        lista_id_sortata=[]
        lista_id_sortata=sorted(lista_id)
        dic=[]
        nr=1
        for i in range(0,len(lista_id_sortata)-1):
            if lista_id_sortata[i]==lista_id_sortata[i+1]:
                nr+=1
            else:
                lista=[lista_id_sortata[i],nr]
                dic.append(lista)
                nr=1
        
        if len(lista_id_sortata)>0:
            lista1=[lista_id_sortata[len(lista_id_sortata)-1],nr]
            dic.append(lista1)
       
        lista_clienti=[]
        for i in range(a,b+1):
            for el in dic:
                if el[1]==i:
                    for elem in inchirieri:
                        client=elem.get_client()
                        if client.get_id_client()==el[0]:
                            if client not in lista_clienti:
                                lista_clienti.append(ClientDTO(client).get_client())
    
        return lista_clienti 
    
    def R5(self):
        """
        Aceasta functie returneaza o lista cu primii 30% clienti cu filme inchiriate ordonata dupa numarul de inchirieri
        """
        lista_id=[]
        for el in self.__repos.returneaza_inchirieri():
            client=el.get_client()
            id=client.get_id_client()
            lista_id.append(id)
        lista_id_sortata=[]
        lista_id_sortata=sorted(lista_id)
        dic=[]
        nr=1
        maxx=1
        for i in range(0,len(lista_id_sortata)-1):
            if lista_id_sortata[i]==lista_id_sortata[i+1]:
                nr+=1
                if nr>maxx:
                    maxx=nr
            else:
                lista=[lista_id_sortata[i],nr]
                dic.append(lista)
                nr=1
        
        if len(lista_id_sortata)>0:
            lista1=[lista_id_sortata[len(lista_id_sortata)-1],nr]
            dic.append(lista1)
        
        lista_clienti=[]
        clienti=[]
        for i in range(maxx,0,-1):
            for el in dic:
                if el[1]==i:
                    for elem in self.__repos.get_all():
                        client=elem.get_client()
                        if client.get_id_client()==el[0]:
                            if client not in clienti:
                                clienti.append(client)
                                
        for i in range(maxx,0,-1):
            for el in dic:
                if el[1]==i:
                    for client in clienti:
                        if client.get_id_client()==el[0]:
                            nume=client.get_nume()
                            lista_clienti.append([R3DTO(nume,el[1]).get_nume(),R3DTO(nume,el[1]).get_numar_inreg()])
                                       
        lista=insertSort(lista_clienti,key=list[0],key2=list[1])
        return lista
        
    
    



