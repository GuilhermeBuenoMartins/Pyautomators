# -*- coding: utf-8 -*-
'''
Created on 12 de mar de 2019

@author: vgama
'''
from time import sleep

class PESConfiguracaoPrazos(object):

    def __init__(self, context):

        self.context = context
        self.JANELA = "Janela"
        self.OK = "OK"

    
    def entrar_configuracao_prazos(self):
        self.context.app.clica(self.JANELA, "name", 3)
        self.context.app.clica_imagem(self.context.path+"data/images/preferencias.png", 1, "left")
        sleep(3)
        self.context.asserts.verifica_tela(self.context.path+"data/images/viewPreferencia.png", 80)
    
    
    def pesquisar_configuracao(self):
        self.context.app.escrever_direto("Prazos")
        sleep(2)
        self.context.app.clica_imagem(self.context.path+"data/images/configuracaoPrazos.png", 1, "left", similar=70)
        sleep(5)
    
    def atualizar_classificacao_urgente(self):
        self.context.app.clica_imagem(self.context.path+"data/images/emissao.png")
        self.context.app.digitos(("tab",12))
        self.context.app.combo_digitos("ctrl", "a")
        self.context.app.escrever_direto("0")
        
        self.context.app.digitos(("tab",2))
        self.context.app.combo_digitos("ctrl", "a")
        self.context.app.escrever_direto("0")
        
        self.context.app.digitos(("tab",2))
        self.context.app.combo_digitos("ctrl", "a")
        self.context.app.escrever_direto("2")
        
        
        self.context.app.clica_imagem(self.context.path+"data/images/botaoAlterar.png", 1, "left")
        self.context.asserts.verifica_tela(self.context.path+"data/images/prazoAlterado.png", 80)
        self.context.app.digitos("enter")
        self.context.app.clica_imagem(self.context.path+"data/images/botaoOK.png", 1, "left", similar=60)

    def atualizar_classificacao_prazo(self):
        self.context.app.clica_imagem(self.context.path+"data/images/emissao.png")
        self.context.app.digitos(("tab",12))
        self.context.app.combo_digitos("ctrl", "a")
        self.context.app.escrever_direto("0")
        
        self.context.app.digitos(("tab",2))
        self.context.app.combo_digitos("ctrl", "a")
        self.context.app.escrever_direto("6")
        
        self.context.app.digitos(("tab",2))
        self.context.app.combo_digitos("ctrl", "a")
        self.context.app.escrever_direto("0")
        
        self.context.app.clica_imagem(self.context.path+"data/images/botaoAlterar.png", 1, "left")
        self.context.asserts.verifica_tela(self.context.path+"data/images/prazoAlterado.png", 80)
        self.context.app.digitos("enter")
        self.context.app.clica_imagem(self.context.path+"data/images/botaoOK.png", 1, "left", similar=60)
        
    def atualizar_classificacao_normal(self):
        self.context.app.clica_imagem(self.context.path+"data/images/emissao.png", 1,"left", similar=60)
        self.context.app.digitos(("tab",12))
        self.context.app.combo_digitos("ctrl", "a")
        self.context.app.escrever_direto("4")
        
        self.context.app.digitos(("tab",2))
        self.context.app.combo_digitos("ctrl", "a")
        self.context.app.escrever_direto("0")
        
        self.context.app.digitos(("tab",2))
        self.context.app.combo_digitos("ctrl", "a")
        self.context.app.escrever_direto("0")
        
        self.context.app.clica_imagem(self.context.path+"data/images/botaoAlterar.png", 1, "left")
        self.context.asserts.verifica_tela(self.context.path+"data/images/prazoAlterado.png", 80)
        self.context.app.digitos("enter")
        self.context.app.clica_imagem(self.context.path+"data/images/botaoOK.png", 1, "left", similar=60)

