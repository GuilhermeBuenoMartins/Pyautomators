# -*- coding: utf-8 -*-
'''
Created on 11 de set de 2018

@author: gcruzm
'''
from time import sleep


class Iniciar_atendimento_da_os_pelo_workflow(object):
    
    def __init__(self, context):
        self.context = context
        
    
    def abrir_view_lista_de_recursos_do_servico_de_rede(self):
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/carregandoBDI.png", 80) != None):
            pass

        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Lista de Recursos")
        self.context.app.digitos("enter")
        
    def selecionando_servico_de_rede_pendente(self):
        self.context.app.clica_imagem(self.context.path+"data/images/janelaIngrid.png", 1, "left", similar=80)
        self.context.app.clica_imagem(self.context.path+"data/images/carregarJanela.png", 1, "left", similar=80)
        self.context.app.clica_imagem(self.context.path+"data/images/outros....png", 1, "left", similar=80)
        sleep(2)
        self.context.app.escreve("texto do filtro de tipos", "Serviços de Rede", "name")
        self.context.app.clica_imagem(self.context.path +"data/images/servicosRedePendentes.png",2, "left", similar=80)
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/refreshServicoPendente.png",60) != None):
            pass
        
        self.context.app.digitos("enter")
        self.context.app.arraste_coordenada(4,76, 81, 704, "left", 4)
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/2017-5582.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/2017-5582.png", 2, "left")
        sleep(2)
    
    def e_selecionando_opcao_iniciar_atendimento_da_ordem_de_servico_pela_equipe(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/despachoVozNegrito.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/despachoVozNegrito.png", 1,"left", similar=60)
        self.context.app.clica_coordenada(1213,555)
        self.context.asserts.verifica_tela(self.context.path+"data/images/inicia_atendimento_da_os_pela_equipe.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/inicia_atendimento_da_os_pela_equipe.png")
        sleep(3)
        self.context.app.clica_imagem(self.context.path+"data/images/botao_ok.png",1,"left", similar=80)
    
class Postergar_o_atendimento_da_os(object):
    
    def __init__(self, context):
        self.context = context
        self.OK = "OK"
        
    def e_selecionar_opcao_adiar(self):
        self.context.app.clica_imagem(self.context.path+"data/images/despachoVozNegrito.png", 1,"left", similar=60)
        self.context.app.clica_coordenada(1213,555)
        self.context.asserts.verifica_tela(self.context.path+"data/images/adiar.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/adiar.png")
    
    def preencher_dados_do_adiar(self):
        self.context.app.digitos("tab","down")
        self.context.app.clica_imagem(self.context.path+"data/images/botao_ok.png", 1, "left", similar=70)
    
    
class Reiniciar_o_atendimento_da_os(object):
    def __init__(self, context):
        self.context = context
        self.OK = "OK"
        
    def e_selecionar_opcao_inicia_deslocamento_ate_o_local_de_atendimento(self):
        self.context.app.clica_imagem(self.context.path+"data/images/despachoVozNegrito.png", 1,"left", similar=60)
        self.context.app.clica_coordenada(1213,555)
        self.context.asserts.verifica_tela(self.context.path+"data/images/inicia_deslocamento_ate_o_local_de_atendimento.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/inicia_deslocamento_ate_o_local_de_atendimento.png")
    
    def concluir_inicio_do_deslocamento(self):
        self.context.app.clica(self.OK,"name",2)
    
class Abertura_manobra(object):
    def __init__(self, context):
        self.context = context
        
    
    def clicar_em_manobras(self):
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/carregandoBDI.png", 80) != None):
            pass
        self.context.app.clica_imagem(self.context.path+"data/images/janelaIngrid.png", 1, "left", similar=80)
        self.context.app.clica_imagem(self.context.path+"data/images/carregarJanela.png", 1, "left", similar=80)
        self.context.app.clica_imagem(self.context.path+"data/images/outros....png", 1, "left", similar=80)
        sleep(2)
        self.context.app.escreve("texto do filtro de tipos", "Serviços de Rede", "name")
        self.context.app.clica_imagem(self.context.path +"data/images/servicoPendente.png",2, "left", similar=80)
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/refreshServicoPendente.png",60) != None):
            pass

        self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD.png",100)
        self.context.app.digitos("down")
        self.context.asserts.verifica_tela(self.context.path+"data/images/manobra.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/manobra.png")
        sleep(8)
    
    def preencher_dados_da_abertura_da_manobra(self):
        self.context.app.mantenha_e_digite("shift","tab","tab")
        self.context.app.digitos("up",("down",18),"tab")
        self.context.app.escrever_direto("TAT01230")
        self.context.app.digitos("tab")
        sleep(2)
        self.context.asserts.verifica_tela(self.context.path+"data/images/execucaoManobra.png",80)
        self.context.app.clica_imagem(self.context.path+"data/images/execucaoManobra.png")

      
class View_interrupcoes(object):
    def __init__(self, context):
        self.context = context
    
    def abrir_view_interrupcoes(self):
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/carregandoBDI.png", 80) != None):
            pass
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Interrup")
        self.context.app.clica_imagem(self.context.path+"data/images/interrupcoes.png",2, "left", similar=80)
    
    def selecionar_servico_de_rede(self):
        self.context.app.clica_imagem(self.context.path+"data/images/janelaIngrid.png", 1, "left", similar=80)
        self.context.app.clica_imagem(self.context.path+"data/images/carregarJanela.png", 1, "left", similar=80)
        self.context.app.clica_imagem(self.context.path+"data/images/outros....png", 1, "left", similar=80)
        sleep(2)
        self.context.app.escreve("texto do filtro de tipos", "Serviços de Rede", "name")
        self.context.app.clica_imagem(self.context.path +"data/images/servicoPendente.png",2, "left", similar=80)
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/refreshServicoPendente.png",60) != None):
            pass
        
        self.context.app.clica_imagem(self.context.path+"data/images/campoPesquisaRotulo.png", 1, "left", similar=80) 
        self.context.app.escrever_direto("2017-3890")
        self.context.app.digitos("enter")
        self.context.app.arraste_coordenada(4,76, 81, 704, "left", 4)
        self.context.asserts.verifica_tela(self.context.path+"data/images/2017-3890.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/viaCC.png")
    
    def atualizar_view_interrupcoes(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/atualizar.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/atualizar.png",1,"left", similar=80)
    
class Fechamento_manobra(object):
    def __init__(self,context):
        self.context = context
    
    def preeencher_dados_do_fechamento_da_manobra(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/acaoFecharManobra.png",80)
        sleep(2)
        self.context.asserts.verifica_tela(self.context.path+"data/images/execucaoManobra.png",80)
        self.context.app.clica_imagem(self.context.path+"data/images/execucaoManobra.png")


class Definir_elemento_de_referencia_da_ordem_de_servico(object):
    def __init__(self, context):
        self.context = context
        self.OK = "OK"
        
    def e_selecionando_opcao_definir_elemento_de_referencia_da_os(self):
        self.context.app.clica_imagem(self.context.path+"data/images/2017-6768.png", 2,"left", similar=80)
        self.context.app.clica_imagem(self.context.path+"data/images/despachoVozNegrito.png", 1,"left", similar=50)
        self.context.app.clica_coordenada(1213,555)
        self.context.asserts.verifica_tela(self.context.path+"data/images/elementoReferencia.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/elementoReferencia.png")
        self.context.app.clica(self.OK,"name")
        self.context.asserts.verifica_tela(self.context.path+"data/images/informacao.png",100)
        self.context.app.clica(self.OK,"name",3)
        

class Definir_causa_da_ordem_de_servico(object):
    def __init__(self, context):
        self.context = context
        self.OK = "OK"

    def e_selecionando_opcao_definir_causa_da_os(self):
        self.context.app.clica_imagem(self.context.path+"data/images/2017-6768.png", 2,"left", similar=80)
        self.context.app.clica_imagem(self.context.path+"data/images/despachoVozNegrito.png", 1,"left", similar=50)
        self.context.app.clica_coordenada(1213,555)
        self.context.asserts.verifica_tela(self.context.path+"data/images/causa.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/causa.png")
        self.context.app.digitos(("tab",2))
        self.context.app.clica(self.OK,"name")
        
      
class Incluir_material_na_ordem_de_servico(object):
    def __init__(self, context):
        self.context = context
        self.SIM = "Sim"
        self.OK = "OK"
    
    def e_selecionando_opcao_material(self):
        self.context.app.clica_imagem(self.context.path+"data/images/2017-6768.png", 2,"left", similar=80)
        self.context.app.clica_imagem(self.context.path+"data/images/despachoVozNegrito.png", 1,"left", similar=50)
        self.context.app.clica_coordenada(1213,555)
        self.context.asserts.verifica_tela(self.context.path+"data/images/material.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/material.png")
    
    def clicar_em_adicao_para_incluir_materiais(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/adicionarMaterial.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/adicionarMaterial.png")
    
    def preencher_dados_da_inclusao_de_material(self):
        self.context.app.digitos(("tab",2),"down","right","down")
        self.context.asserts.verifica_tela(self.context.path+"data/images/quantidadeMaterial.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/quantidadeMaterial.png")
        self.context.app.escrever_direto("1")
        self.context.app.clica(self.SIM,"name",2)
        self.context.app.clica(self.OK,"name",2)
            
class Incluir_um_servico_para_a_ordem_de_servico(object):
    def __init__(self, context):
        self.context = context
        self.OK = "OK"
    
    def e_selecionando_opcao_atividade(self):
        self.context.app.clica_imagem(self.context.path+"data/images/2017-6768.png", 2,"left", similar=80)
        self.context.app.clica_imagem(self.context.path+"data/images/despachoVozNegrito.png", 1,"left", similar=50)
        self.context.app.clica_coordenada(1213,555)
        self.context.asserts.verifica_tela(self.context.path+"data/images/atividade.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/atividade.png")
    
    def clicar_em_adicao_para_incluir_servicos(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/adicionarMaterial.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/adicionarMaterial.png")
        
    def preencher_dados_da_inclusao_de_servico(self):
        self.context.app.digitos(("tab",2),"right","down",("tab",2))
        self.context.app.escrever_direto("1")
        self.context.app.clica(self.OK,"name",2)
        self.context.app.clica(self.OK,"name",2)
        
class Finalizar_atendimento_da_ordem_de_servico(object):
    def __init__(self, context):
        self.context = context
        self.OK = "OK"
      
    def  e_selecionando_opcao_finalizar_atendimento(self):
        self.context.app.clica_imagem(self.context.path+"data/images/2017-6768.png", 2,"left", similar=80)
        self.context.app.clica_imagem(self.context.path+"data/images/despachoVozNegrito.png", 1,"left", similar=50)
        self.context.app.clica_coordenada(1213,555)
        self.context.asserts.verifica_tela(self.context.path+"data/images/finalizaOS.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/finalizaOS.png")
        self.context.app.clica(self.OK,"name",5)
    