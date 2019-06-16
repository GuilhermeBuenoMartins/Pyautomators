# -*- coding: utf-8 -*-
'''
Created on 25 de fev de 2019

@author: vgama
'''
from time import sleep
import pyautogui


class UnificarVariosSR(object):

    def __init__(self, context):

        self.context = context
        self.JANELA = "Janela"
        self.SERVICO_PENDENTE = "Serviços de Rede Pendentes"
        
    def abrindo_view_servico_rede_pendentes(self):
        self.context.app.clica(self.JANELA,"name", 3)
        self.context.app.digitos(("down",3),"right","down","enter")
        
        self.context.app.escreve("texto do filtro de tipos", self.SERVICO_PENDENTE,"name")
        self.context.app.digitos(("tab",2),"down","enter")
        
        
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/refreshSR.png", 50) != None):
            pass
        
        sleep(10)
        
    def selecionado_varios_sr(self):
        self.context.app.clica_imagem(self.context.path+"data/images/2016_585109.png", 1,"left", similar=60)  
        self.context.app.mantenha_e_digite('shift',['up','up'])    
        sleep(5)
        
        
    def selecionar_opcao_unificar(self):
        #self.context.app.clica("Unificar Serviço de Rede","name",2)
        self.context.app.clica_imagem(self.context.path+"data/images/encontrarSR.png", 1, "right", similar=50)
        sleep(3)
        self.context.app.clica_imagem(self.context.path+"data/images/opcaounificarServicosRede.png", 1, "left", similar=60)
        #sleep(4)
        
    def informar_sr_e_confirmar(self):
        self.context.app.escrever_direto("2016-585109")
        self.context.app.clica_imagem(self.context.path+"data/images/botao_ok.png", 1, "left", similar=60)
        self.context.app.digitos("enter")
        
    def lista_sr_passiveis_unificacao(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/lista_eventos.png", 80)
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/incidencia.png", 80, similaridade=60) == None):
            raise NameError('Nenhum Servico para Unificar') 
        
    def seleciono_sr_para_unificar(self):
        self.context.app.clica_imagem(self.context.path+"data/images/incidencia.png", 1, "left", similar=60)
        self.context.app.clica_imagem(self.context.path+"data/images/btnUnificar.png", 1, "left", similar=60)
        
        self.context.app.clica_imagem(self.context.path+"data/images/ok.png", 1, "left", similar=60)
        
        
    def verifico_unificacao(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/informacao.png", 80, 1)
        self.context.app.digitos("enter")
        
        
class UnificarSREncerrado(object):

    def __init__(self, context):
        self.context = context 
        
    def buscar_sr_encerrado(self):
        self.context.app.combo_digitos('ctrl','h')
        self.context.asserts.verifica_tela(self.context.path+"data/images/servico_rede.png", 70)
        self.context.app.clica_imagem(self.context.path+"data/images/servico_rede.png", 1,"left")
        self.context.asserts.verifica_tela(self.context.path+"data/images/procurar.png", 80)

        self.context.app.digitos(("tab",9))
        self.context.app.combo_digitos('alt','down')
        self.context.app.digitos(("left",10))
        #self.context.app.combo_digitos('ctrl','left')
        self.context.app.digitos("enter","tab","space")
        
        self.context.app.clica_imagem(self.context.path+"data/images/fechado.png", 1, "left", similar=60)
        self.context.app.digitos("space")
        self.context.app.clica_imagem(self.context.path+"data/images/pendente.png", 1, "left", similar=60)
        self.context.app.digitos("space","enter")
        
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/refresh.png", 50) != None):
            pass
        
    def selecionar_sr_encerrado(self):
        self.context.app.clica("Origem","name",2)
        self.context.app.clica("Origem","name",2)
        self.context.app.digitos("down")
        self.context.app.mantenha_e_digite('shift',["down","down","down","down","down"])
        
        
    def informar_um_sr_encerrado(self):
        self.context.app.escrever_direto("2019-603")
        self.context.app.clica_imagem(self.context.path+"data/images/botao_ok.png", 1, "left", similar=60)
        self.context.app.digitos("enter")
        
        