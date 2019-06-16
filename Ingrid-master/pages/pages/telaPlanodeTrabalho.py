# -*- coding: utf-8 -*- ]
'''
Created on 5 de nov de 2018

@author: vgama
'''
from time import sleep
class AgendamentoOS(object):

    def __init__(self, context):
        self.context = context
        self.OK = "OK"
        
    def abrirPerspectiva(self):
        sleep(3)         
        self.context.app.clica_imagem(self.context.path+"data/images/janelaIngrid.png", 1, "left", similar=70)
        
        self.context.app.digitos(("down", 2), "right", "enter", ("down", 19),"enter")
        sleep(3)
        aux = 0
        while(self.context.asserts.verifica_tela(self.context.path +"data/images/agendamentoPlanoTrabalho.png", 50) == None and aux < 50):
            aux = aux +1
            pass
           
        
    def selecionarOS(self):
        sleep(2)
    
        self.context.app.clica_coordenada(199, 366)
        sleep(3)
        
        self.context.app.combo_digitos("alt", "down")
        self.context.app.digitos("left", "enter")        
        self.context.app.clica_imagem(self.context.path +"data/images/atualizar.png", 1, "left", similar=40)
        self.context.app.digitos(("tab", 3),("down", 4), "space", "enter")
       
        
        #enquanto esta atualizando, nao executa nenhuma acao
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/atualizando.png", 50) != None):
            pass
        sleep(5)
        self.context.app.clica_coordenada(703,156)                  
        self.context.app.clica_imagem(self.context.path + "data/images/listadeOS.png")
        aux = 0
        #verifica se a equipe esta disponivel para a OS
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/disponivel.png",50) == None and aux <= 10):
            self.context.app.digitos(( "down"))
            aux = aux + 1
            sleep(2)
        
        
    
    def arrastarOS(self):
        self.context.app.arraste_coordenada(11, 173, 618, 469, 'left', 3)
        sleep(5)
        
    def janelaOrdem(self):     
        if(self.context.asserts.verifica_tela(self.context.path + "data/images/agendarOrdem.png",80) == True):
            pass
    
    def preencheAgendamento(self):
        self.context.app.digitos(("tab", 5), "down")
        self.context.app.clica(self.OK , "name",5)
        
        
        #Verifica se o agendamento nao possui cobertura
        if(self.context.asserts.verifica_tela(self.context.path + "data/images/semCoberturaAgendar.png",20)):
            self.context.app.clica(self.OK ,"name",5)
            
            self.context.app.digitos(( "down"))
            aux = 0 
            #verifica se outra equipe esta disponivel
            while(self.context.asserts.verifica_tela(self.context.path + "data/images/disponivel.png",50) == None and aux <= 10):
                self.context.app.digitos(( "down"))
                aux = aux + 1
                sleep(2)
        
        #Verifica se a OS foi agendada com sucesso
        elif(self.context.asserts.verifica_tela(self.context.path + "data/images/agendamentoCriado.png",20)):
            self.context.app.clica(self.OK ,"name",5)
        
        
class AgendamentoPosterior(object):

    def __init__(self, context):
        self.context = context
        
    def agendarOS(self):
        if(self.context.asserts.verifica_tela(self.context.path +"data/images/agendarOrdem.png",50) != None):
            self.context.app.digitos("enter")
            
        self.context.app.digitos(("tab",5),"down")
        self.context.app.clica_imagem(self.context.path+"data/images/botao_ok.png", 1, "left", similar=70)
        sleep(3)
        self.context.asserts.verifica_tela(self.context.path + "data/images/agendamentoCriado.png")
        self.context.app.digitos("enter")
        
    def conectarPDA(self):
        self.context.app.clica_coordenada(703,156, 1, "right")
        sleep(3)
        self.context.app.digitos("down","enter")
        
        
class AgendamentoDataHora(object):

    def __init__(self, context):
        self.context = context
    
    def arrastarMarcacao(self):
        #self.context.app.clica_imagem(self.context.path+"data/images/agendamento.png", 1, "left", similar=60)
        self.context.app.arraste_coordenada(618, 469, 523,464, "left",3)
        

class ExibirPlanoTrabalho(object):
    def __init__(self, context):
        '''
        Constructor
        '''
        self.context = context
        
    def selecionarIntervalo(self):
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/carregandoBDI.png", 50) != None):
            pass
        
        sleep(3)         
        self.context.app.clica("Janela", "name", 1)
        self.context.app.digitos(("down", 2), "right", "enter", ("down", 19),"enter")
        sleep(3)
        
        self.context.asserts.verifica_tela(self.context.path +"data/images/listadeOS.png", 50)
        
        self.context.app.clica_coordenada(208,349)
        self.context.app.combo_digitos("alt","down")
        self.context.app.digitos(("left",15),"enter")
        self.context.app.clica("Atualizar", "name", 1)
    
    def selecionarDezEquipes(self):
        self.context.app.digitos(("tab",3))
        aux = 0 
        while(aux < 10):
            self.context.app.digitos("space","down")
            sleep(3)
            aux += 1
        self.context.app.clica("OK","name",5)
        
    def selecionarEquipes(self):
        aux = 0
        sleep(3)
        self.context.app.clica_imagem(self.context.path +"data/images/listaEquipe.png",1)
        while(aux < 10):
            self.context.app.digitos("space","down")
            sleep(3)
            aux += 1


class AgendamentoFixo(object):

    def __init__(self, context):

        self.context = context
        self.OK = "OK"
    def tipoFixo(self):
        sleep(4)
        self.context.app.digitos(("tab", 5),("down",2))
        self.context.app.clica(self.OK, "name",5)
        sleep(3)
        self.context.asserts.verifica_tela(self.context.path + "data/images/agendamentoCriado.png")
        sleep(3)
        self.context.app.clica(self.OK, "name",5)
        
class AgendamentoDespachoPDA(object):

    def __init__(self, context):
        self.context = context
        self.OK = "OK"
    
    def editarAgendamento(self):
        self.context.app.clica_imagem(self.context.path+"data/images/marcacao.png", 1, "right", similar=60)
        self.context.app.digitos(("down",2),"enter")
        self.context.app.digitos(("tab",3))
        self.context.app.combo_digitos("alt","down")
        self.context.app.digitos("right","enter","tab")
        self.context.app.combo_digitos("alt","down")
        self.context.app.digitos("right","enter")
        self.context.app.digitos("enter")
        self.context.app.clica(self.OK,"name",5)
        sleep(5)
        
    def efetuarLogin(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Efetuar Login")
        self.context.app.digitos("enter")
        self.context.asserts.verifica_tela(self.context.path+"data/images/iniciesessao.png", 100)
        sleep(3)
        self.context.app.clica_imagem(self.context.path+"data/images/busca.png", 1, "left", similar=60)
        self.context.app.digitos(("down",6),("tab",5),"down","tab","enter",("tab",2),"space","tab")
        sleep(4)
        self.context.app.escrever_direto("100")
        self.context.app.digitos("tab",("down",18),"tab")
        self.context.app.escrever_direto("TAT01230")
        self.context.app.clica(self.OK, "name",5)
        
        self.context.app.verifica_tela(self.context.path+"data/images/informacao.png",60)
        
class RemoverAgendamento(object):
    def __init__(self, context):
        self.context = context
        
    def removeragendamento(self):
        self.context.app.clica_imagem(self.context.path+"data/images/marcacao.png", 1, "right", similar=60)
        self.context.app.digitos("down","enter")
    
    def verificaRemocao(self):
        if(self.context.app.verifica_tela(self.context.path+"data/images/marcacao.png", 50) == None ):
            pass
            