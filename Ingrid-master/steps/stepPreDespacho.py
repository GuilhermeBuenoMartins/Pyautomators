'''
Created on 26 de nov de 2018

@author: vgama
'''

''' SR DESPACHADO '''
@given("que estou na view servicos pendentes")
def step(context):
    context.SRDespachado.view_SR_pendentes()

@when("selecionar um servico despachado")
def step(context):
    context.SRDespachado.selecionar_sr_despachado()
    
@when("clicar em Marcar Desmarcar SR pre despacho")
def step(context):
    context.SRDespachado.selecionar_opcao_marcar_desmarcar_pre_despacho()
    
@then("retorna uma mensagem devido ter ordem de execucao pendente")
def step(context):
    context.SRDespachado.verifica_pre_despacho_nao_realizado()
    
''' SR AGENDADO '''

@given("que estou na view servicos de rede")
def step(context):
    context.SRAgendado.view_servico_rede()

@when("seleciono um sr agendado")
def step(context):
    context.SRAgendado.selecionar_sr_agendado()
    
''' SR MARCAR '''
@when(u'que eu seleciono um servico sem agendamento e equipe')
def step_impl(context):
    context.SRMarcar.selecionarSR()


@when(u'preencher os campos solicitados')
def step_impl(context):
    context.SRMarcar.preencherSR()


@then(u'na view Servico de Rede sera apresentado o campo pre despacho flegado e as datas preenchidas')
def step_impl(context):
    context.SRMarcar.verificaPreDespacho()    

@when(u'seleciono diversos servicos de rede')
def step_impl(context):
    context.SRMarcar.selecionarVariosSR()

'''SR Marcado Pre Despacho '''
@given(u'abrir view de recursos propostos')
def step_impl(context):
    context.SRMarcadoPreDespacho.abrir_view_recursos_propostos()

@when(u'selecionar um sr pre despachado')
def step_impl(context):
    context.SRMarcadoPreDespacho.selecionar_sr_pre_despachado()


@when(u'arrastar para alguma equipe')
def step_impl(context):
    context.SRMarcadoPreDespacho.arrastar_para_equipe()


@then(u'apresenta uma mensagem de erro')
def step_impl(context):
    context.SRMarcadoPreDespacho.apresenta_mensagem_erro()

''' Desmarca Pre Despacho Manual '''
    

@when(u'seleciono um servico')
def step_impl(context):
    context.DesmarcarPreDespacho.selecionar_sr_predespachado()

@then(u'desmarco o predespacho')
def step_impl(context):
    context.DesmarcarPreDespacho.desmarcarDespacho()

@when(u'seleciono diversos servicos')
def step_impl(context):
    context.DesmarcarPreDespacho.selecionarServicos()

@then(u'verifica sr desmarcado')
def step_impl(context):
    context.DesmarcarPreDespacho.verifica_sr_desmarcado()   

''' Desmarca Pre Despacho Automatico '''
    
@when(u'preencher dados com data fim')
def step_impl(context):
    context.DesmarcarPreDespachoAut.preencheDadosDataFim()

@then(u'verifica sr sem pre despacho')
def step_impl(context):
    context.DesmarcarPreDespachoAut.verifica_sr_sem_predespacho()
    
    
''' DESPACHO AUTOMATICO 1 '''

@then(u'clica em desmarcar pre despacho para o SR selecionado')
def step_impl(context):
    context.DespachoAutomatico1.desmarcaSR() 

''' DESPACHO AUTOMATICO 2 '''
@given(u'verifica se foi despachado automaticamente')
def step_impl(context):
    context.DespachoAutomatico1.servicoRedePendente()
    context.DespachoAutomatico2.selecionarOSPerto()
    context.DespachoAutomatico1.alerta()

@when(u'horario data fim for atingida predespacho e desmarcado')
def step_impl(context):
    context.DespachoAutomatico2.verificaDespacho()
