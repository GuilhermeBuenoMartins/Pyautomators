'''
Created on 26 de nov de 2018
@author: gcruzm
'''

#CRIACAO DE AVISO
@given("abrir perspectiva atencao de avisos")
def step(context):
    context.Criacao_de_aviso.abrir_perspectiva_atencao_de_avisos()

@when("buscar contato desejado")
def step(context):
    context.Criacao_de_aviso.buscar_contato_desejado()

@then("clicar em novo aviso")
def step(context):
    context.Criacao_de_aviso.clicar_em_novo_aviso()
    
@then("preencher dados do novo aviso")
def step(context):
    context.Criacao_de_aviso.preencher_dados_do_novo_aviso()


#CRIACAO DE AVISO SEM CLIENTE
@then("preencher dados do cliente nao cadastrado")
def step(context):
    context.Criacao_de_aviso_sem_cliente.preencher_dados_do_cliente_nao_cadastrado()
    
@then("verificar aviso criado")
def step(context):
    context.Criacao_de_aviso_sem_cliente.verificar_aviso_criado()

@then("visualizar mensagem do aviso")
def step(context):
    context.Criacao_de_aviso_sem_cliente.visualizar_mensagem_do_aviso()


#Associacao de avisos
@when("selecionar servico rede associacao aviso")
def step(context):
    context.Associacao_de_avisos.selecionar_servico_rede_associacao_aviso()

@then("realizar manobra servico rede da associacao aviso")
def step(context):
    context.Associacao_de_avisos.realizar_manobra_servico_rede_da_associacao_aviso()

#:::::::::::::::::::::::::
'''Extrair aviso novo'''
#:::::::::::::::::::::::::
@given("abrir view avisos de servico de rede")
def step(context):
    context.Extrair_aviso_novo.abrir_view_avisos_de_servico_de_rede()

@when("selecionando aviso novo")
def step(context):
    context.Extrair_aviso_novo.selecionando_aviso_novo()

@then("clico na view avisos servico de rede")
def step(context):
    context.Extrair_aviso_novo.clico_na_view_avisos_servico_de_rede()

@then("selecionando aviso dentro da view")
def step(context):
    context.Extrair_aviso_novo.selecionando_aviso_dentro_da_view()
    
@then("clicar em extrair aviso")
def step(context):
    context.Extrair_aviso_novo.clicar_em_extrair_aviso()
    

#:::::::::::::::::::::::::::::::::
''' Extrair aviso existente'''
#:::::::::::::::::::::::::::::::::
@when("selecionar aviso existentes")
def step(context):
    context.Extrair_aviso_existente.selecionar_aviso_existente()
    
@then("realizar extracao de aviso existente")
def step(context):
    context.Extrair_aviso_existente.realizar_extracao_de_aviso_existente()
    
#:::::::::::::::::::::::::::
'''Anular aviso associado'''
#:::::::::::::::::::::::::::
@then("selecionar view aviso cliente")
def step(context):
    context.Anular_aviso_associado_a_um_cliente.selecionar_view_aviso_cliente()
    
@then("selecionar aviso associado ao cliente")
def step(context):
    context.Anular_aviso_associado_a_um_cliente.selecionar_aviso_associado_ao_cliente()
    
@then("selecionar opcao anular aviso associado")
def step(context):
    context.Anular_aviso_associado_a_um_cliente.selecionar_opcao_anular_aviso_associado()
    
'''Anular servico de rede despachado'''
@then("selecionar servico de rede para despachar")
def step(context):
    context.Anular_servico_de_rede_despachado.selecionar_servico_de_rede_para_despachar()

@then("realizar o despacho do servico de rede")
def step(context):
    context.Anular_servico_de_rede_despachado.realizar_o_despacho_do_servico_de_rede()

@then("clicar em resgatar ordem de servico")
def step(context):
    context.Anular_servico_de_rede_despachado.clicar_em_resgatar_ordem_de_servico()


#::::::::::::::::::::::
'''arvore de avisos'''
#::::::::::::::::::::::
@when("abrir view arvore de avisos")
def step(context):
    context.View_arvore_de_avisos.apertar_ctrl_e_3_e_pesquisar_view_arvore_de_aviso()

@then("clicar em atualizar")
def step(context):
    context.View_arvore_de_avisos.clicar_em_atualizar()

@then("clicar em desmembrar")
def step(context):
    context.View_arvore_de_avisos.clicar_em_desmembrar()

#::::::::::::::::::::::
'''arvore de avisos'''
#::::::::::::::::::::::
@then("clicar em marcar como improcedente")
def step(context):
    context.Aviso_improcedente.clicar_em_marcar_como_improcedente()

@then("preencher dados")
def step(context):
    context.Aviso_improcedente.preencher_dados()