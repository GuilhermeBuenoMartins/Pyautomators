'''
Created on 29 de jun de 2018

@author: gcruzm
'''

#Marcar Servico de Rede como passado
@given("buscar servico de rede encerrado")
def step(context):
    context.MarcarServicoRedeComoPassado.buscar_servico_rede_encerrado()

@when("clicar em marcar servico rede passado")
def step(context):
    context.MarcarServicoRedeComoPassado.abrir_marcar_servico_rede_passado()

@then("preencher campos para marcar servico rede passado")
def step(context):
    context.MarcarServicoRedeComoPassado.concluir_marcar_servico_rede_passado()
    context.MarcarServicoRedeComoPassado.verifica_servico_passado()
    
#Simular Servico de Rede
@when('clicar em simular servico rede passado')
def step_impl(context):
    context.SimularServicoRede.clicar_simular_servico_rede()
    
@when("preencher campos se necessario")
def step_impl(context):
    context.SimularServicoRede.preencher_campos_simulacao_sr()

@then('carrega o Entorno de Trabalho Simulado')
def step_impl(context):
    context.SimularServicoRede.carrega_entorno_trabalho()
    
#Excluir Manobras Simuladas
@when("selecionar uma manobra")
def step(context):
    context.ExcluirManobrasSimuladas.selecionar_uma_manobra()
    
@when("selecionar a segunda manobra")
def step(context):
    context.ExcluirManobrasSimuladas.selecionar_segunda_manobra()
    
@then("apagar a manobra selecionada")
def step(context):
    context.ExcluirManobrasSimuladas.apagar_manobra_simulada()

#Incluir Manobras Simuladas

@when(u'clicar na opcao Nova Manobra')
def step_impl(context):
    context.IncluirManobrasSimuladas.clicar_em_nova_manobra()
    
@then(u'inclui uma manobra de abertura')
def step_impl(context):
    context.IncluirManobrasSimuladas.incluir_a_manobra_simulada_aberta()

@then(u'incluir uma manobra de fechamento')
def step_impl(context):
    context.IncluirManobrasSimuladas.incluir_a_manobra_simulada_fechada()
    
#Executar Manobra Simuladas
@when("selecionar a ultima manobra simulada")
def step(context):
    context.ExecutarManobrasSimuladas.selecionar_ultima_manobra()

@then("as manobras executadas e carregada em Lista de Manobras Temporarias")
def step(context):
    context.ExecutarManobrasSimuladas.manobras_carregadas()

#Gerar Interrupcao Temporaria
@when('seleciono a opcao Gerar Interrupcoes')
def step_impl(context):
    context.GerarInterrupcao.geraInterrupcoes()
 
@then('sistema cria interrucoes no elemento manobrado')
def step_impl(context):
    context.GerarInterrupcao.verifica_interrupcao()
 
#Gerar Interrupcao Consumidor
@when('seleciono a opcao Gerar interrupcoes temporarias de consumidores')
def step_impl(context):
    context.InterrupcaoConsumidor.gerar_Interrupcao_Consumidor()

@then('apresenta a view Interrupcoes Previstas')
def step_impl(context):
    context.InterrupcaoConsumidor.verifica_geracao_interrupcao_consumidor()

#Finalizar Reprogramação Manobra
@when(u'clico na opcao para validar a simulacao')
def step_impl(context):
    context.FinalizarInterrupcao.clicar_validar_simulacao()
    
@when('selecionar a ultima manobra temporaria e clicar na opcao Finalizar Reprogramacao')
def step_impl(context):
    context.FinalizarInterrupcao.clicar_em_finalizar_reprogramacao()

@then(u'fechar o entorno de simulacoes e selecionar o servico de rede abrindo Manobras e Ordens de Manobras')
def step_impl(context):
    context.FinalizarInterrupcao.volta_selecionar_sr()
    
@then('abrir a view de Interrupcoes do Servico de Rede')
def step_impl(context):
    context.FinalizarInterrupcao.abrir_view_interrupcoes()

    
#Encerrar Servico Rede


@when('clicar em encerrar servico rede passado')
def step_impl(context):
    context.EncerrarServicoRedeMarcadoComoPassado.encerrar_servico_rede_passada()

@then("servico de rede e encerrado com sucesso")
def step(context):
    context.EncerrarServicoRedeMarcadoComoPassado.verifica_servico_encerrado()