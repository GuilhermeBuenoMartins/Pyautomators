'''
Created on 21 de mai de 2018
    
@author: gdiamante
'''
from Pyautomators.Runner_Pyautomators import orquestrador
from Pyautomators import Ambiente
Ambiente.irDiretorio(Ambiente.path_atual(False))
path=Ambiente.path_atual()
orquestrador(path+'data/run.yaml')
