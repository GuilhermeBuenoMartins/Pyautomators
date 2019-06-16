'''
Created on 11 de mar de 2019

@author: vgama
'''

@given('que estou na tela de criacao do PES')
def step_impl(context):
    context.PESGeracaoManual.abrir_pes()

@when('preencher todas as telas e clicar em concluir')
def step_impl(context):
    context.PESGeracaoManual.criacao_PES()

@then('apresenta janela para preencher a classificacao urgente')
def step_impl(context):
    context.PESGeracaoManual.janela_classificacao()

@when('pesquisar o pes criado seleciono a opcao viabilizar')
def step_impl(context):
    context.PESGeracaoManual.pesquisar_pes_criado()

@then('o servico e viabilizado')
def step_impl(context):
    context.PESGeracaoManual.viabilizar_PES()

@when('clicar em reprovar PES e preencher o motivo')
def step_impl(context):
    context.PESGeracaoManual.reprovar_PES()
     
@then('o PES e reprovado') 
def step_impl(context):
    context.PESGeracaoManual.verifica_PES_reprovado()
