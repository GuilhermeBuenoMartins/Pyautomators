# -*- coding: utf-8 -*-
'''
Created on 11 de mar de 2019

@author: vgama
'''
from time import sleep

class PESGeracaoManual(object):

    def __init__(self, context):
        self.context = context
        self.CONDICAO2 = "Condição de Segurança 2"
        self.CONDICAO3 = "Condição de Segurança 3"
        self.CONDICAO4 = "Condição de Segurança 4"
        self.NENHUMA = "Nenhuma"
        self.PES = "PES"
        self.OK = "OK"
    
    def abrir_pes(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/pes.png", 80)
        self.context.app.clica_imagem(self.context.path+"data/images/pes.png", 1, "left")
        sleep(4)
        self.context.asserts.verifica_tela(self.context.path+"data/images/pedidoExecucao.png", 70)
        
        
    def criacao_PES(self):
        self.context.app.digitos("tab")
        self.context.app.combo_digitos("shift","tab")
        self.context.app.digitos("tab","down","tab")
        self.context.app.escrever_direto("t")
        self.context.app.digitos("down","tab")
        self.context.app.escrever_direto("TAT01230")
        self.context.app.digitos("tab","space",("tab",4))
        self.context.app.escrever_direto("teste")
        self.context.app.digitos(("tab",2),"right","tab","right",("tab",2),"right")
        
        self.context.app.clica_imagem(self.context.path+"data/images/avancar.png", 1, "left")
        self.context.app.clica_imagem(self.context.path+"data/images/calendario.png", 1, "left", similaridade=70)
        self.context.app.digitos("right", "space", "tab")
        self.context.app.combo_digitos("alt","down")
        self.context.app.digitos("right", "space", ("tab",2),"down","tab")
        self.context.app.escrever_direto("teste")
        self.context.app.clica_imagem(self.context.path+"data/images/campoNome.png", 1, "left", similaridade=70)
        self.context.app.combo_digitos("ctrl","h")
        self.context.app.digitos("down","enter", "tab")        
        self.context.app.clica_imagem(self.context.path+"data/images/avancar.png", 1, "left")
        
        self.context.app.clica(self.NENHUMA, "name", 2)        
        self.context.app.clica(self.CONDICAO2, "name", 2)
        self.context.app.clica(self.NENHUMA, "name", 2)
        
        self.context.app.clica(self.CONDICAO3, "name", 3)
        self.context.app.clica(self.NENHUMA, "name", 2)
        
        self.context.app.clica(self.CONDICAO4, "name", 4)
        self.context.app.clica(self.NENHUMA, "name", 2)
        self.context.app.clica_imagem(self.context.path+"data/images/concluir.png", 1, "left")
        sleep(6)
        
    def janela_classificacao(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/atencaoAtendimento.png", 70)
        self.context.app.digitos("enter")
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/adcionarMotivo.png", 70)
        self.context.app.digitos("tab","down","tab")
        self.context.app.escrever_direto("Teste")
        
        self.context.app.clica_imagem(self.context.path+"data/images/botao_ok.png", 1, "left")
        self.context.asserts.verifica_tela(self.context.path+"data/images/viewSucesso.png", 70)
        self.context.app.digitos("enter")
        
        
    def pesquisar_pes_criado(self):        
        self.context.app.combo_digitos("ctrl", 3)
        self.context.app.escrever_direto("Pendentes")
        self.context.asserts.verifica_tela(self.context.path+"data/images/viewPedidoExecucaoPendente.png", 70)
        self.context.app.clica_imagem(self.context.path+"data/images/viewPedidoExecucaoPendente.png", 1, "left")

        #Verificando View Aberta Pedido de Execucao pendente
        self.context.asserts.verifica_tela(self.context.path+"data/images/janelaPedidoExecucaoPendente.png", 70)
        
        self.context.app.clica(self.PES, "name", 4)
        self.context.app.clica(self.PES, "name", 4)
        self.context.app.digitos("down","up")
        
        
    
    def viabilizar_PES(self):
        self.context.app.clica_coordenada()#Pegar coordenada    
        self.context.asserts.verifica_tela(self.context.path+"data/images/opcaoViabilizarPES.png", 70)
        self.context.app.clica_imagem(self.context.path+"data/images/opcaoViabilizarPES.png", 1, "left")
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/viewSucesso.png", 70)
        self.context.app.digitos("enter")

    def reprovar_PES(self):        
        self.contet.app.clica_coordenada()#Pegar coordenada 
        self.context.clica_imagem(self.context.path+"data/images/opcaoReprovarPES.png", 1, "left")
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/viewReprovarPES.png", 70)
        self.context.app.digitos(("tab",2),"down","tab")
        self.context.app.escrever_direto("TESTE")
        self.context.app.clica(self.OK,"name", 3)
        
    def verifica_PES_reprovado(self):        
        self.context.asserts.verifica_tela(self.context.path+"data/images/pesReprovadoSucesso.png", 70)
        self.context.app.clica(self.OK,"name", 3)


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        