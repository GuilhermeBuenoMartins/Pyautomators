@PESConfiguracaoPrazos
Feature: PES Configuracao Manual

  @1ConfigPrazos
  Scenario: Realiza a configuracao de prazos por fase do workflow
    Given entrar em preferencias
    When pesquisar a configuracao de prazos por fase de workflow
    Then atualizar classificacao urgente

  @PESClassificadoUrgente
  Scenario: Adcionar pedido com classificacao urgente
    Given que estou na View Outros
    When pesquiso e seleciono o pedido de execucao de servico
    And preencho os campos e adiciono um pedido classificado urgente
    Then pedido e adicionado com sucesso
    When abrir a view Pedido de Execucao de Servicos Pendentes
    Then verifico o PES no status Emissao e classificao urgente

  @2ConfigPrazos
  Scenario: Realiza a configuracao de prazos por fase do workflow
    Given entrar em preferencias
    When pesquisar a configuracao de prazos por fase de workflow
    Then atualizar classificacao fora de prazo

  @PESClassificadoForaPrazo
  Scenario: Adcionar pedido com classificacao fora de prazo
    Given que estou na View Outros
    When pesquiso e seleciono o pedido de execucao de servico
    And preencho os campos e adiciono um pedido classificado como fora prazo
    Then pedido e adicionado com sucesso
    When abrir a view Pedido de Execucao de Servicos Pendentes
    Then verifico o PES no status Emissao e classificao fora de prazo

  @3ConfigPrazos
  Scenario: Realizar a configuracao de prazos por fase do workflow
    Given entrar em preferencias
    When pesquisar a configuracao de prazos por fase de workflow
    Then atualizar classificacao normal

  @PESClassificadoNormal
  Scenario: Adcionar pedido com Classificao Normal
    Given que estou na view Outros
  	When pesquiso e seleciono o pedido de execucao de servico
    And preencho os campos e adiciono um pedido classificado como normal
    Then pedido normal e adicionado com sucesso
    When abrir a view Pedido de Execucao de Servicos Pendentes
    Then verifico o PES no status Emissao e classificao Normal
