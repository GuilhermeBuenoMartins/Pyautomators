# -*- coding: utf-8 -*-
'''
Created on 14 de jun de 2018

@author: gcruzm
'''


from time import sleep

#Criacao de OS restricao operativa
@given("View de Restricao Operativa aberta")
def step(context):
    context.CriarOS.abreViewRestricaoOperativa()

@when("Criar restricao operativa do tipo subestacao")
def step(context):
    context.CriarOS.criar_restricao_operativa()

@Then("Preencher dados da restricao operativa subestacao e conclui")
def step(context):
    context.CriarOS.preencher_dados_criacao_subestacao()
    context.CriarOS.concluir_criacao_restricao_operativa()

@when("Criar restricao operativa do tipo transformador")
def step(context):
    context.CriarOS.criar_restricao_operativa()
    
@then("Preencher dados da restricao operativa transformador e conclui")
def step(context):
    context.CriarOS.preencher_dados_criacao_transformador()

'''Listar restricoes operativas do tipo subestacao'''
@when("Listar restricao operativa do tipo subestacao")
def step(context):
    context.Atender_encerrar_subestacao_transformador.listar_restricao_operativa_subestacao()


'''Listar restricoes operativas do tipo transformador'''
@when("Listar restricao operativa do tipo transformador")
def step(context):
    context.Atender_encerrar_subestacao_transformador.listar_restricao_operativa_transformador()

'''Incluir e editar a restricao operativa'''
@when("buscar restricao operativa")
def step(context):
    context.Incluir_editar_restricao_operativa.buscar_restricao_operativa()

@then("modificar restricao operativa")
def step(context):
    context.Incluir_editar_restricao_operativa.modificar_restricao_operativa()


'''Ordenacao de colunas'''
@when("realizar ordenacao das colunas subestacao matricula")
def step(context):
    context.Ordenacao_de_colunas.realizar_ordenacao_das_colunas_subestacaoMatricula()

@then("realizar ordenacao da coluna alimentador matricula")
def step(context):
    context.Ordenacao_de_colunas.realizar_ordenacao_da_coluna_alimentador_matricula()

@then("realizar ordenacao da coluna tipo elemento")
def step(context):
    context.Ordenacao_de_colunas.realizar_ordenacao_da_coluna_tipo_elemento()

@then("realizar ordenacao da coluna matricula")
def step(context):
    context.Ordenacao_de_colunas.realizar_ordenacao_da_coluna_matricula()

@then("realizar ordenacao da coluna data inicio")
def step(context):
    context.Ordenacao_de_colunas.realizar_ordenacao_da_coluna_data_inicio()

@then("realizar ordenacao da coluna data fim previsto")
def step(context):
    context.Ordenacao_de_colunas.realizar_ordenacao_da_coluna_data_fim_previsto() 

@then("realizar ordenacao da coluna data fim")
def step(context):
    context.Ordenacao_de_colunas.realizar_ordenacao_da_coluna_data_fim()
    
@then("realizar ordenacao da coluna observacao")
def step(context):
    context.Ordenacao_de_colunas.realizar_ordenacao_da_coluna_observacao()

@then("realizar ordenacao da coluna responsavel aberta")
def step(context):
    context.Ordenacao_de_colunas.realizar_ordenaca_da_coluna_responsavel_aberta()

@then("realizar ordenacao da coluna responsavel encerramento")
def step(context):
    context.Ordenacao_de_colunas.realizar_ordenaca_da_coluna_responsavel_encerramento()

@then("realizar ordenacao da coluna estado")
def step(context):
    context.Ordenacao_de_colunas.realizar_ordenaca_da_coluna_estado()

@then("realizar ordenacao da coluna motivo")
def step(context):
    context.Ordenacao_de_colunas.realizar_ordenaca_da_coluna_motivo()
    
    
'''Localizar elemento graficamente'''
@when("Selecionar restricao operativa existente")
def step(context):
    context.Localizar_restricao_operativa_graficamente.selecionar_restricao_operativa_existente()

@then("Selecionar icone localizar elemento graficamente")
def step(context):
    context.Localizar_restricao_operativa_graficamente.selecionar_icone_localizar_elemento_graficamente()


''' Busca Operativa '''
@given(u'que estou na view Restricoes Operativas')                                                                      
def step_impl(context):
    context.BuscaOperativa.abrirView()

@when(u'buscar por um Tipo de Elemento')
def step_impl(context):
    context.BuscaOperativa.buscarElemento()
    
@then(u'o sistema filtra por tipo de elemento buscado')
def step_impl(context):                                                                                                     
    context.BuscaOperativa.verificaElemento()

'''Busca Responsavel '''
@given(u'que estou na tela de Restricoes Operativas')                                                                      
def step_impl(context):
    context.BuscaOperativa.abrirView()

@when(u'realizar uma busca por Responsavel')
def step_impl(context):
    context.BuscaOperativa.buscarResponsavel()

@then(u'o sistema filtra por Responsavel')                                                                              
def step_impl(context):
    context.BuscaOperativa.verificaResponsalvel()

''' Busca Matricula '''
@given(u'que estou na tela Restricoes Operativas')                                                                      
def step_impl(context):
    context.BuscaOperativa.abrirView()

@when(u'realizar uma busca por Matricula')                                                                      
def step_impl(context):
    context.BuscaOperativa.buscarMatricula()

@then(u'o sitema filtra por Matricula')                                                                      
def step_impl(context):
    context.BuscaOperativa.verificaMatricula()
    
    
'''Encerrar restricao Operativa'''
@when("Selecionar restricao operativa pendente")
def step(context):
    context.Encerrar_restricao_operativa.selecionar_restricao_operativa_pendente()
    
@then("Clicar no icone encerrar restricao operativa")
def step(context):
    context.Encerrar_restricao_operativa.clicar_no_icone_encerrar_restricao_operativa()
