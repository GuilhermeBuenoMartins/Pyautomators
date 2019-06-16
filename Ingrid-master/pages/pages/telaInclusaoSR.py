# -*- coding: utf-8 -*- ]
'''
Created on 22 de out de 2018

@author: vgama
'''
from time import sleep
from Pyautomators import Dados 
from Pyautomators import Inspecionador
from Pyautomators import Documentacao
from Pyautomators.Ambiente import path_atual
import logging


class CriarEvento(object):
    '''
    classdocs
    '''
    def __init__(self, context):
        '''
        Constructor
        '''
        self.context = context
        self.SERVICO_PENDENTE = "Serviços de Rede"
        self.JANELA = "Janela"
        
    def abrirEvento(self):
        
        self.context.app.clica(self.JANELA,"name", 3)
        self.context.app.digitos(("down",3),"right","down","enter")
        
        self.context.app.escreve("texto do filtro de tipos", self.SERVICO_PENDENTE,"name")
        sleep(2)
        self.context.app.clica_imagem(self.context.path+"data/images/servico_rede.png", 2, "left", similar = 50)
        self.context.asserts.verifica_tela(self.context.path+"data/images/servicoRedeView.png",80)
        self.context.app.clica_imagem(self.context.path+"data/images/novoServicoRede.png", 1, "left", similar = 70)
        sleep(3)
        self.context.app.digitos("enter")
    
    def preencheCampos(self):
        sleep(10)
        self.context.app.digitos("down","tab","down")
        self.context.asserts.verifica_tela(self.context.path +"data/images/campoElemento.png", 50)
        self.context.app.clica_imagem(self.context.path +"data/images/campoElemento.png",1 )
        self.context.app.digitos(("down", 18),"tab")
        self.context.app.escrever_direto("TAT01230")
        self.context.app.digitos("tab","enter")
        
    
    def concluir_e_verifica(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/concluir2.png",80)
        self.context.app.clica_imagem(self.context.path+"data/images/concluir2.png", 1, "left")
        
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/informacao.png", 50) == None):
            pass
        
        aux = self.context.app.elemento_list('Static','class', 1)
        logging.info(vars(aux))
        
        sleep(3)
        self.context.app.digitos("enter")
        
class ServicoRede(object):

    def __init__(self, context):
        self.context = context
        self.OK = "OK"
        
    def abrir_view_servicos_pendentes(self):
         
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/carregandoBDI.png", 50) != None):
            pass
        
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Redes Pendentes")
        sleep(2)         
        self.context.app.digitos("enter")
        
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/refreshServicoPendente.png", 50) != None):
            pass
            
    def servicoRede(self):
        self.context.app.combo_digitos("ctrl",'3')
        sleep(5)
        self.context.app.escrever_direto("Recursos Propostos")
        self.context.app.digitos("enter")
        
        self.context.asserts.verifica_tela(self.context.path + "data/images/recursosPropostoView.png", 80)
        self.context.app.arraste_coordenada(299,76, 344,728, "left", 3)
        
        self.context.app.clica_imagem(self.context.path+"data/images/srvPendentes.png", 1, "left", similar=60)
        self.context.app.digitos("down", ("up",3))
        sleep(5)
        
    
    def arrastaServico(self):
        self.context.app.clica_imagem(self.context.path+"data/images/encontrarSR.png", 2, "left", similar=50)
        self.context.app.arraste_coordenada(None, None, 33, 671, "left", 3)
        self.context.asserts.verifica_tela(self.context.path + "data/images/despacho.png", 10)
        self.context.app.digitos("enter")
        sleep(5)
    
    def verificar_despacho(self):
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/erroDespachar.png",60) != None ):
            raise NameError('Erro ao despachar')
    
        elif(self.context.asserts.verifica_tela(self.context.path+"data/images/despachadaSucesso.png",70) != None):
            self.context.app.digitos(self.OK,"name",2)
        
class IncidenciaAtendimento(object):

    def __init__(self, context):
        '''
        Constructor
        '''
        self.context = context
        
    def monobrar(self):    
        self.context.app.digitos("down")
        sleep(3)
        self.context.app.clica_imagem(self.context.path + "data/images/manobra.png", 1, "left")
        sleep(6)
        self.context.asserts.verifica_tela(self.context.path + "data/images/manobraServicoRede.png", 80)
        
        #VERIFICA CAMPOS PREENCHIDOS
        if(self.context.asserts.verifica_tela(self.context.path + "data/images/campoElementoManobra.png", 50)):
            self.context.app.mantenha_e_digite("shift","tab", "tab")
            self.context.app.digitos(("down",18),"tab")
            self.context.app.escrever_direto("AGI01675")
            self.context.app.digitos("tab")
            self.context.asserts.verifica_tela(self.context.path + "data/images/execucaoManobra.png", 80)
            self.context.app.clica_imagem(self.context.path+"data/images/execucaoManobra.png", 1, "left", similar=60)
            sleep(3)
            #VERIFICA SE A MANOBRA FOI ASSOCIADA
            while(self.context.asserts.verifica_tela(self.context.path + "data/images/campoElementoManobra.png", 70, similaridade=50) == None):
                pass
            
            sleep(4)
            self.context.app.clica_imagem(self.context.path+"data/images/cancelarManobras.png", 1, "left", similar=60)
            
            
        else:
            self.context.asserts.verifica_tela(self.context.path + "data/images/execucaoManobra.png", 80)
            self.context.app.clica_imagem(self.context.path+"data/images/execucaoManobra.png", 1, "left", similar=60)
            sleep(3)
            #VERIFICA SE A MANOBRA FOI ASSOCIADA
            while(self.context.asserts.verifica_tela(self.context.path + "data/images/campoElementoManobra.png", 60, similaridade=50) == None):
                pass
            sleep(5)
            self.context.app.clica_imagem(self.context.path+"data/images/cancelarManobras.png", 1, "left", similar=60)
            
            
    def atendimentoOS(self):
        self.context.app.clica_imagem(self.context.path+"data/images/srvPendentes.png", 1, "left", similar =60)
        sleep(5)
        self.context.app.clica_imagem(self.context.path + "data/images/atendimentoUnico.png", 1, "left", similar=60)
        self.context.app.clica("OK", "name", 5)
        sleep(5)
        
    def verifica_atendimento_executado(self):
        self.context.asserts.verifica_tela(self.context.path + "data/images/processandoAtendimento.png", 80)
        sleep(5)
        
        
        
class STDTransformador(object):
    
    def __init__(self, context):
        
        self.context = context
        
    
    def abrir_View_Servico_Rede(self):
        
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/carregandoBDI.png", 50) != None):
            pass
        
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Rede")
        sleep(2)         
        self.context.app.clica_imagem(self.context.path+"data/images/opcaoServicoRede.png", 2, "left", similar=60)
        sleep(5)
    
    def abrir_Nova_Ordem_Servico(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/servicoRedeView.png", 50,similaridade=80)
        self.context.app.clica_imagem(self.context.path+"data/images/ordemServicos.png", 1, "left", similar=80)
        
    def preenche_dados_tipo_std_transformador(self):
        sleep(10)
        self.context.app.mantenha_e_digite("shift",["tab","tab","tab","tab"])
        self.context.app.combo_digitos("alt","down")
        sleep(5)        
        self.context.app.escrever_direto("S")
        self.context.app.digitos(("down",3),"enter")
        
    
    def preenche_dados_finais(self):
        
        self.context.app.digitos("tab","down","tab",("down",18),"tab")
        self.context.app.escrever_direto("TAT01230")
        self.context.app.digitos("tab")
        sleep(5)
        self.context.app.clica_imagem(self.context.path+"data/images/concluir2.png", 1, "left")
        sleep(4)
        
    def verifica_ordem_servico_criada(self):
        
        self.context.asserts.verifica_tela(self.context.path + "data/images/concluido.png",20, similaridade=80)   
        self.context.app.digitos("enter")
                
    def abri_view_recursos_propostos(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Recursos Propostos")
        self.context.app.digitos("enter")
        sleep(5)
        self.context.asserts.verifica_tela(self.context.path + "data/images/recursosPropostoView.png", 80)
        self.context.app.arraste_coordenada(299,76, 344,728, "left", 3)
        
    def clicar_servico_rede_pendente_transformador(self):
        self.context.app.clica_imagem(self.context.path+"data/images/srvPendentes.png",1,"left", similar=80)
        self.context.app.digitos(("tab",17))
        self.context.app.escrever_direto("2019")
        sleep(4)
        self.context.app.clica_imagem(self.context.path+"data/images/stdTransformador.png", 2, "left", similar=80)
        sleep(5)
        
    def arrasta_para_equipe(self):
        
        self.context.app.arraste_coordenada(None,None, 33, 671, "left",3)
        sleep(4)
        self.context.app.digitos("enter")
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/despachoConcluido.png", 50) != None):
            self.context.app.clica("OK","name",4)
            
    def realiza_atendimento(self):
        self.context.app.clica_imagem(self.context.path+"data/images/atendimento.png", 1, "left", similar=80)
        
        sleep(4)
        self.context.app.clica("OK","name",5)
        
    def verifica_finalizacao_atendimento(self):
        self.context.app.verifica_tela(self.context.path+"data/images/processandoAtendimento.png",30)
        sleep(5)
        
    def atendimento_std_transformador(self):
        self.context.app.digitos(("tab",17))
        self.context.app.escrever_direto("2019")
        sleep(4)
        self.context.app.arraste_coordenada( 28, 678, 110, 678, "left", 3)
        self.context.app.clica_imagem(self.context.path+"data/images/stdTransformador.png", 2, "left", similar=80)
        sleep(5)
            
        
        
class STDDiversos(object):
    
    def __init__(self, context):
        
        self.context = context        

    def preenche_dados_tipo_std_diversos(self):
            sleep(10)
            self.context.app.mantenha_e_digite("shift",["tab","tab","tab","tab"])
            self.context.app.combo_digitos("alt","down")
            sleep(5)        
            self.context.app.escrever_direto("S")
            self.context.app.digitos("enter")
            
    def clicar_servico_rede_pendente_diversos(self):
        self.context.app.clica_imagem(self.context.path+"data/images/srvPendentes.png",1,"left", similar=80)
        self.context.app.digitos(("tab",17))
        self.context.app.escrever_direto("2019")
        sleep(4)
        self.context.app.arraste_coordenada( 28, 678, 110, 678, "left", 3)
        self.context.app.clica_imagem(self.context.path+"data/images/stdDiversos.png", 2, "left", similar=80)
        sleep(5)
        
    def arrasta_std_diversos_para_equipe(self):
                
        self.context.app.arraste_coordenada(None,None, 1014,255, "left",3)
        sleep(4)
        self.context.app.digitos("enter")
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/despachoConcluido.png", 50) != None):
            self.context.app.clica("OK","name",4)
            
    def atendimento_std_diversos(self):
        self.context.app.digitos(("tab",17))
        self.context.app.escrever_direto("2018")
        sleep(4)
        self.context.app.arraste_coordenada( 28, 678, 110, 678, "left", 3)
        self.context.app.clica_imagem(self.context.path+"data/images/stdDiversos.png", 2, "left", similar=80)
        sleep(5)
            
class STDRedeDistribuicao(object):
    
    def __init__(self, context):
        
        self.context = context        

    def preenche_dados_tipo_std_rede_distribuicao(self):
            sleep(10)
            self.context.app.mantenha_e_digite("shift",["tab","tab","tab","tab"])
            self.context.app.combo_digitos("alt","down")
            sleep(5)        
            self.context.app.escrever_direto("S")
            self.context.app.digitos("down","enter")
            
    def clicar_servico_rede_pendente_rede_distribuicao(self):
        self.context.app.clica_imagem(self.context.path+"data/images/srvPendentes.png",1,"left", similar=80)
        self.context.app.digitos(("tab",17))
        self.context.app.escrever_direto("2018")
        sleep(4)
        self.context.app.arraste_coordenada( 28, 678, 110, 678, "left", 3)
        if(self.context.asserts.verifica_tela(self.context.path + "data/images/stdRedeDistribuicao.png",80) == None):
            STDTransformador.abrir_Nova_Ordem_Servico(self)
            STDRedeDistribuicao.preenche_dados_tipo_std_rede_distribuicao(self)
            STDTransformador.preenche_dados_finais(self)
            STDTransformador.verifica_ordem_servico_criada(self)
            sleep(7)
            
        self.context.app.clica_imagem(self.context.path+"data/images/stdRedeDistribuicao.png", 2, "left", similar=80)
        sleep(5)
        
    def arrasta_std_rede_distribuicao_para_equipe(self):
                
        self.context.app.arraste_coordenada(None,None, 1014,255, "left",3)
        sleep(4)
        self.context.app.digitos("enter")
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/despachoConcluido.png", 50) != None):
            self.context.app.clica("OK","name",4)
    
            
    def atendimento_std_rede_distribuicao(self):
        self.context.app.digitos(("tab",17))
        self.context.app.escrever_direto("2018")
        sleep(4)
        self.context.app.arraste_coordenada( 28, 678, 110, 678, "left", 3)
        if(self.context.asserts.verifica_tela(self.context.path + "data/images/stdRedeDistribuicao.png",80) == None):
            STDTransformador.abrir_Nova_Ordem_Servico(self)
            STDRedeDistribuicao.preenche_dados_tipo_std_rede_distribuicao(self)
            STDTransformador.preenche_dados_finais(self)
            STDTransformador.verifica_ordem_servico_criada(self)
            STDTransformador.abri_view_recursos_propostos(self)
            self.context.app.clica_imagem(self.context.path+"data/images/stdRedeDistribuicao.png", 2, "left", similar=80)
            STDRedeDistribuicao.arrasta_std_rede_distribuicao_para_equipe(self)
            sleep(7)
        else:
            self.context.app.clica_imagem(self.context.path+"data/images/stdRedeDistribuicao.png", 2, "left", similar=80)
        sleep(5)
        
class STDSubestacao(object):
    
    def __init__(self, context):
        
        self.context = context        
        
        
    def preenche_dados_tipo_std_subestacao(self):
            sleep(10)
            self.context.app.mantenha_e_digite("shift",["tab","tab","tab","tab"])
            self.context.app.combo_digitos("alt","down")
            sleep(5)        
            self.context.app.escrever_direto("S")
            self.context.app.digitos(("down",2),"enter")
    
    def clicar_servico_rede_pendente_subestacao(self):
        self.context.app.clica_imagem(self.context.path+"data/images/srvPendentes.png",1,"left", similar=80)
        self.context.app.digitos(("tab",17))
        self.context.app.escrever_direto("2018")
        sleep(4)
        self.context.app.arraste_coordenada( 28, 678, 110, 678, "left", 3)
        if(self.context.asserts.verifica_tela(self.context.path + "data/images/stdSubestacao.png",80) == None):
            STDTransformador.abrir_Nova_Ordem_Servico(self)
            STDSubestacao.preenche_dados_tipo_std_subestacao(self)
            STDTransformador.preenche_dados_finais(self)
            STDTransformador.verifica_ordem_servico_criada(self)
            sleep(7)
            
        self.context.app.clica_imagem(self.context.path+"data/images/stdSubestacao.png", 2, "left", similar=80)
        sleep(5)
    
    def arrasta_std_estacao_para_equipe(self):
                
        self.context.app.arraste_coordenada(None,None, 1014,255, "left",3)
        sleep(4)
        self.context.app.digitos("enter")
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/despachoConcluido.png", 50) != None):
            self.context.app.clica("OK","name",4)
            
    def atendimento_std_subestacao(self):
        self.context.app.digitos(("tab",17))
        self.context.app.escrever_direto("2018")
        sleep(4)
        self.context.app.arraste_coordenada( 28, 678, 110, 678, "left", 3)
        if(self.context.asserts.verifica_tela(self.context.path + "data/images/stdSubestacao.png",80) == None):
            STDTransformador.abrir_Nova_Ordem_Servico(self)
            STDSubestacao.preenche_dados_tipo_std_subestacao(self)
            STDTransformador.preenche_dados_finais(self)
            STDTransformador.verifica_ordem_servico_criada(self)
            STDTransformador.abri_view_recursos_propostos(self)
            self.context.app.clica_imagem(self.context.path+"data/images/stdSubestacao.png", 2, "left", similar=80)
            STDSubestacao.arrasta_std_estacao_para_equipe(self)
            sleep(7)
        else:
            self.context.app.clica_imagem(self.context.path+"data/images/stdSubestacao.png", 2, "left", similar=80)
        sleep(5)


class Evento_rede_nao_programado(object):
    def __init__(self, context):
        self.context = context
        self.OK = "OK"
        self.CONCLUIR = "Concluir"
        self.ATENDIMENTO_UNICO = "Atendimento Único"
        self.Descricao = "Descrição Tipo"
    
    def preencher_dados_nao_programado(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/novo_evento_rede.png",100)
        self.context.app.digitos("n","tab","down")
        self.context.asserts.verifica_tela(self.context.path+"data/images/tipoelemente.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/tipoelemente.png")
        self.context.app.digitos("down",("t",2),"tab")
        self.context.app.escrever_direto("TAT01230")
        self.context.app.digitos("tab","space")
        self.context.app.clica(self.CONCLUIR,"name",2)
        self.context.asserts.verifica_tela(self.context.path+"data/images/informacao.png",100)
        self.context.app.clica(self.OK,"name",2)
    
    def verifica_evento_nao_programado(self):
        self.context.asserts.verifica_tela(self.context.path + "data/images/informacao.png", 100)
        sleep(3)
        self.context.app.digitos("enter")
        
    def selecionar_evento_rede_criado(self):
        self.context.app.clica(self.Descricao, "name", 2)
        self.context.app.clica_imagem(self.context.path+"data/images/atuacaoNaoProgramada.png",1,"left", similar=60)
        sleep(4)
        
    def seleciono_evento_atuacao(self):
        self.context.app.clica_imagem(self.context.path+"data/images/campoPesquisaRotulo.png", 1, "left")
        self.context.app.escrever_direto("2016-586797")
        self.context.app.digitos("tab","down")
        sleep(4)        
     
    
class Evento_rede_programado(object):
    def __init__(self, context):
        self.context = context
        self.CONCLUIR = "Concluir"
        self.OK = "OK"
        self.Descricao = "Descrição Tipo"
        
        
    def preencher_dados_programado(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/novo_evento_rede.png",100)
        self.context.app.digitos("p","tab","down")
        self.context.app.digitos(("tab",3))
        self.context.app.combo_digitos("alt","down")
        self.context.app.digitos("right","enter",("tab",2))
        self.context.app.combo_digitos("alt","down")
        self.context.app.digitos(("right",2),"enter")
        self.context.asserts.verifica_tela(self.context.path+"data/images/tipoelemente.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/tipoelemente.png")
        self.context.app.digitos("down",("t",2),"tab")
        self.context.app.escrever_direto("TAT01230")
        self.context.app.digitos("tab","space")
        sleep(5)
        self.context.app.clica(self.CONCLUIR,"name",2)
        self.context.asserts.verifica_tela(self.context.path+"data/images/informacao.png",100)
        self.context.app.clica(self.OK,"name",2)
        
    def selecionar_evento_atuacao_programado(self):
        self.context.app.clica(self.Descricao, "name", 2)
        self.context.app.clica_imagem(self.context.path+"data/images/atuacaoProgramada.png",1,"left", similar=60)
        sleep(4)
          
    def selecionar_opcao_novo_servico_rede_evento_rede_programado(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD.png")
        self.context.asserts.verifica_tela(self.context.path+"data/images/criar_servico_rede.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/criar_servico_rede.png")
        self.context.asserts.verifica_tela(self.context.path+"data/images/ok.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/ok.png")
   
    def seleciono_evento_atuacao_programado(self):
        self.context.app.clica_imagem(self.context.path+"data/images/campoPesquisaRotulo.png", 1, "left")
        self.context.app.escrever_direto("2018-9879")
        self.context.app.digitos("tab","down")
        sleep(4)      
        
    
