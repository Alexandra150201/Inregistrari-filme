from domeniu.entitati import Filme,Clienti
from validare.validatori import Validator_film,Validator_client,Validator_inchiriere
from erori.exceptii import ValidError,RepoError
from infrastructura.repo import Repository_filme,Repository_clienti,\
    Repository_inchirieri
from infrastructura.repoFiles import FilmRepositoryFile,ClientRepositoryFile,InchirieriRepositoryFile
from business.servicii import ServiceFilme,ServiceClienti, ServiciiRapoarte,\
    ServiceInchirieri
from Utile import goleste_fisier
class Teste(object):
    
    
    def __ruleaza_teste_domeniu(self):
        id_film=1234
        titlu="marea neagra"
        descriere="un film documentar despre lumea acvatica din marea neagra"
        gen="documentar"
        film=Filme(id_film,titlu,descriere,gen)
        assert(film.get_id_film()==id_film)
        assert(film.get_titlu()==titlu)
        assert(film.get_descriere()==descriere)
        assert(film.get_gen()==gen)
        assert(str(film)=="1234,marea neagra,un film documentar despre lumea acvatica din marea neagra,documentar")
        alt_film=Filme(id_film,"cocos","gfghh","hyguy")
        assert(alt_film==film)
        
        id_client=123
        nume="Andrei"
        cnp=5072256211111
        client=Clienti(id_client,nume,cnp)
        assert(client.get_id_client()==id_client)
        assert(client.get_nume()==nume)
        assert(client.get_cnp()==cnp)
        assert(str(client)=="123,Andrei,5072256211111")
        alt_client=Clienti(id_client,"Ana",6042256211111)
        assert(alt_client==client)

    def __ruleaza_teste_validare(self):
        valid=Validator_film()
        film_invalid=Filme(-22,"","","")
        try:
            valid.valideaza(film_invalid)
            assert(False)
        except ValidError as ve:
            assert(str(ve)=="id invalid\ntitlu invalid\ndescriere invalida\ngen invalid\n")
        
        val=Validator_client()
        client_invalid=Clienti(-22,"",2345)
        try:
            val.valideaza(client_invalid)
            assert(False)
        except ValidError as ve:
            assert(str(ve)=="id invalid\nnume invalid\ncnp invalid\n")
    

    def __ruleaza_teste_repo(self):
        repo=Repository_filme()
        assert(len(repo)==0)
        id_film=1234
        titlu="marea neagra"
        descriere="un film documentar despre lumea acvatica din marea neagra"
        gen="documentar"
        film=Filme(id_film,titlu,descriere,gen)
        repo.adauga(film)
        assert(len(repo)==1)
        gasit=repo.cauta_dupa_id(id_film)
        assert(gasit.get_titlu()==titlu)
        assert(gasit.get_descriere()==descriere)
        assert(gasit.get_gen()==gen)
        try:
            repo.adauga(film)
            assert(False)
        except RepoError as re:
            assert(str(re)=="element existent\n")
        try:
            repo.cauta_dupa_id(id_film+4)
            assert(False)
        except RepoError as re:
            assert(str(re)=="element inexistent\n")
        film_nou=Filme(id_film,"Fanta","hg","horror")
        repo.modifica(film_nou)
        gasit=repo.cauta_dupa_id(id_film)
        assert(gasit.get_titlu()=="Fanta")
        assert(gasit.get_descriere()=="hg")
        assert(gasit.get_gen()=="horror")
        film_rau=Filme(id_film+3,"Fanta","hg","horror")
        try:
            repo.modifica(film_rau)
            assert(False)
        except RepoError as re:
            assert(str(re)=="element inexistent\n")
        alls=repo.get_all()
        assert(len(alls)==1)
        assert(alls[0].get_titlu()=="Fanta")
        assert(alls[0].get_descriere()=="hg")
        assert(alls[0].get_gen()=="horror")
        repo.sterge_dupa_id(id_film)
        assert(len(repo)==0)
        try:
            repo.sterge_dupa_id(id_film)
            assert(False)
        except RepoError as re:
            assert(str(re)=="element inexistent\n")
            
        rep=Repository_clienti()
        assert(len(rep)==0)
        id_client=123
        nume="Andrei"
        cnp=5072256211111
        client=Clienti(id_client,nume,cnp)
        rep.adauga(client)
        assert(len(rep)==1)
        gas=rep.cauta_dupa_id(id_client)
        assert(gas.get_nume()==nume)
        assert(gas.get_cnp()==cnp)
        try:
            rep.adauga(client)
            assert(False)
        except RepoError as re:
            assert(str(re)=="element existent\n")
        try:
            rep.cauta_dupa_id(id_client+4)
            assert(False)
        except RepoError as re:
            assert(str(re)=="element inexistent\n")
        client_nou=Clienti(id_client,"Suzu",5072256211145)
        rep.modifica(client_nou)
        gas=rep.cauta_dupa_id(id_client)
        assert(gas.get_nume()=="Suzu")
        assert(gas.get_cnp()==5072256211145)
        client_rau=Clienti(id_client+3,"Suzu",5072256211145)
        try:
            rep.modifica(client_rau)
            assert(False)
        except RepoError as re:
            assert(str(re)=="element inexistent\n")
        alls=rep.get_all()
        assert(len(alls)==1)
        assert(alls[0].get_nume()=="Suzu")
        assert(alls[0].get_cnp()==5072256211145)
        rep.sterge_dupa_id(id_client)
        assert(len(rep)==0)
        try:
            rep.sterge_dupa_id(id_client)
            assert(False)
        except RepoError as re:
            assert(str(re)=="element inexistent\n")

    def __ruleaza_teste_service(self):
        
        goleste_fisier(r"C:\Users\user\OneDrive\Desktop\fundamentele programarii\python\teme\tema04\testFilme.txt")
        goleste_fisier(r"C:\Users\user\OneDrive\Desktop\fundamentele programarii\python\teme\tema04\testClienti.txt")
        goleste_fisier(r"C:\Users\user\OneDrive\Desktop\fundamentele programarii\python\teme\tema04\testInchirieri.txt")
        valid=Validator_film()
        repo=FilmRepositoryFile(r"C:\Users\user\OneDrive\Desktop\fundamentele programarii\python\teme\tema04\testFilme.txt")
        repos=InchirieriRepositoryFile(r"C:\Users\user\OneDrive\Desktop\fundamentele programarii\python\teme\tema04\testInchirieri.txt")
        val=Validator_client()
        rep=ClientRepositoryFile(r"C:\Users\user\OneDrive\Desktop\fundamentele programarii\python\teme\tema04\testClienti.txt")
        srv=ServiceClienti(val,rep)
        sv=ServiceFilme(valid,repo)
        vali=Validator_inchiriere()
        serv=ServiceInchirieri(vali,repos,repo,rep)    
        id_film=1233
        titlu="marea gri"
        descriere="un film documentar despre lumea acvatica din marea gri"
        gen="documentar"
        sv.adauga_film(id_film,titlu,descriere,gen)
        filme=sv.get_filme()
        assert(len(filme)==1)
        try:
            sv.adauga_film(id_film,titlu,descriere,gen)
            assert(False)
        except RepoError as re:
            assert(str(re)=="element existent\n")
        try:
            sv.adauga_film(-id_film,titlu,descriere,gen)
            assert(False)
        except ValidError as ve:
            assert(str(ve)=="id invalid\n")
        
        
        id_client=126
        nume="Paula"
        cnp=6072256211145
        srv.adauga_client(id_client,nume,cnp)
        clienti=srv.get_clienti()
        assert(len(clienti)==1)
        try:
            srv.adauga_client(id_client,nume,cnp)
            assert(False)
        except RepoError as re:
            assert(str(re)=="element existent\n")
        try:
            srv.adauga_client(-id_client,nume,cnp)
            assert(False)
        except ValidError as ve:
            assert(str(ve)=="id invalid\n")
            
    
        
        srv.adauga_client(24,"mana",6004567899000)
        srv.adauga_client(4,"dudu",5004567899000)
        clienti=srv.get_clienti()
        assert(len(clienti)==3)
        sv.adauga_film(7,"popo","dfg","sdfg")
        sv.adauga_film(11,"ahhh","dfghj","sdfgh")
        filme=sv.get_filme()
        assert(len(filme)==3)
        serv.inchiriere(1,7,24)
        serv.inchiriere(2,7,4)
        serv.inchiriere(3,11,126)
        serv.inchiriere(4,11,4)
        serv.inchiriere(5,1233,126)
        inchirieri=serv.get_inchirieri()
        assert(len(inchirieri)==5)
        serviciu=ServiciiRapoarte(repos)
        lista=serviciu.R4(2,3)
        assert(len(lista)==2)
    
    
    def __ruleaza_teste_fisier(self):
        
        fileName = r"C:\Users\user\OneDrive\Desktop\fundamentele programarii\python\teme\tema04\testClienti.txt"
        goleste_fisier(fileName)
        repo = ClientRepositoryFile(fileName)
        assert len(repo._elems)==0
        repo.store(Clienti(1,"Ion",1234567890123))
        assert len(repo._elems)==1
        try:
            repo.store(Clienti(1,"Ion",1234567890123))
        except RepoError:
            pass
        assert len(repo._elems)==1
        repo.store(Clienti(2,"Andrei",4234567833123))
        assert len(repo._elems)==2
    
    def ruleaza_teste(self):
        
        
        self.__ruleaza_teste_domeniu()
        self.__ruleaza_teste_validare()
        self.__ruleaza_teste_repo()
        self.__ruleaza_teste_fisier()
        self.__ruleaza_teste_service()
    
    


