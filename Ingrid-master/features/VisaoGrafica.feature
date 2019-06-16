@VisaoGrafica
Feature: Visao Grafica

	@localizar_elemento_graficamente
	Scenario: localizar elemento graficamente visao grafica
		Given abrir view de servico de redes pendentes
		When  selecionar servico rede e apertar botao direito mouse
		Then  selecionar opcao localizar elemento graficamente

	@sprint8
	@localizar_recursos_propostos_graficamente
	Scenario: localizar recurso graficamente
		Given abrir view de servico de redes pendentes
		When  selecionar servico rede e apertar botao direito mouse
		And selecionar opcao localizar recursos propostos graficamente

	@sprint8
	@redesenhar_janela_visao_grafica
	Scenario: redesenhar janela visao grafica
		Given abrir view visao grafica
		When  selecionar camadas visao grafica
		Then  apertar botao redesenhar

	@GerarEtiqueta
	@SPRINT8
	Scenario: cria uma etiqueta na visao grafica
		Given abrir view visao grafica
		When clico na opcao Criar Etiqueta
		Then preencho os dados da etiqueta e confirmo a operacao

	@ExcluirEtiqueta
	@SPRINT8
	Scenario: realiza a exclusao de uma etiqueta
		Given abrir view visao grafica
		When clico na opcao para excluir etiqueta
		Then realizo a exclusao


	@sprint10
	@fluxo_solicitacao
	Scenario: realizar solicitacao de fluxo de carga
		Given abrir view visao grafica
		When selecionar opcao fluxo por solicitacao
		And selecionar elemento rede fluxo solicitacao
		Then sistema realiza o calculo
		When selecionar a opcao Resultados fluxo carga
		Then sistema exibe os calculos realizados

	@sprint8
	@listar_elemento_jusante
	Scenario: listar elementos a jusante
		Given abrir view visao grafica
		When  selecionar opcao a jusante
		Then  preencher dados a jusante

	@sprint8
	@listar_elemento_montante
	Scenario: Listar elementos a montante
		Given abrir view visao grafica
		When  selecionar opcao a montante
		Then  preencher dados a montante

	@InstalacoesDoisPontos
	@SPRINT8
	Scenario: Realiza uma lista das instalacoes entre dois pontos
		Given abrir view visao grafica
		When 	clicar na opcao Intalacoes em dois pontos
		And 	selecionar um elemento de rede
		Then 	selecionar outro elemente de rede

	@FluxoCorrente
	@SPRINT8
	Scenario: Realizar uma consulta de fluxo de corrente
		Given abrir view visao grafica
		When selecionar a opcao Fluxo de Corrente e uma rede MT

	@sprint10
	@entorno_de_trabalho_por_selecao
	Scenario: Exibir o entorno de trabalho por selecao
		Given abrir view visao grafica
		When  selecionar seta ao lado da opcao entorno de trabalho
		Then  selecionar opcao abrir entorno de trabalho por selecao
		And   clicar em um elemento na visao grafica

	@sprint10
	@entorno_de_trabalho_pela_view_servico_de_redes_pendentes
	Scenario: Exibir o entorno de trabalho pela view servico de redes pendentes
		Given abrir view de servico de redes pendentes
		When  selecionar servico de rede para o entorno de trabalho
		Then  selecionar icone abrir entorno de trabalho

	@EsquemaOrtogonal
	@SPRINT10
	Scenario: Visualiza o esquema ortogonal do elemento de rede
		Given abrir view visao grafica
		And seleciono a opcao Esquema Ortogonal Agrupado
		When selecionar um elemento de rede visao grafica
		Then busco por unidade seccionadora na view esquema ortogonal
		When volto para visao grafica
		And seleciono opcao Esquema Ortogonal Reduzido
		And seleciono um elemento de rede
		Then verifico abertura do esquema ortogonal reduzido

	@EsquemaUnifilar
	@SPRINT10
	Scenario: Visualiza o esquema unifilar do elemento de rede
		Given abrir view visao grafica
		When selecionar a opcao Esquema Unifilar
		And selecionar um elemento de rede visao grafica
		Then verifico a abertura do esquema unifilar

	@AbrangenciaFalta1
	@SPRINT12
	Scenario: Realiza busca na selecao de entidade
		Given estou na visao grafica simulada
		When selecionar a opcao Seccionador Media e apontar
		Then A view e redesenhada

	@AbrangenciaFalta2
	@SPRINT12
	Scenario: Realiza busca por um Grupo Gerador
		Given estou na visao grafica simulada
		When selecionar a opcao Gerador e apontar
		Then A view e redesenhada

	@AbrangenciaFalta3
	@SPRINT12
	Scenario: Realiza busca por um Grupo Gerador
		Given estou na visao grafica simulada
		When selecionar a opcao Transformador e apontar
		Then A view e redesenhada

	@sprint10
	@estudo_manobra
	Scenario: realizar estudo da manobra
		Given abrir view visao grafica
		When  selecionar opcao estudar manobra
		Then  preencher info rede mt estudar manobra
		And   selecionar seccionador
		And  	selecionar icone localizar seccionador graficamente