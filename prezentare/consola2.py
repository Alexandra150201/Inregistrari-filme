'''
Created on 18 nov. 2020

@author: user
'''
from erori.exceptii import ValidError, RepoError
import random
class UI(object):
    
    def __ui_R1_nume(self):
        clienti=[]
        clienti=self.__serviciu.R1_nume()
        if len(clienti)==0:
            print("nu exista inchirieri\n")
        
        else:
            for client in clienti:
                print(client)
    
    
    def __ui_R1_numar(self):
        clienti=[]
        clienti=self.__serviciu.R1_numar()
        if len(clienti)==0:
            print("nu exista inchirieri\n")
        
        else:
            for client in clienti:
                print(client)
    
    
    def __ui_R2(self):
        filme=[]
        filme=self.__serviciu.R2()
        if len(filme)==0:
            print("nu exista inchirieri\n")
        
        else:
            for film in filme:
                print(film)
    
    
    def __ui_R3(self):
        clienti=[]
        clienti=self.__serviciu.R3()
        if len(clienti)==0:
            print("prea putine inchirieri\n")
        
        else:
            for client in clienti:
                print(client[0],client[1])
    
    
    
    
    def __ui_R4(self):
        print("introduceti intervalul (a,b) intre care doriti sa afisati clientii cu acest numar de inchirieri incadrat")
        a=int(input("a="))
        b=int(input("b="))
        clienti=[]
        clienti=self.__serviciu.R4(a,b)
        if len(clienti)==0:
            print("nu exista clienti cu acest numar de inchirieri\n")
        
        else:
            for client in clienti:
                print(client)
    
        
    
    
    def __init__(self, srv,serv,servi,serviciu):
        self.__srv = srv
        self.__serv = serv
        self.__servi = servi
        self.__serviciu = serviciu
        self.__comenzi={"adauga film":self.__ui_adaugafilm,
                        "print filme":self.__ui_printfilme,
                        "cauta film":self.__ui_cautafilm,
                        "sterge film":self.__ui_stergefilm,
                        "modifica film":self.__ui_modificafilm,
                        "adauga client":self.__ui_adaugaclient,
                        "print clienti":self.__ui_printclienti,
                        "cauta client":self.__ui_cautaclient,
                        "sterge client":self.__ui_stergeclient,
                        "modifica client":self.__ui_modificaclient,
                        "inchiriaza":self.__ui_inchiriaza,
                        "returneaza":self.__ui_returneaza,
                        "print inchirieri":self.__ui_printinchirieri,
                        "R1 nume":self.__ui_R1_nume,
                        "R1 numar":self.__ui_R1_numar,
                        "R2":self.__ui_R2,
                        "R3":self.__ui_R3,
                        "R4":self.__ui_R4}
        
    def __ui_adaugafilm(self):
        id_film=int(input("introduceti idul filmului: "))
        titlu=input("introduceti titlul filmului: ")
        descriere=input("introduceti descrierea: ")
        genul=input("introduceti genul filmului: ")
        self.__srv.adauga_film(id_film,titlu,descriere,genul)
    
    
    def __ui_printfilme(self):
        filme=self.__srv.get_filme()
        if(len(filme)==0):
            print("nu exista filme")
            return 
        for film in filme:
            print(film)
    
    def __ui_cautafilm(self):
        id_film=int(input("introduceti idul filmului: "))
        film=self.__srv.cauta(id_film)
        print(film)
    
    
    def __ui_stergefilm(self):
        id_film=int(input("introduceti idul filmului: "))
        self.__srv.sterge_film(id_film)
        self.__servi.returnare_id_f(id_film)
        
    
    def __ui_modificafilm(self):
        id_film=int(input("introduceti idul filmului: "))
        titlu=input("introduceti titlul filmului: ")
        descriere=input("introduceti descrierea: ")
        genul=input("introduceti genul filmului: ")
        self.__srv.modifica_film(id_film, titlu, descriere, genul)
        film=self.__srv.cauta(id_film)
        self.__servi.modifica_dupa_film(film)
    
    def __ui_adaugaclient(self):
        id_client=int(input("introduceti idul clientuli: "))
        nume=input("introduceti numele clientului: ")
        cnp=int(input("introduceti cnpul: "))
        self.__serv.adauga_client(id_client,nume,cnp)
     
    def __ui_printclienti(self):
        clienti=self.__serv.get_clienti()
        if(len(clienti)==0):
            print("nu exista clienti")
            return 
        for client in clienti:
            print(client) 
              
    def __ui_cautaclient(self):
        id_client=int(input("introduceti idul clientului: "))
        client=self.__serv.cauta(id_client)
        print(client)
    
    
    def __ui_stergeclient(self):
        id_client=int(input("introduceti idul clientului: "))
        self.__serv.sterge_client(id_client)
        self.__servi.returnare_id_c(id_client)
        
    
    def __ui_modificaclient(self):
        id_client=int(input("introduceti idul clientului: "))
        nume=input("introduceti numele clientului: ")
        cnp=int(input("introduceti cnpul: "))
        self.__serv.modifica_client(id_client,nume,cnp)
        client=self.__serv.cauta(id_client)
        self.__servi.modifica_dupa_client(client)
    
    def __ui_inchiriaza(self):
        id=int(input("introduceti idul inchirierii: "))
        id_film=int(input("introduceti idul filmului: "))
        id_client=int(input("introduceti idul clientlui: "))
        self.__servi.inchiriere(id,id_film,id_client)
    
    
    def __ui_returneaza(self):
        id=int(input("introduceti idul inchirierii: "))
        self.__servi.returnare(id)
        
    def __ui_printinchirieri(self):
        inchirieri=self.__servi.get_inchirieri()
        if(len(inchirieri)==0):
            print("nu exista inchirieri")
            return 
        for inchiriat in inchirieri:
            print(inchiriat)
    
    
    def run(self):
        print("Alegeti una dintre optiunile urmatoare:")
        print("<adauga film> pentru a adauga un film\n<print filme> pentru a afisa lista filmelor\n<cauta film> pentru a cauta un film dupa id\n<sterge film> pentru a sterge un film din lista\n<modifica film> pentru a modifica un film din lista\n")
        print("<adauga client> pentru a adauga un client\n<print clienti> pentru a afisa lista clientilor\n<cauta client> pentru a cauta un client dupa id\n<sterge client> pentru a sterge un client din lista\n<modifica client> pentru a modifica un client din lista\n<inchiriaza> pentru a inchiria un film\n<returneaza> pentru a returna un film\n<print inchirieri> pentru a afisa lista inchirierilor\n<R1 nume> pentru a afisa lista clientilor ordonati dupa nume\n<R1 numar> pentru a afisa lista clientilor ordonati dupa numarul de filme inchiriate\n<R2> pentru a afisa cele mai inchiriate filme\n<R3> pentru a afisa primii 30% clienti cu cele mai multe filme (nume client si numarul de filme inchiriate)\n<R4> pentru a afisa clientii cu n nr de inchirieri intr un interval citit\n")
        while True:
            try:
                n=int(input("Cate filme sau cati clienti?"))
                m=int(input("Cate inchirieri?"))
                break
            except ValueError:
                pass
        id_filme=[]
        id_clienti=[]
        while n:
            titlu_list=["Marea Neagra","Antarctica","Insulele gornee", "familia perfecta","Visul","Doua lumi identice","Dragoni si strigoi","Ana"]
            gen_list=["horror","documentar","sf","actiune","dragoste","comedie"]
            id_film=random.randrange(1,100)
            if id_film not in id_filme:
                id_filme.append(id_film)
            titlu=random.choice(titlu_list)
            descr_range=random.randrange(20,80)
            descriere=""
            for i in range(descr_range):
                litera=chr(random.randrange(97,122))
                descriere=descriere+litera
            genul=random.choice(gen_list)   
            try:
                self.__srv.adauga_film(id_film,titlu,descriere,genul)
                
            except RepoError:
                pass
                
            id_client=random.randrange(1,100)
            if id_client not in id_clienti:
                id_clienti.append(id_client)
            nume_list=["Ana","Nadia","Matei","Andrei","Maria","Gabi","Tania","Tudor","Pavel","Sami","Razvan","Ramona","Teodor","Geo"]
            nume=random.choice(nume_list)
            cnp=random.randrange(1000000000000,10000000000000)
            try:
                self.__serv.adauga_client(id_client,nume,cnp)
                
            except RepoError:
                pass
            n=n-1  
            
        while m:
            id=random.randrange(1,100)
            id_film=random.choice(id_filme)
            id_client=random.choice(id_clienti)
            try:
                self.__servi.inchiriere(id,id_film,id_client)
            except RepoError:
                pass
            m=m-1  
        
        while True:
            cmd=input(">>>")
            if cmd=="exit":
                print("iesire aplicatie")
                return 
            if cmd in self.__comenzi:
                try:
                    self.__comenzi[cmd]()
                except ValueError:
                    print("valoare numerica invalida")
                except ValidError as ve:
                    print(ve)
                except RepoError as re:
                    print(re)
            else:
                print("comanda invalida")
            