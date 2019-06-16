# -*- coding: utf-8 -*-

'''
Created on 8 de mai de 2018

@author: gdiamante
'''
from time import sleep

#LOGINEQUIPE
@given("entro no Login de Equipe")
def step(context):
    context.LoginEquipe.entrar_tela_Login_Equipe()
 
@when("entro na tela Login Equipe e acho uma equipe")
def step(context):
    context.LoginEquipe.selecionando_equipe(imagem_opcao_equipe='aa18') 
   
@when("preencho os dados necessarios")
def step(context):
    context.LoginEquipe.preenche_dados_Equipe(Nome_profissional="JOSE APARECIDO DA SILVA")
     
@then("aparece botao de 'OK' e confirmar")
def step(context):
    context.LoginEquipe.confirmar_Login()

#LOGOFFEQUIPE
@given("que estou na tela das equipes logadas")
def step(context):
    context.LogoffEquipe.abrirTelaLogoffEquipe()
    
@When("selecionar equipe para fazer logoff e concluir logoff")
def step(context):
    context.LogoffEquipe.selecionarEquipeLogoff("aa-18")

#EDITARDADOSLOGIN
@given("Abrir tela de edicao")
def step(context):
    context.EditarLogin.abrirTelaEdicao()
    
@when("Quando Abrir a edicao e editar dados na equipe")
def step(context):
    context.EditarLogin.editar_dados_login()
    
@when('Vou concluir edicao')
def step(context):
    context.EditarLogin.concluir()
    
@then("Aparecera 'OK'")
def step(context):
    context.EditarLogin.confirmar_sucesso()
    
#LOGOOF COM ORDEM DE SERVICO
@when("seleciono uma equipe com execucao pendente")
def step(context):
    context.LogoffOE.selecionar_equipe_pendente()

@then("apresenta mensagem de aviso")
def step(context):
    context.LogoffOE.verifica_mensagem()