@AtendimentoWorkflow
Feature: Atendimento WorkFlow OE

	@iniciar_atendimento_os_pelo_workflow_de_oe
	Scenario: Iniciar o atendimento da Ordem de Servico pelo Workflow
	Given abrir view lista de recursos do servico de rede
	When selecionando servico de rede pendente
	Then e selecionando opcao iniciar atendimento da ordem de servico pela equipe
	
	@postergar_atendimento_da_os
	Scenario: Realiza a acao Postergar atendimento OS
	Given abrir view lista de recursos do servico de rede
	When selecionando servico de rede pendente
	And seleciono opcao adiar
	Then preencho dados do adiar
	
	@reiniciar_o_atendimento_da_os
	Scenario: Reinicia o atendimento da OS adiada
	Given abrir view lista de recursos do servico de rede
	When selecionando servico de rede pendente
	Then e selecionar opcao inicia deslocamento ate o local de atendimento
	And concluir inicio do deslocamento

	@executar_manobra_abertura
	Scenario: Realizar a abertura da manobra
	Given clicar em manobras
	When preencher dados da abertura da manobra

	@abrir_view_interrupcoes
	Scenario: Abrir view interrupcoes
	Given abrir view interrupcoes
	When selecionar servico de rede
	Then atualizar view interrupcoes
	
	@executar_manobra_fechamento
	Scenario: Realizar o fechamento da manobra
	Given clicar em manobras
	When preencher dados do fechamento da manobra

	@definir_elemento_de_referencia
	Scenario: Definir elemento de referencia da ordem de servico
	Given abrir view lista de recursos do servico de rede
	When selecionando servico de rede pendente
	Then e selecionando opcao definir elemento de referencia da os
	
	@definir_causa_da_os
	Scenario: Definir causa da os
	Given abrir view lista de recursos do servico de rede
	When selecionando servico de rede pendente
	Then e selecionando opcao definir causa da os
	
	@incluir_material_na_ordem_de_servico
	Scenario: Incluir material na ordem de servico
	Given abrir view lista de recursos do servico de rede
	When selecionando servico de rede pendente
	And e selecionando opcao material
	And clicar em adicao para incluir materiais
	Then preencher dados da inclusao de material
	
	@incluir_servico_na_ordem_de_servico
	Scenario: Incluir servico na ordem de servico
	Given abrir view lista de recursos do servico de rede
	When selecionando servico de rede pendente
	Then e selecionando opcao servico
	And clicar em adicao para incluir servicos
	And preencher dados da inclusao de servico
	
	@finalizar_atendimento_os
	Scenario: Finalizar o atendimento da os
	Given abrir view lista de recursos do servico de rede
	When selecionando servico de rede pendente
	Then e selecionando opcao finalizar atendimento
	
	
	