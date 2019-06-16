# -*- coding: utf-8 -*-
'''
Created on 11 de jul de 2018
@author: gdiamante

Modified on 11 de dez de 2018
@author: gcruzm
'''

from time import sleep


class Criar_filtro_zonal(object):

    def __init__(self,context):
        self.context=context
        self.CRIAR = "Criar"
        self.PUBLICO = "Público:"
        self.ELEKTRO = "ELEKTRO"
        self.OK = "OK"
        self.NOME_DO_FILTRO = "Test InGrid Automation v8"
        self.DESCRICAO_DO_FILTRO = "Test InGrid Automation Filter Zonal" 
        self.EXIBIR = "Exibir filtros públicos"
    
    def clicar_alterar_o_filtro_de_area(self):
        self.context.asserts.verifica_tela(self.context.path+"/data/images/alterar_filtro_zonal.png",100)
        self.context.app.clica_imagem(self.context.path+"/data/images/alterar_filtro_zonal.png", 1, "left", similar=70)
    
    def clicar_no_botao_criar_e_preencher_dados(self):
        self.context.app.clica(self.CRIAR,"name",2) 
        self.context.app.digitos("tab")
        self.context.app.escrever_direto(self.NOME_DO_FILTRO)
        self.context.app.digitos("tab")
        self.context.app.escrever_direto(self.DESCRICAO_DO_FILTRO)
        
        self.context.app.clica(self.PUBLICO,"name",2)
        self.context.app.clica(self.ELEKTRO,"name",2)
        sleep(3)
        self.context.asserts.verifica_tela(self.context.path+"data/images/setRight.png",100)
        self.context.app.clica_imagem(self.context.path+"data/images/setRight.png")
        sleep(3)
        self.context.asserts.verifica_tela(self.context.path+"data/images/ok.png",100)
        self.context.app.clica(self.OK,"name")
    
    def verifica_filtro_zonal_aplicado(self):
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/exibirFIltrosPublicos.png",100, similaridade=70)):
            self.context.app.clica_imagem(self.context.path+"data/images/exibirFIltrosPublicos.png",1,"left", similar=60)
            self.context.app.digitos(("tab",3))
            
            self.context.app.escrever_direto(self.NOME_DO_FILTRO)
            sleep(5)
            self.context.app.clica(self.NOME_DO_FILTRO, "name", 4)
            self.context.app.digitos("tab", "down")
            self.context.app.clica_imagem(self.context.path+"data/images/botao_ok.png",1,"left")
            sleep(4)
            self.context.app.digitos("enter")
            
        elif(self.context.asserts.verifica_tela(self.context.path+"data/images/exibirFiltrosClicado.png",100, similaridade=70)):
            self.context.app.clica("Nome","name",3)
            self.context.app.digitos("down","enter")
            self.context.app.escrever_direto(self.NOME_DO_FILTRO)
            self.context.app.clica(self.NOME_DO_FILTRO, "name", 4)
            self.context.app.digitos("tab", "down")
            self.context.app.clica_imagem(self.context.path+"data/images/botao_ok.png",1,"left")
            sleep(4)
            self.context.app.digitos("enter")
            
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/filtroZonalConfigurado.png",100)
        
