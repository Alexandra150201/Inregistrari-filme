from erori.exceptii import ValidError
class Validator_film(object):
    
    
    def valideaza(self, film):
        """
    Aceasta functie valideaza un film introdus
        """
        erori=""
        if film.get_id_film()<0:
            erori+="id invalid\n"
        if film.get_titlu()=="":
            erori+="titlu invalid\n"
        if film.get_descriere()=="":
            erori+="descriere invalida\n"
        if film.get_gen()=="":
            erori+="gen invalid\n"
        if len(erori)>0:
            raise ValidError(erori)
            
    
    



class Validator_client(object):
    
    
    def valideaza(self, client):
        """
    Aceasta functie valideaza un client introdus
        """
        erori=""
        if client.get_id_client()<0:
            erori+="id invalid\n"
        if client.get_nume()=="":
            erori+="nume invalid\n"
        if client.get_cnp()<1000000000000 or client.get_cnp()>=10000000000000:
            erori+="cnp invalid\n"
        if len(erori)>0:
            raise ValidError(erori)
    
    



class Validator_inchiriere(object):
    
    def valideaza(self, inchiriat):
        """
    Aceasta functie valideaza o inchiere introdusa
        """
        erori=""
        if inchiriat.get_id()<0:
            erori+="id invalid\n"
        
        if len(erori)>0:
            raise ValidError(erori)


