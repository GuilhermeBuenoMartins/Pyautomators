#Pacote pyautomators 
from Pyautomators.desk import Desk
from Pyautomators.Verifica import Valida
from Pyautomators import Documentacao
from Pyautomators import Ambiente
from lib.metodos import Metodos


#Modulos Extras
from time import sleep

#Atendimento SR
from pages.pages.telaAtendimentoSR import Logar_equipe
from pages.pages.telaAtendimentoSR import Localizar_consistencia_dos_dados_de_uma_os
from pages.pages.telaAtendimentoSR import Despachar_servico_de_rede_para_equipe_distinta
from pages.pages.telaAtendimentoSR import Resgatar_os_despachada_por_voz
from pages.pages.telaAtendimentoSR import Interromper_rejeitar_os_sem_agendamento
from pages.pages.telaAtendimentoSR import Logoff_da_equipe

#Atendimento Workflow
from pages.pages.telaAtendimentoWorkflow import Iniciar_atendimento_da_os_pelo_workflow 
from pages.pages.telaAtendimentoWorkflow import Postergar_o_atendimento_da_os
from pages.pages.telaAtendimentoWorkflow import Reiniciar_o_atendimento_da_os
from pages.pages.telaAtendimentoWorkflow import Abertura_manobra
from pages.pages.telaAtendimentoWorkflow import View_interrupcoes
from pages.pages.telaAtendimentoWorkflow import Definir_elemento_de_referencia_da_ordem_de_servico
from pages.pages.telaAtendimentoWorkflow import Definir_causa_da_ordem_de_servico
from pages.pages.telaAtendimentoWorkflow import Incluir_material_na_ordem_de_servico
from pages.pages.telaAtendimentoWorkflow import Incluir_um_servico_para_a_ordem_de_servico
from pages.pages.telaAtendimentoWorkflow import Finalizar_atendimento_da_ordem_de_servico
from pages.pages.telaAtendimentoWorkflow import Fechamento_manobra

#Atuacao nao programada
from pages.pages.telaAtuacaoNaoProgramada import criar_evento_de_rede
from pages.pages.telaAtuacaoNaoProgramada import manobrar_evento_de_rede_nao_programado
from pages.pages.telaAtuacaoNaoProgramada import Atendimento_passado_atuacao_nao_programada
from pages.pages.telaAtuacaoNaoProgramada import Iniciar_atendimento_da_oe_e_inicio_deslocamento
from pages.pages.telaAtuacaoNaoProgramada import Inclusao_de_material_servico_causa_e_observacao
from pages.pages.telaAtuacaoNaoProgramada import Finalizar_ordem_de_servico
from pages.pages.telaAtuacaoNaoProgramada import Anular_servico_de_rede_pendente
from pages.pages.telaAtuacaoNaoProgramada import Anular_servico_de_rede_com_atendimento_iniciado

#AtuacaoProgramada
from pages.pages.telaAtuacaoProgramada import Despachar_servico_de_rede_manualmente
from pages.pages.telaAtuacaoProgramada import Iniciar_Atendimento_atuacao_programada
from pages.pages.telaAtuacaoProgramada import InclusaoMaterial
from pages.pages.telaAtuacaoProgramada import Executar_manobra_e_ordem_de_manobra
from pages.pages.telaAtuacaoProgramada import View_interrupcoes_ap
from pages.pages.telaAtuacaoProgramada import FinalizarAtendimentoAtuacao
from pages.pages.telaAtuacaoProgramada import AlteracaoCampos

#Geracao de avisos
from pages.pages.telaGeracaoDeAvisos import Criacao_de_aviso
from pages.pages.telaGeracaoDeAvisos import Criacao_de_aviso_sem_cliente
from pages.pages.telaGeracaoDeAvisos import Associacao_de_avisos
from pages.pages.telaGeracaoDeAvisos import Extrair_aviso_novo
from pages.pages.telaGeracaoDeAvisos import Extrair_aviso_existente
from pages.pages.telaGeracaoDeAvisos import Anular_aviso_associado_a_um_cliente
from pages.pages.telaGeracaoDeAvisos import Anular_servico_de_rede_despachado

