'''
Created on 27 de ago de 2018

@author: koliveirab
'''

class Metodos():
    
    def __init__(self,app):
        self.app=app
        
        
    def preencher(self):    
        self.app.digitos(("down",6))
        self.app.clica("Novo Aviso","name")
        self.app.digitos("space","tab")
        self.app.escrever_direto(self.data["telaAviso"]["telefonePessoa"])
        self.app.digitos(("tab",7),"down","tab",("down",2))
        self.app.clica("Concluir","name")
        self.app.clica("OK","name")