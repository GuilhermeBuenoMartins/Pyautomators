'''
Created on 4 de jul de 2018

@author: gcruzm
'''

#Localizar elemento graficamente
@given("abrir view de servico de redes pendentes")
def step(context):
    context.Localizar_elemento_graficamente.abrir_view_servicos_de_rede_pendentes()

@when("selecionar servico rede e apertar botao direito mouse")
def step(context):
    context.Localizar_elemento_graficamente.selecionar_servico_rede_e_apertar_botao_direito_mouse()

@then("selecionar opcao localizar elemento graficamente")
def step(context):
    context.Localizar_elemento_graficamente.selecionar_opcao_localizar_elemento_graficamente()

#Localizar recursos propostos graficamente
    
@when("selecionar opcao localizar recursos propostos graficamente")
def step(context):
    context.Localizar_recurso_proposto_graficamente.selecionar_opcao_localizar_recursos_propostos_graficamente()

#Redesenhar mapa da visao grafica
@given("abrir view visao grafica")
def step(context):
    context.Redesenhar_janela_visao_grafica.abrir_view_visao_grafica()
    
@when("selecionar camadas visao grafica")
def step(context):
    context.Redesenhar_janela_visao_grafica.selecionar_camadas_visao_grafica()
    
@then("apertar botao redesenhar")
def step(context):
    context.Redesenhar_janela_visao_grafica.apertar_botao_redesenhar()
    
#Gerar etiqueta
@when(u'clico na opcao Criar Etiqueta')
def step_impl(context):
    context.GerarEtiqueta.criarEtiqueta()
@then(u'preencho os dados da etiqueta e confirmo a operacao')
def step_impl(context):
    context.GerarEtiqueta.camposEtiqueta()

#Excluir etiqueta
@when(u'clico na opcao para excluir etiqueta')
def step_impl(context):
    context.ExcluirEtiqueta.selecionaEtiqueta()
@then(u'realizo a exclusao')
def step_impl(context):
    context.ExcluirEtiqueta.excluirEtiqueta()

#Fluxo solicitacao

@when("selecionar opcao fluxo por solicitacao")
def step(context):
    context.Fluxo_solicitacao.selecionar_opcao_fluxo_por_solicitacao()

@when("selecionar elemento rede fluxo solicitacao")
def step(context):
    context.Fluxo_solicitacao.selecionar_elemento_rede_fluxo_solicitacao()

@then("sistema realiza o calculo")
def step(context):
    context.Fluxo_solicitacao.sistema_realiza_calculo()
    
@when("selecionar a opcao Resultados fluxo carga")
def step(context):
    context.Fluxo_solicitacao.seleciona_opcao_resultado_fluxo_carga()

@then("sistema exibe os calculos realizados")
def step(context):
    context.Fluxo_solicitacao.verifica_view_resultado_fluxo_carga()
    

#Listar elemento a jusante

@when("selecionar opcao a jusante")
def step(context):
    context.Listar_elemento_jusante.selecionar_opcao_a_jusante()

@then("preencher dados a jusante")
def step(context):
    context.Listar_elemento_jusante.preencher_dados_a_jusante()
    
#Listar elemento a montante

@when("selecionar opcao a montante")
def step(context):
    context.Listar_elemento_a_montante.selecionar_opcao_a_montante()

@then("preencher dados a montante")
def step(context):
    context.Listar_elemento_a_montante.preencher_dados_a_montante()
    
#Entre dois pontos
@when(u'clicar na opcao Intalacoes em dois pontos')
def step_imple(context):
    context.InstalacoesPontos.clicaDoisPontos()
@when(u'selecionar um elemento de rede')
def step_impls(context):
    context.InstalacoesPontos.primeiroPonto()
@then(u'selecionar outro elemente de rede')
def step_implen(context):
    context.InstalacoesPontos.segundoPonto()

#fluxo corrente
@when(u'selecionar a opcao Fluxo de Corrente e uma rede MT')
def step_impl(context):
    context.FluxoCorrente.opcaoFluxoCorrente()

