# -*- coding: utf-8 -*-
'''
Created on 26 de nov de 2018
@author: gcruzm

'''

from time import sleep



class criar_evento_de_rede(object):
    def __init__(self, context):
        self.context = context
        self.OK = "OK"
        self.CONCLUIR = "Concluir"
        self.ATENDIMENTO_UNICO = "Atendimento Único"
        
    def carregar_view_sr_pendente_e_clicar_na_ferramenta_verde(self):
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/carregandoBDI.png", 80) != None):
            pass
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Servi")
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/servicos_de_rede_pendentes.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/servicos_de_rede_pendentes.png")
            self.context.app.digitos("enter")
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD.png",100)
        self.context.asserts.verifica_tela(self.context.path+"data/images/criar_servico_rede.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/criar_servico_rede.png")
        self.context.app.clica(self.OK,"name",2)
        
    def preencher_dados_novo_evento_rede(self):
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/novo_evento_rede.png",100)):
            self.context.app.digitos("n","tab","down")
        self.context.asserts.verifica_tela(self.context.path+"data/images/tipoelemente.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/tipoelemente.png")
        self.context.app.digitos("down",("t",2),"tab")
        self.context.app.escrever_direto("CAN00141")
        self.context.app.digitos("tab","space")
        self.context.app.clica(self.CONCLUIR,"name",2)
        self.context.asserts.verifica_tela(self.context.path+"data/images/informacao.png",100)
        self.context.app.clica(self.OK,"name",2)
    
