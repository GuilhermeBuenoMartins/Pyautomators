@RestricaoOperativa
Feature: Restricao Operativa

  @restricao_operativa_subestacao
  Scenario: Criar restricao operativa do tipo subestacao
  Given View de Restricao Operativa aberta
  When  Criar restricao operativa do tipo subestacao
  Then 	Preencher dados da restricao operativa subestacao e conclui
  
  @restricao_operativa_transformador
	Scenario: Criar restricao operativa do tipo transformador
	Given View de Restricao Operativa aberta
	When  Criar restricao operativa do tipo transformador
	Then  Preencher dados da restricao operativa transformador e conclui
  
  @listar_restricao_operativa_subestacao
	Scenario: Listar restricao operativa do tipo subestacao
	Given   View de Restricao Operativa aberta
	When    Listar restricao operativa do tipo subestacao
	
	@sprint8
	@listar_restricao_operativa_transformador
	Scenario: Listar restricao operativa do tipo transformador
	Given   View de Restricao Operativa aberta
	When    Listar restricao operativa do tipo transformador

	@sprint8
	@incluir_editar_restricao_operativa
	Scenario: incluir e editar restricao operativa
	Given 	View de Restricao Operativa aberta
	When    buscar restricao operativa
	Then    modificar restricao operativa

	@sprint8
	@ordenacao_de_colunas
	Scenario: ordenar colunas da restricao operativa
	Given View de Restricao Operativa aberta
	When  realizar ordenacao das colunas subestacao matricula
	Then  realizar ordenacao da coluna alimentador matricula 
	And   realizar ordenacao da coluna tipo elemento
	And   realizar ordenacao da coluna matricula
	And   realizar ordenacao da coluna data inicio
	And   realizar ordenacao da coluna data fim previsto
	And   realizar ordenacao da coluna data fim
	And   realizar ordenacao da coluna observacao
	And   realizar ordenacao da coluna responsavel aberta
	And   realizar ordenacao da coluna responsavel encerramento
	And   realizar ordenacao da coluna estado
	And   realizar ordenacao da coluna motivo
	
	@sprint8
	@localizar_restricao_operativa_graficamente
	Scenario: Localizar elemento graficamente
	Given View de Restricao Operativa aberta
	When  Selecionar restricao operativa existente
	Then  Selecionar icone localizar elemento graficamente
	
 	@BuscaOperativa
  @SPRINT8
  Scenario: Fazer uma busca por Tipo de Elemento de Rede
    "Neste cenario e realizo a busca por tipo de elemento de rede, responsavel e matricula"

    Given que estou na view Restricoes Operativas
    When buscar por um Tipo de Elemento
    Then o sistema filtra por tipo de elemento buscado
		When realizar uma busca por Responsavel
    Then o sistema filtra por Responsavel
		When realizar uma busca por Matricula
    Then o sitema filtra por Matricula
    
		
	@sprint8
  @encerrar_restricao_operativa
	Scenario: encerrar restricao operativa
	Given View de Restricao Operativa aberta
	When  Selecionar restricao operativa pendente
	Then  Clicar no icone encerrar restricao operativa
		
	