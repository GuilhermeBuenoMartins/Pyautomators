# -*- coding: utf-8 -*- ]
'''
Created on 3 de dez de 2018

@author: vgama
'''
from time import sleep
import subprocess
import os

class Scada(object):
    def __init__(self, context):
        '''
        Constructor
        '''
        self.context = context
        self.JANELA = "Janela"
        self.ROTULO = "Rótulo"
        self.ALIMENTADOR = "Alimentador"
    
        
    def enviar_sinal_scada_aberto(self):
        '''
        #abrindo o scada no soap
        self.context.asserts.verifica_tela(self.context.path+"dat/images/scadaSoap.png")
        self.context.app.clica_imagem(self.context.path+"data/images/scadaSoap.png",1, "left", similar=80)
        self.context.app.digitos(("right",3))
        self.context.app.clica_imagem(self.context.path+"data/images/executeSwitchSOAP.png",1, "left", similar=80)
        self.context.app.digitos(("right",2),"enter")
    
       
        self.context.app.clica_coordenada(459,193,2)
        self.context.app.escrever_direto("1080")
        sleep(2)
        
        self.context.app.clica_coordenada(453,219, 2)
        self.context.app.escrever_direto("10230070")
        sleep(2)
        
        #SINAL SCADA ABERTO
        self.context.app.clica_coordenada(444,245, 2)
        self.context.app.escrever_direto("0")
        sleep(2)
        
        self.context.app.clica_imagem(self.context.path+"data/images/dataSoap.png", 1, "left", similar=80)
        self.context.app.clica_coordenada(548,508)
        self.context.app.combo_digitos("shift","tab")
        sleep(2)
        self.context.app.escrever_direto("1200")
        sleep(2)
        self.context.app.clica_imagem(self.context.path+"data/images/okSoap.png",1, "left", similar=80)
        self.context.app.clica_imagem(self.context.path+"data/images/executarSoap.png", 1, "left", similar=80)
        '''
        
        os.system('cd C:/Program Files (x86)/SmartBear/SoapUI-5.4.0/bin & testrunner.bat "C:/Users/vgama/Desktop/scada/scadaAbrir.xml"')
        
    def abrindo_servicos_de_rede(self):
        self.context.app.combo_digitos("ctrl", "h")
        sleep(3)
        self.context.app.clica_imagem(self.context.path+"data/images/servico_rede.png", 1,"left")
        sleep(10)
        self.context.app.digitos(("tab",23),"down","space")
        self.context.app.digitos(("tab",4),"down","space","enter")
        
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/refreshServicoPendente.png", 50) != None):
            pass
        
    def verificando_view_manobra(self):
        self.context.app.clica(self.ROTULO,"name",5)
        self.context.app.clica(self.ROTULO,"name",5)
        self.context.app.digitos("down","up","enter")
        self.context.asserts.verifica_tela(self.context.path+"data/images/matriculaScada.png", 100, similaridade=80)
        sleep(5)
    
    def abrir_view_ordens_de_manobra(self):
        self.context.app.combo_digitos("ctrl", "3")
        self.context.app.escrever_direto("Manobras e Ordens de Manobras")
        self.context.app.digitos("enter")
        self.context.app.arraste_coordenada(120, 76, 81, 704,"left", 3)
        sleep(3)
    
    def abrir_view_painel_integracao(self):
        self.context.app.combo_digitos("ctrl", "3")
        self.context.app.escrever_direto("Painel de Inte")
        self.context.app.digitos("enter")
        sleep(3)
        self.context.app.clica(self.ALIMENTADOR,"name",3)
        self.context.app.clica(self.ALIMENTADOR,"name",3)
        self.context.asserts.verifica_tela(self.context.path+"data/images/elementoScada.png", 50)
        
        
    def envia_sinal_scada_fechado(self):
        '''
        self.context.app.clica_coordenada(459,193, 2)
        self.context.app.escrever_direto("1080")
        sleep(2)
        
        self.context.app.clica_coordenada(453,219, 2)
        self.context.app.escrever_direto("10230070")
        sleep(2)
        
        #SINAL SCADA FECHADO
        self.context.app.clica_coordenada(444,245, 2)
        self.context.app.escrever_direto("1")
        sleep(2)
        self.context.app.clica_imagem(self.context.path+"data/images/dataSoap.png", 1, "left", similar=80)
        self.context.app.clica_coordenada(548,508)
        self.context.app.combo_digitos("shift","tab")
        sleep(2)
        self.context.app.escrever_direto("1530")
        sleep(2)
        self.context.app.clica_imagem(self.context.path+"data/images/okSoap.png",1, "left", similar=80)
        #self.context.app.clica_imagem(self.context.path+"data/images/executarSoap.png", 1, "left", similar=80)
        '''
        os.system('cd C:/Program Files (x86)/SmartBear/SoapUI-5.4.0/bin & testrunner.bat "C:/Users/vgama/Desktop/scada/scadaFechado.xml"')
        
    def verificando_view_manobra_acao_fechado(self):
        self.context.app.clica(self.ROTULO,"name",5)
        self.context.app.clica(self.ROTULO,"name",5)
        self.context.app.digitos("down","up",("enter",2))
        self.context.asserts.verifica_tela(self.context.path+"data/images/scadaFechado.png", 50, similaridade=80)