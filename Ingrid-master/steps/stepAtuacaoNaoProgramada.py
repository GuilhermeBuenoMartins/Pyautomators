'''
Created on 26 de nov de 2018

@author: gcruzm
'''


'''Criar evento de rede'''
@given("carregar view sr pendente e clicar na ferramenta verde")
def step(context):
    context.criar_evento_de_rede.carregar_view_sr_pendente_e_clicar_na_ferramenta_verde()
@when("preencher dados do novo evento rede")
def step(context):
    context.criar_evento_de_rede.preencher_dados_novo_evento_rede()
    
'''Manobrar'''
@given("procurar evento de rede nao programado")
def step(context):
    context.manobrar_evento_de_rede_nao_programado.procurar_evento_de_rede_nao_programado()
@when("clicar no icone de manobra para manobrar o evento de rede")
def step(context):
    context.manobrar_evento_de_rede_nao_programado.clicar_no_icone_de_manobra_para_manobrar_o_evento_de_rede()
@then("clicar no botao executar para executar a manobra")
def step(context):
    context.manobrar_evento_de_rede_nao_programado.clicar_no_botao_executar_para_executar_a_manobra()


'''Atendimento passado'''
@when("realizar atendimento passado ordem servico")
def step(context):
    context.Atendimento_passado_atuacao_nao_programada.clicar_na_seta_do_lado_do_lapis()


'''iniciar atendimento da ordem de evento'''
@given("selecionar servico de rede para o atendimento da oe")
def step(context):
    context.Iniciar_atendimento_da_oe_e_inicio_deslocamento.selecionar_servico_de_rede_para_o_atendimento_da_oe()

@when("clicar em atendimento unico e preencher dados necessarios")
def step(context):
    context.Iniciar_atendimento_da_oe_e_inicio_deslocamento.clicar_em_atendimento_unico_e_preencher_dados_necessarios()

@then("confirmar o atendimento da oe")
def step(context):
    context.Iniciar_atendimento_da_oe_e_inicio_deslocamento.confirmar_o_atendimento_da_oe()
    

'''Inclusao de material, servico e causa'''
@given("selecionar ordem de servico para inclusao")
def step(context):
    context.Inclusao_de_material_servico_causa_e_observacao.selecionar_ordem_de_servico_para_inclusao()

@when("abrir atendimento unico")
def step(context):
    context.Inclusao_de_material_servico_causa_e_observacao.abrir_atendimento_unico()

@then("incluir material")
def step(context):
    context.Inclusao_de_material_servico_causa_e_observacao.incluir_material()

@then("incluir servico")
def step(context):
    context.Inclusao_de_material_servico_causa_e_observacao.incluir_servico()

@then("incluir causa")
def step(context):
    context.Inclusao_de_material_servico_causa_e_observacao.incluir_causa()
    

'''Finalizar ordem de servico'''
@given("selecionar o servico de rede para finalizar")
def step(context):
    context.Finalizar_ordem_de_servico.selecionaServico()
    
@when("clicar na opcao atendimento")
def step2(context):
    context.Finalizar_ordem_de_servico.opcaoAtendimento()

@then("preencho a data final, Elemento Falha e clico em OK")
def step3(context):
    context.Finalizar_ordem_de_servico.preencheCampo()

    

'''Anular servico de rede pendente'''
@given("localizar sr")
def step(context):
    context.Anular_servico_de_rede_pendente.selecionar_sr_pendente()

@when("apertar botao direito no sr")
def step(context):
    context.Anular_servico_de_rede_pendente.botao_direito_no_sr()

@then("selecionar opcao anular aviso")
def step(context):
    context.Anular_servico_de_rede_pendente.selecionar_opcao_anular_aviso()

@then("concluir anulacao aviso pendente")
def step(context):
    context.Anular_servico_de_rede_pendente.concluir_anulacao_aviso_pendente() 
    

'''Anular servico de rede com atendimento iniciado'''
@given("Selecionar o SR iniciado")
def step(context):
    context.Anular_servico_de_rede_com_atendimento_iniciado.selecionarSRIniciado()

@when("Escolher a opcao anular aviso")
def step(context):
    context.Anular_servico_de_rede_com_atendimento_iniciado.escolherOpcaoAnularAviso()

@then("preencher dados da anulacao")
def step(context):
    context.Anular_servico_de_rede_com_atendimento_iniciado.preencherDadosAnularAviso()