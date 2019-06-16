# -*- coding: utf-8 -*-
'''
Created on 26 de nov de 2018

@author: gcruzm
'''
from time import sleep

class Criacao_de_aviso(object):
    def __init__(self, context):
        self.context = context
        self.NOME_DO_CLIENTE = "GABRIEL"
        self.TELEFONE_DO_CLIENTE = "99999999999"
        self.ATENCAO_DE_AVISOS = "Atenção de Avisos"
        self.CLIENTES_NORMAL = "0 - CLIENTES NORMAL"
        self.NOVO_AVISO = "Novo Aviso"
        self.CONCLUIR = "Concluir"
        self.OK = "OK"
        
    def abrir_perspectiva_atencao_de_avisos(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Aten")
        self.context.asserts.verifica_tela(self.context.path+"data/images/atencao_de_avisos_perspectiva.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/atencao_de_avisos_perspectiva.png")
        self.context.app.digitos("enter")

    def buscar_contato_desejado(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/buscaCliente.png",100)
        self.context.app.digitos(("tab",15))
        self.context.app.escrever_direto(self.NOME_DO_CLIENTE)
        #self.context.app.escrever_direto(self.context.data.variaveis["tela_atencao_de_aviso"]["nome_cliente"])
        self.context.app.digitos("enter")

        sleep(5)
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/clientes_normais.png",100)):
            self.context.app.clica(self.CLIENTES_NORMAL,"name",2)
            #self.context.app.digitos(("down",7))
    
    def clicar_em_novo_aviso(self):
        self.context.app.clica(self.NOVO_AVISO,"name",2)
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/atencao_icone.png",100)):
            self.context.app.clica(self.OK,"name",2)
        else:
            pass
    
    def preencher_dados_do_novo_aviso(self):
        self.context.app.digitos(("tab"))
        self.context.app.escrever_direto(self.TELEFONE_DO_CLIENTE)
        self.context.app.digitos(("tab",7),("down",2),"tab",("down",2))
        sleep(10)
        self.context.app.clica(self.CONCLUIR,"name",2)
        self.context.app.clica(self.OK,"name",2)

class Criacao_de_aviso_sem_cliente(object):
    def __init__(self, context):
        self.context = context
        self.CONCLUIR = "Concluir"
        self.NOME_DA_PESSOA = "JOAO"
        self.TELEFONE_DA_PESSOA = "99999999999"
        self.ENDERECO_DA_PESSOA = "Rua dos teste"
        self.OK = "OK"
        self.SERVICOS_DE_REDE = "Serviços de Rede"
        self.PROPRIEDADES = "Propriedades"
    
    def preencher_dados_do_cliente_nao_cadastrado(self):
        self.context.app.escrever_direto(self.NOME_DA_PESSOA)
        self.context.app.digitos("tab")
        
        self.context.app.escrever_direto(self.TELEFONE_DA_PESSOA)
        self.context.app.digitos("tab")
        
        self.context.app.escrever_direto(self.ENDERECO_DA_PESSOA)
        self.context.app.digitos(("tab",2))
        
        self.context.app.combo_digitos("ctrl","space")
        self.context.app.digitos("enter")
        self.context.app.digitos("tab")
        self.context.app.combo_digitos("ctrl","space")
        self.context.app.digitos("enter")
        self.context.app.digitos("tab")
        self.context.app.combo_digitos("ctrl","space")
        self.context.app.digitos("enter")
        self.context.app.digitos(("tab",5),"down","tab","down")
        self.context.app.digitos(("tab",10),"space")
        self.context.app.clica(self.CONCLUIR,"name") 
        self.context.app.clica(self.OK,"name")
        
    def verificar_aviso_criado(self):
        self.context.app.combo_digitos("ctrl","h")
        self.context.app.clica(self.SERVICOS_DE_REDE,"name")
        self.context.app.digitos(("tab",29))
        
    def visualizar_mensagem_do_aviso(self):
        self.context.app.escrever_direto("2019-139")##A mudar
        self.context.app.digitos("enter")
        self.context.asserts.verifica_tela(self.context.path+"data/images/viaCC2.png",100)
        self.context.app.digitos("down")
        sleep(2)
        self.context.app.clica(self.PROPRIEDADES,"name")
        self.context.asserts.verifica_tela(self.context.path+"data/images/mensagens.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/mensagens.png")
        sleep(2)
        self.context.app.arraste_coordenada(1347,315,1350,416,"left",3)
        sleep(2)
        self.context.asserts.verifica_tela(self.context.path+"data/images/mensagemVerde.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/mensagemVerde.png")
        self.context.app.digitos("down")
        sleep(2)

class Associacao_de_avisos(object):
    def __init__(self, context):
        self.context = context
        self.EXECUTAR = "Executar"
        self.OK = "OK"
    
    def selecionar_servico_rede_associacao_aviso(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD.png",100)
        self.context.app.digitos(("down",2))
        sleep(2)
    
    def realizar_manobra_servico_rede_da_associacao_aviso(self):
        #verifica se possui associacao e realiza a associacao, caso nao tiver, manobra normalmente. 
        #self.context.app.clica("Manobrar","name")
        self.context.asserts.verifica_tela(self.context.path+"data/images/manobra.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/manobra.png")
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/ha_alerta_operativa.png",100)):
            self.context.app.clica(self.OK,"name",2)
        else:
            pass
        
        #self.context.app.combo_digitos("shift","tab")
        #sleep(2)
        #self.context.app.combo_digitos("shift","tab")
        #sleep(2)
        #self.context.app.digitos(["down","down","down","down","down","down","down","down","down","down","down","down","down","down","down","down","down","down","enter"])
        #sleep(2)
        #self.context.app.digitos(["tab","space"])
        self.context.asserts.verifica_tela(self.context.path+"data/images/buttonExecutar.png",100)
        self.context.app.clica(self.EXECUTAR,"name",2)
    
class Extrair_aviso_novo(object):
    def __init__(self, context):
        self.context = context
        self.OK = "OK"
        self.PROCESSAR_AUTOMATICAMENTE = "Processar Automaticamente"
        self.AVISOS_SERVICO_DE_REDE = "Avisos Serviço de rede"
        self.EXTRAIR_AVISO = "Extrair Aviso"
        
    def abrir_view_avisos_de_servico_de_rede(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("avisos servi")
        self.context.app.digitos("enter")
        sleep(5)
   
    def selecionando_aviso_novo(self):
        #self.context.asserts.verifica_tela(self.context.path+"data/images/2018-10137.png",100)
        #self.context.app.clica_imagem(self.context.path+"data/images/2018-10137.png")
        self.context.app.combo_digitos("ctrl","h")
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/servico_rede.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/servico_rede.png")
        self.context.app.digitos(("tab",29))
        self.context.app.escrever_direto("2019-416")
        self.context.app.digitos("enter")
        sleep(5)
        #3self.context.app.digitos("down","enter")
        self.context.asserts.verifica_tela(self.context.path+"data/images/2019-416.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/2019-416.png")
        self.context.app.digitos("enter")
        
    def clico_na_view_avisos_servico_de_rede(self):
        pass
        
    def selecionando_aviso_dentro_da_view(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/pendente.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/pendente.png")
    
    def clicar_em_extrair_aviso(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/extrairAviso.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/extrairAviso.png")
        self.context.app.clica(self.PROCESSAR_AUTOMATICAMENTE,"name")

class Extrair_aviso_existente(object):
    def __init__(self, context):
        self.context = context
        self.OK = "OK"
        self.AVISOS_SERVICO_DE_REDE = "Avisos Serviço de rede"
        self.PROCESSAR_MANUALMENTE = "Processar Manualmente"
        self.GERAR_NOVO_SERVICO_DE_REDE = "Gerar novo Serviço de rede"
    
    def selecionar_aviso_existente(self):
        self.context.app.combo_digitos("ctrl","h")
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/servico_rede.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/servico_rede.png")
        self.context.app.digitos(("tab",29))
        self.context.app.escrever_direto("2019-522")
        self.context.app.digitos("enter")

        self.context.asserts.verifica_tela(self.context.path+"data/images/2019-522.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/2019-522.png",2,"left")

        self.context.asserts.verifica_tela(self.context.path+"data/images/avisos_servico_de_rede.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/avisos_servico_de_rede.png")
        self.context.app.digitos("down")
        
    def realizar_extracao_de_aviso_existente(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/extrairAviso.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/extrairAviso.png")
        self.context.app.clica(self.PROCESSAR_MANUALMENTE,"name",2)
        self.context.app.clica(self.GERAR_NOVO_SERVICO_DE_REDE,"name",2)
    
    

class Anular_aviso_associado_a_um_cliente(object):
    
    def __init__(self, context):
        self.context = context
        self.OK = "OK"
        self.AVISOS_DO_CLIENTE = "Avisos do Cliente"
        self.SIM = "Sim"
        
    def selecionar_view_aviso_cliente(self):        
        #self.context.asserts.verifica_tela(self.context.path+"elementosImagem/avisoCliente.png",100)
        #self.context.app.clica_imagem(self.context.path+"elementosImagem/avisoCliente.png")
        self.context.app.clica(self.AVISOS_DO_CLIENTE,"name",2)
        self.context.app.digitos("enter")
    
    def selecionar_aviso_associado_ao_cliente(self): 
        self.context.asserts.verifica_tela(self.context.path+"data/images/pendente.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/pendente.png")
        
    def selecionar_opcao_anular_aviso_associado(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/anularAviso.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/anularAviso.png")
    
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/aviso_em_gestao_deseja_continuar..png",100)):
            self.context.asserts.verifica_tela(self.context.path+"data/images/sim.png",100)
            self.context.app.clica_imagem(self.context.path+"data/images/sim.png")
        else:
            pass
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/validacao_tela_anular_aviso.png",100)
        self.context.app.digitos("tab")
        sleep(2)
        self.context.app.digitos("down")
        sleep(2)
        self.context.app.digitos("tab")
        sleep(2)
        self.context.app.escrever_direto("Teste automatizado do InGrid")
        self.context.app.clica(self.OK,"name",2)
        
class Anular_servico_de_rede_despachado(object): 
    def __init__(self, context):
        self.context = context
        self.OK = "OK"
        self.RESGATAR_ORDEM_DE_SERVICO = "Resgatar Ordem de Serviço"

    def selecionar_servico_de_rede_para_despachar(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD.png",100)

        if(self.context.asserts.verifica_tela(self.context.path+"data/images/2017-6719.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/2017-6719.png",2,"left")
            self.context.app.digitos("enter")

    def realizar_o_despacho_do_servico_de_rede(self):
        self.context.app.arraste_coordenada(494,389,1111,288,"left",5)
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/despacho_de_ordem_de_servico.png",100)):
            self.context.app.clica(self.OK,"name",2)
        sleep(5)

        if(self.context.asserts.verifica_tela(self.context.path+"data/images/2017-6719.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/2017-6719.png",2,"left")
            self.context.app.digitos("enter")

    def clicar_em_resgatar_ordem_de_servico(self):
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/resgatar.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/resgatar.png",100)
        else:
            self.context.app.clica(self.RESGATAR_ORDEM_DE_SERVICO,"name",2)

        if(self.context.asserts.verifica_tela(self.context.path+"data/images/motivoRecuperacao.png",100)):
            self.context.app.digitos("down")
            self.context.app.clica(self.OK,"name",2)



class View_arvore_de_avisos(object):
    def __init__(self, context):
        self.context = context
        self.EQUIPE = "Equipe"
        self.SIM = "Sim"
        
    def apertar_ctrl_e_3_e_pesquisar_view_arvore_de_aviso(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("avisos")
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/arvore_de_avisos1.png",100)!=None):
            self.context.app.clica_imagem(self.context.path+"data/images/arvore_de_avisos1.png")
        
        self.context.app.digitos("enter")
        self.context.app.arraste_coordenada(256,86,1364,195,"left",5)
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/2018-10137.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/2018-10137.png")
        self.context.app.digitos("enter")
        # self.context.asserts.verifica_tela(self.context.path+"elementosImagem/2016-583184.png",100)
        #self.context.app.clica_imagem(self.context.path+"elementosImagem/2016-583184.png")
        #self.context.app.digitos("enter")
    
    def clicar_em_atualizar(self):
        sleep(4)
        self.context.asserts.verifica_tela(self.context.path+"data/images/atualizar.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/atualizar.png")
        
   
    def clicar_em_desmembrar(self):
        self.context.app.digitos("down")
        self.context.asserts.verifica_tela(self.context.path+"data/images/desmembrar_evento_rede.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/desmembrar_evento_rede.png")
        self.context.app.clica(self.SIM,"name",2)
        
class Aviso_improcedente(object):
    def __init__(self, context):
        self.context = context
        
    def clicar_em_marcar_como_improcedente(self):
        self.context.app.digitos(("down",8))
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/marcar_como_improcedente.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/marcar_como_improcedente.png")
    
    def preencher_dados(self):
        self.context.app.digitos("down","tab")
        self.context.app.escrever_direto("testando")
        self.context.app.clica("OK","name",2)