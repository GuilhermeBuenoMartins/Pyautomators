@PausarEquipe
Feature: Pausar Equipe Despacho Multiplo

	@pausar_a_equipe
	Scenario: pausar equipe nao despachada
	Given abrir recursos propostos
	When  abrir view de servico de redes pendentes
	Then  selecionar equipe nao despachada	
	And 	clicar no icone pausa a equipe
	
	@despacho_multiplo
	Scenario: realizar despacho de uma sr para equipes distintas
	Given abrir recursos propostos
	When  abrir view de servico de redes pendentes
	Then  selecionando servicos de rede para despacho multiplo
	And   arrastando servicos para equipe
	And  despachando servicos para equipe
	
	@pausar_atendimento_da_equipe
	Scenario: pausar equipe despachada
	Given abrir recursos propostos
	When  abrir view de servico de redes pendentes
	Then  selecionar equipe despachada
	And 	clicar no icone pausa a equipe
	And   preenche dados motivo recuperacao