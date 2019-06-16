# -*- coding: utf-8 -*-
'''
Created on 26 de nov de 2018

@author: vgama
'''

from time import sleep

class SRDespachado(object):
    def __init__(self, context):

        self.context = context
        self.JANELA = "Janela"
        self.SERVICO_PENDENTE = "Serviços de Rede Pendentes"
        self.ROTULO = "Rótulo"
        
        
    def view_SR_pendentes(self):
        self.context.app.clica(self.JANELA,"name", 3)
        self.context.app.digitos(("down",3),"right","down","enter")
        
        self.context.app.escreve("texto do filtro de tipos", self.SERVICO_PENDENTE,"name")
        self.context.app.digitos(("tab",2),"down","enter")
        
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/refreshServicoPendente.png", 80) != None):
            pass
        sleep(5)
    def selecionar_sr_despachado(self):
        self.context.app.clica(self.ROTULO,"name",4)
        self.context.app.clica(self.ROTULO,"name",4)
        sleep(3)
        
        self.context.app.clica_imagem(self.context.path+"data/images/aa-31_negrito.png", 1, "left", similar=70)
        sleep(5)
    
    def selecionar_opcao_marcar_desmarcar_pre_despacho(self):
        self.context.app.clica_imagem(self.context.path+"data/images/encontrarSR.png", 1, "right", similar=50)
        sleep(3)
        self.context.app.clica_imagem(self.context.path+"data/images/marcarPreDespacho.png", 1, "left", similar=60)
        self.context.app.digitos("tab","enter",("tab",2),"enter")
        
    def verifica_pre_despacho_nao_realizado(self):
        self.context.asserts.verifica_tela(self.context.path +"data/images/execucaoPendente.png", 100)
        sleep(5)


