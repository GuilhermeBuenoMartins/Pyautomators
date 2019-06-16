@ServicoRedePassado
Feature: Servico Rede Passado

  @marcarServicoRedePassado
  Scenario: marcar servico de rede como passado
    Given buscar servico de rede encerrado
    When clicar em marcar servico rede passado
    Then preencher campos para marcar servico rede passado

  @SimularServicoRede 
  @SPRINT7
  Scenario: Realizar a simulacao do servico de rede
    Given buscar servico de rede encerrado
    When clicar em simular servico rede passado
    And preencher campos se necessario
    Then carrega o Entorno de Trabalho Simulado
	
  @excluirManobrasSimuladas
  Scenario: excluir manobra simulada
    Given buscar servico de rede encerrado
    When clicar em simular servico rede passado
		Then carrega o Entorno de Trabalho Simulado
		When selecionar uma manobra 
		Then apagar a manobra selecionada
		When selecionar a segunda manobra
		Then apagar a manobra selecionada
		
  @incluirManobrasSimuladas
  Scenario: Inclusao de novas manobras simuladas
    Given buscar servico de rede encerrado
    When clicar em simular servico rede passado
		Then carrega o Entorno de Trabalho Simulado
		When selecionar uma manobra 
		Then apagar a manobra selecionada
		When selecionar a segunda manobra
		Then apagar a manobra selecionada
		When clicar na opcao Nova Manobra
		Then inclui uma manobra de abertura
		And  incluir uma manobra de fechamento

  @executarManobrasSimuladas
  Scenario: executar manobras simuladas
   	Given buscar servico de rede encerrado
    When clicar em simular servico rede passado
		Then carrega o Entorno de Trabalho Simulado
		When selecionar a ultima manobra simulada
		Then as manobras executadas e carregada em Lista de Manobras Temporarias
    
  @GerarInterrupcaoTemporaria 
  @SPRINT7
  Scenario: Realizar uma interrupcao temporaria
    "Esse cenario realiza uma interrupcao temporaria"
		Given buscar servico de rede encerrado
    When clicar em simular servico rede passado
		Then carrega o Entorno de Trabalho Simulado
		When selecionar a ultima manobra simulada
		Then as manobras executadas e carregada em Lista de Manobras Temporarias
    When seleciono a opcao Gerar Interrupcoes
		Then sistema cria interrucoes no elemento manobrado
		
  @GerarInterrupcaoConsumidor 
  @SPRINT7
  Scenario: Este cenario realiza a interrupcao temporario em consumidores
    "Esse cenario realiza uma interrupcao temporaria em consumidor"
		Given buscar servico de rede encerrado
    When clicar em simular servico rede passado
		Then carrega o Entorno de Trabalho Simulado
		When selecionar a ultima manobra simulada
		Then as manobras executadas e carregada em Lista de Manobras Temporarias
    When seleciono a opcao Gerar Interrupcoes
		Then sistema cria interrucoes no elemento manobrado
    When seleciono a opcao Gerar interrupcoes temporarias de consumidores
    Then apresenta a view Interrupcoes Previstas
	
  @FinalizarReprogramacaoManobra 
  @SPRINT7
  Scenario:
  	Given buscar servico de rede encerrado
    When clicar em simular servico rede passado
		Then carrega o Entorno de Trabalho Simulado
		When selecionar a ultima manobra simulada
		Then as manobras executadas e carregada em Lista de Manobras Temporarias
    When seleciono a opcao Gerar Interrupcoes
		Then sistema cria interrucoes no elemento manobrado
    When seleciono a opcao Gerar interrupcoes temporarias de consumidores
    Then apresenta a view Interrupcoes Previstas
    When clico na opcao para validar a simulacao
    And selecionar a ultima manobra temporaria e clicar na opcao Finalizar Reprogramacao
    Then fechar o entorno de simulacoes e selecionar o servico de rede abrindo Manobras e Ordens de Manobras
    And abrir a view de Interrupcoes do Servico de Rede

  @encerrarServicoRedeMarcadoComoPassado
  Scenario: Finalizar reprogramacao de manobras
    Given buscar servico de rede encerrado
    When clicar em encerrar servico rede passado
    Then servico de rede e encerrado com sucesso 


