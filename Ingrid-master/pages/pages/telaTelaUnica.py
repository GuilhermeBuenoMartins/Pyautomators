# -*- coding: utf-8 -*-
'''
Created on 6 de dez de 2018

@author: vgama
'''
from time import sleep
from lxml import etree as ET

class TelaUnica(object):

    def __init__(self, context):

        self.context = context
        
    def abrir_soap(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/soap.png",80)
        self.context.app.clica_imagem(self.context.path+"data/images/soap.png", 1, "left", similar=60)
        
    def abrir_metodo_getOutageById(self):
        sleep(5)
        self.context.app.clica_imagem(self.context.path+"data/images/soapTelaUnica.png", 1, "left", similar=70)
        self.context.app.digitos(("right",2))
        self.context.app.clica_imagem(self.context.path+"data/images/getOutageById.png", 1, "left", similar=60)
        sleep(2)
        self.context.app.digitos(("right",2),"enter")
        sleep(3)
        
        
    def preenche_id_telaUnica(self):
        self.context.app.clica_imagem(self.context.path+"data/images/campoIdSoap.png",2,"left",similar=40)
        self.context.app.escrever_direto("36368408")
        self.context.app.clica_imagem(self.context.path+"data/images/executarSoap.png", 1, "left", similar=80)
        sleep(3)
        
        #self.context.app.digitos(("tab",24),"up")
        #self.context.app.clica_imagem(self.context.path+"data/images/opcaoXMLSoap.png", 1, "left", similar=80)
        sleep(3)
        #self.context.app.combo_digitos("ctrl","s")
        #self.context.app.escrever_direto("teste.xml")
        #self.context.app.clica_imagem(self.context.path+"data/images/saveXML.png", 1, "left", similar=80)
        
    def verificacao_xml(self):
        '''
        tree = ET.parse('teste.xml')
        root = tree.getroot()
        
        for child in root.iter('result'):    
            valor = child.text            
            resultado = int(valor)
            assert resultado == 0            
        '''
        self.context.app.clica_imagem(self.context.path+"data/images/ajustarTelaSOAP.png", 1, "left")
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/responseSOAP.png", 70)
        self.context.app.clica_imagem(self.context.path+"data/images/responseSOAP.png", 1, "left")
        self.context.app.clica_imagem(self.context.path+"data/images/opcaoXMLSoap.png", 1, "left", similar=80)
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/resultadoXMLTelaUnica.png", 80, similaridade=80)
            
     
    def preenche_uc_telaUnica(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/requestSOAP.png", 80)
        self.context.app.clica_imagem(self.context.path+"data/images/campoIdSoap.png",2,"left",similar=40)
        self.context.app.escrever_direto("1143980")
        self.context.asserts.verifica_tela(self.context.path+"data/images/requestSOAP.png", 80)
        self.context.app.clica_imagem(self.context.path+"data/images/executarSoap.png", 1, "left", similar=80)
        sleep(3)
        
        
    def abrir_metodo_getCallsByCustomer(self):
        self.context.app.clica_imagem(self.context.path+"data/images/soapTelaUnica.png", 1, "left", similar=80)
        self.context.app.digitos(("right",2))
        self.context.app.clica_imagem(self.context.path+"data/images/opcaoCallsByCustomer.png", 1, "left", similar=80)
        sleep(2)
        self.context.app.digitos(("right",2),"enter")
        sleep(3)
        
    def abrir_metodo_getOutagesByCustomer(self):
        self.context.app.clica_imagem(self.context.path+"data/images/soapTelaUnica.png", 1, "left", similar=80)
        self.context.app.digitos(("right",2))
        self.context.app.clica_imagem(self.context.path+"data/images/getOutagesByCustomer.png", 1, "left", similar=80)
        sleep(2)
        self.context.app.digitos(("right",2),"enter")
        sleep(3)
        
    def preenche_campo_uc_telaUnica(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/requestSOAP.png", 80)    
        self.context.app.clica_imagem(self.context.path+"data/images/campoIdSoap.png", 2,"left",similar=40)
        self.context.app.escrever_direto("9102434")
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/requestSOAP.png", 80)
        self.context.app.clica_imagem(self.context.path+"data/images/executarSoap.png", 1, "left", similar=80)
        sleep(3)
        
    def abrir_metodo_getCallByLabel(self):
        self.context.app.clica_imagem(self.context.path+"data/images/soapTelaUnica.png", 1, "left", similar=80)    
        self.context.app.digitos(("right",5),"enter")
    
        sleep(3)
        
    def preenche_campo_rotulo_telaUnica(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/requestSOAP.png", 80)
        self.context.app.clica_imagem(self.context.path+"data/images/campoIdSoap.png", 3,"left",similar=40)
        self.context.app.escrever_direto("2015-146221")
        self.context.app.clica_imagem(self.context.path+"data/images/executarSoap.png", 1, "left", similar=80)
        sleep(3)
        
    def abrir_metodo_insertTroubleCall(self):
        self.context.app.clica_imagem(self.context.path+"data/images/soapTelaUnica.png", 1, "left", similar=80)
        self.context.app.digitos(("right",2))
        self.context.app.clica_imagem(self.context.path+"data/images/insertTroubleCall.png", 1, "left", similar=80)
        sleep(2)
        self.context.app.digitos(("right",2),"enter")
        sleep(3)
        
    def preencher_campos_insertTroubleCall(self):
        
        self.context.app.clica_imagem(self.context.path+"data/images/campoUC.png", 2, "left", similar=40)
        self.context.app.escrever_direto("39654605") #UC
        
        self.context.app.clica_imagem(self.context.path+"data/images/callerName.png", 2, "left", similar=40)
        self.context.app.escrever_direto("ADRIELI VITOR") #name
        
        self.context.app.clica_imagem(self.context.path+"data/images/phone.png", 2, "left", similar=40)
        self.context.app.escrever_direto("81758213") #fone
        
        self.context.app.clica_imagem(self.context.path+"data/images/vizinhanca.png", 2, "left", similar=40)
        self.context.app.escrever_direto("397") #vizinhan�a
        
        self.context.app.clica_imagem(self.context.path+"data/images/endereco.png", 3, "left", similar=40)
        self.context.app.escrever_direto("RUA ABILIO ZANCA, 571") #endereco
        
        self.context.app.clica_imagem(self.context.path+"data/images/cidade.png", 2, "left", similar=40)
        self.context.app.escrever_direto("LEME") #cidade
        
        self.context.app.clica_imagem(self.context.path+"data/images/estadoSoap.png", 2, "left", similar=40)
        self.context.app.escrever_direto("1") #estado
        
        self.context.app.clica_imagem(self.context.path+"data/images/location.png", 2, "left", similar=40)
        self.context.app.escrever_direto("1") #location
        
        self.context.app.clica_imagem(self.context.path+"data/images/condicaoClima.png", 2, "left", similar=40)
        self.context.app.escrever_direto("A") #condicao de tempo
        
        self.context.app.clica_imagem(self.context.path+"data/images/callOrigin.png", 2, "left", similar=40)
        self.context.app.escrever_direto("1") #callOrigin
        
        self.context.app.clica_imagem(self.context.path+"data/images/callType.png", 2, "left", similar=40)
        self.context.app.escrever_direto("FORN") #tipo
        
        self.context.app.clica_imagem(self.context.path+"data/images/callSubType.png", 2, "left", similar=40)
        self.context.app.escrever_direto("FE01") #subtipo
        
        self.context.app.digitos(("down",13))
        sleep(4)
        
        self.context.app.clica_imagem(self.context.path+"data/images/informacaoImportante.png", 2, "left", similar=40)
        self.context.app.escrever_direto("N") #informacao importante
                
        self.context.app.clica_imagem(self.context.path+"data/images/receiveDate.png", 3, "left", similar=40)
        self.context.app.escrever_direto("11/02/2019 09:45:28") #receive data
        
        self.context.app.clica_imagem(self.context.path+"data/images/scheduleDate.png", 3, "left", similar=40)
        self.context.app.escrever_direto("15/03/2010 12:21:10") # data final
        
        self.context.app.clica_imagem(self.context.path+"data/images/deathRisk.png", 2, "left", similar=40)
        self.context.app.escrever_direto("N") #risco de morte
        
        self.context.app.clica_imagem(self.context.path+"data/images/confirmTroubleCall.png", 2, "left", similar=40)
        self.context.app.escrever_direto("N") #TroubeCall
        
        self.context.app.clica_imagem(self.context.path+"data/images/confirmProcess.png", 2, "left", similar=40)
        self.context.app.escrever_direto("N") #Process
        
        self.context.app.clica_imagem(self.context.path+"data/images/executarSoap.png", 1, "left", similar=40)
        sleep(10)
        
    def abrir_metodo_getCustomerSituation(self):
        self.context.app.clica_imagem(self.context.path+"data/images/soapTelaUnica.png", 1, "left", similar=80)
        self.context.app.digitos(("right",2))
        self.context.app.clica_imagem(self.context.path+"data/images/getCustomerSituation.png", 1, "left", similar=80)
        sleep(2)
        self.context.app.digitos(("right",2),"enter")
        sleep(3)
          
        
    def verifica_customer_situation(self):
        self.context.app.clica_imagem(self.context.path+"data/images/ajustarTelaSOAP.png", 1, "left")
        
        self.context.asserts.verifica_tela(self.context.path+"data/images/responseSOAP.png", 70)
        self.context.app.clica_imagem(self.context.path+"data/images/responseSOAP.png", 1, "left")
        
        self.context.app.clica_imagem(self.context.path+"data/images/opcaoXMLSoap.png", 1, "left", similar=80)
        self.context.asserts.verifica_tela(self.context.path+"data/images/resultadoCustomerSituation.png",80)
    
    
    ''' Historical Process GMT '''
    def abrir_metodo_historicalProcessGMT(self):
        self.context.app.clica_imagem(self.context.path+"data/images/soapTelaUnica.png", 1, "left", similar=80)
        self.context.app.digitos(("right",2))
        self.context.app.clica_imagem(self.context.path+"data/images/historicalProcessGMT.png", 1, "left", similar=80)
        sleep(2)
        self.context.app.digitos(("right",2),"enter")
        sleep(3)
        
        
    def preenche_campo_uc_gmt(self):
        self.context.asserts.verifica_tela(self.context.path+"data/images/requestSOAP.png", 80)
        self.context.app.clica_imagem(self.context.path+"data/images/campoIdSoap.png", 2,"left",similar=40)
        self.context.app.escrever_direto("35032049")
        self.context.app.clica_imagem(self.context.path+"data/images/executarSoap.png", 1, "left", similar=80)
        sleep(3)
        
    ''' Inclusao de Pedido '''
        
    def abrir_metodo_insertClientRequest(self):
        self.context.app.clica_imagem(self.context.path+"data/images/soapTelaUnica.png", 1, "left", similar=80)
        self.context.app.digitos(("right",2))
        self.context.app.clica_imagem(self.context.path+"data/images/insertClientRequest.png", 1, "left", similar=80)
        sleep(2)
        self.context.app.digitos(("right",2),"enter")
        sleep(3)
        
    def preencher_dados_pedido(self):
        self.context.app.clica_imagem(self.context.path+"data/images/orderRequest.png", 2, "left", similar=40 )
        self.context.app.escrever_direto("Penha seu gostoso")
        sleep(10)