#LOGIN LOGOFF
from pages.pages.telaLogin_Logoff_Equipe import LoginEquipe
from pages.pages.telaLogin_Logoff_Equipe import LogoffEquipe
from pages.pages.telaLogin_Logoff_Equipe import EditarLogin
from pages.pages.telaLogin_Logoff_Equipe import LogoffOE

#PAUSAREQUIPE
from pages.pages.telaPausarEquipeDespachoMultiplo import Despacho_multiplo
from pages.pages.telaPausarEquipeDespachoMultiplo import Pausar_atendimento
from pages.pages.telaPausarEquipeDespachoMultiplo import Pausar_equipe

#PES Geracao Manual
from pages.pages.telaPESGeracaoManual import PESGeracaoManual

#PES Configuracao Prazos
from pages.pages.telaPESConfiguracaoPrazos import PESConfiguracaoPrazos
from pages.pages.telaPESConfiguracaoPrazos import PESClassificadoNormal
from pages.pages.telaPESConfiguracaoPrazos import PESClassificadoForaPrazo
from pages.pages.telaPESConfiguracaoPrazos import PESClassificadoUrgente

#PLano de Trabalho
from pages.pages.telaPlanodeTrabalho import AgendamentoOS
from pages.pages.telaPlanodeTrabalho import AgendamentoPosterior
from pages.pages.telaPlanodeTrabalho import AgendamentoDataHora
from pages.pages.telaPlanodeTrabalho import ExibirPlanoTrabalho
from pages.pages.telaPlanodeTrabalho import AgendamentoFixo
from pages.pages.telaPlanodeTrabalho import AgendamentoDespachoPDA
from pages.pages.telaPlanodeTrabalho import RemoverAgendamento

#Proposta Falha
from pages.pages.telaPropostaFalha import Configuracao_proposta_falha
from pages.pages.telaPropostaFalha import Proposta_falha_seccionador
from pages.pages.telaPropostaFalha import Proposta_falha_transformador

#Restricao Operativa
from pages.pages.telaRestricaoOperativa import BuscaOperativa
from pages.pages.telaRestricaoOperativa import CriarOS
from pages.pages.telaRestricaoOperativa import Atender_encerrar_subestacao_transformador
from pages.pages.telaRestricaoOperativa import Incluir_editar_restricao_operativa
from pages.pages.telaRestricaoOperativa import Ordenacao_de_colunas
from pages.pages.telaRestricaoOperativa import Localizar_restricao_operativa_graficamente
from pages.pages.telaRestricaoOperativa import Encerrar_restricao_operativa

#Servico de Rede Passado
from pages.pages.telaServicoRedePassado import GerarInterrupcao
from pages.pages.telaServicoRedePassado import InterrupcaoConsumidor
from pages.pages.telaServicoRedePassado import FinalizarInterrupcao
from pages.pages.telaServicoRedePassado import SimularServicoRede
from pages.pages.telaServicoRedePassado import MarcarServicoRedeComoPassado
from pages.pages.telaServicoRedePassado import ExcluirManobrasSimuladas
from pages.pages.telaServicoRedePassado import IncluirManobrasSimuladas
from pages.pages.telaServicoRedePassado import ExecutarManobrasSimuladas
from pages.pages.telaServicoRedePassado import EncerrarServicoRedeMarcadoComoPassado

#Unificar Servico de Rede
from pages.pages.telaUnificarServicoRede import UnificarVariosSR
from pages.pages.telaUnificarServicoRede import UnificarSREncerrado

#VISAO GRAFICA
from pages.pages.telaVisaoGrafica import Localizar_elemento_graficamente
#from pages.pages. telaVisaoGrafica import Localizar_recurso_proposto_graficamente
from pages.pages.telaVisaoGrafica import Redesenhar_janela_visao_grafica
from pages.pages.telaVisaoGrafica import GerarEtiqueta
from pages.pages.telaVisaoGrafica import ExcluirEtiqueta 
from pages.pages.telaVisaoGrafica import Fluxo_solicitacao
from pages.pages.telaVisaoGrafica import Listar_elemento_jusante
from pages.pages.telaVisaoGrafica import Listar_elemento_a_montante
from pages.pages.telaVisaoGrafica import InstalacoesPontos
from pages.pages.telaVisaoGrafica import FluxoCorrente
from pages.pages.telaVisaoGrafica import Entorno_de_trabalho_por_selecao
from pages.pages.telaVisaoGrafica import Entorno_de_trabalho_pela_view_servico_de_redes_pendentes
from pages.pages.telaVisaoGrafica import EsquemaOrtogonal
from pages.pages.telaVisaoGrafica import EsquemaUnifilar
from pages.pages.telaVisaoGrafica import AbrangenciaFalta
from pages.pages.telaVisaoGrafica import Estudo_manobra

