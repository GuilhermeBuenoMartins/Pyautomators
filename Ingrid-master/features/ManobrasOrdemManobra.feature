Feature: realizar as ordens de manobras

@eliminar_ordem_de_manobra_1
Scenario: eliminar a ordem de manobra tipo 1
Given abrir view de servico de redes pendentes
When  abrir view manobras e ordem de manobras
Then  e selecionar servico de rede
And   selecionar opcao excluir manobra
And   concluir exclusao de manobra

@eliminar_ordem_de_manobra2
Scenario:
Given e selecionar servico de rede
When  despachar servico de rede para uma equipe logada
Then 	abrir view manobras e ordem de manobras
And   selecionar ordens e excluir

@eliminar_ordem_de_manobra3
Scenario:
Given buscar um servico de rede finalizado
When  abrir view manobras e ordem de manobras
Then  selecionar servico de rede finalizado
And  	excluir ordem de manobra