class Modificar_filtro_zonal(object):
    
    def __init__(self,context):
        self.context=context
        self.MODIFICAR = "Modificar"
        self.OK = "OK"
        self.TEST_INGRID_AUTOMATION_COPIA = "Test InGRID Automation Copiado"
        self.ELIMINAR = "Eliminar"
        self.PRIVADO = "Privado"
        self.EXIBIR = "Exibir filtros públicos"
        self.Filtro = "Filtro"
        self.NOME_DO_FILTRO = "Test InGrid Automation v8"
        
    def clicar_em_modificar(self):
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/exibirFIltrosPublicos.png",100)):
            self.context.app.clica(self.EXIBIR, "name", 2)
            sleep(3)
            self.context.app.digitos(("tab",3))
        
        else: 
            self.context.app.digitos(("tab",2))
       
        sleep(4)
        self.context.app.escrever_direto(self.NOME_DO_FILTRO)
        sleep(5)
        self.context.app.clica(self.Filtro, "name", 4)
        self.context.app.digitos("down")
        sleep(4)
        self.context.asserts.verifica_tela(self.context.path+"data/images/modificar_filtro_zonal.png",100)
        self.context.app.clica(self.MODIFICAR,"name",2)
    
    def preecher_dados(self):
        self.context.app.digitos("tab")
        self.context.app.combo_digitos("ctrl","a")
        self.context.app.digitos("delete")
        self.context.app.escrever_direto("Filtro Teste Automatizado")
        self.context.app.clica(self.PRIVADO, "name", 2)
        self.context.app.clica(self.OK,"name",2)
        sleep(2)
       
        
    def clica_filtro_zonal_modificado(self):
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/exibirFIltrosPublicos.png",100) == None):
            self.context.app.clica(self.EXIBIR, "name", 2)
            self.context.app.digitos(("tab",3))
            
        else: 
            self.context.app.digitos(("tab",2))
            
        self.context.app.combo_digitos("ctrl","a")
        self.context.app.escrever_direto("Filtro Teste Automatizado")
        sleep(4)
        self.context.app.clica(self.Filtro, "name", 4)
        self.context.app.digitos("down")
        self.context.app.clica(self.OK,"name",2)
        self.context.app.clica(self.OK,"name",2)
        sleep(5)
    
    def verifica_filtro_alterado(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/filtroTesteAutomatizado.png", 100)       
        
class Cria_copia_a_partir_de_um_existente(object):
    
    def __init__(self,context):
        self.context=context
        self.CRIAR_COPIA_A_PARTIR_DE_UM_FILTRO_ATUAL = "Criar Cópia a partir do filtro atual?"
        self.OK = "OK"
        self.NOME = "Nome"
        self.EXIBIR = "Exibir filtros públicos"
        self.Filtro = "Filtro"
        self.NOME_DO_FILTRO = "Test InGrid Automation v8"
        
    def flegar_criar_copia_a_partir_do_filtro(self):
        
        self.context.app.digitos("tab")
        self.context.app.combo_digitos("ctrl","a")
        self.context.app.escrever_direto(self.NOME_DO_FILTRO)
            
        
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/criar_copia_a_partir_do_filtro_atual.png",100)):
            self.context.app.clica(self.CRIAR_COPIA_A_PARTIR_DE_UM_FILTRO_ATUAL,"name",2)
            
        self.context.app.clica(self.OK,"name",2)
    
            
        sleep(5)
            
    def selecionar_filtro_copia(self):
        self.context.app.clica(self.EXIBIR, "name", 5)
        self.context.app.digitos(("tab",3))
        sleep(4)
        self.context.app.combo_digitos("ctrl","a")
        self.context.app.escrever_direto("Filtro copia")
        sleep(4)
        self.context.app.clica(self.Filtro, "name", 4)
        self.context.app.digitos("down")
        self.context.app.clica(self.OK,"name",2)
        self.context.app.clica(self.OK,"name",2)
        sleep(5)

class Eliminar_filtro_zonal(object):
    
    def __init__(self,context):
        self.context=context
        self.OK = "OK"
        self.ELIMINAR = "Eliminar"
        self.EXIBIR = "Exibir filtros públicos"
        self.Filtro = "Filtro"
        self.NOME_DO_FILTRO = "Filtro Teste Automatizado"
        
    def clicar_em_eliminar(self):
        if(self.context.asserts.verifica_tela(self.context.path+"data/images/exibirFiltrosClicado.png",100)):
            self.context.app.clica(self.Filtro,"name",2)
            self.context.app.digitos(("tab",3))
        
        else:
            self.context.app.digitos(("tab",2))
            
        sleep(4)
        self.context.app.combo_digitos("ctrl","a")
        self.context.app.escrever_direto(self.NOME_DO_FILTRO)
        sleep(3)
        self.context.app.clica(self.Filtro, "name", 4)
        self.context.app.digitos("down")
        self.context.asserts.verifica_tela(self.context.path+"data/images/eliminar_filtro_zonal.png",100)
        self.context.app.clica(self.ELIMINAR,"name",2)
        self.context.app.clica(self.OK,"name",2)
        self.context.app.clica(self.OK,"name",2)
        self.context.app.clica(self.OK,"name",2)
