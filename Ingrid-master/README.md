# Testes automatizados Ingrid
##Introdução
Repositorio para os testes automatizados do sistema Ingrid, integrando com VSTS.

##Iniciando
###Steps
1.	Certifique-se que os pré requisitos do sistema, python e Pyautomators estão configurados.
2.	Construa o arquivo de execução do Pyautomators *.yaml* 
3.	Versione o  arquivo *enviroment.py*,para orquestrar os testes da melhor forma
4.	Execute comandos na pasta raiz do projeto

## Execução dos testes
python -m Pyautomators execute -f *Caminho para uma pasta, aonde tenha um 'arquivo.yaml'*
####Dicas:
Configura para rodar os testes com os logs. 

##Executando criador de evidencia
python -m Pyautomators criar_doc