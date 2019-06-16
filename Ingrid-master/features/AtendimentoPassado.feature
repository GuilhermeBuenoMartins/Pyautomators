@AtendimentoPassado
Feature: Realizar o atendimento passado de uma ocorrencia

	@sprint10
	@atendimento_passado
	Scenario: realizacao do atendimento passado de uma ocorrencia
	Given abrir view de servico de redes pendentes
	When  criar ordem de servico
	Then  localizar ordem de servico
	And   realizar atendimento passado ordem servico