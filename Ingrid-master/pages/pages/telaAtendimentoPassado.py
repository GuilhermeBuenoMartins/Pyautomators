# -*- coding: utf-8 -*-
'''
Created on 7 de nov de 2018

@author: gcruzm
'''
from time import sleep


class Atendimento_passado(object):
   
    def __init__(self, context):
        self.context = context
        self.OK = "OK"
        self.OS = "Ordem de Serviço"
        self.CONCLUIR = "Concluir"
    
    def criar_ordem_de_servico(self):        
        self.context.asserts.verifica_tela(self.context.path+"data/images/criar_servico_rede.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/criar_servico_rede.png")
        
        self.context.app.clica(self.OS,"name",2)
        self.context.app.clica(self.OK,"name",2)
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/dados_de_referencia_da_os.png",100)
        sleep(3)
        self.context.app.mantenha_e_digite("shift",["tab","tab","tab","tab"])
        self.context.app.digitos("t","tab","down","tab",("t",2),"tab")
        self.context.app.escrever_direto("TAT01230")
        self.context.app.digitos("tab","space")
        self.context.app.clica(self.CONCLUIR,"name",2)
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/gerada_com_sucesso.png",100)):
            self.context.app.clica(self.OK,"name",2)
        
    def localizar_ordem_de_servico(self):
        self.context.app.combo_digitos("ctrl","h")
        self.context.asserts.verifica_tela(self.context.path+"data/images/servico_rede.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/servico_rede.png")
        self.context.app.digitos(("tab",29))
        self.context.app.escrever_direto("2019-401")
        self.context.app.digitos("enter")
    
    def realizar_atendimento_passado_ordem_servico(self):
        sleep(5)
        self.context.app.digitos("down","enter")
        self.context.app.clica_coordenada(910,88)
        self.context.asserts.verifica_tela(self.context.path+"data/images/atendimentoPassado.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/atendimentoPassado.png")
        self.context.app.digitos("tab",("down",11),"tab")
        self.context.app.escrever_direto("teste automatizado de software")
        self.context.app.clica(self.OK,"name",2)