#Filtro Zonal
from pages.pages.telaFiltroZonal import Criar_filtro_zonal
from pages.pages.telaFiltroZonal import Modificar_filtro_zonal
from pages.pages.telaFiltroZonal import Cria_copia_a_partir_de_um_existente
from pages.pages.telaFiltroZonal import Eliminar_filtro_zonal 

#View Servico de Rede Pendente
from pages.pages.telaViewSRPendente import Propriedades_da_view
from pages.pages.telaViewSRPendente import Ordenacao_das_colunas
from pages.pages.telaViewSRPendente import Criar_filtros

#Inclusao SR
from pages.pages.telaInclusaoSR import CriarEvento
from pages.pages.telaInclusaoSR import ServicoRede
from pages.pages.telaInclusaoSR import IncidenciaAtendimento
from pages.pages.telaInclusaoSR import STDTransformador
from pages.pages.telaInclusaoSR import STDDiversos
from pages.pages.telaInclusaoSR import STDRedeDistribuicao
from pages.pages.telaInclusaoSR import STDSubestacao
from pages.pages.telaInclusaoSR import Evento_rede_nao_programado
from pages.pages.telaInclusaoSR import Evento_rede_programado


#Tela Unica
from pages.pages.telaTelaUnica import TelaUnica

#Scada
from pages.pages.telaScada import Scada

#Pre Despacho
from pages.pages.telaPreDespacho import SRDespachado
from pages.pages.telaPreDespacho import SRAgendado
from pages.pages.telaPreDespacho import SRMarcar
from pages.pages.telaPreDespacho import DesmarcarPreDespacho
from pages.pages.telaPreDespacho import DesmarcarPreDespachoAut
from pages.pages.telaPreDespacho import DespachoAutomatico1
from pages.pages.telaPreDespacho import DespachoAutomatico2
from pages.pages.telaPreDespacho import SRMarcadoPreDespacho

#Clientes Prioritatios
from pages.pages.telaClientesPrioritarios import ClientesPrioritarios

#Schedule
from pages.pages.telaSchedule import Schedule

#Manobras e ordens de manobra
from pages.pages.telaManobraOrdemManobras import Eliminar_ordem_de_manobra_1

#Atendimento passado
from pages.pages.telaAtendimentoPassado import Atendimento_passado


def limpar_name(step):
    return step.replace("<","").replace(">","").replace('"','').replace(" ","_")


