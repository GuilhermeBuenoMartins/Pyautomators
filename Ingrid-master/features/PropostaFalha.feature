@PropostaFalha
Feature: Proposta Falha
	
	@sprint1
	@config_proposta_falha
	Scenario: Configurar proposta falha
	Given abrir configuracao proposta falha
	When  selecionar uma configuracao
	Then  clico no botao ativar
	And   verifico se ela esta ativa 
	
	@sprint1
	@proposta_transformador
	Scenario: gerar proposta no transformador
	Given abrir perspectiva busca clientes
	When procurar por transformador
	And selecionar primeiro cliente e gerar aviso
	Then aviso e criado
	When selecionar segundo cliente e gerar aviso
	Then aviso e criado
	When selecionar terceiro cliente e gerar aviso
	Then aviso e criado
	And verifico se os servicos foram unidos
	
	@sprint1
	@proposta_seccionador
	Scenario: Gerar proposta falha seccionador
	Given abrir perspectiva busca clientes
	When procurar por seccionador
	And selecionar primeiro cliente e gerar aviso
	Then aviso e criado
	When selecionar segundo cliente e gerar aviso
	Then aviso e criado
	When selecionar terceiro cliente e gerar aviso
	Then aviso e criado
	And verifico se os servicos foram unidos
	