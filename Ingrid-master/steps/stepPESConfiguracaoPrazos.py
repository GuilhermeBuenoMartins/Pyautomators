'''
Created on 12 de mar de 2019

@author: vgama

'''

''' 1 Configuracao de Prazos por fase do workflow Emissao  '''
@given('entrar em preferencias')
def step_impl(context):
    context.PESConfiguracaoPrazos.entrar_configuracao_prazos()

@when('pesquisar a configuracao de prazos por fase de workflow')
def step_impl(context):
    context.PESConfiguracaoPrazos.pesquisar_configuracao()
    

@then('atualizar classificacao urgente')
def step_impl(context):
    context.PESConfiguracaoPrazos.atualizar_classificacao_urgente()


''' PES classificado Urgente '''
@given('que estou na view Outros')
def step_impl(context):
    context.PESClassificadoUrgente.view_outros()

@when('pesquiso e seleciono o pedido de execucao de servico')
def step_impl(context):
    context.PESClassificadoUrgente.pesquiso_pedido_execucao()
    
@when('preencho os campos e adiciono um pedido classificado urgente')
def step_impl(context):
    context.PESClassificadoUrgente.preencher_novo_pedido_urgente()

@then('pedido e adicionado com sucesso')
def step_impl(context):
    context.PESClassificadoUrgente.pedido_adicionado()

@when('abrir a view Pedido de Execucao de Servicos Pendentes')
def step_impl(context):
    context.PESClassificadoUrgente.abrir_view_pedido_execucao()

@then('verifico o PES no status Emissao e classificao urgente')
def step_impl(context):
    context.PESClassificadoUrgente.verifico_pes_classificado_urgente()



'' '2 Configuracao de Prazos por fase do workflow '''
@then('atualizar classificacao fora de prazo')
def step_impl(context):
    context.PESConfiguracaoPrazos.atualizar_classificacao_prazo()
        

''' PES classificado Fora de Prazo '''
@when('preencho os campos e adiciono um pedido classificado como fora prazo')
def step_impl(context):
    context.PESClassificadoForaPrazo.preencher_novo_pedido_fora_prazo()

@then('verifico o PES no status Emissao e classificao fora de prazo')
def step_impl(context):
    context.PESClassificadoForaPrazo.verifico_pes_classificado_fora_prazo()


''' 3 Configuracao de Prazos por fase do workflow '''
@then('atualizar classificacao normal')
def step_impl(context):
    context.PESConfiguracaoPrazos.atualizar_classificacao_normal()
 
 
''' PES classificado como Normal '''
    
@then('pedido normal e adicionado com sucesso')
def step_impl(context):
    context.PESClassificadoNormal.pedido_adicionado_normal()
    
@when('preencho os campos e adiciono um pedido classificado como normal')
def step_impl(context):
    context.PESClassificadoNormal.preencher_pedido_normal()

@then('verifico o PES no status Emissao e classificao Normal')
def step_impl(context):
    context.PESClassificadoNormal.verifico_pes_classificado_normal()








