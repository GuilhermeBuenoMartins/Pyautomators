# -*- coding: utf-8 -*-
'''
Created on 18 de mai de 2018

@author: gcruzm
'''

from time import sleep

class LoginEquipe(object):
    '''
    Esta Page Tem como objetivo trabalhar com a tela de Login de Equipe
    '''
    def __init__(self,context):
        self.context=context
    
    def entrar_tela_Login_Equipe(self):
        #verifica se o banco esta carregando
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/carregandoBDI.png", 50) != None):
            pass

        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Recursos Propostos") 
        self.context.app.digitos("enter")
        sleep(10)
        self.context.asserts.verifica_tela(self.context.path+"data/images/iconLoginEquipe.png",80,similaridade=80)
        self.context.app.clica_imagem(self.context.path+"data/images/iconLoginEquipe.png", 2, "left", similar=80)
    
    def selecionando_equipe(self,imagem_opcao_equipe):
        #Na tela de Login de equipe seleciono a opcao ultimo login e clico na equipe 
        self.context.asserts.verifica_tela(self.context.path+"data/images/ultimoLogin.png",100)  
        self.context.app.clica_imagem(self.context.path+"data/images/ultimoLogin.png")
        #Cliando no na equipe passada na qual o nome da imagem deve ser o codigo da equipe
        self.context.asserts.verifica_tela(self.context.path+"data/images/{}.png".format(imagem_opcao_equipe),70,valida=True)
        sleep(2)
        self.context.app.clica_imagem(self.context.path+"data/images/{}.png".format(imagem_opcao_equipe))
        
    def preenche_dados_Equipe(self,Nome_profissional):
        #Preenchendo os dados da equipe de Login
        self.context.asserts.verifica_tela(self.context.path+"data/images/avancar.png",80,valida=True)
        self.context.app.clica_imagem(self.context.path+"data/images/avancar.png", 1, "left", similar=60)
        #Procurando o profissional para logar
        self.context.app.clica_imagem(self.context.path+"data/images/campoPesquisaRotulo.png", 1, "left", similar=40)
        self.context.app.escrever_direto(str("").join(list(Nome_profissional)[:-3]))
        sleep(7)
        self.context.app.digitos(("tab",2),"down")
        sleep(3)
        self.context.app.clica_imagem(self.context.path+"data/images/setRight.png", 1, "left", similar=40)
        self.context.app.digitos(("tab",2),"down","space")
        sleep(3)
        self.context.app.digitos(("tab",3),"enter")

        #Concluindo dados da equipe
        sleep(5)
        self.context.asserts.verifica_tela(self.context.path+"data/images/btConcluir.png",100,valida=True)
        self.context.app.clica_imagem(self.context.path+"data/images/btConcluir.png")
        sleep(2)
        self.context.asserts.verifica_tela(self.context.path+"data/images/informacao.png",100)
        
    def confirmar_Login(self):
        #Verificando se login deu sucesso e clicando em OK
        sleep(2)
        self.context.app.clica_imagem(self.context.path+"data/images/botao_ok.png", 1,"left", similar=40)
        
        
class LogoffEquipe(object):
    '''
    Esta Page Tem como objetivo trabalhar com a tela de Logoff de Equipe 
    '''

    def __init__(self,context):
        self.context = context
    
    # =========================
    # Realizar Logoff na equipe
    # =========================
    def abrirTelaLogoffEquipe(self):
        #aguarda sistema carregar
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/carregandoBDI.png", 50) != None):
            pass
        #abrindo a tela de Logoff 
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Recursos Propostos") 
        self.context.app.digitos("enter")
        sleep(10)
        self.context.asserts.verifica_tela(self.context.path+"data/images/iconLogoffEquipe.png", 100, similaridade=80)
        self.context.app.clica_imagem(self.context.path+"data/images/iconLogoffEquipe.png", 1,"left", similar=40)
        sleep(4)
    
    def selecionarEquipeLogoff(self,opcao_equipe):
        #escolhe a equipe para fazer logoff e finaliza
        self.context.app.digitos("tab")  
        sleep(2) 
        self.context.app.escrever_direto(opcao_equipe)
        sleep(2)
        self.context.app.digitos("enter")
        sleep(2)
        self.context.app.digitos("tab")
        sleep(2)
        self.context.app.digitos("down")
        sleep(2)
        self.context.app.digitos(("tab",2),"down")
        self.context.app.clica_imagem(self.context.path+"data/images/btConcluir.png", 1, "left", similar=60)
        
class EditarLogin():
    def __init__(self,context):
        self.context=context
    
    # =========================
    # Realizar Edicao de dados de Login
    # =========================
    def abrirTelaEdicao(self):
        #Abrindo a tela de edição de login
        
        #Aguardando o sistema carregar
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/carregandoBDI.png", 50) != None):
            pass

        #Entrando na tela de edicao
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Recursos Propostos") 
        self.context.app.digitos("enter")
        sleep(10)
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Redes Pendentes")
        sleep(2)         
        self.context.app.digitos("enter")
        
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/refreshServicoPendente.png", 50) != None):
            pass
        
        self.context.app.digitos("down", "enter")
        
        self.context.app.arraste_coordenada(170, 76, 81, 704, "left", 4)
        sleep(5)
        self.context.app.clica_imagem(self.context.path+"data/images/aa18.png", 1, "left", similar=60)
        self.context.app.clica_coordenada(997, 77)
        sleep(3)
        self.context.app.digitos("down")
        sleep(2)
        self.context.app.digitos("enter")
    
    def editar_dados_login(self):
        #Editar um dos dados 
        self.context.app.mantenha_e_digite("shift",["tab","tab","tab","tab","tab","tab","tab","tab"])
        sleep(3)
        self.context.app.digitos("down")
        sleep(4)
    
    def concluir(self):
        #concluir a ação
        self.context.asserts.verifica_tela(self.context.path+"data/images/concluir.png",100,valida=True)
        self.context.app.clica_imagem(self.context.path+"data/images/concluir.png")
        
    def confirmar_sucesso(self):
        #confirmar o sucesso da edicao
        self.context.asserts.verifica_tela(self.context.path+"data/images/informacao.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/botao_ok.png")
        sleep(3)
    
class LogoffOE():    
    def __init__(self,context):
        self.context=context
    
    # =========================
    # Realizar Logoff na aplicação de uma equipe de OE
    # =========================
    
    def selecionar_equipe_pendente(self):

        self.context.app.digitos("tab")
        self.context.app.escrever_direto("AA-28")
        sleep(4)
        self.context.app.clica_imagem(self.context.path+"data/images/conectadaRetaguarda.png",1,"left", similar=30)
        sleep(2)
        self.context.app.digitos(("tab",2),"down")
        sleep(2)
        self.context.asserts.verifica_tela(self.context.path+"data/images/concluir.png",80)
        self.context.app.clica_imagem(self.context.path+"data/images/concluir.png")
    
    def verifica_mensagem(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/avisoLogoofEquipe.png", 60)
        sleep(5)
        self.context.app.digitos("enter")
