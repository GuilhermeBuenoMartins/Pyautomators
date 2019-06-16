# -*- coding: utf-8 -*-
'''
Created on 12 de dez de 2018

@author: gcruzm
'''
from time import sleep


class Pausar_equipe(object):
    def __init__(self, context):
        self.context = context
        self.OK = "OK"
        self.RECURSOS_PROPOSTOS = "Recursos Propostos"
        self.ROTULO = "Rótulo"
        
    def abrir_recursos_propostos(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("recursos propostos")
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/ctrl_3_recursos_propostos.png",100)):
            self.context.app.digitos("enter")
        sleep(5)
        
    def abrir_view_servico_de_rede_pendente_pausa_e_despacho_multiplo(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Rede Pendentes")
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/ctrl_3_rede_pendentes.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/ctrl_3_rede_pendentes.png")
        else:
            self.context.app.clica_imagem(self.context.path+"data/images/ctrl_3_rede_pendentes_1.png")
            
        sleep(2)         
        self.context.app.digitos("enter")
        
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/refreshServicoPendente.png", 100) != None):
            pass
        self.context.app.clica(self.ROTULO,"name",2)
        sleep(2)
        self.context.app.clica(self.ROTULO,"name",2)
        
    def selecionar_equipe_nao_despachada(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD.png",100) or self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD2.png",100)
        #self.context.app.clica_imagem(self.context.path+"data/images/srp.png",1,"left", similar=50)
        self.context.app.digitos("down","enter")
        sleep(5)
        self.context.asserts.verifica_tela(self.context.path+"data/images/aa-13.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/aa-13.png",1,"left", similar=70)
        
    def clicar_no_icone_pausa_a_equipe(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/pausaequipe.png",80)
        self.context.app.clica_imagem(self.context.path+"data/images/pausaequipe.png", 1, "left", similar=50)
        self.context.app.digitos("down")
        self.context.app.clica_imagem(self.context.path+"data/images/botao_ok.png")
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/informacao.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/botao_ok.png")
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/sim.png",80) !=None):
            self.context.app.clica_imagem(self.context.path+"data/images/sim.png",1, "left", similar=50)
            
    def preenche_campos_motivo_recuperacao(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/motivoRecuperacao.png", 100)
        self.context.app.digitos("down", "enter")
        sleep(6)
        self.context.asserts.verifica_tela(self.context.path+"data/images/informacao.png", 120)
        self.context.app.digitos("enter")
        
class Despacho_multiplo(object):
    def __init__(self, context):
        self.context = context
        self.OK = "OK"
    
    def selecionando_servicos_de_rede_para_despacho_multiplo(self):
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/viaCOD.png",2)
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD2.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/viaCOD2.png",2)
        
        self.context.app.mantenha_e_digite("shift",["down","down","down"])
    
    def arrastando_servicos_para_equipe(self):
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/notebook.png",100)):
            self.context.app.arraste_coordenada(None,None,1110,306,"left",4)
        sleep(2)
        self.context.app.digitos("enter")
        
            
    def despachando_servicos_para_equipe(self):
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/informacao.png",100)):
            self.context.asserts.verifica_tela(self.context.path+"data/images/ok.png",100)
            self.context.app.clica_imagem(self.context.path+"data/images/ok.png",1)
    
class Pausar_atendimento(object):
    def __init__(self, context):
        self.context = context
        self.NAO = "Não"
        self.OK = "OK"
        self.RECURSOS_PROPOSTOS = "Recursos Propostos"
        
    def abrir_recursos_propostos(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("recursos propostos")
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/ctrl_3_recursos_propostos.png",100)):
            self.context.app.digitos("enter")
        sleep(5)
    
    def selecionar_equipe_despachada(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD.png",100)
        self.context.app.digitos(("down",3),"enter")
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/rPropostos2.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/rPropostos2.png",2)
            
            if(self.context.asserts.verifica_tela(self.context.path+"data/images/aa-19.png",100)):
                self.context.app.clica_imagem(self.context.path+"data/images/aa-19.png")
 