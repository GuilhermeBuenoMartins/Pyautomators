@ClientesPrioritarios
Feature: Clientes Prioritarios

  @AtendimentoCliente1 
  @SPRINT12
  Scenario: Cria um servico de Rede Tipo Cliente VIP1
    Given que eu estou na view de Servico de Rede
    When entrar na tela de criacao de servico de rede
    And preencher os campos para cliente Vip
    And marcar o SR como emergencial
    Then o sistema cria o SR
    
  @AtendimentoCliente2
  @SPRINT12
  Scenario: Cria um servico de Rede Tipo Cliente Especifico
    Given que eu estou na view de Servico de Rede
    When entrar na tela de criacao de servico de rede
    And preencher os campos para cliente isolado especifico
    And marcar o SR como emergencial
    Then o sistema cria o SR
    
  @AtendimentoCliente3
  @SPRINT12
  Scenario: Cria um servico de Rede Tipo Cliente Consumo
    Given que eu estou na view de Servico de Rede
    When entrar na tela de criacao de servico de rede
    And preencher os campos para cliente subclasse consumo
    And marcar o SR como emergencial
    Then o sistema cria o SR
    
  @AtendimentoCliente4
  @SPRINT12
  Scenario: Realiza atendimento Prioritario
  Given selecionar um SR que possui clientes a jusante do elemento
  When realizar a manobra de abertura no SR
  Then o sistema verifica SR marcado como prioritario
  When selecionar novamente o SR
  Then realizo a manobra de fechamento 