'''
Created on 15 de fev de 2019

@author: vgama
'''
from time import sleep
        
@given(u'que estou na view plano de trabalho')
def step_impl(context):
    context.Schedule.abrir_view_plano_de_trabalho()


@when(u'buscar por uma equipe')
def step_impl(context):
    context.Schedule.buscar_uma_equipe()


@then(u'seleciono as OS em Lista de Ordens de Servico')
def step_impl(context):
    context.Schedule.selecionar_os_Lista_Ordens()


@when(u'selecionar a opcao planejar e confirmar planejamento')
def step_impl(context):
    context.Schedule.seleciona_opcao_planejar()


@then(u'executa o motor de planejamento automatico')
def step_impl(context):
    context.Schedule.executa_motor_planejamento()

    