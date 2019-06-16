# -*- coding: utf-8 -*-
'''
Created on 14 de jun de 2018

@author: gcruzm
'''

from time import sleep
import pyautogui

class CriarOS(object):
    '''
    classdocs
    '''

    def __init__(self,context):
        self.context=context
        self.OK = "OK"
    
    def abreViewRestricaoOperativa(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("restri")
        self.context.app.digitos("enter")
        self.context.asserts.verifica_tela(self.context.path+"data/images/viewRestricaoOperativa.png",100)
    
    def criar_restricao_operativa(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/criarRestricaoOperativa.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/criarRestricaoOperativa.png")
    
    def preencher_dados_criacao_subestacao(self):
        self.context.app.mantenha_e_digite("shift",["tab","tab"])
        self.context.app.digitos(("down",17 ),"tab")
        self.context.app.escrever_direto("ATI01")
        self.context.app.digitos(("tab",2),"down","tab","down","tab")
        self.context.app.escrever_direto("testando com subestacao")
 
    def concluir_criacao_restricao_operativa(self):
        self.context.app.clica(self.OK,"name",2)
        
    def preencher_dados_criacao_transformador(self):
        self.context.app.mantenha_e_digite("shift",["tab","tab"])
        self.context.app.digitos("t","tab")
        self.context.app.escrever_direto("TAT01230")
        self.context.app.digitos(("tab",2),"down","tab","down","tab")
        self.context.app.escrever_direto("teste sem subestacao")
        self.context.app.clica(self.OK,"name",2)
    
        
class Atender_encerrar_subestacao_transformador(object):
    
    def __init__(self,context):
        self.context=context
    
    def listar_restricao_operativa_subestacao(self):    
        self.context.asserts.verifica_tela(self.context.path+"data/images/listar_matricula.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/listar_matricula.png",1)
        self.context.app.escrever_direto("ATI01")
        sleep(5)
    
    def listar_restricao_operativa_transformador(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/listar_matricula.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/listar_matricula.png",1)
        self.context.app.escrever_direto("TAT01230")
        sleep(5)
        
class Incluir_editar_restricao_operativa(object):
    
    def __init__(self, context):
        self.context = context
        self.OK = "OK"
        
    def buscar_restricao_operativa(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/viewRestricoesOperativas2.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/viewRestricoesOperativas2.png",1,"left")
        self.context.app.digitos(("down",3))
        sleep(3)
        

    def modificar_restricao_operativa(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/editarRestricaoOperativa.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/editarRestricaoOperativa.png",1,"left", similar=70)
        self.context.app.digitos(("tab",3))
        sleep(4)
        self.context.app.escrever_direto("teste de modificacao")
        self.context.app.clica(self.OK,"name",2)
        self.context.asserts.verifica_tela(self.context.path+"data/images/informacao.png",110)
        
class Ordenacao_de_colunas(object):
    
    def __init__(self, context):
        self.context = context
        self.SUBESTACAO_MATRICULA = "Subestação Matrícula"
        self.ALIMENTADOR_MATRICULA = "Alimentador Matrícula"
        self.TIPO_ELEMENTO = "Tipo Elemento"
        self.DATA_INICIO = "Data Início"
        self.DATA_FIM_PREVISTA = "Data Fim Previsto"
        self.DATA_FIM = "Data Fim"
        self.OBSERVAC0ES = "Observações"
        self.RESPONSAVEL_ABERTURA = "Responsável Abertura"
        self.RESPONSAVEL_ENCERRAMENTO ="Responsável Encerramento"
        self.ESTADO = "Estado"
        self.MOTIVO = "Motivo"
        
    def realizar_ordenacao_das_colunas_subestacaoMatricula(self):
        #self.context.asserts.verifica_tela(self.context.path+"data/images/subestacaoMatricula.png",80)
        self.context.app.clica(self.SUBESTACAO_MATRICULA,"name",2)
        self.context.app.clica(self.SUBESTACAO_MATRICULA,"name",2)
       
    def realizar_ordenacao_da_coluna_alimentador_matricula(self):
        #self.context.asserts.verifica_tela(self.context.path+"data/images/alimentadorMatricula.png",80)
        self.context.app.clica(self.ALIMENTADOR_MATRICULA,"name",2)
        self.context.app.clica(self.ALIMENTADOR_MATRICULA,"name",2) 
    
    def realizar_ordenacao_da_coluna_tipo_elemento(self):
        #self.context.asserts.verifica_tela(self.context.path+"data/images/tipoElemento.png",80)
        self.context.app.clica(self.TIPO_ELEMENTO,"name",2)
        self.context.app.clica(self.TIPO_ELEMENTO,"name",2)
      
    
    def realizar_ordenacao_da_coluna_matricula(self):
        #self.context.asserts.verifica_tela(self.context.path+"data/images/matricula.png",80)
        self.context.app.clica_imagem(self.context.path+"data/images/matriculaOrdenacao.png", 2,"left", similar=60)
    
    def realizar_ordenacao_da_coluna_data_inicio(self):
        #self.context.asserts.verifica_tela(self.context.path+"data/images/data_inicio.png",80)
        self.context.app.clica(self.DATA_INICIO,"name",2)
        self.context.app.clica(self.DATA_INICIO,"name",2)
        
    
    def realizar_ordenacao_da_coluna_data_fim_previsto(self):
        #self.context.asserts.verifica_tela(self.context.path+"data/images/data_fim_previsto.png",80)
        self.context.app.arraste_coordenada(28, 678, 563, 678, "left")
        
        self.context.app.clica(self.DATA_FIM_PREVISTA,"name",2)
        self.context.app.clica(self.DATA_FIM_PREVISTA,"name",2)
        
        
    def realizar_ordenacao_da_coluna_data_fim(self):
        self.context.app.clica(self.DATA_FIM,"name",2)
        self.context.app.clica(self.DATA_FIM,"name",2)
        
    def realizar_ordenacao_da_coluna_observacao(self):
        #self.context.asserts.verifica_tela(self.context.path+"data/images/observacoe.png",80)
        self.context.app.clica(self.OBSERVAC0ES,"name",2)
        self.context.app.clica(self.OBSERVAC0ES,"name",2)
        
        
    def realizar_ordenaca_da_coluna_responsavel_aberta(self):
        #self.context.asserts.verifica_tela(self.context.path+"data/images/responsavelAbertura.png",80)
        self.context.app.clica(self.RESPONSAVEL_ABERTURA,"name",2)
        self.context.app.clica(self.RESPONSAVEL_ABERTURA,"name",2)
        
    
    def realizar_ordenaca_da_coluna_responsavel_encerramento(self):
        #self.context.asserts.verifica_tela(self.context.path+"data/images/responsavelEncerramento.png",80)
        self.context.app.clica(self.RESPONSAVEL_ENCERRAMENTO,"name",2)
        self.context.app.clica(self.RESPONSAVEL_ENCERRAMENTO,"name",2)
    
    def realizar_ordenaca_da_coluna_estado(self):
        #self.context.asserts.verifica_tela(self.context.path+"data/images/estado.png",80)
        self.context.app.clica(self.ESTADO,"name",2)
        self.context.app.clica(self.ESTADO,"name",2)
        
    def realizar_ordenaca_da_coluna_motivo(self):
        #self.context.asserts.verifica_tela(self.context.path+"data/images/motivo.png",80)
        self.context.app.clica(self.MOTIVO,"name",2)
        self.context.app.clica(self.MOTIVO,"name",2)
        
class Localizar_restricao_operativa_graficamente(object):
    
    def __init__(self, context):
        self.context = context
        self.LOCALIZAR = "Localizar Elemento Graficamente"
    
    def selecionar_restricao_operativa_existente(self):
        self.context.app.digitos(("down",2))
        
    def selecionar_icone_localizar_elemento_graficamente(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/localizarElementoGraficamente.png",100, similaridade=60)
        self.context.app.clica(self.LOCALIZAR, "name",2)
        sleep(5)
        self.context.asserts.verifica_tela(self.context.path+"data/images/sinalizarElementor.png",100, similaridade=60)

       
class BuscaOperativa(object):

    def __init__(self, context):

        self.context = context
        self.MATRICULA = "Matrícula"
        self.TIPOELEMENTO = "Tipo Elemento"
        self.RESPONSAVEL = "Responsável"
            
    def abrirView(self):
        self.context.app.combo_digitos("ctrl","3")
        sleep(4)
        self.context.app.escrever_direto("Restri")
        self.context.app.digitos("enter")
        sleep(10)
        
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/retricaoOperativa.png", 50) != None):
            pass
        
    def buscarElemento(self):
        self.context.app.clica(self.MATRICULA, "name",3)
        sleep(3)
        self.context.app.clica_imagem(self.context.path+"data/images/buscaTipoElemento.png", 1, "left") 
        self.context.app.escrever_direto("Seccionador")
        
    def verificaElemento(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/seccionador.png",100)
        sleep(5)
        
    def buscarResponsavel(self):
        self.context.app.clica(self.TIPOELEMENTO, "name",3)
        sleep(3)
        self.context.app.clica_imagem(self.context.path+"data/images/buscaResponsavel.png", 1, "left")
        self.context.app.escrever_direto("302568")
    
    def verificaResponsalvel(self):            
        self.context.asserts.verifica_tela(self.context.path+"data/images/responsavel.png",100)
        sleep(5)
        
        
    def buscarMatricula(self):
        self.context.app.clica(self.RESPONSAVEL, "name",3)
        sleep(3)
        self.context.app.clica_imagem(self.context.path+"data/images/buscaMatricula.png", 1, "left")
        self.context.app.escrever_direto("AGI02402")
        
     
    def verificaMatricula(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/matricula.png",100)
        sleep(5)


class Encerrar_restricao_operativa(object):
    
    def __init__(self, context):
        self.context = context
        self.OK = "OK"
        self.Matricula = "Matrícula"
    
    def selecionar_restricao_operativa_pendente(self):
        self.context.app.clica(self.Matricula, "name", 3)
        sleep(3)
        self.context.app.digitos("down","enter")
        self.context.app.escrever_direto("Pendente")
        sleep(4)
        self.context.app.digitos("tab", ("down",2))
    
    
    def clicar_no_icone_encerrar_restricao_operativa(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/encerrarRestricaoOperativa.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/encerrarRestricaoOperativa.png", 1, "left", similar=70)
        self.context.app.clica(self.OK,"name",3)
        sleep(4)