def before_scenario(context,scenario):
    execucao = context.config.userdata['user']
    
    #abre a aplicacao InGrid
    context.path = Ambiente.path_atual() 
    
    if(execucao == 'vgama'):
        context.app = Desk("C:/Users/vgama/Desktop/InGRID_5.4.0.8/zeus.exe",context.path+"drivers/Winium.Desktop.Driver.exe",)
    
    if(execucao == 'QA'):
        context.app = Desk("C:/Users/vgama/Desktop/ingrid-dms/zeus.exe",context.path+"drivers/Winium.Desktop.Driver.exe",)
    
    if(execucao == 'gcruzm'):
        context.app. = Desk("C:/Users/gcruzm/Desktop/InGrid - new version/ingrid-dms-client-TRUNK-18-03-1510/zeus.exe",context.path+"drivers/Winium.Desktop.Driver.exe",)
    
    #Instancia de Metodos    
    context.asserts = Valida()
    context.docs = Documentacao
    
    #Pages
    #Atendimento SR
    context.Logar_equipe = Logar_equipe(context)
    context.Localizar_consistencia_dos_dados_de_uma_os = Localizar_consistencia_dos_dados_de_uma_os(context)
    context.Despachar_servico_de_rede_para_equipe_distinta = Despachar_servico_de_rede_para_equipe_distinta(context)
    context.Resgatar_os_despachada_por_voz = Resgatar_os_despachada_por_voz(context)
    context.Interromper_rejeitar_os_sem_agendamento = Interromper_rejeitar_os_sem_agendamento(context)
    context.Logoff_da_equipe = Logoff_da_equipe(context)

    #Atendimento Workflow
    context.Iniciar_atendimento_da_os_pelo_workflow = Iniciar_atendimento_da_os_pelo_workflow(context)
    context.Postergar_o_atendimento_da_os = Postergar_o_atendimento_da_os(context)
    context.Reiniciar_o_atendimento_da_os = Reiniciar_o_atendimento_da_os(context)
    context.Abertura_manobra = Abertura_manobra(context)
    context.View_interrupcoes = View_interrupcoes(context)
    context.Definir_elemento_de_referencia_da_ordem_de_servico = Definir_elemento_de_referencia_da_ordem_de_servico(context)
    context.Definir_causa_da_ordem_de_servico = Definir_causa_da_ordem_de_servico(context)
    context.Incluir_material_na_ordem_de_servico = Incluir_material_na_ordem_de_servico(context)
    context.Incluir_um_servico_para_a_ordem_de_servico = Incluir_um_servico_para_a_ordem_de_servico(context)
    context.Finalizar_atendimento_da_ordem_de_servico = Finalizar_atendimento_da_ordem_de_servico(context)
    context.Fechamento_manobra = Fechamento_manobra(context)

    #Atuacao Nao Programada
    context.criar_evento_de_rede = criar_evento_de_rede(context)
    context.manobrar_evento_de_rede_nao_programado = manobrar_evento_de_rede_nao_programado(context)
    context.Atendimento_passado_atuacao_nao_programada = Atendimento_passado_atuacao_nao_programada(context)
    context.Iniciar_atendimento_da_oe_e_inicio_deslocamento = Iniciar_atendimento_da_oe_e_inicio_deslocamento(context)
    context.Inclusao_de_material_servico_causa_e_observacao = Inclusao_de_material_servico_causa_e_observacao(context)
    context.Finalizar_ordem_de_servico = Finalizar_ordem_de_servico(context)
    context.Anular_servico_de_rede_pendente = Anular_servico_de_rede_pendente(context)
    context.Anular_servico_de_rede_com_atendimento_iniciado = Anular_servico_de_rede_com_atendimento_iniciado(context)

    #AtuacaoProgramada
    context.Despachar_servico_de_rede_manualmente = Despachar_servico_de_rede_manualmente(context)
    context.Iniciar_Atendimento_atuacao_programada = Iniciar_Atendimento_atuacao_programada(context)
    context.Executar_manobra_e_ordem_de_manobra = Executar_manobra_e_ordem_de_manobra(context)
    context.View_interrupcoes_ap = View_interrupcoes_ap(context)
    context.FinalizarAtendimentoAtuacao = FinalizarAtendimentoAtuacao(context)
    context.InclusaoMaterial = InclusaoMaterial(context)
    context.AlteracaoCampos = AlteracaoCampos(context)
    
    #Geracao de avisos
    context.Criacao_de_aviso = Criacao_de_aviso (context)
    context.Criacao_de_aviso_sem_cliente = Criacao_de_aviso_sem_cliente (context)
    context.Associacao_de_avisos = Associacao_de_avisos (context)
    context.Extrair_aviso_novo = Extrair_aviso_novo (context)
    context.Extrair_aviso_existente = Extrair_aviso_existente (context)
    context.Anular_aviso_associado_a_um_cliente = Anular_aviso_associado_a_um_cliente (context)
    context.Anular_servico_de_rede_despachado = Anular_servico_de_rede_despachado (context)

    #Login Logoff
    context.LoginEquipe = LoginEquipe(context)
    context.LogoffEquipe = LogoffEquipe(context)
    context.EditarLogin = EditarLogin(context)
    context.LogoffOE = LogoffOE(context)

    #PAUSAEQUIPEDESPACHO
    context.Despacho_multiplo = Despacho_multiplo(context)
    context.Pausar_atendimento = Pausar_atendimento(context)
    context.Pausar_equipe = Pausar_equipe(context)

    #PES Geracao Manual
    context.PESGeracaoManual = PESGeracaoManual(context)
    
    #PES Configuracao Prazos
    context.PESConfiguracaoPrazos = PESConfiguracaoPrazos(context)
    context.PESClassificadoNormal = PESClassificadoNormal(context)
    context.PESClassificadoForaPrazo = PESClassificadoForaPrazo(context)
    context.PESClassificadoUrgente = PESClassificadoUrgente(context)
    
    
    #PLANO DE TRABALHO
    context.AgendamentoOS = AgendamentoOS(context)
    context.AgendamentoPosterior = AgendamentoPosterior(context)
    context.AgendamentoDataHora =  AgendamentoDataHora(context)
    context.ExibirPlanoTrabalho = ExibirPlanoTrabalho(context)
    context.AgendamentoFixo = AgendamentoFixo(context)
    context.AgendamentoDespachoPDA = AgendamentoDespachoPDA(context)
    context.RemoverAgendamento = RemoverAgendamento(context)
    
    #Proposta Falha
    context.Proposta_falha_transformador = Proposta_falha_transformador(context)
    context.Configuracao_proposta_falha = Configuracao_proposta_falha(context)
    context.Proposta_falha_seccionador = Proposta_falha_seccionador(context)

    #Restricao Operativa
    context.BuscaOperativa = BuscaOperativa(context)
    context.CriarOS = CriarOS(context)
    context.Atender_encerrar_subestacao_transformador = Atender_encerrar_subestacao_transformador(context)
    context.Incluir_editar_restricao_operativa = Incluir_editar_restricao_operativa(context)
    context.Ordenacao_de_colunas = Ordenacao_de_colunas(context)
    context.Localizar_restricao_operativa_graficamente = Localizar_restricao_operativa_graficamente(context)
    context.Encerrar_restricao_operativa =  Encerrar_restricao_operativa(context)

    #Servico de Rede Passado
    context.GerarInterrupcao = GerarInterrupcao(context)
    context.InterrupcaoConsumidor = InterrupcaoConsumidor(context)
    context.FinalizarInterrupcao = FinalizarInterrupcao(context)
    context.SimularServicoRede = SimularServicoRede(context)
    context.MarcarServicoRedeComoPassado = MarcarServicoRedeComoPassado(context)
    context.ExcluirManobrasSimuladas = ExcluirManobrasSimuladas(context)
    context.IncluirManobrasSimuladas = IncluirManobrasSimuladas(context)
    context.ExecutarManobrasSimuladas = ExecutarManobrasSimuladas(context)
    context.EncerrarServicoRedeMarcadoComoPassado = EncerrarServicoRedeMarcadoComoPassado(context)

    #Unificar Servico de Rede
    context.UnificarVariosSR = UnificarVariosSR(context)
    context.UnificarSREncerrado = UnificarSREncerrado(context)

    #VISAO GRAFICA
    context.Localizar_elemento_graficamente = Localizar_elemento_graficamente(context)
    context.Redesenhar_janela_visao_grafica = Redesenhar_janela_visao_grafica(context)
    context.GerarEtiqueta = GerarEtiqueta(context)
    context.ExcluirEtiqueta = ExcluirEtiqueta(context)
    context.Fluxo_solicitacao = Fluxo_solicitacao(context)
    context.Listar_elemento_jusante = Listar_elemento_jusante(context)
    context.Listar_elemento_a_montante = Listar_elemento_a_montante(context)
    context.FluxoCorrente = FluxoCorrente(context)
    context.InstalacoesPontos = InstalacoesPontos(context)
    context.Entorno_de_trabalho_por_selecao = Entorno_de_trabalho_por_selecao(context)
    context.Entorno_de_trabalho_pela_view_servico_de_redes_pendentes = Entorno_de_trabalho_pela_view_servico_de_redes_pendentes(context)
    context.EsquemaOrtogonal = EsquemaOrtogonal(context)
    context.EsquemaUnifilar = EsquemaUnifilar(context)
    context.AbrangenciaFalta = AbrangenciaFalta(context)
    context.Estudo_manobra = Estudo_manobra(context)

    #Filtro Zonal
    context.Criar_filtro_zonal = Criar_filtro_zonal (context)
    context.Modificar_filtro_zonal = Modificar_filtro_zonal (context)
    context.Cria_copia_a_partir_de_um_existente = Cria_copia_a_partir_de_um_existente (context)
    context.Eliminar_filtro_zonal = Eliminar_filtro_zonal (context)

    #View servico de redes pendentes
    context.Propriedades_da_view = Propriedades_da_view (context)
    context.Ordenacao_das_colunas = Ordenacao_das_colunas (context)
    context.Criar_filtros = Criar_filtros (context)
    
    #INCLUSAO SR
    context.CriarEvento = CriarEvento(context)
    context.ServicoRede = ServicoRede(context)
    context.IncidenciaAtendimento = IncidenciaAtendimento(context)
    context.STDTransformador = STDTransformador(context)
    context.STDDiversos = STDDiversos(context)
    context.STDRedeDistribuicao = STDRedeDistribuicao(context)
    context.STDSubestacao = STDSubestacao(context)
    context.Evento_rede_nao_programado = Evento_rede_nao_programado(context)
    context.Evento_rede_programado = Evento_rede_programado(context)

    #Tela Unica
    context.TelaUnica = TelaUnica(context)
    
    #Scada
    context.Scada = Scada(context)

    #Pre Despacho
    context.SRDespachado = SRDespachado(context)
    context.SRAgendado = SRAgendado(context)
    context.SRMarcar = SRMarcar(context)
    context.DesmarcarPreDespacho = DesmarcarPreDespacho(context)
    context.DesmarcarPreDespachoAut =DesmarcarPreDespachoAut(context)
    context.DespachoAutomatico1 = DespachoAutomatico1(context)
    context.DespachoAutomatico2 = DespachoAutomatico2(context)
    context.SRMarcadoPreDespacho = SRMarcadoPreDespacho(context)
    
    #Clientes Prioritarios
    context.ClientesPrioritarios = ClientesPrioritarios(context)
      
    #Schedule
    context.Schedule = Schedule(context)

    #Manobras e ordem de manobra
    context.Eliminar_ordem_de_manobra_1 = Eliminar_ordem_de_manobra_1 (context)

    #Atendimento passado
    context.Atendimento_passado = Atendimento_passado (context)

    context.app_metodos=Metodos(context.app)
    
    #efetua login do usuario no sistema
    
    #login para base de QA
    if(execucao == 'QA'):
        context.asserts.verifica_tela(context.path+"data/images/loginIngridDVENTURINI.png",100,valida=True)
        context.app.clica_imagem(context.path+"data/images/dventurini.png",1,"left",similar=40)
        context.app.digitos("tab")
        context.app.escrever_direto("dventurini")
        context.app.digitos("enter")
        sleep(1)
    
    #Login utilizando codigo vgama
    if(execucao == 'vgama'):
        context.asserts.verifica_tela(context.path+"data/images/loginIngrid.png",100,valida=True)
        context.app.clica_imagem(context.path+"data/images/campoLogin.png",1,"left",similar=40)
        context.app.digitos("tab")
        context.app.escrever_direto("PASS")
        context.app.digitos("enter")
        sleep(1)

    #Login utilizando codigo gcruzm
    if(execucao == 'gcruzm'):
        context.asserts.verifica_tela(context.path+"data/images/automacao_2.png",100)
        context.app.clica_imagem(context.path+"data/images/automacao_2.png")
        context.app.digitos("tab")
        context.app.escrever_direto("PASS")
        context.app.digitos("enter")
        sleep(1)
        
        
    #aguarda abertura total da tela de introducao
    context.asserts.verifica_tela(context.path+"data/images/introInGrid.png", 100, 1, valida=True)
     #espera o banco carregar
    while(context.asserts.verifica_tela(context.path + "data/images/carregandoBDI.png", 80) != None):
        pass
    sleep(10)
    
#apos cada step tira um screenshot com o nome do passo realizado
def after_step(context,step):
    context.docs.printarTela(context.path+"docs/{}-{}.png".format(limpar_name(str(context.scenario.name)),limpar_name(step.name)))
    
    
def after_scenario(context,scenario):
    context.app.fechar_programa()