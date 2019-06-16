
# -*- coding: utf-8 -*-
'''
Created on 17 de dez de 2018
@author: gcruzm


'''
from time import sleep


class Eliminar_ordem_de_manobra_1(object):
    
    def __init__(self, context):
        self.context = context
        self.OK="OK"
        self.SERVICOS_DE_REDES_PENDENTES = "Serviços de Redes Pendentes"
        self.MANOBRAS_E_ORDENS_DE_MANOBRA = "Manobras e Ordens de Manobras"
        self.ELIMINAR_ORDEM_DE_MANOBRA = "Eliminar Ordem de Manobra"
    
    def abrir_view_manobras_e_ordem_de_manobras(self):
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/carregandoBDI.png",80)!= None):
            pass
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Manobras")
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/opcao_manobras_e_ordens.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/opcao_manobras_e_ordens.png")
            self.context.app.digitos("enter")
        sleep(5)
        
        self.context.app.arraste_coordenada(275,86,235,687,"left",5)
        self.context.app.clica(self.SERVICOS_DE_REDES_PENDENTES,"name",2)
    
    def e_selecionar_servico_de_rede(self):
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/2018-10164.png")):
            self.context.app.clica_imagem(self.context.path+"data/images/2018-10164.png",2,"left")
        '''
        self.context.asserts.verifica_tela(self.context.path+"data/images/manobras_e_ordens.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/manobras_e_ordens.png")
        '''
        self.context.app.clica(self.MANOBRAS_E_ORDENS_DE_MANOBRA,"name",2)
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/transformador.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/transformador.png")
            
        elif(self.context.asserts.verifica_tela(self.context.path+"data/images/transforma....png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/transforma....png")
            
    def selecionar_opcao_excluir_manobra(self): 
        #self.context.asserts.verifica_tela(self.context.path+"data/images/exclusao_de_manobra.png",100)
        #self.context.app.clica_imagem(self.context.path+"data/images/exclusao_de_manobra.png")
        self.context.app.clica(self.ELIMINAR_ORDEM_DE_MANOBRA,"name",2)
    
    def concluir_exclusao_de_manobra(self):
        sleep(2)
        self.context.asserts.verifica_tela(self.context.path+"data/images/confirmar_exclusao_de_ordem_de_manobra.png",100)
        self.context.app.clica(self.OK,"name",2)
    

class Eliminar_ordem_de_Manobra_2(object):
    def __init__(self, context):
            self.context = context
            self.OK = "OK"
            
    def e_selecionar_servico_de_rede(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Redes Pendentes")
        self.context.app.digitos("enter")
        
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/carregandoBDI.png",80)!= None):
            pass
        self.context.asserts.verifica_tela(self.context.path+"data/images/2017-5582.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/2017-5582.png",2,"left")
        self.context.app.digitos("enter")
    
    def despachar_servico_de_rede_para_uma_equipe_logada(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Recursos Propostos")
        self.context.app.digitos("enter")
        
        self.context.app.arraste_coordenada(510,312,1099,305,"left",5)
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/despachadaSucesso.png",100)):
            self.context.asserts.verifica_tela(self.context.path+"data/images/ok.png",100)
            self.context.app.clica(self.OK,"name",2)
        sleep(2)
    
    def abrir_view_manobras_e_ordem_de_manobras(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Manobras e")
        self.context.app.digitos("enter")
        sleep(5)
    
    def selecionar_ordens_e_excluir(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD.png")
        self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD_2017-5582.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/viaCOD_2017-5582.png")
        self.context.app.digitos("enter")
        sleep(2)
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/transforma....png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/transforma....png")
        #self.context.asserts.verifica_tela(self.context.path+"elementosImagem/manobras_e_ordens.png",100)
        #self.context.app.clica_imagem(self.context.path+"elementosImagem/manobras_e_ordens.png")
        
        sleep(2)
        
        #self.context.asserts.verifica_tela(self.context.path+"elementosImagem/manobras_e_ordens.png",100)
        self.context.app.mantenha_e_digite("shift",["down","down","down"])
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/exclusao_de_manobra.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/exclusao_de_manobra.png")
        self.context.asserts.verifica_tela(self.context.path+"data/images/ok.png",100)
        self.context.app.clica(self.OK,"name",2)


class Eliminar_ordem_de_manobra_3(object):
    def __init__(self, context):
            self.context = context
        
    def buscar_um_servico_de_rede_finalizado(self):
        self.context.app.combo_digitos("ctrl","h")
        self.context.asserts.verifica_tela(self.context.path+"data/images/servico_rede.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/servico_rede.png")
        
        sleep(5)
        self.context.app.digitos(("tab",9))
        self.context.app.digitos("space",("right",2))
        self.context.app.escrever_direto("10")
        
        sleep(2)
        self.context.asserts.verifica_tela(self.context.path+"data/images/fechado.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/fechado.png")
        self.context.app.digitos("space","enter")
    
    def abrir_view_manobras_e_ordem_de_manobras(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Manobras e")
        self.context.app.digitos("enter")
    
    def selecionar_servico_de_rede_finalizado(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/2018-9777.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/2018-9777.png")
        self.context.app.digitos("enter")
    
    def excluir_ordem_de_manobra(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/exclusao_de_manobra_desligado.png",100)

# -*- coding: utf-8 -*-
'''
Created on 17 de dez de 2018
@author: gcruzm


'''
from time import sleep


class Eliminar_ordem_de_manobra_1(object):
    
    def __init__(self, context):
        self.context = context
        self.OK="OK"
        self.SERVICOS_DE_REDES_PENDENTES = "Serviços de Redes Pendentes"
        self.MANOBRAS_E_ORDENS_DE_MANOBRA = "Manobras e Ordens de Manobras"
        self.ELIMINAR_ORDEM_DE_MANOBRA = "Eliminar Ordem de Manobra"
    
    def abrir_view_manobras_e_ordem_de_manobras(self):
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/carregandoBDI.png",80)!= None):
            pass
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Manobras")
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/opcao_manobras_e_ordens.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/opcao_manobras_e_ordens.png")
            self.context.app.digitos("enter")
        sleep(5)
        
        self.context.app.arraste_coordenada(275,86,235,687,"left",5)
        self.context.app.clica(self.SERVICOS_DE_REDES_PENDENTES,"name",2)
    
    def e_selecionar_servico_de_rede(self):
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/2018-10164.png")):
            self.context.app.clica_imagem(self.context.path+"data/images/2018-10164.png",2,"left")
        '''
        self.context.asserts.verifica_tela(self.context.path+"data/images/manobras_e_ordens.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/manobras_e_ordens.png")
        '''
        self.context.app.clica(self.MANOBRAS_E_ORDENS_DE_MANOBRA,"name",2)
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/transformador.png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/transformador.png")
            
        elif(self.context.asserts.verifica_tela(self.context.path+"data/images/transforma....png",100)):
            self.context.app.clica_imagem(self.context.path+"data/images/transforma....png")
            
    def selecionar_opcao_excluir_manobra(self): 
        #self.context.asserts.verifica_tela(self.context.path+"data/images/exclusao_de_manobra.png",100)
        #self.context.app.clica_imagem(self.context.path+"data/images/exclusao_de_manobra.png")
        self.context.app.clica(self.ELIMINAR_ORDEM_DE_MANOBRA,"name",2)
    
    def concluir_exclusao_de_manobra(self):
        sleep(2)
        self.context.asserts.verifica_tela(self.context.path+"data/images/confirmar_exclusao_de_ordem_de_manobra.png",100)
        self.context.app.clica(self.OK,"name",2)
    

class Eliminar_ordem_de_Manobra_2(object):
    def __init__(self, context):
            self.context = context
            self.OK = "OK"
            
    def e_selecionar_servico_de_rede(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Redes Pendentes")
        self.context.app.digitos("enter")
        
        while(self.context.asserts.verifica_tela(self.context.path+"data/images/carregandoBDI.png",80)!= None):
            pass
        self.context.asserts.verifica_tela(self.context.path+"data/images/2017-5582.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/2017-5582.png",2,"left")
        self.context.app.digitos("enter")
    
    def despachar_servico_de_rede_para_uma_equipe_logada(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Recursos Propostos")
        self.context.app.digitos("enter")
        
        self.context.app.arraste_coordenada(510,312,1099,305,"left",5)
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/despachadaSucesso.png",100)):
            self.context.asserts.verifica_tela(self.context.path+"data/images/ok.png",100)
            self.context.app.clica(self.OK,"name",2)
        sleep(2)
    
    def abrir_view_manobras_e_ordem_de_manobras(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Manobras e")
        self.context.app.digitos("enter")
        sleep(5)
    
    def selecionar_ordens_e_excluir(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD.png")
        self.context.asserts.verifica_tela(self.context.path+"data/images/viaCOD_2017-5582.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/viaCOD_2017-5582.png")
        self.context.app.digitos("enter")
        sleep(2)
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/transforma....png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/transforma....png")
        #self.context.asserts.verifica_tela(self.context.path+"elementosImagem/manobras_e_ordens.png",100)
        #self.context.app.clica_imagem(self.context.path+"elementosImagem/manobras_e_ordens.png")
        
        sleep(2)
        
        #self.context.asserts.verifica_tela(self.context.path+"elementosImagem/manobras_e_ordens.png",100)
        self.context.app.mantenha_e_digite("shift",["down","down","down"])
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/exclusao_de_manobra.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/exclusao_de_manobra.png")
        self.context.asserts.verifica_tela(self.context.path+"data/images/ok.png",100)
        self.context.app.clica(self.OK,"name",2)


class Eliminar_ordem_de_manobra_3(object):
    def __init__(self, context):
            self.context = context
        
    def buscar_um_servico_de_rede_finalizado(self):
        self.context.app.combo_digitos("ctrl","h")
        self.context.asserts.verifica_tela(self.context.path+"data/images/servico_rede.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/servico_rede.png")
        
        sleep(5)
        self.context.app.digitos(("tab",9))
        self.context.app.digitos("space",("right",2))
        self.context.app.escrever_direto("10")
        
        sleep(2)
        self.context.asserts.verifica_tela(self.context.path+"data/images/fechado.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/fechado.png")
        self.context.app.digitos("space","enter")
    
    def abrir_view_manobras_e_ordem_de_manobras(self):
        self.context.app.combo_digitos("ctrl","3")
        self.context.app.escrever_direto("Manobras e")
        self.context.app.digitos("enter")
    
    def selecionar_servico_de_rede_finalizado(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/2018-9777.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/2018-9777.png")
        self.context.app.digitos("enter")
    
    def excluir_ordem_de_manobra(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/exclusao_de_manobra_desligado.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/exclusao_de_manobra_desligado.png")