#Entorno de trabalho por selecao
@when("selecionar seta ao lado da opcao entorno de trabalho")
def step(context):
    context.Entorno_de_trabalho_por_selecao.selecionar_seta_ao_lado_da_opcao_entorno_de_trabalho()

@then("selecionar opcao abrir entorno de trabalho por selecao")
def step(context):
    context.Entorno_de_trabalho_por_selecao.selecionar_opcao_abrir_entorno_de_trabalho_por_selecao()

@then("clicar em um elemento na visao grafica")
def step(context):
    context.Entorno_de_trabalho_por_selecao.clicar_em_um_elemento_na_visao_grafica()

#Entorno de trabalho pela view de servicos pendentes
@when("selecionar servico de rede para o entorno de trabalho")
def step(context):
    context.Entorno_de_trabalho_pela_view_servico_de_redes_pendentes.selecionar_servico_de_rede_para_o_entorno_de_trabalho()

@then("selecionar icone abrir entorno de trabalho")
def step(context):
    context.Entorno_de_trabalho_pela_view_servico_de_redes_pendentes.selecionar_icone_abrir_entorno_de_trabalho()
    
#esquema orgonal
@given(u'seleciono a opcao Esquema Ortogonal Agrupado')
def step_impl(context):
    context.EsquemaOrtogonal.clica_esquema_ortogonal_agrupado()
@when(u'selecionar um elemento de rede visao grafica')
def step_impl(context):
    context.EsquemaOrtogonal.selecionar_elemento_rede()
@then(u'busco por unidade seccionadora na view esquema ortogonal')
def step_impl(context):
    context.EsquemaOrtogonal.buscar_unidade_seccionadora()
@when(u'volto para visao grafica')
def step_impl(context):
    context.EsquemaOrtogonal.voltar_para_visao_grafica()
@when(u'seleciono opcao Esquema Ortogonal Reduzido')
def step_impl(context):
    context.EsquemaOrtogonal.clica_esquema_ortogonal_reduzido()
@when(u'seleciono um elemento de rede')
def step_impl(context):
    context.EsquemaOrtogonal.selecionar_elemento_rede()
@then(u'verifico abertura do esquema ortogonal reduzido')
def step_impl(context):
    context.EsquemaOrtogonal.verifica_janela_esquema_ortogonal_aberta()
    
#esquema unifiliar
@when(u'selecionar a opcao Esquema Unifilar')
def step_impl(context):
    context.EsquemaUnifilar.clicar_esquema_unifilar()

@then(u'verifico a abertura do esquema unifilar')
def step_impl(context):
    context.EsquemaUnifilar.verifica_janela_esquema_unifilar_aberta()
    

''' Abrangencia de Falta '''
@given(u'estou na visao grafica simulada')
def step_impl(context):
    context.AbrangenciaFalta.abrir_visao_grafica_simulada()

@when(u'selecionar a opcao Seccionador Media e apontar')
def step_impl(context):
    context.AbrangenciaFalta.selecionar_seccionador_media()

@then(u'A view e redesenhada')
def step_impl(context):
    context.AbrangenciaFalta.redesenhar()
    
    
''' Abrangencia de Falta 2'''
@when(u'selecionar a opcao Gerador e apontar')
def step_impl(context):
    context.AbrangenciaFalta.selecionar_gerador()
    
''' Abrangencia de Falta 3'''
@when(u'selecionar a opcao Transformador e apontar')
def step_impl(context):
    context.AbrangenciaFalta.selecionar_transformador()
    

#Estudo de manobra
@when("selecionar opcao estudar manobra")
def step(context):
    context.Estudo_manobra.selecionar_opcao_estudar_manobra()

@then("preencher info rede mt estudar manobra")
def step(context):
    context.Estudo_manobra.preencher_info_rede_mt_estudar_manobra()

@then("selecionar seccionador")
def step(context):
    context.Estudo_manobra.selecionar_seccionador()

@then("selecionar icone localizar seccionador graficamente")
def step(context):
    context.Estudo_manobra.selecionar_icone_localizar_seccionador_graficamente()

