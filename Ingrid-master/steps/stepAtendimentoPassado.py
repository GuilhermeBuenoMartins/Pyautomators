'''
Created on 7 de nov de 2018

@author: gcruzm
'''
@when("criar ordem de servico")
def step(context):
    context.Atendimento_passado.criar_ordem_de_servico()

@then("localizar ordem de servico")
def step(context):
    context.Atendimento_passado.localizar_ordem_de_servico()

@then("realizar atendimento passado ordem servico")
def step(context):
    context.Atendimento_passado.realizar_atendimento_passado_ordem_servico()