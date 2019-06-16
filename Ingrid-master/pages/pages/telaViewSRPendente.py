# -*- coding: utf-8 -*-
'''
Created on 17 de jul de 2018
@author: gdiamante

Modified on 09 de jan de 2019
@author: gcruzm
'''

from time import sleep

class Ordenacao_das_colunas(object):
    def __init__(self,context):
        self.context=context
        self.COR = "Cor"
        self.ERRO_INTEGRACAO = "Erro Integração"
        self.ORIGEM = "Origem"
        self.ROTULO = "Rótulo"
        self.PRE_DESPACHO = "Pré-despacho"
        self.EQUIPE = "Equipe"
        self.QTD_EQUIPES = "Quantidade de Equipes"
        self.ASSOCIACAO = "Associação"
        self.SIGLA_TIPO = "Sigla Tipo"
        self.SIGLA_SUBTIPO = "Sigla Subtipo"
        self.DESCRICAO_TIPO = "Descrição Tipo"
        self.MULTA_ATUAL = "Multa Atual"
        self.JANELA = "Janela"

    def Abrir_view_servico_de_rede_pendente(self):
        
        self.context.app.clica(self.JANELA, "name", 3)
        self.context.app.digitos(("down",3),"right", "down", "enter")
        self.context.app.escreve("texto do filtro de tipos","Serviços de Rede Pendentes","name")
        self.context.app.digitos(("down",2),"enter")
        #self.context.asserts.verifica_tela(self.context.path+"data/images/servicosRedesPendentes.png",100)
        #self.context.app.clica_imagem(self.context.path+"data/images/servicosRedesPendentes.png",1,"left")
        #self.context.app.digitos("enter")
        
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/refreshServicoPendente.png", 50) != None):
            pass

    def Realizar_ordenacao_das_colunas(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD.png",100)
        
        '''COR'''
        self.context.app.clica(self.COR, "name", 5)
        sleep(2)
        self.context.app.clica(self.ERRO_INTEGRACAO,"name",5)
    
        '''Erro de integracao'''
        self.context.app.clica("Erro Integração","name",2)
        sleep(2)
        self.context.app.clica("Erro Integração","name",2)
        
        '''Origem'''
        self.context.app.clica(self.ORIGEM,"name",2)
        sleep(2)
        self.context.app.clica(self.ORIGEM,"name",2)
        
        '''Rotulo'''
        self.context.app.clica(self.ROTULO,"name",2)
        sleep(2)
        self.context.app.clica(self.ROTULO,"name",2)
        
        '''Pre despacho'''
        self.context.app.clica(self.PRE_DESPACHO,"name",2)
        sleep(2)
        self.context.app.clica(self.PRE_DESPACHO,"name",2)
        
        '''Equipe'''
        self.context.app.clica(self.EQUIPE,"name",2)
        sleep(2)
        self.context.app.clica(self.EQUIPE,"name",2)
        
        '''Qnt de equipes'''
        self.context.app.clica(self.QTD_EQUIPES,"name",2)
        sleep(2)
        self.context.app.clica(self.QTD_EQUIPES,"name",2)
        
        '''Associacao'''
        self.context.app.clica(self.ASSOCIACAO,"name",2)
        sleep(2)
        self.context.app.clica(self.ASSOCIACAO,"name",2)
        
        '''Sigla tipo'''
        self.context.app.clica(self.SIGLA_TIPO,"name",2)
        sleep(2)
        self.context.app.clica(self.SIGLA_TIPO,"name",2)
        
        '''Sigla Subtipo'''
        self.context.app.clica(self.SIGLA_SUBTIPO,"name",2)
        sleep(2)
        self.context.app.clica(self.SIGLA_SUBTIPO,"name",2)
        
        '''Descricao tipo'''
        self.context.app.clica(self.DESCRICAO_TIPO,"name",2)
        sleep(2)
        self.context.app.clica(self.DESCRICAO_TIPO,"name",2)
        
        '''Multa atual'''
        self.context.app.clica(self.MULTA_ATUAL,"name",2)
        sleep(2)
        self.context.app.clica(self.MULTA_ATUAL,"name",2)
        
        
class Criar_filtros(object):
    def __init__(self,context):
        self.context=context
        self.CONFIGURAR_FILTRO = "Configurar Filtro..."
        self.NOVO = "Novo"
        self.OK = "OK"
        self.ORDEM_DE_SERVICO_GERAL = "Ordem de Serviço - Geral"
        self.SIM = "Sim"
    
    def clicar_na_seta_pra_baixo(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD.png",100)
        self.context.asserts.verifica_tela(self.context.path+"data/images/seta_pra_baixo.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/seta_pra_baixo.png")
        #self.context.app.clica_coordenada(1007,107)
        sleep(5)
    
    def selecionar_opcao_configurar_filtro(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/configurar_filtro.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/configurar_filtro.png",2,"left")
        sleep(4)
    
    def clicar_no_botao_novo(self):
        self.context.app.clica(self.NOVO,"name",2)
        self.context.app.escrever_direto("Teste automatizado do InGrid")
        self.context.app.clica(self.OK,"name",2)
        self.context.app.clica(self.ORDEM_DE_SERVICO_GERAL,"name",2)
        self.context.app.clica(self.OK,"name",2)
        self.context.app.arraste_coordenada(1014,170,1009,303,"left",5)
        self.context.app.clica(self.SIM,"name",2)
        self.context.app.digitos("space")
        sleep(3)
        self.context.app.clica(self.OK,"name",2)
        
    
class Propriedades_da_view(object):
    def __init__(self,context):
        self.context=context
        self.PROPRIEDADES = "Propriedades"
    def selecionar_um_servico_de_rede_pendente(self):
        self.context.app.clica_imagem(self.context.path+"data/images/campoPesquisaRotulo.png", 1, "left", similar=60)
        self.context.app.escrever_direto("2017-6719")
        self.context.asserts.verifica_tela(self.context.path+"data/images/2017-6719_nao_selecionado.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/2017-6719_nao_selecionado.png", 1, "left", similar=80)
        self.context.app.digitos("enter")
        sleep(3)
    
    def abrir_view_propriedades_da_view(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("propriedades")
        self.context.app.digitos("enter")
        sleep(4)
        
    def verificar_informacoes_do_servico_de_rede(self):
        self.context.app.arraste_coordenada(1350,533,1359,668,"left",5)
        self.context.app.arraste_coordenada(204,687,787,696,"left",5)
        