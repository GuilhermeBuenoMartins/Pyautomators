@UnificarServicoRede
Feature: Unificar Servico de Rede

  @SelecionandoVariosSR
  Scenario: Unifica SR pendentes selecionando varios SR
    Given abrir a view de Servicos de Redes Pendentes
    When selecionar varios sr clicando com o botao direito
    Then seleciono opcao Unificar Servico de Rede
    When digitar um dos Servicos de Rede e confirmar acoes
    Then o sistema lista os Servicos de Rede passiveis de unificacao
    When selecionar os Servicos que possam unificar
    Then sistema unifica os servicos de rede

  @UnificarSRResolvido
  Scenario: Unifica SR Pendente a um SR Resolvido
    Given busco um servico de rede com situacao resolvido
    When selecionar sr

  @UnificarSREncerrado
  Scenario: Unifica SR Pendente a um SR Encerrado
    Given busco um servico de rede com situacao encerrado
    When selecionar um SR com situacao Encerrado
    Then seleciono opcao Unificar Servico de Rede
    When escrever um dos servico de rede
    Then o sistema lista os Servicos de Rede passiveis de unificacao
    When selecionar os Servicos que possam unificar
    Then sistema unifica os servicos de rede
