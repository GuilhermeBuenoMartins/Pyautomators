'''
Created on 20 de dez de 2018

@author: vgama
'''

''' Atendimento Cliente Prioritario 1 '''
@given(u'que eu estou na view de Servico de Rede')
def step_impl(context):
    context.ClientesPrioritarios.view_servico_rede()

@when(u'entrar na tela de criacao de servico de rede')
def step_impl(context):
    context.ClientesPrioritarios.criacao_servico_rede()
    
@when(u'preencher os campos para cliente Vip')
def step_impl(context):
    context.ClientesPrioritarios.preencher_campos_cliente_vip()
    
@when(u'marcar o SR como emergencial')
def step_impl(context):
    context.ClientesPrioritarios.marcar_sr_comercial()

@then(u'o sistema cria o SR')
def step_impl(context):
    context.ClientesPrioritarios.verifica_criacao_os_emergencial()

''' Atendimento Cliente Prioritario 2 '''
@when(u'preencher os campos para cliente isolado especifico')
def step_impl(context):
    context.ClientesPrioritarios.preencher_campos_cliente_especifico()
    
    
''' Atendimento Cliente Prioritario 3 '''
@when(u'preencher os campos para cliente subclasse consumo')
def step_impl(context):
    context.ClientesPrioritarios.preencher_campos_cliente_especifico()
    
    
''' Atendimento Cliente Prioritario 4 '''
@given(u'selecionar um SR que possui clientes a jusante do elemento')
def step_impl(context):
    context.ClientesPrioritarios.selecionar_sr_da_pre_condicao()

@when(u'realizar a manobra de abertura no SR')
def step_impl(context):
    context.ClientesPrioritarios.realizar_manobra_abertura()
    
@then(u'o sistema verifica SR marcado como prioritario')
def step_impl(context):
    context.ClientesPrioritarios.verifica_sr()
    
@when(u'selecionar novamente o SR')
def step_impl(context):
    context.ClientesPrioritarios.seleciona_sr_novamente()
    
@then(u'realizo a manobra de fechamento')
def step_impl(context):
    context.ClientesPrioritarios.realiza_manobra_fechamento()
    
    