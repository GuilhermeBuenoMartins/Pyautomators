@FiltroZonal
Feature: Filtro Zonal


@criar_filtro_zonal
Scenario: criar o filtro zonal
Given clicar alterar o filtro de area
When  clicar no botao criar e preencher dados
Then verifica se o filtro zonal foi aplicado

@modificar_filtro_zonal
Scenario: modificar editar filtro zonal
Given clicar alterar o filtro de area
When  clicar em modificar
Then  preeche os dados
When  selecionar filtro modificado
Then  verifica filtro zonal modificado aplicado


@criar_copia_existente
Scenario: realizar uma copia de um filtro zonal existente
Given clicar alterar o filtro de area
When  clicar em modificar
Then  flegar criar copia a partir do filtro
And   selecionar o filtro copia

@eliminar_filtro_zonal
Scenario: Apagar um filtro zonal
Given clicar alterar o filtro de area
When  clicar em eliminar