class manobrar_evento_de_rede_nao_programado(object):
    def __init__(self, context):
        self.context = context
        self.OK = "OK"
    
    def procurar_evento_de_rede_nao_programado(self):
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/carregandoBDI.png", 80) != None):
            pass
        self.context.app.combo_digitos("ctrl","h")
        self.context.asserts.verifica_tela(self.context.path+"data/images/servico_rede.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/servico_rede.png",100)
        self.context.app.digitos(("tab",29))
        self.context.app.escrever_direto("2019-486")
        self.context.app.digitos("enter")

        if(self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/viaCOD.png")
        
        elif(self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD2.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/viaCOD2.png")

        elif(self.context.asserts.verifica_tela(self.context.path+"data/images/viaSCADA.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/viaSCADA.png")

        self.context.app.digitos("enter")
    
    def clicar_no_icone_de_manobra_para_manobrar_o_evento_de_rede(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/manobra.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/manobra.png")
        sleep(5)
        self.context.app.mantenha_e_digite("shift",["tab","tab"])
        self.context.app.digitos("up",("down",18),"tab")
        self.context.app.escrever_direto("CAN00141")
        self.context.app.digitos("tab")
        sleep(2)
    
    def clicar_no_botao_executar_para_executar_a_manobra(self):
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/fecharAoExecutar.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/fecharAoExecutar.png")
        sleep(5)
           
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/buttonExecutar.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/buttonExecutar.png")
    
class Atendimento_passado_atuacao_nao_programada(object):
    def __init__(self, context):
        self.context = context
        self.OK = "OK"

    def clicar_na_seta_do_lado_do_lapis(self):
        self.context.app.clica_coordenada(1249,85)
        self.context.asserts.verifica_tela(self.context.path+"data/images/atendimentoPassado.png",100)      
        self.context.app.clica_imagem(self.context.path+"data/images/atendimentoPassado.png",100)
        self.context.app.digitos("tab","down","tab")
        self.context.app.escrever_direto("teste automatizado de software")
        self.context.asserts.verifica_tela(self.context.path+"data/images/ok.png",100)
        self.context.app.clica(self.OK,"name",2)
              
class Iniciar_atendimento_da_oe_e_inicio_deslocamento(object):
    def __init__(self, context):
        self.context = context
        self.ADICIONAR = "Adicionar"
        self.ATENDIMENTO_UNICO = "Atendimento Único"
        
    def selecionar_servico_de_rede_para_o_atendimento_da_oe(self):
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/carregandoBDI.png", 80) != None):
            pass
        self.context.app.combo_digitos("ctrl","h")
        self.context.asserts.verifica_tela(self.context.path+"data/images/servico_rede.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/servico_rede.png",100)
        self.context.app.digitos(("tab",29))
        self.context.app.escrever_direto("2019-486")
        self.context.app.digitos("enter")
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/viaCOD.png")
        
        elif(self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD2.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/viaCOD2.png")

        elif(self.context.asserts.verifica_tela(self.context.path+"data/images/viaSCADA.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/viaSCADA.png")
        
    def clicar_em_atendimento_unico_e_preencher_dados_necessarios(self):
        self.context.app.clica(self.ATENDIMENTO_UNICO,"name",2)
        self.context.app.clica(self.ADICIONAR,"name",2)
        self.context.app.escrever_direto("testando um dois tres")
        self.context.app.clica(self.ADICIONAR,"name",2)
        
    def confirmar_o_atendimento_da_oe(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/ok.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/ok.png")

class Inclusao_de_material_servico_causa_e_observacao(object):
    def __init__(self, context):
        self.context = context
        self.OK = "OK"
        self.SIM = "Sim"
        self.ATENDIMENTO_UNICO = "Atendimento Único"
        
    def selecionar_ordem_de_servico_para_inclusao(self):
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/carregandoBDI.png", 80) != None):
            pass
        '''
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Servi")
        self.context.app.digitos("enter")
        self.context.asserts.verifica_tela(self.context.path+"elementosImagem/viaCC.png",100)
        self.context.app.digitos(("down",4),"enter")
        '''
        self.context.app.combo_digitos("ctrl","h")
        self.context.asserts.verifica_tela(self.context.path+"data/images/servico_rede.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/servico_rede.png",100)
        self.context.app.digitos(("tab",29))
        self.context.app.escrever_direto("2019-486")
        self.context.app.digitos("enter")
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/viaCOD.png")
        
        elif(self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD2.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/viaCOD2.png")

        elif(self.context.asserts.verifica_tela(self.context.path+"data/images/viaSCADA.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/viaSCADA.png")
        
    def abrir_atendimento_unico(self):
        self.context.app.clica(self.ATENDIMENTO_UNICO,"name",2)
        sleep(4)
        
    def incluir_material(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/materiaisBotao.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/materiaisBotao.png")
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/adicionarMateriais.png",100)
        self.context.app.clica_imagem(self.context.path+"/data/images/adicionarMateriais.png")
        sleep(2)
        self.context.asserts.verifica_tela(self.context.path+"data/images/sem_material.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/sem_material.png")
        sleep(2)
        self.context.app.digitos("right","down","right","down")
        #self.context.app.digitos(("tab",2),"right","down","right","down","tab")
        self.context.app.clica_imagem(self.context.path+"/data/images/quantidadeMaterial.png")
        self.context.app.escrever_direto("1")
        sleep(2)
        self.context.app.digitos("tab")
        self.context.app.digitos("down")
        self.context.app.clica(self.OK,"name",1)
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/interrogacao.png",100)):
            self.context.app.clica(self.SIM,"name",2)
        else:
            pass
        self.context.app.clica(self.OK,"name",2)

    
    def incluir_servico(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/botao_servicos.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/botao_servicos.png")
        
        self.context.asserts.verifica_tela(self.context.path+"/data/images/recurso.png",100)
        self.context.asserts.verifica_tela(self.context.path+"data/images/adicionarMateriais.png",100)
        self.context.app.clica_imagem(self.context.path+"/data/images/adicionarMateriais.png")

        self.context.app.digitos(("tab",2),"right","down","right","down","right","down",("tab",2))
        #self.context.app.digitos(("tab",2),"right","down","right","down",("tab",2))
        self.context.app.escrever_direto("1")
        self.context.asserts.verifica_tela(self.context.path+"data/images/ok.png",20)
        self.context.app.clica_imagem(self.context.path+"data/images/ok.png")
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/interrogacao.png",100)):
            self.context.app.clica(self.SIM,"name",2)
        else:
            pass
        
        self.context.app.clica(self.OK,"name",2)

    def incluir_causa(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/campo_causa.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/campo_causa.png")
        self.context.app.escrever_direto("PD32")
        self.context.app.clica(self.OK,"name",2)
        #self.context.app.combo_digitos("ctrl","space")
        #self.context.app.digitos(("down",2),"enter")
        #self.context.app.asserts.verifica_tela(self.context.path+"elementosImagem/ok.png",100)
        #self.context.app.clica_imagem(self.context.path+"elementosImagem/ok.png")
                
        
class Finalizar_ordem_de_servico(object):
    def __init__(self, context):
        self.context = context
        self.OK = "OK"
        self.ATENDIMENTO_UNICO = "Atendimento Único"
    
    def selecionaServico(self):
        '''
        while(self.context.asserts.verifica_tela(self.context.path+"elementosImagem/carregandoBDI.png", 80) != None):
            pass
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Servi")
        
        if(self.context.asserts.verifica_tela(self.context.path+"elementosImagem/servicos_de_rede_pendentes.png",100)):
            self.context.app.clica_imagem(self.context.path+"elementosImagem/servicos_de_rede_pendentes.png")
            self.context.app.digitos("enter")
        sleep(5)
        self.context.asserts.verifica_tela(self.context.path + "elementosImagem/viaCOD.png", 100)
        self.context.app.digitos(('down', 3))
        
        self.context.asserts.verifica_tela(self.context.path+"elementosImagem/ff-27.png",100)
        self.context.app.clica_imagem(self.context.path+"elementosImagem/ff-27.png")
        '''
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/carregandoBDI.png", 80) != None):
            pass
        '''
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Servi")
        self.context.app.digitos("enter")
        self.context.asserts.verifica_tela(self.context.path+"elementosImagem/viaCC.png",100)
        self.context.app.digitos(("down",4),"enter")
        '''
        self.context.app.combo_digitos("ctrl","h")
        self.context.asserts.verifica_tela(self.context.path+"data/images/servico_rede.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/servico_rede.png",100)
        self.context.app.digitos(("tab",29))
        self.context.app.escrever_direto("2019-173")
        self.context.app.digitos("enter")
        self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD2.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/viaCOD2.png",2)
    
    def opcaoAtendimento(self):
        sleep(5)
        #self.context.asserts.verifica_tela(self.context.path + "elementosImagem/atendimentoUnico.png", 100)
        #self.context.app.clica_imagem(self.context.path + "elementosImagem/atendimentoUnico.png", 100)
        self.context.app.clica(self.ATENDIMENTO_UNICO,"name",2)
        
    def preencheCampo(self):
        self.context.app.clica_coordenada(248, 184)
        #condição para verificar os checkbox da area Gerais e realizar sua marcação
        aux = 0
        while(aux < 4):
            if(self.context.asserts.verifica_tela(self.context.path + "data/images/marcado.png", 50) or self.context.asserts.verifica_tela(self.context.path + "data/images/marcado.png", 50) == None):
                self.context.app.digitos(("tab"))    
                          
            elif(self.context.asserts.verifica_tela(self.context.path + "data/images/marcado.png", 50)):
                self.context.app.digitos(("space")) 
                self.context.app.digitos(("tab"))                
            aux += 1
        sleep(5)
        
        
        self.context.app.clica_coordenada(619, 318)
        self.context.app.digitos(('down', 12))
        self.context.app.digitos(('enter'))
        sleep(3)
        self.context.app.clica_coordenada(621, 347)
        self.context.app.escrever_direto("TAT01230")
        self.context.app.clica("OK", "name", 5)

    
        
class Anular_servico_de_rede_pendente(object):
    def __init__(self, context):
        self.context = context
        self.OK = "OK"
    
    def selecionar_sr_pendente(self):
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/carregandoBDI.png", 80) != None):
            pass
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Servi")
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/servicos_de_rede_pendentes.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/servicos_de_rede_pendentes.png")
            self.context.app.digitos("enter")
            
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD.png",100)):
            pass
    
    def botao_direito_no_sr(self):
        self.context.app.clica_imagem(self.context.path+"data/images/2018-10166.png",2,"right")
    
    def selecionar_opcao_anular_aviso(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/anularAviso.png",20)
        self.context.app.clica_imagem(self.context.path+"data/images/anularAviso.png")
        self.context.asserts.verifica_tela(self.context.path+"data/images/interrogacao.png",100)
        self.context.app.clica(self.OK,"name",2)
        self.context.app.digitos("tab","down","tab")
        self.context.app.escrever_direto("teste automatizado de software")
        
    def concluir_anulacao_aviso_pendente(self):
        self.context.app.clica(self.OK,"name",1)
        self.context.asserts.verifica_tela(self.context.path+"data/images/interrogacao.png")
        self.context.app.digitos("enter")
            
        
class Anular_servico_de_rede_com_atendimento_iniciado(object):
    def __init__(self, context):
        self.context = context
        self.OK = "OK"
        self.NAO_PROGRAMADA = "Não Programada"
    
    def selecionarSRIniciado(self):
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/carregandoBDI.png", 80) != None):
            pass

        self.context.app.combo_digitos("ctrl","h")
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/servico_rede.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/servico_rede.png",100)
        self.context.app.clica(self.NAO_PROGRAMADA,"name",2)
        self.context.app.digitos("space",("tab",8),"space","right")
        
        self.context.app.escrever_direto("01")
        self.context.app.digitos("right")

        self.context.app.escrever_direto("01")
        self.context.app.digitos("enter")

        if(self.context.asserts.verifica_tela(self.context.path+"data/images/2019-34.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/2019-34.png",1,"right")
        else:
            self.context.app.fechar_programa()


    def escolherOpcaoAnularAviso(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/anularAviso.png",20)
        self.context.app.clica_imagem(self.context.path+"data/images/anularAviso.png")
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/confirmacaoAnularSR.png",20)):
                self.context.app.clica(self.OK,"name",2)
        else:
            pass
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/deseja_anular_mesmo_assim..png",100 )):
            self.context.app.clica(self.OK,"name",2)
        else:
            pass
        
    def preencherDadosAnularAviso(self):
        self.context.app.digitos("tab","down")
        self.context.app.clica(self.OK,"name",1)
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/erro.png",20)):
            self.context.app.clica(self.OK,"name",1)