'''
Created on 15 de jun de 2018

@author: gcruzm
'''

'''Despachar manualmente'''
@given("abrindo a view de servico de rede")
def step(context):
    context.Despachar_servico_de_rede_manualmente.abrindo_view_servico_rede()

@given("abrir view de equipes")
def step(context):
    context.Despachar_servico_de_rede_manualmente.abir_recursos_propostos()

@when("selecionar o servico de rede de atuacao programada")
def step(context):
    context.Despachar_servico_de_rede_manualmente.selecionar_o_servico_de_rede_de_atuacao_programada()

@then("realizar o despacho manualmente para uma equipe")
def step(context):
    context.Despachar_servico_de_rede_manualmente.realizar_o_despacho_manualmente_para_uma_equipe()

'''Atendimento Unico'''
@given(u'que abro a view de Servico de Rede')
def step_impl(context):
    context.Iniciar_Atendimento_atuacao_programada.abrir_view_servico_de_rede()
@given(u'selecionar o servico de rede de atuacao programada')
def step_impl(context):
    context.Iniciar_Atendimento_atuacao_programada.selecionar_o_servico_de_rede()
@when(u'clicar no lapis para o atendimento unico')
def step_impl(context):
    context.Iniciar_Atendimento_atuacao_programada.clicar_no_lapis_para_o_atendimento_unico()
@then(u'flegar informacao inicio deslocamento e chegada ao local')
def step_impl(context):
    context.Iniciar_Atendimento_atuacao_programada.flegar_informacao_inicio_deslocamento_e_chegada_ao_local()

''' Inclusao Material Servico '''
@then(u'abrir a view para incluir material')
def step_impl(context):
    context.InclusaoMaterial.incluirMaterial() 

@then(u'abrir a view para incluir servico')
def step_impl(context):
    context.InclusaoMaterial.incluirServico() 
    
    
''' Executar manobra e comentario '''
@given("abrir a view de manobras e ordens de manobras")
def step(context):
    context.Executar_manobra_e_ordem_de_manobra.abrir_manobras_ordens_manobras()

@then("view manobras e ordens de manobras e atualizada")
def step_impl(context):
    context.Executar_manobra_e_ordem_de_manobra.verifica_atualizacao_view_ordens_manobras()

'''APRESENTANDO ERRO AO CLICAR EM UMA MANOBRA'''
''' Editar Manobra e Comentarios '''
@then(u'seleciono a ultima manobra na view Manobras e Ordens de Manobras')
def step_impl(context):
    pass

@when(u'clicar no botao Executar Manobra')
def step_impl(context):
    pass

@then(u'preencho os campos necessarios')
def step_impl(context):
    pass

@then(u'clicar em executar')
def step_impl(context):
    pass

@when(u'clicar na opcao modificar e alterar data')
def step_impl(context):
    pass

@then(u'alteracao realizada com sucesso')
def step_impl(context):
    pass
    
''' View interrupcoes '''
@given("abrir a view de Interrupcoes")
def step(context):
    context.View_interrupcoes_ap.abrir_view_interrupcoes()

@then("atualizar a view Interrupcoes")
def step(context):
    context.View_interrupcoes_ap.atualizar_view_interrupcao()

''' Finalizar Atendimento '''

@then("preencho a data final Elemento Falha e clico em OK")
def step(context):
    context.FinalizarAtendimentoAtuacao.preencheCampo()
    
''' Alteracao Campos '''
@given("abrindo a view de servicos de rede programado")
def step_impl(context):
    context.AlteracaoCampos.view_servicos_rede_programado()

@when(u'abrir view de propriedades')
def step_impl(context):
    context.AlteracaoCampos.view_propriedades()

@then(u'alterar campos referente a datas')
def step_impl(context):
    context.AlteracaoCampos.alterar_campo_data()
    
@then(u'alterar campo descricao')
def step_impl(context):
    context.AlteracaoCampos.altera_campo_descricao()
