@PreDespacho
Feature: Realizar o Pre-Despacho

	@SRDespachado
  @SPRINT8
  Scenario: Realiza um pre-despacho
    "Esse cenario realiza o pre despacho de um servico pendente"

    Given que estou na view servicos pendentes
   	When selecionar um servico despachado
    And clicar em Marcar Desmarcar SR pre despacho
    Then retorna uma mensagem devido ter ordem de execucao pendente
    
  @SRAgendado
  @SPRINT8
  Scenario: Realiza um pre-despacho agendado
    """Este cenario realiza um pre despacho em um servico de rede agendado"""

    Given que estou na view servicos de rede
    When seleciono um sr agendado
    And clicar em Marcar Desmarcar SR pre despacho
    Then retorna uma mensagem devido ter ordem de execucao pendente
	
  @MarcarPreDespacho
  @SPRINT8
  Scenario: Fazer um unico pre despacho de um Servico de Rede
    "Neste cenario e executado o pre depacho de um Servico de Rede"

    Given que estou na view servicos pendentes
    When que eu seleciono um servico sem agendamento e equipe
    And clicar em Marcar Desmarcar SR pre despacho
    And preencher os campos solicitados
    Then na view Servico de Rede sera apresentado o campo pre despacho flegado e as datas preenchidas
    When seleciono diversos servicos de rede
    And clicar em Marcar Desmarcar SR pre despacho
    And preencher os campos solicitados
    Then na view Servico de Rede sera apresentado o campo pre despacho flegado e as datas preenchidas
	
	
	@SRMarcadoPreDespacho
	Scenario: Arrasta um SR pre despachado para uma equipe
	Given que estou na view servicos pendentes
	And abrir view de recursos propostos
	When selecionar um sr pre despachado
	And arrastar para alguma equipe
	Then apresenta uma mensagem de erro
  
  @DesmarcarPreDespacho
  @SPRINT9
  Scenario: Desmarca os servico que constam com Pre Despacho
    Given que estou na view servicos pendentes
    When seleciono um servico 
    Then desmarco o predespacho
    When seleciono diversos servicos
		Then desmarco o predespacho
		And verifica sr desmarcado
		
		
  @DesmarcarPreDespachoAut
  @SPRINT9
  Scenario: Desmarcar o pre despacho automatico
    Given que estou na view servicos pendentes
    When que eu seleciono um servico sem agendamento e equipe
    And clicar em Marcar Desmarcar SR pre despacho
    And preencher dados com data fim
    Then verifica sr sem pre despacho
		
  @DespachoAutomatico1
  @SPRINT9
  Scenario: Realizar o despacho automatico de um SR
    Given que estou na view servicos pendentes
   	And abrir view de recursos propostos
		When selecionar um sr pre despachado
		And arrastar para alguma equipe
		Then apresenta uma mensagem de erro
    And clica em desmarcar pre despacho para o SR selecionado
	
  @DespachoAutomatico2
  @SPRINT9
  Scenario: Realizar o despacho automatico de um SR
    Given que estou na view servicos pendentes
    When que eu seleciono um servico sem agendamento e equipe
    And clicar em Marcar Desmarcar SR pre despacho
    And preencher dados com data fim
    Then verifica sr sem pre despacho
