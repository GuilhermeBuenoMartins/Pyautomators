'''
Created on 26 de nov de 2018
@author: gcruzm

'''
from time import sleep


class Configuracao_proposta_falha(object):
   
    def __init__(self, context):
        self.context = context
        self.ATIVAR_DESATIVAR = "Ativar/Desativar"
        self.SIM = "Sim"
        self.OK = "OK"
        self.ATIVA = "Ativa"
    
    def abrir_configuracao_proposta_falha(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/outros.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/outros.png")
        self.context.app.clica_imagem(self.context.path+"data/images/configurarPropostaFalha.png", 1, "left")
    
    def selecionar_uma_configuracao(self):
        self.context.app.digitos("tab")
        self.context.app.combo_digitos("shift","tab")
        self.context.app.mantenha_e_digite('ctrl',['right'])
        
        aux = 0
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/naoAtiva.png",20) == None):
            if(aux == 50):
                raise("nenhuma configuracao marcada como nao ativa")
            self.context.app.digitos(("down",5))
            aux = aux + 1
            
            
  
    def clicar_em_desativar_ativar(self):
        self.context.app.clica_imagem(self.context.path+"data/images/naoAtiva.png", 1, "left")
        self.context.app.clica(self.ATIVAR_DESATIVAR,"name",4)
        self.context.app.clica(self.SIM,"name",2)
        
    def verifica_configuracao_ativa(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/ativa.png",70)
        
class Proposta_falha_transformador(object):
        
    def __init__(self, context):
        self.context = context
        self.NOVO_AVISO = "Novo Aviso"
        self.CONCLUIR = "Concluir"
        self.OK = "OK"
        self.CONFIABILIDADE = "Confiabilidade: "
        self.BUSCAR = "Buscar"
        self.ROTULO = "Rótulo"
        self.CIDADE = "Cidade"
        
    def abrir_view_busca_cliente(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Busca de Clientes")
        self.context.app.digitos("enter")
        sleep(5)
   
    def buscar_por_transformador(self):
        self.context.app.mantenha_e_digite('shift',["tab","tab","tab","tab","tab","tab","tab","tab","tab","tab",])
        self.context.app.escrever_direto("TRANSFORMADOR")
        self.context.app.clica(self.BUSCAR,"name",3)
        sleep(4)
        self.context.app.clica(self.CIDADE, "name", 3)
        
    '''Transformador 1'''
    def selecionar_primeiro_cliente(self):
        self.context.app.digitos(("down",6))
        self.context.app.clica(self.NOVO_AVISO, "name", 3)
        
        #verifica notificacao e prossegue com a criacao do aviso
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/avisoPendenteCliente.png", 60) != None):
            self.context.app.digitos("enter")
            
        self.context.asserts.verifica_tela(self.context.path+"data/images/telaNovoAviso.png", 60)
        self.context.app.digitos("tab")
        self.context.app.escrever_direto("89435262738")
        self.context.app.digitos(("tab",7),("down",3))
        self.context.app.digitos("tab",("down",3))
        self.context.app.clica(self.CONCLUIR,"name",3)
        
    def aviso_criado(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/dadosAviso.png",60)
        self.context.app.clica(self.OK, "name", 4)
    
    
    '''Transformador 2''' 
    def selecionar_segundo_cliente(self):
        self.context.app.digitos("down")
        self.context.app.clica(self.NOVO_AVISO, "name", 3)
        
        #verifica notificacao e prossegue com a criacao do aviso
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/avisoPendenteCliente.png", 60) != None):
            self.context.app.digitos("enter")
            
        self.context.asserts.verifica_tela(self.context.path+"data/images/telaNovoAviso.png", 60)
        self.context.app.digitos("tab")
        self.context.app.escrever_direto("89435262738")
        self.context.app.digitos(("tab",7),("down",3))
        self.context.app.digitos("tab",("down",4))
        self.context.app.clica(self.CONCLUIR,"name",3)

    
    '''Transformador 3'''
    def selecionar_terceiro_cliente(self):
        self.context.app.digitos("down")
        self.context.app.clica(self.NOVO_AVISO, "name", 3)
        
        #verifica notificacao e prossegue com a criacao do aviso
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/avisoPendenteCliente.png", 60) != None):
            self.context.app.digitos("enter")
            
        self.context.asserts.verifica_tela(self.context.path+"data/images/telaNovoAviso.png", 60)
        self.context.app.digitos("tab")
        self.context.app.escrever_direto("89435262738")
        self.context.app.digitos(("tab",7),("down",3))
        self.context.app.digitos("tab",("down",3))
        self.context.app.clica(self.CONCLUIR,"name",3)
    
     
    def verifica_servico_unidos(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Redes Pendentes")
        self.context.app.digitos("enter")
        
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/refresh.png", 60) != None):
            pass
        
        self.context.app.clica(self.ROTULO, "name", 3)
        self.context.app.clica(self.ROTULO, "name", 3)
        self.context.app.digitos("down")
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/despachoDesmarcado.png", 60)
        
        
        
class Proposta_falha_seccionador(object):
    
    def __init__(self, context):
        self.context = context
        self.BUSCAR = "Buscar"
        self.CIDADE = "Cidade"
        
    def buscar_por_seccionador(self):
        self.context.app.mantenha_e_digite('shift',["tab","tab","tab","tab","tab","tab","tab","tab","tab","tab",])
        self.context.app.escrever_direto("IND01898")
        self.context.app.clica(self.BUSCAR,"name",3)
        sleep(4)
        self.context.app.clica(self.CIDADE, "name", 3)
