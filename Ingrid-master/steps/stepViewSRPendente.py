'''
Created on 17 de jul de 2018
@author: gdiamante

Modified on 20 de dez de 2018
@author: gcruzm
'''

'''Ordenacao das colunas'''
@given("Abrir view servico de rede pendente")
def step(context):
    context.Ordenacao_das_colunas.Abrir_view_servico_de_rede_pendente()

@when("Realizar ordenacao das colunas")
def step(context):
    context.Ordenacao_das_colunas.Realizar_ordenacao_das_colunas()


'''Criando sub-filtro'''
@when("clicar na seta pra baixo")
def step(context):
    context.Criar_filtros.clicar_na_seta_pra_baixo()

@then("selecionar opcao configurar filtro")
def step(context):
    context.Criar_filtros.selecionar_opcao_configurar_filtro()

@then("clicar no botao novo")
def step(context):
    context.Criar_filtros.clicar_no_botao_novo()


'''Propriedades da view'''
@when("selecionar um servico de rede pendente")
def step(context):
    context.Propriedades_da_view.selecionar_um_servico_de_rede_pendente()

@then("abrir view propriedades da view")
def step(context):
    context.Propriedades_da_view.abrir_view_propriedades_da_view()

@then("verificar informacoes do servico de rede")
def step(context):
    context.Propriedades_da_view.verificar_informacoes_do_servico_de_rede()