'''
Created on 5 de nov de 2018

@author: vgama
'''

#Agendamento Diario
''' Agendamento diario Despachando Equipe'''
@given("selecionar um OS na view de Lista de OS")
def step(context):
    context.AgendamentoOS.abrirPerspectiva()
    context.AgendamentoOS.selecionarOS()

    
@when('arrastar a OS para a equipe')
def step_impl(context):
    context.AgendamentoOS.arrastarOS()


@then('preencher o tipo de agendamento')
def step_impl(context):
    context.AgendamentoOS.janelaOrdem()
    context.AgendamentoOS.preencheAgendamento()

'''Agendamento Posterior '''

@when('preencher o tipo de  agendamento diario')
def step_impl(context):
    context.AgendamentoPosterior.agendarOS()

@then('conectar o PDA no dia posterior')
def step_impl(context):
    context.AgendamentoPosterior.conectarPDA()
    

'''Agendamento Data/Hora''' 
    
@then(u'Aumentar Diminuir a marcacao')
def step_impl(context):
    context.AgendamentoDataHora.arrastarMarcacao()


'''Exibir plano de trabalho'''    
@given(u'na view Plano de trabalho selecionar um intervalo inferior de 15 dias')
def step_impl(context):
    context.ExibirPlanoTrabalho.selecionarIntervalo()


@when(u'selcionar dez equipes e clicar em Ok')
def step_impl(context):
    context.ExibirPlanoTrabalho.selecionarDezEquipes()


@then(u'na view Lista de equipes selecionar as 10 equipes')
def step_impl(context):
    context.ExibirPlanoTrabalho.selecionarEquipes()



#Agendamento Fixo

@given(u'que as OS estao no plano de trabalho')
def step_impl(context):
    context.AgendamentoOS.abrirPerspectiva()
    context.AgendamentoOS.selecionarOS()


@when(u'colocar uma OS em uma equipe')
def step_impl(context):
    context.AgendamentoOS.arrastarOS()


@then(u'preencher os dados marcando tipo Fixo')
def step_impl(context):
    context.AgendamentoFixo.tipoFixo()
    
''' Agendamento Despacho PDA'''
@given(u'na view de plano de trabalho')
def step_impl(context):
    context.AgendamentoOS.abrirPerspectiva()
    
@given(u'selecionar alguma OS')
def step_impl(context):
    context.AgendamentoOS.selecionarOS()

@when(u'arrasta-la para uma equipe')
def step_impl(context):
    context.AgendamentoOS.arrastarOS()
    
@when(u'preencher o agendamento tipo Fixo')
def step_impl(context):
    context.AgendamentoFixo.tipoFixo()
    
@when(u'seleciono o agendamento e edito')
def step_impl(context):
    context.AgendamentoDespachoPDA.editarAgendamento()
    
@then(u'faco login da Equipe')
def step_impl(context):
    context.AgendamentoDespachoPDA.efetuarLogin()
    
    
''' Remover Agendamento'''

@when('remover o agendamento')
def step(context):
    context.RemoverAgendamento.removeragendamento()


@then("entao o agendamento e removido")
def step(context):
    context.RemoverAgendamento.verificaRemocao()