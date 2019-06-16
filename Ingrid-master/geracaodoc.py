import os
from Pyautomators import Documentacao

class Metodo():
    
    def __init__(self,app):
        self.app=app

    def criar_doc(self):
        for json in os.listdir('./docs/reports'):
            if(json.find('.json')!=-1):
                Documentacao.tranforma_cucumber(json)
        Documentacao.tranforma_cucumber('teste.pdf','./docs/reports/' + 'json', './docs/')
    
    criar_doc()