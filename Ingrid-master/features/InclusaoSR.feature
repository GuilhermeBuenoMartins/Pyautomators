@InclusaoSR
Feature: Inclusao SR

  @IncidenciaCriarEvento
  @SPRINT8
  Scenario: criar incidencia
    "Este cenario cria um novo evento de rede com a classificacao de incidencia"

    Given que eu estou na janela Novo Evento de Rede
    When preencho os dados
    Then clico no botao Concluir

  @IncidenciaServicoRede 
  @SPRINT8
  Scenario: Selecionar um servico de rede pendente e colocar em uma equipe desejada
    "Este cenario executa a funcaoo de pesquisa de uma OS marcada como evento de Rede e arrasta para uma equipe"

    Given que estou na tela de Servicos de Rede Pendente
    When dar duplo clique no servico me apresenta as equipes disponiveis na view Recursos Propostos
    Then arrasto o servico de rede para uma equipe
    And verifico se despachado com sucesso

  @IncidenciaAtendimento 
  @SPRINT8
  Scenario: Executar o atendimento da OS manobrada
    "Nesse cenario e realizado a manobra de uma OS e coloca a mesma para uma equipe"

    Given que estou na tela de Servicos de Rede Pendente
    When eu realizo a manobra da OS
    And  entro na view de atendimento da OS
    Then o atendimento e executado com sucesso

  @STDTransformadorCriar 
  @SPIRNT10
  Scenario: Realizar a criacao de uma ordem de servico
    "Nesse cenario e realizado a criacao de uma ordem de servico"

    Given estou na view Servicos de Rede
    When clicar na opcao nova ordem de servico e preencher tipo STD Transformador
    And preencher os outros dados e concluir
    Then uma ordem de servico e criada

  @STDTransformadorAtendimento 
  @SPIRNT10
  Scenario: Realiza o atendimento da ordem de servico
    "Nesse cenario e realizado o atendimento da Ordem de Servico"

    Given que estou na tela de Servicos de Rede Pendente
    And abrir a view de Recursos Propostos
    When clicar duas vezes em um servico pendente STD Transformador
    Then arrasto ordem de servico para a view de recursos propostos

  @STDTransformadorFinalizar 
  @SPIRNT10
  Scenario: Finaliza o atendimento da ordem de servico
    Given que estou na tela de Servicos de Rede Pendente
    When realizar o atendimento da ordem de servico
    Then atendimento e manobra e executado com sucesso

  @STDDiversosCriar 
  @SPRINT10
  Scenario: Cria uma ordem de servico tipo STD Diversos
    Given estou na view Servicos de Rede
    When clicar na opcao ordem de servico e preenche tipo STD Diversos
    And preencher os outros dados e concluir
    Then uma ordem de servico e criada

  @STDDiversosAtendimento 
  @SPRINT10
  Scenario: Realiza o atendimento da Ordem tipo STD Diversos
    Given que estou na tela de Servicos de Rede Pendente
    And abrir a view de Recursos Propostos
    When clicar duas vezes em um servico pendente STD Diversos
    Then arrasto ordem de servico diversos para a view de recursos propostos

  @STDDiversosFinalizar 
  @SPRINT10
  Scenario: Finaliza o atendimento da ordem de servico STD Diversos
    Given que estou na tela de Servicos de Rede Pendente
    When realizar o atendimento da ordem de servico STD Diversos
    Then atendimento e manobra e executado com sucesso

  @STDRedeDistribuicaoCriar 
  @SPRINT10
  Scenario: Cria uma ordem de servico tipo STD Rede Distribuicao
    Given estou na view Servicos de Rede
    When clicar na opcao ordem de servico e preenche tipo STD Rede Distribuicao
    And preencher os outros dados e concluir
    Then uma ordem de servico e criada

  @STDRedeDistribuicaoAtendimento 
  @SPRINT10
  Scenario: Realiza o atendimento da ordem STD Rede Distribuicao
    Given que estou na tela de Servicos de Rede Pendente
    And abrir a view de Recursos Propostos
    When clicar duas vezes em um servico pendente STD Rede de Distribuicao
    Then arrasto ordem de servico rede distribuicao para a view de recursos propostos

  @STDRedeDistribuicaoFinalizar 
  @SPRINT10
  Scenario: Finaliza o atendimento da ordem de servico STD Diversos
    Given que estou na tela de Servicos de Rede Pendente
    When realizar o atendimento da ordem de servico STD Rede Distribuicao
    Then atendimento e manobra e executado com sucesso

  @STDSubestacaoCriar 
  @SPRINT10
  Scenario: Cria uma ordem de servico tipo STD Subestacao
    Given estou na view Servicos de Rede
    When clicar na opcao ordem de servico e preenche tipo STD Substacao
    And preencher os outros dados e concluir
    Then uma ordem de servico e criada

  @STDSubestacaoAtendimento 
  @SPRINT10
  Scenario: Realiza o atendimento da ordem STD Subestacao
    Given que estou na tela de Servicos de Rede Pendente
    And abrir a view de Recursos Propostos
    When clicar duas vezes em um servico pendente STD Subestacao
    Then arrasto ordem de servico subestacao para a view de recursos propostos

  @STDSubestacaoFinalizar 
  @SPRINT10
  Scenario: Finaliza o atendimento da ordem de servico STD Diversos
    Given que estou na tela de Servicos de Rede Pendente
    When realizar o atendimento da ordem de servico STD Subestacao
    Then atendimento e manobra e executado com sucesso
  
  @EventoRedeNaoProgramadoCriar
  Scenario: Cria um novo evento de rede do tipo Nao programada
  Given que eu estou na janela Novo Evento de Rede
  When  preencher dados tipo nao programado
  Then  e criado um novo evento nao programado
  
  @EventoRedeNaoProgramadoSimular
	Scenario: Arrastar a uma equipe desejada
	Given que estou na tela de Servicos de Rede Pendente
	And abrir a view de Recursos Propostos
	When selecionar um evento atuacao nao programada
	Then arrasto o servico de rede para uma equipe
  And verifico se despachado com sucesso
  
  @EventoRedeNaoProgramadoAtender
	Scenario: Arrastar a uma equipe desejada
	Given que estou na tela de Servicos de Rede Pendente
	When seleciono um evento atuacao
	And eu realizo a manobra da OS
	And entro na view de atendimento da OS
  Then o atendimento e executado com sucesso
    
  @EventoRedeProgramadoCriar
 	Scenario: Cria um novo evento de rede do tipo programado
  Given que eu estou na janela Novo Evento de Rede
  When  preencher dados tipo programado
  Then  e criado um novo evento nao programado
  
  
  @EventoRedeProgramadoSimular
	Scenario: Arrastar a uma equipe desejada
	Given que estou na tela de Servicos de Rede Pendente
	And abrir a view de Recursos Propostos
	When selecionar um evento atuacao programada
	Then arrasto o servico de rede para uma equipe
  And verifico se despachado com sucesso
  
  @EventoRedeProgramadoAtender
	Scenario: Arrastar a uma equipe desejada
	Given que estou na tela de Servicos de Rede Pendente
	When seleciono um evento atuacao programado
	And eu realizo a manobra da OS
	And entro na view de atendimento da OS
  Then o atendimento e executado com sucesso

  