@Atendimento_sr
Feature: Atendimento SR

	@sprint1
	@logar_equipe_atendimento_sr
	Scenario: Realizar Login de Equipe
	Given clicar na chave positiva para o login de equipe
	When  escolho a equipe desejada 
	And   seleciono opcao ultimo login e concluo
	
	@sprint1
	@localizar_consistencia_os_atendimento_sr
	Scenario: Localizar e verificar consistencia de dados
	Given abrir view de servico de redes pendentes
	When  selecionar servico de rede desejado - atendimento sr
	Then  abrir view propriedades
	And   listar referencia da os
	And   listar datas da os
	And   listar causa da os
	And   listar descricoes da os
	And   listar materiais da os
	And   listar Servicos
	And   listar Logs
	And   listar Associacao
	And   listar Unificacoes
	And   listar Formularios
	And   listar Mensagens
	And   listar Indicadores
	And   listar Pes Associados
	And   listar Logs Scada
	And   listar Pre-despacho
	
	@sprint1
	@despachar_servico_de_rede_para_equipe_distinta
	@AtendimentoSR
	Scenario: Despachar um servico de rede 
	Given abrir_view_recursos_propostos - atendimento servico rede
	When  abrir view de servico de redes pendentes - atendimento servico rede 
	Then  selecionar servico de rede desejado - atendimento servico rede
	And   despachar para determinada equipe
	
	@sprint1
	@resgatar_os_despachada_por_voz_atendimento_sr
	Scenario: Resgatar a os despachada
	#Given abrir view e mostrar equipes recursos propostos
	When  abrir view de servico de redes pendentes - atendimento servico rede 
	Then  selecionar os despachada
	And   selecionar icone resgatar os despachada

	@sprint1
	@interromper_e_rejeitar_os
	@AtendimentoSR
	Scenario: Interromper e rejeitar uma os
	Given abrir view e mostrar equipes recursos propostos
	When  selecionar equipe para interrupcao e rejeicao
	Then  selecionar icone interrupcao e rejeicao
	
	@sprint1
	@logoff_da_equipe_atendimento_sr
	Scenario:Realiza o logoff equipe
	Given clicar na chave negativa para o logoff de equipe
	When  escolho equipe logada
	Then  preencho dados e concluo o logoff
	