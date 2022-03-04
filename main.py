'''
Created on 7 nov. 2020

@author: user
'''
#from testare.teste import Teste
from validare.validatori import Validator_film,Validator_client,Validator_inchiriere
#from infrastructura.repo import Repository_filme,Repository_clienti,Repository_inchirieri
from infrastructura.repoFiles import ClientRepositoryFile,FilmRepositoryFile,InchirieriRepositoryFile
from business.servicii import ServiceFilme,ServiceClienti,ServiceInchirieri,ServiciiRapoarte
from prezentare.consola import UI
if __name__ == '__main__':
    #teste=Teste()
    #teste.ruleaza_teste()
    valid=Validator_film()
    #repo=Repository_filme()
    repo=FilmRepositoryFile(r"Filme.txt")
    #repos=Repository_inchirieri()
    repos=InchirieriRepositoryFile(r"Inchirieri.txt")
    srv=ServiceFilme(valid,repo)
    val=Validator_client()
    #rep=Repository_clienti()
    rep=ClientRepositoryFile(r"Clienti.txt")
    serv=ServiceClienti(val,rep)
    vali=Validator_inchiriere()
    servi=ServiceInchirieri(vali,repos,repo,rep)
    serviciu=ServiciiRapoarte(repos)
    cons=UI(srv,serv,servi,serviciu)
    cons.run()