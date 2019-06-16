'''
Created on 14 de dez de 2018

@author: gcruzm
'''

#iniciar_atendimento_os_pelo_workflow_de_oe
@given("abrir view lista de recursos do servico de rede")
def step(context):
    context.Iniciar_atendimento_da_os_pelo_workflow.abrir_view_lista_de_recursos_do_servico_de_rede()

@when("selecionando servico de rede pendente")
def step(context):
    context.Iniciar_atendimento_da_os_pelo_workflow.selecionando_servico_de_rede_pendente()

@then("e selecionando opcao iniciar atendimento da ordem de servico pela equipe")
def step(context):
    context.Iniciar_atendimento_da_os_pelo_workflow.e_selecionando_opcao_iniciar_atendimento_da_ordem_de_servico_pela_equipe()
    

#Postergar_o_atendimento_da_os
@when("seleciono opcao adiar")
def step(context):
    context.Postergar_o_atendimento_da_os.e_selecionar_opcao_adiar()

@then("preencho dados do adiar")
def step(context):
    context.Postergar_o_atendimento_da_os.preencher_dados_do_adiar()


#Reiniciar o atendimento da os 
@then("e selecionar opcao inicia deslocamento ate o local de atendimento")
def step(context):
    context.Reiniciar_o_atendimento_da_os.e_selecionar_opcao_inicia_deslocamento_ate_o_local_de_atendimento()

@then("concluir inicio do deslocamento")
def step(context):
    context.Reiniciar_o_atendimento_da_os.concluir_inicio_do_deslocamento()


#executar manobra - abertura
@given("clicar em manobras")
def step(context):
    context.Abertura_manobra.clicar_em_manobras()
    
@when("preencher dados da abertura da manobra")
def step(context):
    context.Abertura_manobra.preencher_dados_da_abertura_da_manobra()

#executar manobra - fechamento
@when("preencher dados do fechamento da manobra")
def step(context):
    context.Fechamento_manobra.preeencher_dados_do_fechamento_da_manobra()


#view interrupcoes
@given("abrir view interrupcoes")
def step(context):
    context.View_interrupcoes.abrir_view_interrupcoes()
@when("selecionar servico de rede")
def step(context):
    context.View_interrupcoes.selecionar_servico_de_rede()
@then("atualizar view interrupcoes")
def step(context):
    context.View_interrupcoes.atualizar_view_interrupcoes()


#Definir elemento de referencia
@then("e selecionando opcao definir elemento de referencia da os")
def step(context):
    context.Definir_elemento_de_referencia_da_ordem_de_servico.e_selecionando_opcao_definir_elemento_de_referencia_da_os()

#Definir causa da os
@then("e selecionando opcao definir causa da os")
def step(context):
    context.Definir_causa_da_ordem_de_servico.e_selecionando_opcao_definir_causa_da_os()

#incluir material
@when("e selecionando opcao material")
def step(context):
    context.Incluir_material_na_ordem_de_servico.e_selecionando_opcao_material()

@when("clicar em adicao para incluir materiais")
def step(context):
    context.Incluir_material_na_ordem_de_servico.clicar_em_adicao_para_incluir_materiais()

@then("preencher dados da inclusao de material")
def step(context):
    context.Incluir_material_na_ordem_de_servico.preencher_dados_da_inclusao_de_material()
    

#incluir servico
@then("e selecionando opcao servico")
def step(context):
    context.Incluir_um_servico_para_a_ordem_de_servico.e_selecionando_opcao_atividade()
@then("clicar em adicao para incluir servicos")
def step(context):
    context.Incluir_um_servico_para_a_ordem_de_servico.clicar_em_adicao_para_incluir_servicos()
@then("preencher dados da inclusao de servico")
def step(context):
    context.Incluir_um_servico_para_a_ordem_de_servico.preencher_dados_da_inclusao_de_servico()

#finalizar atendimento
@then("e selecionando opcao finalizar atendimento")
def step(context):
    context.Finalizar_atendimento_da_ordem_de_servico.e_selecionando_opcao_finalizar_atendimento()