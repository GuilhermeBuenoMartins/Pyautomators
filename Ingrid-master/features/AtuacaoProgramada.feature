@AtuacaoProgramada
Feature: Atuacao Programada

  @DespacharSRManualmente
  Scenario: Despachar o servico de rede manualmente para uma equipe
    Given abrindo a view de servico de rede
    And abrir view de equipes
    When selecionar o servico de rede de atuacao programada
    Then realizar o despacho manualmente para uma equipe

  @Iniciaratendimento
  Scenario: Realizar o atendimento unico do servico de rede
    Given abrindo a view de servico de rede
    When selecionar o servico de rede de atuacao programada
    And clicar no lapis para o atendimento unico
    Then flegar informacao inicio deslocamento e chegada ao local

  @InclusaoMaterialServico
  Scenario: Incluir o material e a causa
    Given abrindo a view de servico de rede
    When selecionar o servico de rede de atuacao programada
    And clicar no lapis para o atendimento unico
    Then abrir a view para incluir material
    And abrir a view para incluir servico

  @ExecutarManobraComentario
  Scenario: Executar manobra e executar o comentario
    Given abrindo a view de servico de rede
    And abrir a view de manobras e ordens de manobras
    When selecionar o servico de rede de atuacao programada
    Then view manobras e ordens de manobras e atualizada

  @EditarManobraComentario
  Scenario: Executar manobras e comentarios
    Given abrindo a view de servico de rede
    And abrir a view de manobras e ordens de manobras
    When selecionar o servico de rede de atuacao programada
    Then seleciono a ultima manobra na view Manobras e Ordens de Manobras
    When clicar no botao Executar Manobra
    Then preencho os campos necessarios
    And clicar em executar
    When clicar na opcao modificar e alterar data
    Then alteracao realizada com sucesso

  @ViewInterrupcoes
  Scenario: realizar a listagem de interrupcoes
    Given abrindo a view de servico de rede
    And abrir a view de Interrupcoes
    When selecionar o servico de rede de atuacao programada
    Then atualizar a view Interrupcoes

  @FinalizarAtendimento
  Scenario: finalizacao de atendimento
    Given abrindo a view de servico de rede
    When selecionar o servico de rede de atuacao programada
    And clicar no lapis para o atendimento unico
    Then preencho a data final Elemento Falha e clico em OK

  @AlteracaoCampos
  Scenario: Alteracao de Campos
    Given abrindo a view de servicos de rede programado
    When selecionar o servico de rede de atuacao programada
    And abrir view de propriedades
    Then alterar campos referente a datas
    And alterar campo descricao
