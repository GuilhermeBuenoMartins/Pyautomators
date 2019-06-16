'''
Created on 3 de dez de 2018

@author: vgama
'''
from time import sleep
        
@given(u'envio o sinal scada aberto')
def step_impl(context):
    context.Scada.enviar_sinal_scada_aberto()
    
@when(u'o ingrid recebe o sinal e cria um servico de rede')
def step_impl(context):
    context.Scada.abrindo_servicos_de_rede()
    context.Scada.abrir_view_ordens_de_manobra()
    context.Scada.verificando_view_manobra()

@then(u'verifica a atualizacao da view no painel integracao')
def step_impl(context):
    context.Scada.abrir_view_painel_integracao()
    
''' Scada sinal fechado '''
@given(u'envio sinal fechado')
def step_impl(context):
    context.Scada.envia_sinal_scada_fechado()

@when(u'ingrid recebe sinal fechado e cria servico de rede')
def step_impl(context):
    context.Scada.abrindo_servicos_de_rede()
    context.Scada.abrir_view_ordens_de_manobra()
    context.Scada.verificando_view_manobra_acao_fechado()