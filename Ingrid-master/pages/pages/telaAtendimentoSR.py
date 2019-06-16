# -*- coding: utf-8 -*-
'''
Created on 21 de jul de 2018
@author: gdiamante

Modified on 11 de dez de 2018
@author: gcruzm
'''

from time import sleep


class Logar_equipe(object):
    def __init__(self,context):
        self.context=context
        self.CONCLUIR = "Concluir"
        self.OK = "OK"
        self.LOGIN_EQUIPE = "Login Equipe"
        self.EQUIPE_AA10 = "AA-10"
    def clicar_na_chave_positiva_para_o_login_de_equipe(self):
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/carregandoBDI.png",80)!=None):
            pass
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("recursos propostos")
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/ctrl_3_recursos_propostos.png",100)):
            self.context.app.digitos("enter")
        sleep(5)
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/login_de_equipe.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/login_de_equipe.png")
        else:
            self.context.app.clica(self.LOGIN_EQUIPE,"name",2)
        sleep(3)
            
    def escolho_a_equipe(self):
        '''
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/elektro_comercializadora.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/elektro_comercializadora.png")
        
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/concluir.png",100)==None):
            self.context.app.digitos("down")
        else:
            if(self.context.asserts.verifica_tela(self.context.path+"data/images/concluir.png",100)):
                self.context.app.clica_imagem(self.context.path+"data/images/concluir.png")
            else:
                self.context.app.clica(self.CONCLUIR,"name",2)
        '''
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/procurar_equipe.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/procurar_equipe.png")
        
        self.context.app.escrever_direto("AA-10")
        
        sleep(2)
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/equipe_aa_10.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/equipe_aa_10.png")
        else:
            self.context.app.clica(self.EQUIPE_AA10,"name",2)
    
    def seleciono_opcao_ultimo_login_e_concluo(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/ultimoLogin.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/ultimoLogin.png")
        sleep(5)
        self.context.app.clica(self.CONCLUIR,"name",1)
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/atencao_icone.png",100)):
            self.context.app.clica(self.OK,"name",2)
            
            if(self.context.asserts.verifica_tela(self.context.path+"data/images/concluir.png",100)):
                self.context.app.clica_imagem(self.context.path+"data/images/concluir.png")
            else:
                self.context.app.clica(self.CONCLUIR,"name",2)
        else:
            pass
                
        self.context.asserts.verifica_tela(self.context.path+"data/images/equipe_logada_com_sucesso.png",100)
        self.context.app.clica(self.OK,"name",2)
        
class Localizar_consistencia_dos_dados_de_uma_os(object):
    def __init__(self,context):
        self.context=context
        self.DATAS = "Datas"
        self.CAUSAS = "Causas"
        self.DESCRICOES = "Descrições"
        self.MATERIAIS = "Materiais"
        self.SERVICOS = "Serviços"
        self.LOGS = "Logs"
        self.ASSOCIACAO = "Associação"
        self.UNIFICACOES = "Unificações"
        self.FORMULARIOS = "Formulários"
        self.MENSANGES = "Mensagens"
        self.INDICADORES = "Indicadores"
        self.PES_ASSOCIADOS = "Pes Associados"
        self.LOGS_SCALA = "Logs Scada"
        self.PRE_DESPACHO = "Pré-despacho"
        self.ROTULO = "Rótulo"
    
    def abrir_view_de_servico_de_redes_pendentes(self):
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/carregandoBDI.png",80)!=None):
            pass
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("recursos propostos")
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/ctrl_3_recursos_propostos.png",100)):
            self.context.app.digitos("enter")
        sleep(5)

    def selecionar_servico_de_rede_desejado(self):
        self.context.app.clica(self.ROTULO,"name",2)
        sleep(3)
        self.context.app.clica(self.ROTULO,"name",2)
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/viaCOD.png")
        
        elif(self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD2.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/viaCOD2.png")
    
    def abrir_view_propriedades(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("propriedades")
        self.context.app.digitos("enter")
        self.context.asserts.verifica_tela(self.context.path+"data/images/propriedades3.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/propriedades3.png")
        
    def listar_referencia_da_os(self):
        self.context.app.arraste_coordenada(1349,431,1350,580,"left",5)
    
    def listar_datas_da_os(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/datas_view_propriedade.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/datas_view_propriedade.png")
        self.context.app.arraste_coordenada(1350,580,1349,431,"left",5)

    def listar_causa_da_os(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/causas.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/causas.png")
        self.context.app.arraste_coordenada(1349,431,1350,580,"left",5)

    def listar_descricoes_da_os(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/descricoes.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/descricoes.png")
        self.context.app.arraste_coordenada(1350,580,1349,431,"left",5)

    def listar_materiais_da_os(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/materiais_view_propriedades.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/materiais_view_propriedades.png")
        self.context.app.arraste_coordenada(1349,431,1350,580,"left",5)

    def listar_servicos_da_os(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/servicos.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/servicos.png",100)
        self.context.app.arraste_coordenada(1350,580,1349,431,"left",5)

    def listar_logs_da_os(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/logs_.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/logs_.png")
        self.context.app.arraste_coordenada(1349,431,1350,580,"left",5)
    
    def listar_associacao_da_os(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/associacao__.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/associacao__.png")
        self.context.app.arraste_coordenada(1350,580,1349,431,"left",5)
    
    def listar_unificacoes_da_os(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/unificacoes_.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/unificacoes_.png")
        self.context.app.arraste_coordenada(1349,431,1350,580,"left",5)
    
    def listar_formularios_da_os(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/formularios.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/formularios.png")
        self.context.app.arraste_coordenada(1350,580,1349,431,"left",5)
    
    def listar_mensagens_da_os(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/mensagens_view_propriedade.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/mensagens_view_propriedade.png")
        self.context.app.arraste_coordenada(1349,431,1350,580,"left",5)

    def listar_indicadores_da_os(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/seta_pra_baixo_propriedades.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/seta_pra_baixo_propriedades.png")
        self.context.asserts.verifica_tela(self.context.path+"data/images/indicadores.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/indicadores.png")
        self.context.app.arraste_coordenada(1347,673,1349,536,"left",5)

    def listar_pes_associados_da_os(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/seta_pra_baixo_propriedades.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/seta_pra_baixo_propriedades.png",3,"left")
        self.context.asserts.verifica_tela(self.context.path+"data/images/pes_associados.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/pes_associados.png")
        self.context.app.arraste_coordenada(1349,536,1347,673,"left",5)

    def listar_logs_scada_da_os(self):
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/logs_scada_menu.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/logs_scada_menu.png")
            self.context.app.arraste_coordenada(1347,673,1349,536,"left",5)
        else:
            pass

    def listar_pre_despacho_da_os(self):
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/pre_despacho_menu.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/pre_despacho_menu.png")
            self.context.app.arraste_coordenada(1349,536,1347,673,"left",5)
        else:
            pass

    def listar_dependencia(self):
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/dependencia__menu.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/dependencia__menu.png")
        else:
            pass
        
class Despachar_servico_de_rede_para_equipe_distinta(object):
    def __init__(self,context):
        self.context=context
        self.ROTULO = "Rótulo"
        self.SERVICOS_DE_REDES_PENDENTES = "Serviços de Redes Pendentes"
        self.OK = "OK"
        self.SIM = "Sim"
        
    def abrir_view_recursos_propostos(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("recursos propostos")
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/ctrl_3_recursos_propostos.png",100)):
            self.context.app.digitos("enter")
        sleep(5)
        
    def abrir_view_de_servico_de_redes_pendentes(self):
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
        
    def selecionar_servico_de_rede_desejado(self):
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/viaCOD.png",2)
        elif(self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD2.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/viaCOD2.png",2)
            
    def despachar_para_equipe_distinta(self):
        self.context.app.arraste_coordenada(None,None,1081,307,"left",5)
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/atencao_em_despachar.png",100)):
            self.context.app.clica(self.SIM,"name",2)
        else:
            pass
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/despacho_ordem_de_servico.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/despacho_ordem_de_servico.png")
            self.context.app.clica(self.OK,"name",2)
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/despachadaSucesso.png",100) or self.context.asserts.verifica_tela(self.context.path+"data/images/despacho-concluido.png",100)):
            self.context.app.clica(self.OK,"name",2)

class Resgatar_os_despachada_por_voz(object):
    def __init__(self,context):
        self.context=context
        self.RECURSOS_PROPOSTOS = "Recursos Propostos"
        self.OK = "OK" 
        self.RESGATAR_ORDEM_DE_SERVICO = "Resgatar Ordem de Serviço"
    '''
    def abrir_view_recursos_propostos(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("recursos propostos")
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/ctrl_3_recursos_propostos.png",100)):
            self.context.app.digitos("enter")
        sleep(5)
    '''
        
    def selecionar_os_despachada(self):
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/viaCOD.png",2)
        elif(self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD2.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/viaCOD2.png",2)
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/notebook.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/notebook.png")
            self.context.app.digitos(("down",5),"right","down")
    
    def selecionar_icone_resgatar_os_despachada(self):
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/resgatar.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/resgatar.png")
        else:
            self.context.app.clica(self.RESGATAR_ORDEM_DE_SERVICO,"name",2)
            
            if(self.context.asserts.verifica_tela(self.context.path+"data/images/motivo_recuperacao_de_os.png",100)):
                self.context.app.digitos("down")
                self.context.app.clica(self.OK,"name",2)
        sleep(6)
        self.context.asserts.verifica_tela(self.context.path+"data/images/informacao.png",100)
        self.context.app.clica(self.OK,"name",2)
        
class Interromper_rejeitar_os_sem_agendamento(object):
    def __init__(self,context):
        self.context=context
        self.OK = "OK"
    
    def selecionar_equipe_para_interrupcao_e_rejeicao(self):
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/viaCOD.png",2)
        elif(self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD2.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/viaCOD2.png",2)
        self.context.app.clica_imagem(self.context.path+"data/images/recursosPropostos.png",2,"left",similar=10)
        sleep(3)
        self.context.app.digitos(("down",5),"right", ("down",2))
        sleep(3)
        
    def selecionar_icone_interrupcao_e_rejeicao(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/rejeitarOS.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/rejeitarOS.png", 1, "left", similar=70)
        sleep(3)
        
        self.context.app.digitos("tab","down","tab")
        self.context.app.escrever_direto("Teste automatizado de software")
        self.context.app.clica(self.OK,"name",2)
        

class Logoff_da_equipe(object):
    def __init__(self,context):
        self.context=context
        self.CONCLUIR = "Concluir"
        self.AA_10 = "AA-10"
        self.DESLOGAR_EQUIPE = "Deslogar Equipe"
        
    def clicar_na_chave_negativa_para_o_logoff_de_equipe(self):
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/carregandoBDI.png",80)!=None):
            pass
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("recursos propostos")
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/ctrl_3_recursos_propostos.png",100)):
            self.context.app.digitos("enter")
        sleep(5)
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/deslogar_equipe.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/deslogar_equipe.png")
        else:
            self.context.app.clica(self.DESLOGAR_EQUIPE,"name",2)
        
    def escolho_equipe_logada(self):
        self.context.app.digitos("tab")
        self.context.app.escrever_direto("AA-10")
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/equipe_aa_10.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/equipe_aa_10.png")
        else:
            self.context.app.clica(self.AA_10,"nome",2)
    
    def preencho_dados_e_concluo_o_logoff(self):
        self.context.app.digitos(("tab",2),"down")
        self.context.app.clica(self.CONCLUIR,"name",2)