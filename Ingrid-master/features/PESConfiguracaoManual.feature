Feature: PES Configuracao Manual

  @1ConfigPrazos
  Scenario: Realiza a configuracao de prazos por fase do workflow
    Given entrar em preferencias
    When pesquisar a configuracao de prazos por fase de workflow
    Then selecionar um tipo subtipo e atualizar
    