class SRAgendado(object):

    def __init__(self, context):
        
        self.context = context
    
    def view_servico_rede(self):
        self.context.app.combo_digitos("ctrl","h")
        self.context.asserts.verifica_tela(self.context.path+"data/images/servico_rede.png", 80)
        self.context.app.clica_imagem(self.context.path+"data/images/servico_rede.png", 1,"left")
        #self.context.app.digitos("right")
        sleep(2)         
        self.context.app.digitos(("tab",29))
        sleep(3)
        self.context.app.escrever_direto("2018-10013")
        self.context.app.digitos("enter")
        sleep(5)
        
    def selecionar_sr_agendado(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD2.png", 60)
        self.context.app.clica_imagem(self.context.path+"data/images/viaCOD2.png", 1, "left")
        sleep(5)
        
class SRMarcar(object):

    def __init__(self, context):
        self.context = context
        self.JANELA = "Janela"
        self.OK = "OK"
    
    def selecionarSR(self):
        sleep(5)
        self.context.asserts.verifica_tela(self.context.path+"data/images/srSemEquipe.png", 100)
        self.context.app.clica_imagem(self.context.path+"data/images/srSemEquipe.png", 1, "left", similar=70)
        sleep(4)
        
    def preencherSR(self):
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/osNaoMarcadas.png", 60) != None):
            self.context.app.digitos("enter")  
        
        sleep(3)
        self.context.app.combo_digitos("alt","down")
        sleep(3)
        self.context.app.digitos("right","enter", "tab", "down","tab")
        self.context.app.escrever_direto("normal")
        self.context.app.clica(self.OK, "name",3)
        self.context.app.digitos("enter")
        sleep(5)
        
    def verificaPreDespacho(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/srMarcadoPreDespacho.png", 100)
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Propriedades")
        self.context.app.digitos("enter")
        sleep(5)
        self.context.asserts.verifica_tela(self.context.path+"data/images/preDespacho.png", 100)
        
    def selecionarVariosSR(self):
        self.context.app.clica_imagem(self.context.path+"data/images/srp.png", 1, "left", similar=60)
        self.context.app.clica_imagem(self.context.path+"data/images/srSemEquipe.png", 1, "left", similar=60)
        self.context.app.mantenha_e_digite('shift',['down','down'])
            
class SRMarcadoPreDespacho(object):
    def __init__(self, context):        
        self.context = context
        self.OK = "OK"
        
    def abrir_view_recursos_propostos(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("recursos propostos")
        self.context.app.digitos("enter")
        sleep(5)
        self.context.app.arraste_coordenada(178, 76, 81, 704, "left", 3)
         
    def selecionar_sr_pre_despachado(self):
        self.context.app.clica_imagem(self.context.path+"data/images/servicoPendente.png", 1, "left", similar=60)
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/flegado.png",30) == None):
            self.context.app.digitos(("down",19))
            
    def arrastar_para_equipe(self):
        self.context.app.clica_imagem(self.context.path+"data/images/flegado.png", 2, "left", similar=60)
        sleep(5)
        self.context.app.arraste_coordenada(None,None, 33, 201,"left", 3)
        
    def apresenta_mensagem_erro(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/atencao_icone.png", 80)
        sleep(3)
        self.context.app.clica(self.OK, "name",3)
        
        
        
        
class DesmarcarPreDespacho(object):

    def __init__(self, context):

        self.context = context
        self.OK = "OK"
    def selecionar_sr_predespachado(self):
        sleep(5)
        self.context.asserts.verifica_tela(self.context.path+"data/images/flegado.png", 100)
        self.context.app.clica_imagem(self.context.path+"data/images/flegado.png", 1, "right", similar=60)
        sleep(3)
        
    def desmarcarDespacho(self):
        self.context.app.clica_imagem(self.context.path+"data/images/marcarPreDespacho.png", 1, "left", similar=60)
        self.context.app.digitos(("tab",2),"enter","tab","enter")
        self.context.asserts.verifica_tela(self.context.path+"data/images/confirmarAlteracao.png",50)     
        self.context.app.clica(self.OK,"name",5)
   
    def selecionarServicos(self):        
        self.context.asserts.verifica_tela(self.context.path+"data/images/flegado.png", 100)
        self.context.app.clica_imagem(self.context.path+"data/images/flegado.png", 1, "left", similar=60)
        self.context.app.mantenha_e_digite('shift',['down','down'])
        self.context.app.clica_coordenada(None,None, 1, "right")
        sleep(3)
        
    def verifica_sr_desmarcado(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/srDesmarcadoPreDespacho.png",80)
        
class DesmarcarPreDespachoAut(object):

    def __init__(self, context):
        self.context = context
        self.OK = "OK"
    
    def preencheDadosDataFim(self):        
        self.context.app.digitos(("right",4),"up")
        self.context.app.digitos("tab","down","tab")
        self.context.app.escrever_direto("Teste")
        self.context.app.clica(self.OK,"name",4)
        self.context.app.clica(self.OK,"name",4)
        sleep(10)
        
    def verifica_sr_sem_predespacho(self):
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/despachoDesmarcado.png", 30) == None):
            pass
        
class DespachoAutomatico1(object):

    def __init__(self, context):

        self.context = context
        self.OK = "OK"
    
    def desmarcaSR(self):
        self.context.app.clica_imagem(self.context.path+"data/images/srMarcadoPreDespacho.png", 1, "left", similar=40)
        self.context.app.clica_imagem(self.context.path+"data/images/srMarcadoPreDespacho.png", 1, "right", similar=60)
        sleep(4)
        self.context.app.clica_imagem(self.context.path+"data/images/marcarPreDespacho.png", 1,"left")
        self.context.app.digitos(("tab",2),"enter","tab","enter")
        self.context.app.clica(self.OK, "name", 5)
        
class DespachoAutomatico2(object):

    def __init__(self, context):
        self.context = context
    
    def verificaDespacho(self):
        aux = 0
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/despachoDesmarcado.png",20) == None):
            if(aux == 80):
                raise("imagem nao encontrada")
            aux = aux + 1 
            pass
        
    def selecionarOSPerto(self):        
        self.context.app.clica_coordenada(230, 129, 1, "left")
        self.context.app.escrever_direto("2015-2216255")
        sleep(4)
        self.context.app.digitos("tab","down",("enter",2))
        self.context.app.arraste_coordenada(11, 207, 995,237, "left", 3)