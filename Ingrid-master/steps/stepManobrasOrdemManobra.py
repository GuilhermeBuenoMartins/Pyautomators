'''
Created on 17 de dez de 2018

@author: gcruzm
'''

'''Ordem de manobra 1'''
@when("abrir view manobras e ordem de manobras")
def step(context):
	context.Eliminar_ordem_de_manobra_1.abrir_view_manobras_e_ordem_de_manobras()

@then("e selecionar servico de rede")
def step(context):
	context.Eliminar_ordem_de_manobra_1.e_selecionar_servico_de_rede()

@then("selecionar opcao excluir manobra")
def step(context):
	context.Eliminar_ordem_de_manobra_1.selecionar_opcao_excluir_manobra()
	
@then("concluir exclusao de manobra")
def step(context):
	context.Eliminar_ordem_de_manobra_1.concluir_exclusao_de_manobra()
	

#Ordem de manobra 2
@given("e selecionar servico de rede")
def step(context):
    context.Eliminar_ordem_de_Manobra_2.e_selecionar_servico_de_rede()
    
@when("despachar servico de rede para uma equipe logada")
def step(context):
    context.Eliminar_ordem_de_Manobra_2.despachar_servico_de_rede_para_uma_equipe_logada()
    
@then("abrir view manobras e ordem de manobras")
def step(context):
    context.Eliminar_ordem_de_Manobra_2.abrir_view_manobras_e_ordem_de_manobras()
    
@then("selecionar ordens e excluir")
def step(context):
    context.Eliminar_ordem_de_Manobra_2.selecionar_ordens_e_excluir()

''' 
#Ordem de manobra 3 
@given("buscar um servico de rede finalizado")
def step(context):
    context.Eliminar_ordem_de_manobra_3.buscar_um_servico_de_rede_finalizado()

@when("abrir view manobras e ordem de manobras")
def step(context):
    context.Eliminar_ordem_de_manobra_3.abrir_view_manobras_e_ordem_de_manobras()

@then("selecionar servico de rede finalizado")
def step(context):
    context.Eliminar_ordem_de_manobra_3.selecionar_servico_de_rede_finalizado()

@then("excluir ordem de manobra")
def step(context):
    context.Eliminar_ordem_de_manobra_3.excluir_ordem_de_manobra()
'''