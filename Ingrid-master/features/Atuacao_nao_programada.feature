Feature: Atuacoes nao programadas

	#Realizando inclusao e manobra
	@sprint4
	@criar_e_evento_de_rede_nao_programado
	Scenario: criacao de evento de rede como nao programado
	Given carregar view sr pendente e clicar na ferramenta verde
	When  preencher dados do novo evento rede	
	
	@realizar_manobra_da_atuacao_nao_programada
	Scenario: realizar manobra da atuacao nao programada
	Given procurar evento de rede nao programado
	When  clicar no icone de manobra para manobrar o evento de rede
	Then  clicar no botao executar para executar a manobra
	
	@sprint4
	@atendimento_passado_atuacao_nao_programada
	Scenario: realizacao do atendimento passado de uma ocorrencia
	Given procurar evento de rede nao programado
	When  realizar atendimento passado ordem servico
	
	@sprint4
	@atendimento_da_oe_e_inicio_deslocamento
	Scenario: Iniciar atendimento unico
	Given selecionar servico de rede para o atendimento da oe 
	When 	clicar em atendimento unico e preencher dados necessarios
	Then  confirmar o atendimento da oe
	
	#Todas as inclusoes
	@sprint6
	@inclusao_material_servico_causa_observacao
	Scenario: Incluir material, servico, causa e observacao
	Given selecionar ordem de servico para inclusao
	When  abrir atendimento unico
	Then  incluir material
	And   incluir servico	
	And   incluir causa
	
	@sprint4
	@finalizar_ordem_de_servico
 	Scenario: finalizacao de atendimento
  Given selecionar o servico de rede para finalizar
  When 	clicar na opcao atendimento
  Then 	preencho a data final, Elemento Falha e clico em OK

	
	@sprint6
	@anular_servico_de_rede_pendente
	Scenario: Anular SR Pendente da atuacao nao programada
	Given localizar sr
	When  apertar botao direito no sr
	Then  selecionar opcao anular aviso
	And 	concluir anulacao aviso pendente
	
	@sprint6
	@anular_servico_de_rede_com_atendimento_iniciado
	Scenario: Anular SR iniciado da atuacao nao programada
	Given Selecionar o SR iniciado
	When  Escolher a opcao anular aviso
	Then  preencher dados da anulacao