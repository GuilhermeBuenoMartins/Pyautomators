# -*- coding: utf-8 -*-
'''
Created on 25 de fev de 2019

@author: vgama
'''

''' Unificar SR Pendentes selecionando varios SR´s '''
@given(u'abrir a view de Servicos de Redes Pendentes')
def step_impl(context):
    context.UnificarVariosSR.abrindo_view_servico_rede_pendentes()
    
@when(u'selecionar varios sr clicando com o botao direito')
def step_impl(context):
    context.UnificarVariosSR.selecionado_varios_sr()
    
@then(u'seleciono opcao Unificar Servico de Rede')
def step_impl(context):
    context.UnificarVariosSR.selecionar_opcao_unificar()

@when(u'digitar um dos Servicos de Rede e confirmar acoes')
def step_impl(context):
    context.UnificarVariosSR.informar_sr_e_confirmar()

@then(u'o sistema lista os Servicos de Rede passiveis de unificacao')
def step_impl(context):
    context.UnificarVariosSR.lista_sr_passiveis_unificacao()
@when(u'selecionar os Servicos que possam unificar')
def step_impl(context):
    context.UnificarVariosSR.seleciono_sr_para_unificar()

@then(u'sistema unifica os servicos de rede')
def step_impl(context):
    context.UnificarVariosSR.verifico_unificacao()



''' Unificar SR Pendente a um SR Resolvido '''
@given(u'busco um servico de rede com situacao encerrado')
def step_impl(context):
    context.UnificarSREncerrado.buscar_sr_encerrado()
    
@when(u'selecionar um SR com situacao Encerrado')
def step_impl(context):
    context.UnificarSREncerrado.selecionar_sr_encerrado()
    

@when(u'escrever um dos servico de rede')
def step_impl(context):
    context.UnificarSREncerrado.informar_um_sr_encerrado()
    
          
          