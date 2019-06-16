# -*- coding: utf-8 -*- ]
'''
Created on 28 de jun de 2018

@author: vgama
'''
from time import sleep



class Despachar_servico_de_rede_manualmente(object):

    def __init__(self, context):
        self.context = context
    
    def abrindo_view_servico_rede(self):
        self.context.app.combo_digitos("ctrl","h")
        sleep(5)    
        self.context.asserts.verifica_tela(self.context.path+"data/images/servico_rede.png", 70)
        self.context.app.clica_imagem(self.context.path+"data/images/servico_rede.png", 1,"left")
        sleep(5)
        self.context.asserts.verifica_tela(self.context.path+"data/images/eventoRede.png", 80)
        #self.context.app.digitos("tab",("down",4))
        self.context.app.clica_imagem(self.context.path+"data/images/opcaoProgramada.png", 1, "left", similar=70)
        self.context.app.digitos("space")
        self.context.app.digitos(("tab",8))
        self.context.app.combo_digitos("alt","down")
        self.context.app.digitos("left","enter")    
        sleep(3)
        self.context.app.digitos("tab","space")
        self.context.app.clica_imagem(self.context.path+"data/images/pendente.png", 1, "left", similar=80)
        self.context.app.digitos("space","enter")        
        
        while(self.context.asserts.verifica_tela(self.context.path + "data/images/refresh.png", 50) != None):
            pass
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/semRegistro.png", 70)):
            raise("nenhum registro encontrado")
        
        sleep(10)
    
    def abir_recursos_propostos(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Recursos Propostos")
        self.context.app.digitos("enter")
        sleep(3)
        
        self.context.app.arraste_coordenada(183, 76, 81, 704, "left", 3)
        
    
    def selecionar_o_servico_de_rede_de_atuacao_programada(self):
        self.context.app.clica_imagem(self.context.path+"data/images/servico_rede.png", 1, "left", similar=80)
        self.context.app.digitos(("down",5))
        sleep(5)
        self.context.app.clica_imagem(self.context.path+"data/images/encontrarSR.png", 2, "left", similar=80)
        sleep(3)

        
    def realizar_o_despacho_manualmente_para_uma_equipe(self):
        self.context.app.arraste_coordenada(None, None, 33, 201, "left", 5)
        sleep(4)
        self.context.app.digitos("enter")
        self.context.asserts.verifica_tela(self.context.path+"data/images/informacao.png", 100,1)
        self.context.app.digitos("enter")
        
class Iniciar_Atendimento_atuacao_programada(object):
    
    def __init__(self, context):
        self.context = context
        self.OK = "OK"     

    def clicar_no_lapis_para_o_atendimento_unico(self):
        self.context.app.clica_imagem(self.context.path+"data/images/atendimento.png", 1, "left", similar=80)
        sleep(5)
        
    def flegar_informacao_inicio_deslocamento_e_chegada_ao_local(self):
        self.context.app.clica_coordenada(248, 237)
        if(self.context.asserts.verifica_tela(self.context.path + "data/images/campoDesmarcado.png", 50, similaridade=80) == None):
            self.context.app.digitos("space")
            
        self.context.app.clica_coordenada(248, 265)
        if(self.context.asserts.verifica_tela(self.context.path + "data/images/fimDesmarcado.png", 50, similaridade=80) == None):
            self.context.app.digitos("space")
            
        self.context.app.digitos(("tab",3))
        self.context.app.clica_coordenada(849, 319)
        self.context.app.digitos(("down",13 ),"tab")
        sleep(3)
        self.context.app.escrever_direto("TAT01230")
        self.context.app.clica(self.OK,"name",5)

class InclusaoMaterial(object):
 
    def __init__(self, context):
        self.context = context
        self.OK = "OK"
        self.SERVICOS = "Serviços"
        
    def incluirMaterial(self):
        self.context.asserts.verifica_tela(self.context.path+"/data/images/atendimentoOS.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/materiais.png", 1, "left", similar=60)
        self.context.asserts.verifica_tela(self.context.path+"/data/images/recurso.png",100)
        self.context.app.clica_imagem(self.context.path+"/data/images/adicionarMateriais.png")
        self.context.app.digitos(("tab",2),"right","down","right","down")
        self.context.app.clica_imagem(self.context.path+"/data/images/quantidadeMaterial.png")
        self.context.app.escrever_direto("1")
        self.context.app.digitos("tab","down")
        self.context.app.clica(self.OK,"name")
        self.context.app.digitos("enter")
        self.context.app.clica(self.OK,"name")
        
    def incluirServico(self):
        self.context.app.clica_imagem(self.context.path+"data/images/servico.png", 1, "left", similar=60)
        self.context.app.clica(self.SERVICOS, "name", 2)
        self.context.asserts.verifica_tela(self.context.path+"/data/images/recurso.png",100)
        self.context.app.clica_imagem(self.context.path+"/data/images/adicionarMateriais.png")
        self.context.app.digitos("tab","tab","right","down","tab","tab")
        self.context.app.escrever_direto("1")
        self.context.app.clica(self.OK,"name", 2)
        self.context.app.clica(self.OK,"name", 2)
        self.context.app.clica(self.OK,"name", 2)
    
class Executar_manobra_e_ordem_de_manobra(object):
    def __init__(self, context):
        self.context = context
        self.CANCELAR = "Cancelar"
    
    def abrir_manobras_ordens_manobras(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Manobras e Ordens de Manobras")
        self.context.app.digitos("enter")
        sleep(4)
        self.context.app.arraste_coordenada(183, 76, 81, 704, "left", 3)
        
    def verifica_atualizacao_view_ordens_manobras(self):
        sleep(5)
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/semRegistros.png",60, similaridade=80) == None):
            pass

class EditarManobraComentario(object):
    def __init__(self, context):
        self.context = context
        self.CANCELAR = "Cancelar"
    
    def executar_manobra_na_view_manobras_e_ordem_de_manobras(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/manobras_e_ordens.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/manobras_e_ordens.png")
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/manobras_e_ordens_2.png",100)
        self.context.app.digitos("down")
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/executarManobra.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/executarManobra.png")
        sleep(6)
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/buttonExecutar.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/buttonExecutar.png")
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/executarDesligado.png",150)
        self.context.app.clica(self.CANCELAR,"name",2)
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/manobras_e.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/manobras_e.png")
        
        self.context.asserts.verifica_tela("data/images/novo_comentario.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/novo_comentario.png")
    
class View_interrupcoes_ap(object):
    
    def __init__(self, context):
        self.context = context
        self.ATUALIZAR = "Atualizar"
    
    def abrir_view_interrupcoes(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Interrup")
        self.context.asserts.verifica_tela(self.context.path+"data/images/interrupcoes.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/interrupcoes.png", 1, "left", similar=60)
        self.context.app.digitos("enter")
        self.context.app.arraste_coordenada(183, 76, 81, 704, "left", 3)

    def atualizar_view_interrupcao(self):
        sleep(5)
        self.context.app.clica_imagem(self.context.path+"data/images/atualizar.png", 1, "left", similar=60)
        
    def FechamentoInterrupcoes(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/srp.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/srp.png")
        self.context.app.digitos("down","up","enter")
        sleep(2)
        self.context.asserts.verifica_tela(self.context.path+"data/images/interrupcoesDesligado.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/interrupcoesDesligado.png")
        self.context.asserts.verifica_tela(self.context.path+"data/images/atualizar.png",100)
        self.context.app.clica(self.ATUALIZAR,"name",2)
        #self.context.app.clica_imagem(self.context.path+"data/images/atualizar.png") 
        
        
class FinalizarAtendimentoAtuacao(object):
    def __init__(self, context):
        self.context = context
        self.OK = "OK"

    def preencheCampo(self):
        self.context.app.clica_coordenada(306, 306)
        self.context.app.digitos("space")
        self.context.app.clica(self.OK, "name", 5)

class AlteracaoCampos(object):
    def __init__(self, context):
        self.context = context
        self.JANELA = "Janela"
        self.REDE_PROGRAMADO = "Serviços de Rede Programados"
    
    def view_servicos_rede_programado(self):
        self.context.app.clica(self.JANELA,"name", 3)
        self.context.app.digitos(("down",3),"right","down","enter")
        
        self.context.app.escreve("texto do filtro de tipos", self.REDE_PROGRAMADO,"name")
        self.context.app.clica_imagem(self.context.path+"data/images/servicoRedeProgramados.png", 2,"left")
        
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/atualizando.png",50) != None):
            pass

    def view_propriedades(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Propriedades")
        self.context.app.digitos("enter")
        self.context.asserts.verifica_tela(self.context.path+"data/images/propriedades3.png", 80)
     
    def alterar_campo_data(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/datas.png", 80)
        self.context.app.clica_imagem(self.context.path+"data/images/datas.png", 1, "left", similar=70)
        sleep(2)
        self.context.app.clica_imagem(self.context.path+"data/images/lapis.png", 1, "left", similar=50)
        self.context.app.digitos("tab","left","up","tab","left","up",("tab",2),"left","up")
        sleep(3)
        self.context.asserts.verifica_tela(self.context.path+"data/images/opcaoSalvar.png", 80)
        self.context.app.clica_imagem(self.context.path+"data/images/opcaoSalvar.png", 1, "left", similar=70)
        sleep(3)
        
    def altera_campo_descricao(self):
        self.context.app.clica_imagem(self.context.path+"data/images/descricoes.png", 1, "left", similar=70)
        sleep(2)
        self.context.app.clica_imagem(self.context.path+"data/images/lapis.png", 1, "left", similar=50)
        self.context.app.digitos("tab")
        self.context.app.escrever_direto("Teste")        
        self.context.app.clica_imagem(self.context.path+"data/images/opcaoSalvar.png", 1, "left", similar=70)
        sleep(5)

        
        