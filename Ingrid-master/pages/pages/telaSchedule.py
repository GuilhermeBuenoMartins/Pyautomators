# -*- coding: utf-8 -*- ]
'''
Created on 15 de fev de 2019

@author: vgama
'''
from time import sleep

class Schedule(object):
    def __init__(self, context):
        self.context = context
        self.JANELA = "Janela"
    
    def abrir_view_plano_de_trabalho(self):
        self.context.app.clica(self.JANELA,"name", 3)
        self.context.app.digitos(("down",2),"right","enter")
        self.context.app.escrever_direto("Plano de Trabalho")  
        self.context.app.digitos("enter")      
        sleep(5)        
        self.context.asserts.verifica_tela(self.context.path+"data/images/ViewplanoTrabalho.png", 70)
        
    def buscar_uma_equipe(self):
        self.context.app.clica_imagem(self.context.path +"data/images/atualizar.png", 1, "left", similar=40)
        self.context.app.digitos(("tab", 3),("down", 2), "space", "enter")
        
         #enquanto esta atualizando, nao executa nenhuma acao
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/atualizando.png", 50) != None):
            pass
        
        sleep(5)
        
    def selecionar_os_Lista_Ordens(self):
        self.context.app.clica_imagem(self.context.path+"data/images/desmarcado.png",1,"left", similar=40)
        self.context.app.clica_imagem(self.context.path + "data/images/listadeOS.png", similar=60)
        self.context.app.mantenha_e_digite("shift",['down','down'])
        sleep(5)
        
    def seleciona_opcao_planejar(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/planejar.png", 70)
        self.context.app.clica_imagem(self.context.path +"data/images/planejar.png", 1, "left", similar=40)
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/interrogacao.png", 70)
        self.context.app.digitos("enter")
        sleep(3)
        self.context.asserts.verifica_tela(self.context.path+"data/images/interrogacao.png", 70)
        self.context.app.digitos("enter")
        
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/processandoAgendamento.png") != None):
            pass
        sleep(5)
        
    def executa_motor_planejamento(self):
        self.context.app.clica_imagem(self.context.path+"data/images/logsMotor.png", 1,"left")
        sleep(3)
        self.context.app.digitos("tab",("right",3),"down")
        self.context.app.clica_imagem(self.context.path+"data/images/emExecucao.png", 1,"left")
        self.context.app.digitos("enter")
        sleep(5)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        