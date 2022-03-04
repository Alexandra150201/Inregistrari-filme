import unittest
from domeniu.entitati import Filme, Clienti
from validare.validatori import Validator_film, Validator_client,\
    Validator_inchiriere
from erori.exceptii import ValidError, RepoError
from infrastructura.repo import Repository_filme, Repository_clienti
from Utile import goleste_fisier
from infrastructura.repoFiles import FilmRepositoryFile,\
    InchirieriRepositoryFile, ClientRepositoryFile
from business.servicii import ServiceClienti, ServiceFilme, ServiceInchirieri,\
    ServiciiRapoarte
class DomeniuTestCase(unittest.TestCase):
    """
    clasa testcase pentru entitatile din domeniu
    """
    def setUp(self):
        id_film=1234
        titlu="marea neagra"
        descriere="un film documentar despre lumea acvatica din marea neagra"
        gen="documentar"
        self.__film=Filme(id_film,titlu,descriere,gen)
        self.__alt_film=Filme(id_film,"cocos","gfghh","hyguy")
        
        id_client=123
        nume="Andrei"
        cnp=5072256211111
        self.__client=Clienti(id_client,nume,cnp)
        self.__alt_client=Clienti(id_client,"Ana",6042256211111)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testfunctionalitati(self):
        self.assertEqual(self.__film.get_id_film(),1234)
        self.assertEqual(self.__film.get_titlu(),"marea neagra")
        self.assertEqual(self.__film.get_descriere(),"un film documentar despre lumea acvatica din marea neagra")
        self.assertEqual(self.__film.get_gen(),"documentar")
        self.assertEqual(str(self.__film),"1234,marea neagra,un film documentar despre lumea acvatica din marea neagra,documentar")
        self.assertEqual(self.__alt_film,self.__film)
        self.assertEqual( self.__client.get_id_client(),123)
        self.assertEqual( self.__client.get_nume(),"Andrei")
        self.assertEqual( self.__client.get_cnp(),5072256211111)
        self.assertEqual(str( self.__client),"123,Andrei,5072256211111")
        self.assertEqual( self.__alt_client, self.__client)

class ValidateTestCase(unittest.TestCase):
    """
    clasa testcase pentru validari
    """
    def setUp(self):
        self.__valid=Validator_film()
        self.__film_invalid=Filme(-22,"","","")
        self.__val=Validator_client()
        self.__client_invalid=Clienti(-22,"",2345)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testvalidare(self):
        self.assertRaises(ValidError,self.__valid.valideaza,self.__film_invalid)
        self.assertRaises(ValidError,self.__val.valideaza,self.__client_invalid)
        
class RepoTestCase(unittest.TestCase):
    """
    clasa testcase pentru repository in memory
    """
    def setUp(self):
        self.__repo=Repository_filme()
        self.__rep=Repository_clienti()
        self.__film=Filme(1234,"marea neagra","un film documentar despre lumea acvatica din marea neagra","documentar")
        self.__repo.adauga(self.__film)
        self.__gasit=self.__repo.cauta_dupa_id(1234)

        self.__client=Clienti(123,"Andrei",5072256211111)
        self.__rep.adauga(self.__client)
        self.__gas=self.__rep.cauta_dupa_id(123)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testfunctiirep(self):
        self.assertEqual(len(self.__repo),1)
        self.assertEqual(self.__gasit.get_titlu(),"marea neagra")
        self.assertEqual(self.__gasit.get_descriere(),"un film documentar despre lumea acvatica din marea neagra")
        self.assertEqual(self.__gasit.get_gen(),"documentar")
        self.assertRaises(RepoError,self.__repo.adauga,self.__film)
        self.assertRaises(RepoError,self.__repo.cauta_dupa_id,1238)
        self.__film_nou=Filme(1234,"Fanta","hg","horror")
        self.__repo.modifica(self.__film_nou)
        self.__gasit2=self.__repo.cauta_dupa_id(1234)
        self.assertEqual(self.__gasit2.get_titlu(),"Fanta")
        self.assertEqual(self.__gasit2.get_descriere(),"hg")
        self.assertEqual(self.__gasit2.get_gen(),"horror")
        self.__film_rau=Filme(1237,"Fanta","hg","horror")
        self.assertRaises(RepoError,self.__repo.modifica,self.__film_rau)
        self.__alls=self.__repo.get_all()
        self.assertEqual(len(self.__alls),1)
        self.assertEqual(self.__alls[0].get_titlu(),"Fanta")
        self.assertEqual(self.__alls[0].get_descriere(),"hg")
        self.assertEqual(self.__alls[0].get_gen(),"horror")
        self.__repo.sterge_dupa_id(1234)
        self.assertEqual(len(self.__repo),0)
        self.assertRaises(RepoError,self.__repo.sterge_dupa_id,1234)
        
        self.assertEqual(len(self.__rep),1)
        self.assertEqual(self.__gas.get_nume(),"Andrei")
        self.assertEqual(self.__gas.get_cnp(),5072256211111)
        self.assertRaises(RepoError,self.__rep.adauga,self.__client)
        self.assertRaises(RepoError,self.__rep.cauta_dupa_id,127)
        self.__client_nou=Clienti(123,"Suzu",5072256211145)
        self.__rep.modifica(self.__client_nou)
        self.__gas2=self.__rep.cauta_dupa_id(123)
        self.assertEqual(self.__gas2.get_nume(),"Suzu")
        self.assertEqual(self.__gas2.get_cnp(),5072256211145)
        self.__client_rau=Clienti(127,"Suzu",5072256211145)
        self.assertRaises(RepoError,self.__rep.modifica,self.__client_rau)
        self.__alls2=self.__rep.get_all()
        self.assertEqual(len(self.__alls2),1)
        self.assertEqual(self.__alls2[0].get_nume(),"Suzu")
        self.assertEqual(self.__alls2[0].get_cnp(),5072256211145)
        self.__rep.sterge_dupa_id(123)
        self.assertEqual(len(self.__rep),0)
        self.assertRaises(RepoError,self.__rep.sterge_dupa_id,123)

