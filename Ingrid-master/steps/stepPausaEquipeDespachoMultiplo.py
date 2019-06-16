'''
Created on 12 de dez de 2018

@author: gcruzm
'''

#Pausar a equipe
@given("abrir recursos propostos")
def step(context):
    context.Pausar_equipe.abrir_recursos_propostos()
@when("abrir view servico de rede pendente pausa e despacho multiplo")
def step(context):
    context.Pausar_equipe.abrir_view_servico_de_rede_pendente_pausa_e_despacho_multiplo()
@then("selecionar equipe nao despachada")
def step(context):
    context.Pausar_equipe.selecionar_equipe_nao_despachada()

@then("clicar no icone pausa a equipe")
def step(context):
    context.Pausar_equipe.clicar_no_icone_pausa_a_equipe()
    

#Despacho multiplo
@then("selecionando servicos de rede para despacho multiplo")
def step(context):
    context.Despacho_multiplo.selecionando_servicos_de_rede_para_despacho_multiplo()

@then("arrastando servicos para equipe")
def step(context):
    context.Despacho_multiplo.arrastando_servicos_para_equipe()

@then("despachando servicos para equipe")
def step(context):
    context.Despacho_multiplo.despachando_servicos_para_equipe()
    

#Pausa atendimento
@then("selecionar equipe despachada")
def step(context):
    context.Pausar_atendimento.selecionar_equipe_despachada()

@then("preenche dados motivo recuperacao")
def step(context):
    context.Pausar_equipe.preenche_campos_motivo_recuperacao()