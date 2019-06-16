'''
Created on 6 de dez de 2018

@author: vgama
'''

''' Consulta Detalhes Interrupcoes '''
@given(u'que estou na aplicacao Soap')
def step_impl(context):
    context.TelaUnica.abrir_soap()

@when(u'abrir o metodo getOutageById')
def step_impl(context):
    context.TelaUnica.abrir_metodo_getOutageById()
    
@when(u'preencher o campo Id na aplicacao Soap')
def step_impl(context):
    context.TelaUnica.preenche_id_telaUnica()


@then(u'o sistema retorna um xml')
def step_impl(context):
    context.TelaUnica.verificacao_xml()
    
''' Consulta Avisos UC '''
@when(u'abrir o metodo getCallsByCustomer')
def step_impl(context):
    context.TelaUnica.abrir_metodo_getCallsByCustomer()


@when(u'preecher o campo de Id UC')
def step_impl(context):
    context.TelaUnica.preenche_uc_telaUnica()

''' Consultar Interrupcoes '''
@when(u'abrir o metodo getOutagesByCustomer')
def step_impl(context):
    context.TelaUnica.abrir_metodo_getOutagesByCustomer()

@when(u'preencher o campo de UC')
def step_impl(context):
    context.TelaUnica.preenche_campo_uc_telaUnica()
    
''' Consultar Detalhes de Avisos '''
@when(u'abrir o metodo getCallByLabel')
def step_impl(context):
    context.TelaUnica.abrir_metodo_getCallByLabel()

@when(u'preencher o campo de Rotulo')
def step_impl(context):
    context.TelaUnica.preenche_campo_rotulo_telaUnica()
    
''' Criacao de Aviso '''
@when(u'abrir o metodo insertTroubleCall')
def step_impl(context):
    context.TelaUnica.abrir_metodo_insertTroubleCall()

@when(u'preecnher todos os campos')
def step_impl(context):
    context.TelaUnica.preencher_campos_insertTroubleCall()

''' Consulta situacao '''
@when(u'abrir o metodo getCustomerSituation')
def step_impl(context):
    context.TelaUnica.abrir_metodo_getCustomerSituation()
    
@then(u'verifica xml')
def step_iml(context):
    context.TelaUnica.verifica_customer_situation()
    
''' Consulta historico GMT '''

@when(u'abrir o metodo HistoricalProcessGMT')
def step_impl(context):
    context.TelaUnica.abrir_metodo_historicalProcessGMT()
    
@when(u'preencher o campo com UC do GMT')
def step_impl(context):
    context.TelaUnica.preenche_campo_uc_gmt()
    
''' Inclusao Pedido '''
@when('abrir o metodo InsertClientRequest')
def step_impl(context):
    context.TelaUnica.abrir_metodo_insertClientRequest()
    
@when('preencher dados para criacao de pedido')
def step_impl(context):
    context.TelaUnica.preencher_dados_pedido()