class ServiciuTestCase(unittest.TestCase):
    """
    clasa testcase pentru serviciu
    """
    def setUp(self):
        goleste_fisier(r"C:\Users\user\OneDrive\Desktop\fundamentele programarii\python\teme\tema04\testFilme.txt")
        goleste_fisier(r"C:\Users\user\OneDrive\Desktop\fundamentele programarii\python\teme\tema04\testClienti.txt")
        goleste_fisier(r"C:\Users\user\OneDrive\Desktop\fundamentele programarii\python\teme\tema04\testInchirieri.txt")
        self.__valid=Validator_film()
        self.__repo=FilmRepositoryFile(r"C:\Users\user\OneDrive\Desktop\fundamentele programarii\python\teme\tema04\testFilme.txt")
        self.__repos=InchirieriRepositoryFile(r"C:\Users\user\OneDrive\Desktop\fundamentele programarii\python\teme\tema04\testInchirieri.txt")
        self.__val=Validator_client()
        self.__rep=ClientRepositoryFile(r"C:\Users\user\OneDrive\Desktop\fundamentele programarii\python\teme\tema04\testClienti.txt")
        self.__srv=ServiceClienti(self.__val,self.__rep)
        self.__sv=ServiceFilme(self.__valid,self.__repo)
        self.__vali=Validator_inchiriere()
        self.__serv=ServiceInchirieri(self.__vali,self.__repos,self.__repo,self.__rep)    
        self.__sv.adauga_film(1233,"marea gri","un film documentar despre lumea acvatica din marea gri","documentar")
        self.__filme=self.__sv.get_filme()

        self.__srv.adauga_client(126,"Paula",6072256211145)
        self.__clienti=self.__srv.get_clienti()
        

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testservicii(self):
        self.assertEqual(len(self.__filme),1)
        self.assertRaises(RepoError,self.__sv.adauga_film,1233,"marea gri","un film documentar despre lumea acvatica din marea gri","documentar")
        self.assertRaises(ValidError,self.__sv.adauga_film,-1233,"marea gri","un film documentar despre lumea acvatica din marea gri","documentar")
    
        self.assertEqual(len(self.__clienti),1)
        self.assertRaises(RepoError,self.__srv.adauga_client,126,"Paula",6072256211145)
        self.assertRaises(ValidError,self.__srv.adauga_client,-126,"Paula",6072256211145)
        
    
        self.__srv.adauga_client(24,"mana",6004567899000)
        self.__srv.adauga_client(4,"dudu",5004567899000)
        self.__clienti=self.__srv.get_clienti()
        self.assertEqual(len(self.__clienti),3)
        self.__sv.adauga_film(7,"popo","dfg","sdfg")
        self.__sv.adauga_film(11,"ahhh","dfghj","sdfgh")
        self.__filme=self.__sv.get_filme()
        self.assertEqual(len(self.__filme),3)
        self.__serv.inchiriere(1,7,24)
        self.__serv.inchiriere(2,7,4)
        self.__serv.inchiriere(3,11,126)
        self.__serv.inchiriere(4,11,4)
        self.__serv.inchiriere(5,1233,126)
        self.__inchirieri=self.__serv.get_inchirieri()
        self.assertEqual(len(self.__inchirieri),5)
        self.__serviciu=ServiciiRapoarte(self.__repos)
        self.__lista=self.__serviciu.R4(2,3)
        self.assertEqual(len(self.__lista),2)
        