class PESClassificadoUrgente(object):
    
    def __init__(self, context):
        self.context = context
        
        self.CONDICAO2 = "Condição de Segurança 2"
        self.CONDICAO3 = "Condição de Segurança 3"
        self.CONDICAO4 = "Condição de Segurança 4"
        self.NENHUMA = "Nenhuma"
        self.AVANCAR = "Avançar >"
        self.PES = "PES"
        self.NOVO = "NOVO"
        self.PESQUISA = "texto do filtro de tipos"
        self.JANELA = "Janela"
        self.OK = "OK"
    
    def view_outros(self):
        sleep(5)
        self.context.app.clica_imagem(self.context.path+"data/images/arquivo.png", 1, "left", similar=70)
        self.context.app.digitos("down","right","enter")
        self.context.asserts.verifica_tela(self.context.path+"data/images/selecionarAssistente.png", 80)
        
    def pesquiso_pedido_execucao(self):    
        self.context.app.escrever_direto("Pedido")
        self.context.app.digitos("down")
        self.context.app.clica(self.AVANCAR,"name",3)
        sleep(5)
        
    def preencher_novo_pedido_urgente(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/pedidoExecucao.png", 80, similaridade=60)
        
        self.context.app.digitos(("tab",3),"down","tab","down","tab")
        self.context.app.escrever_direto("s")
        self.context.app.digitos(("down",2),"tab")
        self.context.app.escrever_direto("GUA00500")
        self.context.app.digitos("tab","space")
        sleep(3)
        self.context.app.digitos(("tab",4))
        self.context.app.escrever_direto("1")
        sleep(3)
        self.context.app.digitos(("tab",2),"right","tab","right","tab","right","tab","right")
        self.context.app.clica(self.AVANCAR,"name",3)
        
        self.context.app.digitos(("tab",3))
        self.context.app.combo_digitos("alt","down")
        self.context.app.digitos("right", "space","tab")
        self.context.app.combo_digitos("alt","down")
        self.context.app.digitos(("right", 2), "space", ("tab",2),"down","tab")
        self.context.app.escrever_direto("Teste")
        self.context.app.clica_imagem(self.context.path+"data/images/campoNomePES.png", 1, "left", similar=50)
        sleep(3)
        self.context.app.escrever_direto("EMILIO BENTO VIEIRA JUNIOR")
        self.context.app.digitos("tab")
        
        sleep(3)
        self.context.app.clica(self.AVANCAR, "name", 5)
        
        sleep(4)
        
        self.context.app.clica(self.NENHUMA, "name", 2)        
        self.context.app.clica(self.CONDICAO2, "name", 2)
        self.context.app.clica(self.NENHUMA, "name", 2)
        self.context.app.clica(self.CONDICAO3, "name", 3)
        self.context.app.clica(self.NENHUMA, "name", 2)        
        self.context.app.clica(self.CONDICAO4, "name", 4)
        self.context.app.clica(self.NENHUMA, "name", 2)
        
        self.context.app.clica_imagem(self.context.path+"data/images/concluir.png", 1, "left")
    
            
    def pedido_adicionado(self):

        self.context.asserts.verifica_tela(self.context.path+"data/images/atencaoAtendimento.png", 70)
        self.context.app.digitos("enter")
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/adcionarMotivo.png", 70)
        self.context.app.digitos("down","tab")
        self.context.app.escrever_direto("Teste")
        
        self.context.app.clica_imagem(self.context.path+"data/images/botao_ok.png", 1, "left")
        
        sleep(3)
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/informacao.png", 100, 1)):
            self.context.app.digitos("enter")
            
        self.context.asserts.verifica_tela(self.context.path+"data/images/viewSucesso.png", 70)
        self.context.app.digitos("enter")
        
        
    def abrir_view_pedido_execucao(self):
        
        self.context.app.clica(self.JANELA, "name", 3)
        self.context.app.digitos(("down",2),"right","down","enter")
        sleep(3)
        self.context.app.escreve(self.PESQUISA, "Pedido de Execução de Serviços Pendentes","name")
        self.context.app.digitos(("down",2),"enter")
        
        sleep(3)
        while( self.context.asserts.verifica_tela(self.context.path+"data/images/refreshExecucaoPendente.png", 70) != None):
            pass
        
    
    def verifico_pes_classificado_urgente(self):
        self.context.app.clica(self.PES, "name")
        self.context.app.clica(self.PES, "name")
        
        self.context.app.digitos("down", ("up",2))
        
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Propriedades")
        self.context.app.digitos("enter")
        
        #Verifica view propriedades aberta
        self.context.asserts.verifica_tela(self.context.path+"data/images/propriedades3.png", 70)
        
        #verifica PES em estado Emitido
        self.context.asserts.verifica_tela(self.context.path+"data/images/estadoEmitido.png", 70)
        
        #verifica PES classificao URGENTE
        self.context.asserts.verifica_tela(self.context.path+"data/images/classificacaoUrgente.png", 70)

        

class PESClassificadoForaPrazo(object):
    
    def __init__(self, context):
        self.context = context
        
        self.CONDICAO2 = "Condição de Segurança 2"
        self.CONDICAO3 = "Condição de Segurança 3"
        self.CONDICAO4 = "Condição de Segurança 4"
        self.NENHUMA = "Nenhuma"
        self.AVANCAR = "Avançar >"
        self.PES = "PES"
    
        
    def preencher_novo_pedido_fora_prazo(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/pedidoExecucao.png", 80, similaridade=60)
        
        self.context.app.digitos(("tab",3),"down","tab","down","tab")
        self.context.app.escrever_direto("s")
        self.context.app.digitos(("down",2),"tab")
        self.context.app.escrever_direto("GUA00500")
        self.context.app.digitos("tab","space")
        sleep(3)
        self.context.app.digitos(("tab",4))
        self.context.app.escrever_direto("1")
        sleep(3)
        self.context.app.digitos(("tab",2),"right","tab","right","tab","right","tab","right")
        self.context.app.clica(self.AVANCAR,"name",3)
        self.context.app.digitos(("tab",3))
        
        self.context.app.combo_digitos("alt","down")
        self.context.app.digitos("right", "space","tab")
        self.context.app.combo_digitos("alt","down")
        self.context.app.digitos(("right", 6), "space", ("tab",2),"down","tab")
        self.context.app.escrever_direto("Teste")
        self.context.app.clica_imagem(self.context.path+"data/images/campoNomePES.png", 1, "left", similar=50)
        sleep(3)
        self.context.app.escrever_direto("ADALBERTO LEITE FIGUEIRA")
        self.context.app.digitos("tab")
                
        self.context.app.clica(self.AVANCAR, "name", 3)
        
        sleep(4)
        
        self.context.app.clica(self.NENHUMA, "name", 2)        
        self.context.app.clica(self.CONDICAO2, "name", 2)
        self.context.app.clica(self.NENHUMA, "name", 2)
        self.context.app.clica(self.CONDICAO3, "name", 3)
        self.context.app.clica(self.NENHUMA, "name", 2)        
        self.context.app.clica(self.CONDICAO4, "name", 4)
        self.context.app.clica(self.NENHUMA, "name", 2)
        
        self.context.app.clica_imagem(self.context.path+"data/images/concluir.png", 1, "left")
    
    def verifico_pes_classificado_fora_prazo(self):
        self.context.app.clica(self.PES, "name")
        self.context.app.clica(self.PES, "name")
        
        self.context.app.digitos("down", ("up",2))
        
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Propriedades")
        self.context.app.digitos("enter")
        
        #Verifica view propriedades aberta
        self.context.asserts.verifica_tela(self.context.path+"data/images/propriedades3.png", 70)
        
        #verifica PES em estado Emitido
        self.context.asserts.verifica_tela(self.context.path+"data/images/estadoEmitido.png", 70)
        
        #verifica PES classificao URGENTE
        self.context.asserts.verifica_tela(self.context.path+"data/images/classificacaoForaPrazo.png", 70)

        
class PESClassificadoNormal(object):
    
    def __init__(self,context):
        self.context = context
        self.CONDICAO2 = "Condição de Segurança 2"
        self.CONDICAO3 = "Condição de Segurança 3"
        self.CONDICAO4 = "Condição de Segurança 4"
        self.NOVO = "Novo"
        self.AVANCAR = "Avançar >"    
        self.NENHUMA = "Nenhuma"
        self.PES = "PES"
        
    
    def preencher_pedido_normal(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/pedidoExecucao.png", 80, similaridade=60)
        
        self.context.app.digitos(("tab",3),"down","tab","down","tab")
        self.context.app.escrever_direto("s")
        self.context.app.digitos(("down",3),"tab")
        self.context.app.escrever_direto("GUA00500")
        self.context.app.digitos("tab","space")
        sleep(3)
        self.context.app.digitos(("tab",4))
        self.context.app.escrever_direto("1")
        sleep(3)
        self.context.app.digitos(("tab",2),"right","tab","right","tab","right","tab","right")
        self.context.app.clica(self.AVANCAR,"name",3)
        self.context.app.digitos(("tab",3))
        
        self.context.app.combo_digitos("alt","down")
        self.context.app.digitos("right", "space","tab")
        self.context.app.combo_digitos("alt","down")
        self.context.app.digitos(("right", 5), "space", ("tab",2),"down","tab")
        self.context.app.escrever_direto("Teste")
        self.context.app.clica_imagem(self.context.path+"data/images/campoNomePES.png", 1, "left", similar=50)
        sleep(3)
        self.context.app.escrever_direto("ADALBERTO LEITE FIGUEIRA")
        self.context.app.digitos("tab")
                
        self.context.app.clica(self.AVANCAR, "name", 3)
        
        sleep(4)
        
        self.context.app.clica(self.NENHUMA, "name", 2)        
        self.context.app.clica(self.CONDICAO2, "name", 2)
        self.context.app.clica(self.NENHUMA, "name", 2)
        self.context.app.clica(self.CONDICAO3, "name", 3)
        self.context.app.clica(self.NENHUMA, "name", 2)        
        self.context.app.clica(self.CONDICAO4, "name", 4)
        self.context.app.clica(self.NENHUMA, "name", 2)
        
        self.context.app.clica_imagem(self.context.path+"data/images/concluir.png", 1, "left")
    
    def verifico_pes_classificado_normal(self):
        
        self.context.app.clica(self.PES, "name",3)
        self.context.app.clica(self.PES, "name",3)
        
        self.context.app.digitos("down", ("up",2))
        
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Propriedades")
        self.context.app.digitos("enter")
        
        #Verifica view propriedades aberta
        self.context.asserts.verifica_tela(self.context.path+"data/images/propriedades3.png", 70)
        
        #verifica PES em estado Emitido
        self.context.asserts.verifica_tela(self.context.path+"data/images/estadoEmitido.png", 70, similaridade=70)
        
        #verifica PES classificao URGENTE
        self.context.asserts.verifica_tela(self.context.path+"data/images/classificacaoNormal.png", 70, similaridade=80)


        
    def pedido_adicionado_normal(self):
              
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/urgenteOuForaPrazo.png", 100, similaridade=60)):
            self.context.app.digitos("enter")
            
            self.context.asserts.verifica_tela(self.context.path+"data/images/adcionarMotivo.png", 70)
            self.context.app.clica_imagem(self.context.path+"data/images/down.png", 1,"left", similar=60)
                        
            self.context.app.digitos("down","enter","tab")
            self.context.app.escrever_direto("Teste")
            self.context.app.clica_imagem(self.context.path+"data/images/botao_ok.png", 1, "left", similar=60)
            
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/aguardoAtingido.png", 100, similaridade=60)):
            self.context.app.digitos("enter")
            
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/informacao.png", 100, similaridade=60)):
            self.context.app.digitos("enter")
            
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/sucesso.png", 100, similaridade=50)):
            self.context.app.digitos("enter")
                
        
        
        
        
        