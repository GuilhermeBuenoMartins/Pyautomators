# -*- coding: utf-8 -*-
'''
Created on 22 de out de 2018

@author: vgama
'''

''' Criar Evento '''
@given(u'que eu estou na janela Novo Evento de Rede')
def step_impl(context):
    context.CriarEvento.abrirEvento()

@when(u'preencho os dados')
def step_impl(context):
    context.CriarEvento.preencheCampos()

@then(u'clico no botao Concluir')
def step_impl(context):
    context.CriarEvento.concluir_e_verifica()

''' Servico de Rede  '''
@given(u'que estou na tela de Servicos de Rede Pendente')
def step_impl(context):
    context.ServicoRede.abrir_view_servicos_pendentes()

@when(u'dar duplo clique no servico me apresenta as equipes disponiveis na view Recursos Propostos')
def step_impl(context):
    context.ServicoRede.servicoRede()
    
@then(u'arrasto o servico de rede para uma equipe')
def step_impl(context):
    context.ServicoRede.arrastaServico()
    
@then("verifico se despachado com sucesso")
def step_impl(context):
    context.ServicoRede.verificar_despacho()
    
''' Incidencia Atendimento '''
@when(u'eu realizo a manobra da OS')
def step_impl(context):
    context.IncidenciaAtendimento.monobrar()
    
@when(u'entro na view de atendimento da OS')
def step_impl(context):
    context.IncidenciaAtendimento.atendimentoOS()

@then(u'o atendimento e executado com sucesso')
def step_impl(context):
    context.IncidenciaAtendimento.verifica_atendimento_executado()

''' STD Transformador Criar ordem de servico'''

@given(u'estou na view Servicos de Rede')
def step_impl(context):
    context.STDTransformador.abrir_View_Servico_Rede()

@when(u'clicar na opcao nova ordem de servico e preencher tipo STD Transformador')
def step_impl(context):
    context.STDTransformador.abrir_Nova_Ordem_Servico()
    context.STDTransformador.preenche_dados_tipo_std_transformador()

@when(u'preencher os outros dados e concluir')
def step_impl(context):
    context.STDTransformador.preenche_dados_finais()

@then(u'uma ordem de servico e criada')
def step_impl(context):
    context.STDTransformador.verifica_ordem_servico_criada()


''' STDTransformador Atendimento ordem de servico'''
    
@given(u'abrir a view de Recursos Propostos')
def step_impl(context):
    context.STDTransformador.abri_view_recursos_propostos()

@when(u'clicar duas vezes em um servico pendente STD Transformador')
def step_impl(context):
    context.STDTransformador.clicar_servico_rede_pendente_transformador()

@then(u'arrasto ordem de servico para a view de recursos propostos')
def step_impl(context):
    context.STDTransformador.arrasta_para_equipe()
    
'''STDTransformador Finalizar ordem de servico'''
    
@when(u'realizar o atendimento da ordem de servico')
def step_impl(context):
    context.STDTransformador.atendimento_std_transformador()
    context.STDTransformador.realiza_atendimento()

@then(u'atendimento e manobra e executado com sucesso')
def step_impl(context):
    context.STDTransformador.verifica_finalizacao_atendimento()
    
''' STD Diversos Criar '''
@when(u'clicar na opcao ordem de servico e preenche tipo STD Diversos')
def step_impl(context):
    context.STDTransformador.abrir_Nova_Ordem_Servico()
    context.STDDiversos.preenche_dados_tipo_std_diversos()

''' STD Diversos Atendimento '''
@when(u'clicar duas vezes em um servico pendente STD Diversos')
def step_impl(context):
    context.STDDiversos.clicar_servico_rede_pendente_diversos()

@then(u'arrasto ordem de servico diversos para a view de recursos propostos')
def step_impl(context):
    context.STDDiversos.arrasta_std_diversos_para_equipe()
    
''' STDTransformador Finalizar ordem de servico'''
    
@when(u'realizar o atendimento da ordem de servico STD Diversos')
def step_impl(context):
    context.STDDiversos.atendimento_std_diversos()
    context.STDTransformador.realiza_atendimento()

''' STD Rede de Distribuicao Criar '''
@when(u'clicar na opcao ordem de servico e preenche tipo STD Rede Distribuicao')
def step_impl(context):
    context.STDTransformador.abrir_Nova_Ordem_Servico()
    context.STDRedeDistribuicao.preenche_dados_tipo_std_rede_distribuicao()
    
''' STD Rede Distribuicao Atendimento '''
@when(u'clicar duas vezes em um servico pendente STD Rede de Distribuicao')
def step_impl(context):
    context.STDRedeDistribuicao.clicar_servico_rede_pendente_rede_distribuicao()
    
@then(u'arrasto ordem de servico rede distribuicao para a view de recursos propostos')
def step_impl(context):
    context.STDRedeDistribuicao.arrasta_std_rede_distribuicao_para_equipe()
    
'''STDRedeDistribuicao Finalizar ordem de servico'''
    
@when(u'realizar o atendimento da ordem de servico STD Rede Distribuicao')
def step_impl(context):
    context.STDRedeDistribuicao.atendimento_std_rede_distribuicao()
    context.STDTransformador.realiza_atendimento()

''' STD Subestacao Criar '''
@when(u'clicar na opcao ordem de servico e preenche tipo STD Substacao')
def step_impl(context):
    context.STDTransformador.abrir_Nova_Ordem_Servico()
    context.STDSubestacao.preenche_dados_tipo_std_subestacao()
    
''' STD Subestacao Atendimento '''
@when(u'clicar duas vezes em um servico pendente STD Subestacao')
def step_impl(context):
    context.STDSubestacao.clicar_servico_rede_pendente_subestacao()
    
@then(u'arrasto ordem de servico subestacao para a view de recursos propostos')
def step_impl(context):
    context.STDSubestacao.arrasta_std_estacao_para_equipe()
    
        
'''STDSubestacao Finalizar ordem de servico'''
    
@when(u'realizar o atendimento da ordem de servico STD Subestacao')
def step_impl(context):
    context.STDSubestacao.atendimento_std_subestacao()
    context.STDTransformador.realiza_atendimento()
    
''' Evento de Rede Nao Programado criar'''
@when("preencher dados tipo nao programado")
def step_impl(context):
    context.Evento_rede_nao_programado.preencher_dados_nao_programado()

@then("e criado um novo evento nao programado")
def step_impl(context):
    context.Evento_rede_nao_programado.verifica_evento_nao_programado()

''' Evento de rede Nao Programado arrasta equipe '''
@when("selecionar um evento atuacao nao programada")
def step_impl(context):
    context.Evento_rede_nao_programado.selecionar_evento_rede_criado()
    
''' Evento de rede Nao Programado atendimento '''
@when("seleciono um evento atuacao")
def step_impl(context):
    context.Evento_rede_nao_programado.seleciono_evento_atuacao()  


''' Evento de rede programado criar '''
@when("preencher dados tipo programado")
def step_impl(context):
    context.Evento_rede_programado.preencher_dados_programado()


''' Evento de rede programado '''
@when("selecionar um evento atuacao programada")
def step_impl(context):
    context.Evento_rede_programado.selecionar_evento_atuacao_programado()

''' Evento de rede programado Atender'''
@when("seleciono um evento atuacao programado")
def step_impl(context):
    context.Evento_rede_programado.seleciono_evento_atuacao_programado()


