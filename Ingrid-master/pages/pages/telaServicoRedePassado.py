# -*- coding: utf-8 -*-
'''
Created on 29 de jun de 2018

@author: gcruzm
'''
from time import sleep

class MarcarServicoRedeComoPassado(object):
    def __init__(self, context):
        self.context = context
        self.OK = "OK"
    
    def buscar_servico_rede_encerrado(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/introInGrid.png",80)
        self.context.app.combo_digitos("ctrl","h")
        sleep(4)
        self.context.asserts.verifica_tela(self.context.path+"data/images/procurar.png", 80)
        self.context.app.digitos("right")
        sleep(5)
        self.context.asserts.verifica_tela(self.context.path+"data/images/ordemServico.png", 100)
        self.context.app.clica_imagem(self.context.path+"data/images/servico_rede.png", 1, "left", similar=60)
        self.context.app.digitos(("tab",29))
        sleep(10)
        self.context.app.escrever_direto("2019-486")
        self.context.app.digitos("enter")
    
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/refreshSR.png", 50) != None):
            pass
        
        self.context.app.digitos("down")
        
    def abrir_marcar_servico_rede_passado(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/marcarServicoRedePassado.png",80)
        self.context.app.clica_imagem(self.context.path+"data/images/marcarServicoRedePassado.png")
        self.context.asserts.verifica_tela(self.context.path+"data/images/ServicoDeRedePassado.png", 80)
            
    def concluir_marcar_servico_rede_passado(self):
        self.context.app.digitos(("tab",4),"down")
        self.context.app.clica(self.OK,"name",3)
        sleep(5)
        
    def verifica_servico_passado(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Propriedades")
        sleep(4)
        self.context.asserts.verifica_tela(self.context.path+"data/images/srPassadoSim.png",80)
    
class SimularServicoRede(object):
    
    def __init__(self, context): 
        self.context = context
        
    def clicar_simular_servico_rede(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/simularServicoRedePassado.png",80)
        self.context.app.clica_imagem(self.context.path+"data/images/simularServicoRedePassado.png", 1, "left", similar=70)
        
    def preencher_campos_simulacao_sr(self):
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/alimentadoresSimulacao.png",80) != None):
            self.context.app.digitos("tab")
            self.context.app.combo_digitos("shift","tab")
            self.context.app.digitos("s",("down",2),"tab")
            self.context.app.escrever_direto("FER02776")
            self.context.app.digitos("enter")
        
    def carrega_entorno_trabalho(self):
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/entornoSimulacoes.png",80) != None):
            pass
                

class ExcluirManobrasSimuladas(object):
    
    def __init__(self, context):
        self.context = context
        
    def selecionar_uma_manobra(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/manobraSimulacao.png",80)
        sleep(5)
        self.context.app.clica_imagem(self.context.path+"data/images/opcao1.png",1, "left", similar=40)
        sleep(5)
        
    def selecionar_segunda_manobra(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/manobraSimulacao.png",80)
        sleep(5)
        self.context.app.clica_imagem(self.context.path+"data/images/opcao1.png",1, "left", similar=40)
        sleep(5)
       
    def apagar_manobra_simulada(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/apagarManobraSimulada.png", 80)
        self.context.app.clica_imagem(self.context.path+"data/images/apagarManobraSimulada.png", 1, "left", similar=70)
        sleep(5)

class IncluirManobrasSimuladas(object):
    '''
    classdocs
    '''
    
    def __init__(self, context):
        self.context = context
        self.FLAG_MANOBRA = "Flag Manobra"
        self.EXECUTAR= "Executar"
        self.CANCELAR= "Cancelar"
    
    def clicar_em_nova_manobra(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/novaManobra.png",60)
        self.context.app.clica_imagem(self.context.path+"data/images/novaManobra.png", 1, "left")

    def incluir_a_manobra_simulada_aberta(self):
        self.context.app.mantenha_e_digite('shift',["tab","tab"])
        self.context.app.digitos("s",("down",2),"tab")
        self.context.app.escrever_direto("FER02776")
        self.context.app.digitos("tab","space")
        self.context.asserts.verifica_tela(self.context.path+"data/images/acaoAbrirManobra.png",60)
        
        self.context.app.clica_imagem(self.context.path+"data/images/flag_manobra.png", 1, "left")
        
        #self.context.app.clica(self.FLAG_MANOBRA,"name",2)
        self.context.app.digitos(("down",3),"enter")
        sleep(3)
        self.context.app.clica(self.EXECUTAR, "name", 3)
        
    def incluir_a_manobra_simulada_fechada(self):
        sleep(5)
        self.context.asserts.verifica_tela(self.context.path+"data/images/manobras_simuladas.png", 50)
        self.context.app.digitos(("tab",3))
        self.context.app.mantenha_e_digite("shift",["tab","tab"])
        self.context.app.digitos("s",("down",2),"tab")
        self.context.app.escrever_direto("FER02776")
        self.context.app.digitos("tab","space",("tab",2),("down",2))
        #self.context.asserts.verifica_tela(self.context.path+"data/images/acaoAbrirManobra.png",60)
        
        self.context.app.clica_imagem(self.context.path+"data/images/flag_manobra.png", 1, "left")
        self.context.app.digitos(("down",3),"enter")
        sleep(3)
        self.context.app.clica(self.EXECUTAR, "name", 3)
        self.context.app.clica(self.CANCELAR, "name", 3)
        sleep(5)
        

class ExecutarManobrasSimuladas(object):
    def __init__(self, context):
        self.context = context
    
    def selecionar_ultima_manobra(self):
        self.context.app.clica_imagem(self.context.path+"data/images/opcao2.png", 1, "left", similar=40)
        self.context.app.clica_imagem(self.context.path+"data/images/executar.png", 1, "left",  similar=40)
        sleep(5)
        
    def manobras_carregadas(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/registroManobrasTemporarias.png", 70)
        sleep(5)


class GerarInterrupcao(object):
    def __init__(self, context):
        self.context = context
    
    def geraInterrupcoes(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/btnInterrupcao.png", 70)
        self.context.app.clica_imagem(self.context.path+"data/images/btnInterrupcao.png", 1, "left")
        sleep(5)
        
    def verifica_interrupcao(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/verificaInterrupcao.png", 70)
        sleep(7)
        
class InterrupcaoConsumidor(object):
    def __init__(self, context):
        self.context = context
        
    def gerar_Interrupcao_Consumidor(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/interrupcaoConsumidor.png", 100)
        self.context.app.clica_imagem(self.context.path+"data/images/interrupcaoConsumidor.png", 1, "left", similar=60)
        
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/gerandoInterrupcoes.png", 70) != None):
            pass        
        
    def verifica_geracao_interrupcao_consumidor(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/interrupcoesPrevistas.png", 100)
        sleep(5)

class FinalizarInterrupcao(object):

    def __init__(self, context):
 
        self.context = context
        
    def clicar_validar_simulacao(self):
        self.context.app.clica_imagem(self.context.path+"data/images/opcao2selecionada.png", 1, "left", similar=60)
        self.context.app.clica_imagem(self.context.path+"data/images/btnvalidaSimulacao.png", 1, "left", similar=60)
        sleep(3)
        self.context.asserts.verifica_tela(self.context.path+"data/images/validaSimulacao.png", 60)
        self.context.app.clica_imagem(self.context.path+"data/images/botao_ok.png", 1, "left", similar=60)        
        sleep(5)
    
    def clicar_em_finalizar_reprogramacao(self):
        self.context.app.clica_imagem(self.context.path+"data/images/opcao2.png", 1, "left", similar=70)
        self.context.app.clica_imagem(self.context.path+"data/images/reprogramacaoManobra.png", 1, "left", similar=70)
        sleep(10)
        
    def volta_selecionar_sr(self):
        self.context.app.clica_imagem(self.context.path+"data/images/viewEntornoSimulacoes.png", 1, "right")
        self.context.app.digitos(("down",6),"enter")
        sleep(5)
        
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Manobras e Ordens de Manobras")
        self.context.app.digitos("enter")
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/registrosManobras.png", 70)
        sleep(10)
                  
                  
    def abrir_view_interrupcoes(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Manobras e Ordens de Manobras")
        self.context.app.digitos("enter")
        
        self.context.asserts.verifica_tela(self.context/path+"data/images/atualizar.png", 80)
        self.context.app.clica_imagem(self.context.path+"data/images/atualizar.png", 1, "left", similar=60)
        sleep(6)
        
class EncerrarServicoRedeMarcadoComoPassado(object):

    def __init__(self, context):
        self.context = context


    def encerrar_servico_rede_passada(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/encerrarServicoRedePassado.png",80)
        self.context.app.clica_imagem(self.context.path+"data/images/encerrarServicoRedePassado.png", 1, "left")
        sleep(4)
        
    def verifica_servico_encerrado(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/informacao.png",70)
        self.context.app.clica_imagem(self.context.path+"data/images/botao_ok.png", 1, "left")

               