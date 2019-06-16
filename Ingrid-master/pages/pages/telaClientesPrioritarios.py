# -*- coding: utf-8 -*-
'''
Created on 20 de dez de 2018

@author: vgama
'''
from time import sleep

class ClientesPrioritarios(object):
    '''
    classdocs
    '''

    def __init__(self, context):
        '''
        Constructor
        '''
        self.context = context
    
    def view_servico_rede(self):
        #espera o banco carregar
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/carregandoBDI.png", 80) != None):
            pass
        sleep(5)
        #abre a janela servico de rede
        self.context.app.clica_imagem(self.context.path+"data/images/janelaIngrid.png", 1, "left")
        self.context.app.clica_imagem(self.context.path+"data/images/carregarJanela.png", 1, "left")
        self.context.app.clica_imagem(self.context.path+"data/images/outros....png", 1, "left")
        sleep(2)
        self.context.app.escreve("texto do filtro de tipos", "Serviços de Rede", "name")
        sleep(3)
        self.context.app.clica_imagem(self.context.path +"data/images/servico_rede.png",2, "left", similar=80)
    
    def criacao_servico_rede(self):
        #entra na view de criacao SR
        self.context.app.clica_imagem(self.context.path+"data/images/novoServicoRede.png",1,"left",similar=80)
        self.context.app.digitos("enter")
        self.context.asserts.verifica_tela(self.context.path+"data/images/telaServicoRede.png",80)
        
    def preencher_campos_cliente_vip(self):
        self.context.app.digitos("down", "tab")
        self.context.app.escrever_direto("F")
        self.context.app.digitos(("down",4))
        self.context.app.clica_imagem(self.context.path+"data/images/tipoelemente.png",1,"left", similar=80)
        self.context.app.digitos(("down",4), "tab")
        self.context.app.escrever_direto("37442171")
        self.context.app.digitos("tab")
        sleep(3)
        self.context.app.clica_imagem(self.context.path+"data/images/concluir2.png",1,"left",similar=80)
        sleep(5)
        self.context.asserts.verifica_tela(self.context.path+"data/images/informacao.png",80)
        self.context.app.clica_imagem(self.context.path+"data/images/botao_ok.png",1,"left", similar=40)
        sleep(3)
        
        
        
    def marcar_sr_comercial(self):
        self.context.app.clica_imagem(self.context.path+"data/images/servico_rede.png", 1,"left", similar=80)
        self.context.app.combo_digitos("ctrl","h")
        self.context.app.digitos("right",("tab",9),"space","tab")
        self.context.app.combo_digitos("alt","down")
        self.context.app.digitos("right","enter","enter")
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/refresh.png",60) != None):
            pass
        self.context.app.digitos(("down",20))
        sleep(5)
        self.context.app.clica_imagem(self.context.path+"data/images/encontrarSR.png",1,"right",similar=80)
        sleep(5)
        self.context.asserts.verifica_tela(self.context.path+"data/images/marcarOSEmergencial.png",120)
        self.context.app.clica_imagem(self.context.path+"data/images/marcarOSEmergencial.png",1,"left",similar=80)
        self.context.app.digitos("tab","enter")
        sleep(2)
        self.context.app.clica_imagem(self.context.path+"data/images/botaoOK.png",1,"left",similar=80)
        
    def verifica_criacao_os_emergencial(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/emergencialAlterado.png",80)
        self.context.app.digitos("enter")
        
        
    def preencher_campos_cliente_especifico(self):
        self.context.app.digitos("down", "tab")
        self.context.app.escrever_direto("F")
        self.context.app.digitos(("down",4))
        self.context.app.clica_imagem(self.context.path+"data/images/tipoelemente.png",1,"left", similar=80)
        self.context.app.digitos(("down",4), "tab")
        self.context.app.escrever_direto("1421662")
        self.context.app.digitos("tab","enter")
        sleep(3)
        self.context.app.clica_imagem(self.context.path+"data/images/concluir2.png",1,"left",similar=80)
        sleep(5)
        self.context.asserts.verifica_tela(self.context.path+"data/images/informacao.png",120)
        self.context.app.clica_imagem(self.context.path+"data/images/botao_ok.png",1,"left", similar=40)
        sleep(3)
        
    def preencher_campos_cliente_consumo(self):
        self.context.app.digitos("down", "tab")
        self.context.app.escrever_direto("F")
        self.context.app.digitos(("down",4))
        self.context.app.clica_imagem(self.context.path+"data/images/tipoelemente.png",1,"left", similar=80)
        self.context.app.digitos(("down",4), "tab")
        self.context.app.escrever_direto("18454968")
        self.context.app.digitos("tab","enter")
        sleep(3)
        self.context.app.clica_imagem(self.context.path+"data/images/concluir.png",1,"left",similar=30)
        self.context.app.digitos("enter")
        sleep(3)
        
        
    def selecionar_sr_da_pre_condicao(self):
        #espera o banco carregar
        self.context.app.combo_digitos("ctrl","h")
        self.context.app.digitos("right")
        sleep(10)
        self.context.app.clica_imagem(self.context.path+"data/images/pesquisarRotulo.png",1,"left",similar=70)
        sleep(5)
        self.context.app.escrever_direto("2018-881")
        self.context.app.digitos("enter")
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/refresh.png",60) != None):
            pass
        
        
    def realizar_manobra_abertura(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD2.png",80)
        self.context.app.digitos("down")
        self.context.app.clica_imagem(self.context.path+"data/images/manobra.png", 1,"left", similar=80)
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/manobraServicoRede.png",80)
        
        self.context.app.mantenha_e_digite("shift","tab","tab")
        self.context.app.digitos(("down",10),"tab")
        self.context.app.escrever_direto("2102966472")
        self.context.app.digitos("tab")
        sleep(5)
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/informacao.png",80) != None):
            self.context.app.digitos("enter")
            
        self.context.app.clica_imagem(self.context.path+"data/images/execucaoManobra.png")
        sleep(10)
    
    def verifica_sr(self):
        self.context.app.clica_imagem(self.context.path+"data/images/cancelarManobras.png",1,"left",similar=80)
        self.context.asserts.verifica_tela(self.context.path+"data/images/listaEventosUnificados.png",80)
        
    def seleciona_sr_novamente(self):
        self.context.app.clica_imagem(self.context.path+"data/images/servicoRede.png",1,"left",similar=80)
        sleep(3)
        self.context.app.clica_imagem(self.context.path+"data/images/manobra.png", 1,"left", similar=80)
        
    def realiza_manobra_fechamento(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/acaoFecharManobra.png",80)
        self.context.app.clica_imagem(self.context.path+"data/images/execucaoManobra.png")

    
        
        
        
        