@LoginLogoff
Feature: Login-Logoff Equipe

  @loginEquipe
  Scenario: Realizar Login de Equipe
    """Este Cenario tem como meta testar o Login das equipes de campo no sistema"""
    Given entro no Login de Equipe
     When entro na tela Login Equipe e acho uma equipe
      And preencho os dados necessarios
     Then aparece botao de 'OK' e confirmar

  @logoffequipe
  Scenario: Realizar Logoff de Equipe
    Given que estou na tela das equipes logadas
     When selecionar equipe para fazer logoff e concluir logoff
     Then aparece botao de 'OK' e confirmar

  @editarDadosLogin
  Scenario: Editar dados do login
    Given Abrir tela de edicao
     When Quando Abrir a edicao e editar dados na equipe
      And Vou concluir edicao
     Then Aparecera 'OK'


