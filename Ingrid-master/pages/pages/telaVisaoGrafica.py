# -*- coding: utf-8 -*-
'''
Created on 4 de jul de 2018

@author: gcruzm
'''
from time import sleep



class Localizar_elemento_graficamente(object):
    def __init__(self, context):
        self.context = context
        self.JANELA = "Janela"
        self.SERVICO_PENDENTE = "Serviços de Rede Pendentes"
        
    def abrir_view_servicos_de_rede_pendentes(self):
        self.context.app.clica(self.JANELA,"name", 3)
        self.context.app.digitos(("down",3),"right","down","enter")
        
        self.context.app.escreve("texto do filtro de tipos", self.SERVICO_PENDENTE,"name")
        self.context.app.digitos(("tab",2),"down","enter")
        
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/refreshServicoPendente.png", 50) != None):
            pass
        
    def selecionar_servico_rede_e_apertar_botao_direito_mouse(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD.png",100)
        sleep(3)
        self.context.app.clica_imagem(self.context.path+"data/images/20176768.png",1,"right", similar=60)
        sleep(5)
            
    def selecionar_opcao_localizar_elemento_graficamente(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/localizar_elemento_graficamente.png",100,valida=True)
        self.context.app.clica_imagem(self.context.path+"data/images/localizar_elemento_graficamente.png",1,"left", similar=60)
        sleep(5)
        self.context.asserts.verifica_tela(self.context.path+"data/images/visaografica.png", 80, similaridade =40)
        
'''
class Localizar_recurso_proposto_graficamente(object):
    def __init__(self, context):
        self.context = context
    
    def selecionar_opcao_localizar_recursos_propostos_graficamente(self):
        self.context.app.clica_coordenada(708,138)
        self.context.app.digitos("down","enter")
        sleep(15)
'''
class Redesenhar_janela_visao_grafica(object):
    def __init__(self, context):
        self.context = context
        
    def abrir_view_visao_grafica(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Vis")
        self.context.asserts.verifica_tela(self.context.path+"data/images/viewVisaoGrafica.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/viewVisaoGrafica.png", 2, "left", similar=70)
        sleep(5)
        
    def selecionar_camadas_visao_grafica(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/camadas.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/camadas.png")
        
        
    def apertar_botao_redesenhar(self):        
        self.context.asserts.verifica_tela(self.context.path+"data/images/redesenhar.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/redesenhar.png")
        self.context.asserts.verifica_tela(self.context.path+"data/images/redesenhando.png",80, similaridade=60)
        sleep(20)
        
class GerarEtiqueta(object):
    def __init__(self, context):

        self.context = context
        self.JANELA = "Janela"
        self.TIPO_ETIQUETA = "Tipo de Etiqueta"
        
    def criarEtiqueta(self):
        self.context.app.clica_coordenada(1060, 102)
        sleep(3)
        self.context.app.digitos("down","enter")
        sleep(5)
         #CLICA EM UM ELEMENTO NA VIEW VISAO GRAFICA
        self.context.app.clica_imagem(self.context.path+"data/images/elementoVisaoGrafica.png", 1, "left", similar=70)
        
    def camposEtiqueta(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/criarEtiquetaNova.png",80, similaridade=60)
        self.context.app.clica_imagem(self.context.path+"data/images/tipoEtiqueta.png", 1, "left", similar=70)
        sleep(3)
        self.context.app.digitos("down","enter")
        
        
class ExcluirEtiqueta(object):
    def __init__(self, context):
        self.context = context
        self.ELIMINAR_ETIQUETA = "Eliminar Etiqueta"
            
    def selecionaEtiqueta(self):
        sleep(3)
        self.context.app.clica_coordenada(1036, 102)
        self.context.app.digitos(("down",4),"enter")
        sleep(5)
        self.context.app.digitos(("down",14),"enter")
        sleep(4)
        
    def excluirEtiqueta(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/listaEtiquetas.png", 80, similaridade=60)
        self.context.app.clica_imagem(self.context.path+"data/images/botaoExcluir.png", 1, "left", similar=50)
        self.context.app.digitos("enter")


class Fluxo_solicitacao(object):
    def __init__(self, context):
        self.context = context
        
    def selecionar_opcao_fluxo_por_solicitacao(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/fluxo_solicitacao.png")
        self.context.app.clica_imagem(self.context.path+"data/images/fluxo_solicitacao.png", 1, "left", similar=70)
        sleep(12)
        
    def selecionar_elemento_rede_fluxo_solicitacao(self):
        #CLICA EM UM ELEMENTO NA VIEW VISAO GRAFICA
        self.context.app.clica_imagem(self.context.path+"data/images/elementoVisaoGrafica.png", 1, "left", similar=70)
        self.context.asserts.verifica_tela(self.context.path+"data/images/informacao.png", 80)
    
    def sistema_realiza_calculo(self):
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/executandoFluxoCarga.png", 50) != None):
            pass
        
    def seleciona_opcao_resultado_fluxo_carga(self): 
        #SELECIONA OPCAO RESULTADO FLUXO CARGA        
        self.context.app.clica_imagem(self.context.path+"data/images/opcaoResultadoFluxo.png", 1,"left", similar=60)
        self.context.app.clica_imagem(self.context.path+"data/images/elementoVisaoGrafica.png", 1, "left", similar=70)
        
    def verifica_view_resultado_fluxo_carga(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/resultadosFluxoCarga.png", 80)
        sleep(5)
        
class Listar_elemento_jusante(object):
    def __init__(self, context):
        self.context = context
    
    def selecionar_opcao_a_jusante(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/jusante.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/jusante.png")
    
    def preencher_dados_a_jusante(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/selecao_entidade.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/selecao_entidade.png")
        sleep(2)
        self.context.asserts.verifica_tela(self.context.path+"data/images/selecao_entidade.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/selecao_entidade.png")
        sleep(2)
        self.context.asserts.verifica_tela(self.context.path+"data/images/down.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/down.png")
        sleep(2)
        self.context.app.digitos("down",("s",2),"tab")
        self.context.app.escrever_direto("RIB01")
        self.context.app.digitos("tab","enter")
        self.context.app.clica_imagem(self.context.path+"data/images/botaoSelecionar.png", 1, "left", similar=50)
        
        #VERIFICA SE A VIEW ABRIU
        self.context.asserts.verifica_tela(self.context.path+"data/images/consultaConectividade.png",100)
    
    
class Listar_elemento_a_montante(object):
    def __init__(self, context):
        self.context = context
        
    
    def selecionar_opcao_a_montante(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/montante.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/montante.png")
        sleep(2)
    
    def preencher_dados_a_montante(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/selecao_entidade.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/selecao_entidade.png")
        sleep(2)
        self.context.asserts.verifica_tela(self.context.path+"data/images/down.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/down.png")
        sleep(2)
        self.context.app.digitos("down",("s",2),"tab")
        self.context.app.escrever_direto("RIB01")
        sleep(2)
        self.context.app.clica_imagem(self.context.path+"data/images/botaoSelecionar.png", 1, "left", similar=50)
        
        #VERIFICA SE A VIEW ABRIU
        self.context.asserts.verifica_tela(self.context.path+"data/images/consultaConectividade.png",100)

class InstalacoesPontos(object):
    def __init__(self, context):
        self.context = context
        self.INSTALACOES_ENTRE_2_PONTOS = "Instalações Entre 2 Pontos"
        self.SELECIONAR = "Selecionar"

    def clicaDoisPontos(self):
        self.context.app.clica_imagem(self.context.path+"data/images/instalacaoDoisPontos.png", 1, "left", similar=70)
       
    def primeiroPonto(self):
        self.context.app.digitos(("down",3),"tab")
        self.context.app.escrever_direto("35701328")
        self.context.app.clica_imagem(self.context.path+"data/images/botaoSelecionar.png", 1, "left", similar=50)
    
    def segundoPonto(self):
        sleep(3)
        self.context.app.digitos(("down",6),"tab")
        self.context.app.escrever_direto("CON01469")
        self.context.app.clica_imagem(self.context.path+"data/images/botaoSelecionar.png", 1, "left", similar=50)
        sleep(5)
        
class FluxoCorrente(object):
   
    def __init__(self, context):
        self.context = context
        self.JANELA = "Janela"
        self.FLUXO_DE_CORRENTE = "Fluxo de Corrente"
    
    def opcaoFluxoCorrente(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/opcaoFluxoCorrente.png",80, similaridade=70)
        self.context.app.clica_imagem(self.context.path+"data/images/opcaoFluxoCorrente.png", 1, "left", similar=70)
        sleep(5)
        self.context.app.digitos("enter")
        self.context.asserts.verifica_tela(self.context.path+"data/images/elementoVisaoGrafica.png",80, similaridade=70)
        self.context.app.clica_imagem(self.context.path+"data/images/elementoVisaoGrafica.png", 1, "left", similar=70)
        sleep(4)
        self.context.app.digitos(("tab",2),"enter")
        sleep(5)
        self.context.asserts.verifica_tela(self.context.path+"data/images/redeColorida.png",80, similaridade=30)
        


class Entorno_de_trabalho_por_selecao(object):
    def __init__(self, context):
        self.context = context
        self.ABRIR_ENTORNO_DE_TRABALHO_POR_SELECAO = "Abrir Entorno de Trabalho por Seleção"
        
    def selecionar_seta_ao_lado_da_opcao_entorno_de_trabalho(self):
        self.context.app.clica_coordenada(905,117)
        sleep(5)
    
    def selecionar_opcao_abrir_entorno_de_trabalho_por_selecao(self):
        self.context.app.digitos(("down",2),"enter")
    
    def clicar_em_um_elemento_na_visao_grafica(self):
        self.context.app.clica_imagem(self.context.path+"data/images/elementoVisaoGrafica.png", 1, "left", similar=70)
        sleep(5)
        self.context.asserts.verifica_tela(self.context.path+"data/images/entornoTrabalhoZeus.png", 80)

class Entorno_de_trabalho_pela_view_servico_de_redes_pendentes(object):
    def __init__(self, context):
        self.context = context
    
    def selecionar_servico_de_rede_para_o_entorno_de_trabalho(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD.png",100)
        self.context.app.digitos("down")
    
    def selecionar_icone_abrir_entorno_de_trabalho(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/entorno_de_trabalho.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/entorno_de_trabalho.png", 1, "left", similar=60)
        sleep(4)
        self.context.asserts.verifica_tela(self.context.path+"data/images/entornoTrabalhoZeus.png", 80)
        

class EsquemaOrtogonal(object):
    
    def __init__(self, context):
        self.context = context
        self.RECARREGAR = "Recarregar"
    
    def clica_esquema_ortogonal_agrupado(self):
        self.context.app.clica_imagem(self.context.path+"data/images/esquemaOrtognalAgrupado.png", 1, "left")
        sleep(5)
        
    def selecionar_elemento_rede(self):
        self.context.app.clica_imagem(self.context.path+"data/images/elementoVisaoGrafica.png", 1, "left", similar=70)
        sleep(5)
        
    def buscar_unidade_seccionadora(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/visaoEsquemaOrtogonal.png",80)
        
        self.context.app.clica_imagem(self.context.path+"data/images/campoBusca.png", 1, "left", similar=60)
        self.context.app.escrever_direto("CON45102")
        self.context.app.clica_imagem(self.context.path+"data/images/recarregar.png", 1, "left", similar=50)
        sleep(10)
        
    def voltar_para_visao_grafica(self):
        self.context.app.clica_coordenada(39,80)
        sleep(5)
        
    def clica_esquema_ortogonal_reduzido(self):
        self.context.app.clica_imagem(self.context.path+"data/images/esquemaOrtognalReduzido.png", 1, "left")
        sleep(5)
        
    def verifica_janela_esquema_ortogonal_aberta(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/visaoEsquemaOrtogonal2.png",50)
        sleep(5)



class EsquemaUnifilar(object):
    
    def __init__(self, context):
        self.context = context
    
    def clicar_esquema_unifilar(self):
        self.context.app.clica_imagem(self.context.path+"data/images/esquemaUnifilar.png", 1, "left")
        sleep(5)
        
    def verifica_janela_esquema_unifilar_aberta(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/esquemaUnifilar.png",40)
        sleep(5)
        
        
        
class AbrangenciaFalta(object):
    def __init__(self, context):
        self.context = context
        
    def abrir_visao_grafica_simulada(self):
        sleep(5)
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/carregandoBDI.png", 80) != None):
            pass
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Simulada")
        self.context.app.clica_imagem(self.context.path+"data/images/opcaoGraficaSimulada.png", 2, "left", similar=40)
        
    def selecionar_seccionador_media(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/posicional.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/posicional.png",2,"left")
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/redeMT.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/redeMT.png",2,"left")
    
        self.context.asserts.verifica_tela(self.context.path+"data/images/seccionadorMT.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/seccionadorMT.png",1,"left")
        sleep(3)
        self.context.asserts.verifica_tela(self.context.path+"data/images/redesenhar.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/redesenhar.png",1,"left")
        
        #esperar a visao ser redesenhada
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/redesenhando.png",100) != None):
            pass
        self.context.app.clica_imagem(self.context.path+ "data/images/selecaoEntidade.png", 1, "left")
        self.context.app.clica_coordenada(635,300)
        
    def redesenhar(self):
        self.context.asserts.verifica_tela(self.context.path +"data/images/redesenhando.png")
        
    def selecionar_gerador(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/posicional.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/posicional.png",2,"left")
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/redeBT.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/redeBT.png",2,"left")
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/geradorisolado.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/geradorisolado.png",1,"left")
        sleep(3)
        self.context.asserts.verifica_tela(self.context.path+"data/images/redesenhar.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/redesenhar.png",1,"left")
        
        #esperar a visao ser redesenhada
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/redesenhando.png", 80) != None):
            pass
        self.context.asserts.verifica_tela(self.context.path+"data/images/selecaoEntidade.png",100)
        self.context.app.clica_imagem(self.context.path+ "data/images/selecaoEntidade.png", 1, "left")
        self.context.app.clica_coordenada(635,300)
        
    def selecionar_transformador(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/posicional.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/posicional.png",2,"left")
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/redeMT.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/redeMT.png",2,"left")
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/transformadorMT.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/transformadorMT.png",1, "left")
        
        sleep(3)
        self.context.asserts.verifica_tela(self.context.path+"data/images/redesenhar.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/redesenhar.png",1,"left")
        
        #esperar a visao ser redesenhada
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/redesenhando.png", 80) != None):
            pass
        
        self.context.app.clica_imagem(self.context.path+ "data/images/selecaoEntidade.png", 1, "left")
        self.context.app.clica_coordenada(635,300)
        
        
class Estudo_manobra(object):
    def __init__(self, context):
        self.context = context
        
    
    def selecionar_opcao_estudar_manobra(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/estudar_manobra.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/estudar_manobra.png")
        sleep(5)
    def preencher_info_rede_mt_estudar_manobra(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/selecao_entidade.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/selecao_entidade.png",100)
        self.context.app.digitos("r","tab")
        self.context.app.escrever_direto("9006318")
        self.context.app.clica_imagem(self.context.path+"data/images/botaoSelecionar.png", 1, "left", similar=50)
        sleep(2)
    
    def selecionar_seccionador(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/quadrado_verde.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/quadrado_verde.png")
    
    def selecionar_icone_localizar_seccionador_graficamente(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/localizar_seccionador_graficamente.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/localizar_seccionador_graficamente.png", 1, "left", similar=60)
        self.context.asserts.verifica_tela(self.context.path+"data/images/sinalizarElementor.png",100, similaridade=50)
        sleep(10)