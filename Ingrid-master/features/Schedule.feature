@Schedule
Feature: Schedule
  
  @PlanejarAutomaticamenteSchedule
  Scenario: Realiza o planejamento de OS´s automaticamente
    Given que estou na view plano de trabalho
    When  buscar por uma equipe
    Then seleciono as OS em Lista de Ordens de Servico
    When selecionar a opcao planejar e confirmar planejamento
    Then executa o motor de planejamento automatico
