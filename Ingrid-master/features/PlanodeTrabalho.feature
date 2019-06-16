@PlanoDeTrabalho
Feature: Plano de Trabalhando

  @AgendamentoDespachandoEquipe
  @SPRINT8
  Scenario: Realiza o agendamento de OS
    "Este cenario realiza o agendamento de uma OS para uma equipe selecionada"
    Given selecionar um OS na view de Lista de OS
    When arrastar a OS para a equipe
    Then preencher o tipo de agendamento
  
  
  @AgendamentoPosterior
  @SPRINT9
  Scenario: Agendameto tipo diario data posterior agendamento
    Given selecionar um OS na view de Lista de OS
    When arrastar a OS para a equipe
    And preencher o tipo de  agendamento diario
    Then conectar o PDA no dia posterior
    
  @AgendamentoDataHora
  @SPRINT9
  Scenario: Realizar o agendameno e editar nova dataHora
    Given selecionar um OS na view de Lista de OS
    When arrastar a OS para a equipe
    And preencher o tipo de  agendamento diario
    Then Aumentar Diminuir a marcacao

  @ExibirPlanoTrabalho
  @SPRINT9
  Scenario: Realizar a exibicao do plano de trabalho para agendamento de OS
    Given na view Plano de trabalho selecionar um intervalo inferior de 15 dias
    When selcionar dez equipes e clicar em Ok
    Then na view Lista de equipes selecionar as 10 equipes

  @AgendamentoFixo
  @SPRINT9
  Scenario: Realizar o agendamento por tipo Fixo
    Given que as OS estao no plano de trabalho
    When colocar uma OS em uma equipe
    Then preencher os dados marcando tipo Fixo
    
  @AgendamentoDespachoPDA
  @SPRINT9
  Scenario: Realizar o agendamento e depois edita-lo e logar na equipe
    Given na view de plano de trabalho
    And selecionar alguma OS
    When arrasta-la para uma equipe
    And preencher o agendamento tipo Fixo
    And seleciono o agendamento e edito
    Then faco login da Equipe
	
  @EditarRemoverAgendamento
  @SPRINT9
  Scenario: Realizar a remocao do agendamento
    Given na view de plano de trabalho
    And selecionar alguma OS
    When arrasta-la para uma equipe
    And preencher o agendamento tipo Fixo
    And remover o agendamento
    Then entao o agendamento e removido

 