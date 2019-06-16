@ViewSRPendente
Feature: View SR Pendentes

  @view_servico_de_redes_pendentes_ordenacao
  @ViewSRPendente
  Scenario: View Servico Rede Pendente
 	Given Abrir view servico de rede pendente
 	When  Realizar ordenacao das colunas
 	
 	@criar_filtro
 	@ViewSRPendente
 	Scenario: Criar sub-filtro
 	Given Abrir view servico de rede pendente
 	When  clicar na seta pra baixo
 	Then  selecionar opcao configurar filtro
 	And   clicar no botao novo
 	
 	@propriedades_da_view
 	@ViewSRPendente
 	Scenario: Visualizar propriedades informcaoes do servico de rede pendente
 	Given Abrir view servico de rede pendente
 	When  selecionar um servico de rede pendente
 	Then  abrir view propriedades da view
 	And   verificar informacoes do servico de rede