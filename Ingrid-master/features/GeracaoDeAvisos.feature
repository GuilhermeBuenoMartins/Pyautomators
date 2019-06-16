Feature: Realizar a consulta de avisos

		@sprint1
		@criar_novo_aviso
		Scenario: Criar um novo aviso
		Given abrir perspectiva atencao de avisos
		When 	buscar contato desejado
		Then 	clicar em novo aviso
		And 	preencher dados do novo aviso
		
		@sprint1
		@criacao_de_aviso_sem_cliente
		Scenario: Criar um Aviso sem cliente
		Given abrir perspectiva atencao de avisos
		Then clicar em novo aviso
		Then preencher dados do cliente nao cadastrado
		Then verificar aviso criado
		And visualizar mensagem do aviso
		
		@sprint1
		@associacao_de_aviso
		Scenario: Associacao aviso SR
		#***caso tenha um sr semelhante, sera associado. se nao, nao. ***
		Given abrir view de servico de redes pendentes
		When  selecionar servico rede associacao aviso
		Then  realizar manobra servico rede da associacao aviso
		
		@sprint1
		@extrair_aviso_novo
		Scenario: Extrair aviso novo
		#Given abrir view de servico de redes pendentes
		Given abrir view avisos de servico de rede
		When selecionando aviso novo
		Then clico na view avisos servico de rede
		And  selecionando aviso dentro da view
		And  clicar em extrair aviso
	
		@sprint1
		@extrair_aviso_existente
		Scenario: Extrair aviso existente
		#Given abrir view de servico de redes pendentes
		Given  abrir view avisos de servico de rede
		When  selecionar aviso existentes
		Then   realizar extracao de aviso existente
			
		@sprint1
		@anular_aviso_associado
		Scenario: Anular aviso associado a um cliente
		Given abrir perspectiva atencao de avisos 
		When  buscar contato desejado
		Then selecionar view aviso cliente
		And  selecionar aviso associado ao cliente
		And  selecionar opcao anular aviso associado
		
		@anular_servico_de_rede
		Scenario: Anular um servico de rede despachado
		Given abrir recursos propostos
		When  abrir view de servico de redes pendentes
		Then  selecionar servico de rede para despachar
		And   realizar o despacho do servico de rede
		And   clicar em resgatar ordem de servico
		
		@sprint11
		@view_arvore_avisos
	  	Scenario: View Arvore de Avisos
	  	Given abrir view de servico de redes pendentes
	  	When  Abrir view arvore de avisos
	  	Then  clicar em atualizar
	  	And  clicar em desmembrar
	  
	  
	  @sprint11
	  @aviso_improcedente
	  Scenario: Marcar aviso como improcedente
	  Given Abrir view arvore de avisos
	  When  clicar em atualizar
	  Then  clicar em marcar como improcedente
	  And   preencher dados

		
