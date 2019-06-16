@PESGeracaoManual
Feature: PES

  @IncluiPesquisarViabilizarReprovar
  Scenario: Realiza a inclusao e reprova de um PES
    Given que estou na tela de criacao do PES
    When preencher todas as telas e clicar em concluir
    Then apresenta janela para preencher a classificacao urgente
    When pesquisar o pes criado seleciono a opcao viabilizar
    Then o servico e viabilizado
    When clicar em reprovar PES e preencher o motivo
    Then o PES e reprovado
    
    
		
