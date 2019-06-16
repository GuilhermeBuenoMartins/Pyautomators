'''
Created on 8 de jan de 2019

@author: gcruzm
'''

'''Criar filtro zonal'''
@given("clicar alterar o filtro de area")
def step(context):
    context.Criar_filtro_zonal.clicar_alterar_o_filtro_de_area()
    
@when("clicar no botao criar e preencher dados")
def step(context):
    context.Criar_filtro_zonal.clicar_no_botao_criar_e_preencher_dados()
    
@then("verifica se o filtro zonal foi aplicado")
def step(context):
    context.Criar_filtro_zonal.verifica_filtro_zonal_aplicado()

    
'''Modificar Filtro Zonal'''
@when("clicar em modificar")
def step(context):
    context.Modificar_filtro_zonal.clicar_em_modificar()
    
@then("preeche os dados")
def step(context):
    context.Modificar_filtro_zonal.preecher_dados()

@when("selecionar filtro modificado")
def step(context):
    context.Modificar_filtro_zonal.clica_filtro_zonal_modificado()
    
@then("verifica filtro zonal modificado aplicado")
def step(context):
    context.Modificar_filtro_zonal.verifica_filtro_alterado()

'''Criar copia de um filtro zonal existente'''
    
@then("flegar criar copia a partir do filtro")
def step(context):
    context.Cria_copia_a_partir_de_um_existente.flegar_criar_copia_a_partir_do_filtro()
    
@then("selecionar o filtro copia")
def step(context):
    context.Cria_copia_a_partir_de_um_existente.selecionar_filtro_copia()
    
    
'''Eliminar filtro zonal'''
@when("clicar em eliminar")
def step(context):
    context.Eliminar_filtro_zonal.clicar_em_eliminar()