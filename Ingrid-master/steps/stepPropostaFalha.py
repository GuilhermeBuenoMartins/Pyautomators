'''
Created on 4 de jul de 2018

@author: gcruzm
'''

#Configuracao da proposta falha
@given("abrir configuracao proposta falha")
def step(context):
    context.Configuracao_proposta_falha.abrir_configuracao_proposta_falha()


@when("selecionar uma configuracao")
def step(context):
    context.Configuracao_proposta_falha.selecionar_uma_configuracao()

@then("clico no botao ativar")
def step(context):
    context.Configuracao_proposta_falha.clicar_em_desativar_ativar()

@then("verifico se ela esta ativa")
def step(context):
    context.Configuracao_proposta_falha.verifica_configuracao_ativa()

#Proposta transformador
@given("abrir perspectiva busca clientes")
def step(context):
    context.Proposta_falha_transformador.abrir_view_busca_cliente()
    
@when("procurar por transformador")
def step(context):
    context.Proposta_falha_transformador.buscar_por_transformador()
    
@when("selecionar primeiro cliente e gerar aviso")
def step(context):
    context.Proposta_falha_transformador.selecionar_primeiro_cliente()

@then("aviso e criado")
def step(context):
    context.Proposta_falha_transformador.aviso_criado()
    
@when("selecionar segundo cliente e gerar aviso")
def step(context):
    context.Proposta_falha_transformador.selecionar_segundo_cliente()
    
@when("selecionar terceiro cliente e gerar aviso")
def step(context):
    context.Proposta_falha_transformador.selecionar_terceiro_cliente()

@then("verifico se os servicos foram unidos")
def step(context):
    context.Proposta_falha_transformador.verifica_servico_unidos()

#Proposta seccionador
@when("procurar por seccionador")
def step(context):
    context.Proposta_falha_seccionador.buscar_por_seccionador()
    
