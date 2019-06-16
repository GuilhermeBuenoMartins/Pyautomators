@TelaUnica
Feature: Funcionalidade Tela Unica

  @ConcultarDetalhesInterrupcoes
  @Sprint11
  Scenario: Realiza a consulta de destalhes Interrupcoes
    Given que estou na aplicacao Soap
    When abrir o metodo getOutageById
    And preencher o campo Id na aplicacao Soap
    Then o sistema retorna um xml

  @ConsultaAvisosUC
  @Sprint11
  Scenario: Realiza a consulta de Avisos
    Given que estou na aplicacao Soap
    When abrir o metodo getCallsByCustomer
    And preecher o campo de Id UC
    Then o sistema retorna um xml

  @ConsultaInterrupcoes
  @Sprint11
  Scenario: Realiza a consulta de interrupcoes
    Given que estou na aplicacao Soap
    When abrir o metodo getOutagesByCustomer
    And preencher o campo de UC
    Then o sistema retorna um xml

  @ConsultaDetalhesAvisos
  @Sprint11
  Scenario: Realiza a consulta de avisos
    Given que estou na aplicacao Soap
    When abrir o metodo getCallByLabel
    And preencher o campo de Rotulo
    Then o sistema retorna um xml

   @ConsultaAltaAviso
   @Sprint11
   Scenario: Realiza a criacao de um aviso
   Given que estou na aplicacao Soap
   When abrir o metodo insertTroubleCall
   And preecnher todos os campos
   Then o sistema retorna um xml
   
   @ConsultaSituacaoUC
   @Sprint11
   Scenario: Realiza a consulta da situacao da UC
   Given que estou na aplicacao Soap
   When abrir o metodo getCustomerSituation
   And preencher o campo de UC
   Then verifica xml
   
   @DetalheHistoricoGMT
   @Sprint16
   Scenario: Realiza a consulta de processos do GMT
   Given que estou na aplicacao Soap
   When abrir o metodo HistoricalProcessGMT
   And preencher o campo com UC do GMT
   Then o sistema retorna um xml
   
   @InclusaoPedido
   Scenario: Realizar uma inclusao de pedido pelo SOAP
   Given que estou na aplicacao Soap
   When abrir o metodo InsertClientRequest
   And preencher dados para criacao de pedido
   Then o sistema retorna um xml
   