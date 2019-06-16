@Scada
Feature: Realiza a execucao das funcionaidades Scada

  @EnviarSinalScada1
  Scenario: Realiza o envio de sinal Scada aberto
   Given envio o sinal scada aberto
   When o ingrid recebe o sinal e cria um servico de rede
   Then verifica a atualizacao da view no painel integracao

	@EnviarSinalScada2
	Scenario: Realiza o envio de sinal Scada fechado
	Given envio sinal fechado
	When ingrid recebe sinal fechado e cria servico de rede
	Then verifica a atualizacao da view no painel integracao
	