class RepoFileTestCase(unittest.TestCase):
    """
    clasa testcase pentru repository fisiere
    """
    def setUp(self):
        goleste_fisier(r"C:\Users\user\OneDrive\Desktop\fundamentele programarii\python\teme\tema04\testFilme.txt")
        goleste_fisier(r"C:\Users\user\OneDrive\Desktop\fundamentele programarii\python\teme\tema04\testClienti.txt")
        self.__valid=Validator_film()
        self.__repo=FilmRepositoryFile(r"C:\Users\user\OneDrive\Desktop\fundamentele programarii\python\teme\tema04\testFilme.txt")
        self.__val=Validator_client()
        self.__rep=ClientRepositoryFile(r"C:\Users\user\OneDrive\Desktop\fundamentele programarii\python\teme\tema04\testClienti.txt")
        self.__film=Filme(1234,"marea neagra","un film documentar despre lumea acvatica din marea neagra","documentar")
        self.__repo.adauga(self.__film)
        self.__gasit=self.__repo.cauta_dupa_id(1234)

        self.__client=Clienti(123,"Andrei",5072256211111)
        self.__rep.adauga(self.__client)
        self.__gas=self.__rep.cauta_dupa_id(123)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testfunctiirepFile(self):
        self.assertEqual(len(self.__repo),1)
        self.assertEqual(self.__gasit.get_titlu(),"marea neagra")
        self.assertEqual(self.__gasit.get_descriere(),"un film documentar despre lumea acvatica din marea neagra")
        self.assertEqual(self.__gasit.get_gen(),"documentar")
        self.assertRaises(RepoError,self.__repo.adauga,self.__film)
        self.assertRaises(RepoError,self.__repo.cauta_dupa_id,1238)
        self.__film_nou=Filme(1234,"Fanta","hg","horror")
        self.__repo.modifica(self.__film_nou)
        self.__gasit2=self.__repo.cauta_dupa_id(1234)
        self.assertEqual(self.__gasit2.get_titlu(),"Fanta")
        self.assertEqual(self.__gasit2.get_descriere(),"hg")
        self.assertEqual(self.__gasit2.get_gen(),"horror")
        self.__film_rau=Filme(1237,"Fanta","hg","horror")
        self.assertRaises(RepoError,self.__repo.modifica,self.__film_rau)
        self.__alls=self.__repo.get_all()
        self.assertEqual(len(self.__alls),1)
        self.assertEqual(self.__alls[0].get_titlu(),"Fanta")
        self.assertEqual(self.__alls[0].get_descriere(),"hg")
        self.assertEqual(self.__alls[0].get_gen(),"horror")
        self.__repo.sterge_dupa_id(1234)
        self.assertEqual(len(self.__repo),0)
        self.assertRaises(RepoError,self.__repo.sterge_dupa_id,1234)
        
        self.assertEqual(len(self.__rep),1)
        self.assertEqual(self.__gas.get_nume(),"Andrei")
        self.assertEqual(self.__gas.get_cnp(),5072256211111)
        self.assertRaises(RepoError,self.__rep.adauga,self.__client)
        self.assertRaises(RepoError,self.__rep.cauta_dupa_id,127)
        self.__client_nou=Clienti(123,"Suzu",5072256211145)
        self.__rep.modifica(self.__client_nou)
        self.__gas2=self.__rep.cauta_dupa_id(123)
        self.assertEqual(self.__gas2.get_nume(),"Suzu")
        self.assertEqual(self.__gas2.get_cnp(),5072256211145)
        self.__client_rau=Clienti(127,"Suzu",5072256211145)
        self.assertRaises(RepoError,self.__rep.modifica,self.__client_rau)
        self.__alls2=self.__rep.get_all()
        self.assertEqual(len(self.__alls2),1)
        self.assertEqual(self.__alls2[0].get_nume(),"Suzu")
        self.assertEqual(self.__alls2[0].get_cnp(),5072256211145)
        self.__rep.sterge_dupa_id(123)
        self.assertEqual(len(self.__rep),0)
        self.assertRaises(RepoError,self.__rep.sterge_dupa_id,123)

    if __name__=="__main__":
        unittest.main()
        
        
        
        
        