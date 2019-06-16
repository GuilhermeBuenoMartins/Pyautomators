# -*- coding: utf-8 -*-

'''
Created on 21 de jul de 2018
@author: gdiamante

modified on 30 de nov de 2018
@author: gcruzm

'''

#Login de equipe
@given("clicar na chave positiva para o login de equipe")
def step(context):
    context.Logar_equipe.clicar_na_chave_positiva_para_o_login_de_equipe()

@when("escolho a equipe desejada")
def step(context):
    context.Logar_equipe.escolho_a_equipe()

@when("seleciono opcao ultimo login e concluo")
def step(context):
    context.Logar_equipe.seleciono_opcao_ultimo_login_e_concluo()


#Localizar consistencia dos dados de uma os
@when("selecionar servico de rede desejado - atendimento sr")
def step(context):
    context.Localizar_consistencia_dos_dados_de_uma_os.selecionar_servico_de_rede_desejado()

@then("abrir view propriedades")
def step(context):
    context.Localizar_consistencia_dos_dados_de_uma_os.abrir_view_propriedades()

@then("listar referencia da os")
def step(context):
    context.Localizar_consistencia_dos_dados_de_uma_os.listar_referencia_da_os()
    
@then("listar datas da os")
def step(context):
    context.Localizar_consistencia_dos_dados_de_uma_os.listar_datas_da_os()
    
@then("listar causa da os")
def step(context):
    context.Localizar_consistencia_dos_dados_de_uma_os.listar_causa_da_os()
    
@then("listar descricoes da os")
def step(context):
    context.Localizar_consistencia_dos_dados_de_uma_os.listar_descricoes_da_os()
    
@then("listar materiais da os")
def step(context):
    context.Localizar_consistencia_dos_dados_de_uma_os.listar_materiais_da_os()
    
@then("listar Servicos")
def step(context):
    context.Localizar_consistencia_dos_dados_de_uma_os.listar_servicos_da_os()
    
@then("listar Logs")
def step(context):
    context.Localizar_consistencia_dos_dados_de_uma_os.listar_logs_da_os()
    
@then("listar Associacao")
def step(context):
    context.Localizar_consistencia_dos_dados_de_uma_os.listar_associacao_da_os()

@then("listar Unificacoes")
def step(context):
    context.Localizar_consistencia_dos_dados_de_uma_os.listar_unificacoes_da_os()
    
@then("listar Formularios")
def step(context):
    context.Localizar_consistencia_dos_dados_de_uma_os.listar_formularios_da_os()
    
@then("listar Mensagens")
def step(context):
    context.Localizar_consistencia_dos_dados_de_uma_os.listar_mensagens_da_os()
    
@then("listar Indicadores")
def step(context):
    context.Localizar_consistencia_dos_dados_de_uma_os.listar_indicadores_da_os()
    
@then("listar Pes Associados")
def step(context):
    context.Localizar_consistencia_dos_dados_de_uma_os.listar_pes_associados_da_os()
    
@then("listar Logs Scada")

def step(context):
    context.Localizar_consistencia_dos_dados_de_uma_os.listar_logs_scada_da_os()
    
@then("listar Pre-despacho")
def step(context):
    context.Localizar_consistencia_dos_dados_de_uma_os.listar_pre_despacho_da_os()


#Despachar para equipe distinta
@given("abrir_view_recursos_propostos - atendimento servico rede")
def step(context):
    context.Despachar_servico_de_rede_para_equipe_distinta.abrir_view_recursos_propostos()

@when("abrir view de servico de redes pendentes - atendimento servico rede")
def step(context):
    context.Despachar_servico_de_rede_para_equipe_distinta.abrir_view_de_servico_de_redes_pendentes()

@then("selecionar servico de rede desejado - atendimento servico rede")
def step(context):
    context.Despachar_servico_de_rede_para_equipe_distinta.selecionar_servico_de_rede_desejado()

@then("despachar para determinada equipe")
def step(context):
    context.Despachar_servico_de_rede_para_equipe_distinta.despachar_para_equipe_distinta()


#Resgatar os despachada por voz
@given("abrir view e mostrar equipes recursos propostos")
def step(context):
    context.Resgatar_os_despachada_por_voz.abrir_view_recursos_propostos()
    
@then("selecionar os despachada")
def step(context):
    context.Resgatar_os_despachada_por_voz.selecionar_os_despachada()
    
@then("selecionar icone resgatar os despachada")
def step(context):
    context.Resgatar_os_despachada_por_voz.selecionar_icone_resgatar_os_despachada()   
     
#Interromper e rejeitar os
@given("abrir view recursos propostos e sr pendente")
def step(context):
    context.Interromper_rejeitar_os_sem_agendamento.abrir_view_recursos_propostos_e_sr_pendente()
    
@when("selecionar equipe para interrupcao e rejeicao")
def step(context):
    context.Interromper_rejeitar_os_sem_agendamento.selecionar_equipe_para_interrupcao_e_rejeicao()

@then("selecionar icone interrupcao e rejeicao")
def step(context):
    context.Interromper_rejeitar_os_sem_agendamento.selecionar_icone_interrupcao_e_rejeicao()


#Logoff da equipe
@given("clicar na chave negativa para o logoff de equipe")
def step(context):
    context.Logoff_da_equipe.clicar_na_chave_negativa_para_o_logoff_de_equipe()

@when("escolho equipe logada")
def step(context):
    context.Logoff_da_equipe.escolho_equipe_logada()
    
@then("preencho dados e concluo o logoff")
def step(context):
    context.Logoff_da_equipe.preencho_dados_e_concluo_o_logoff()
