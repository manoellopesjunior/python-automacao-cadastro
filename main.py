"""
Automação de cadastro de produtos em sistema web.

Este script utiliza PyAutoGUI para automatizar o processo de:
- abrir o navegador
- acessar o sistema
- realizar login
- cadastrar produtos automaticamente a partir de um arquivo CSV.

Projeto desenvolvido durante o Intensivão de Python da Hashtag Programação.
"""

# bibliotes = pacotes de código   /pip install *****/
import pyautogui
import time
import pandas

email = "teste@gmail.com"
senha = "Teste12345?"

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

# passo a passo do meu programa
#pyautogui.click         #clica na tela
#pyautogui.write()       #escreve um texto
#pyautogui.press()       #apertar uma tecla
#pyautogui.hotkey()      #aperta um atalho de teclado (ex: ctrl + v)
#pyautogui.scroll()      #roda a tela para cima ou para baixo

pyautogui.PAUSE = 1  #toda vez que usar um comando do pyautogui, ele vai esperar 1 segundo para executar o próximo comando

# Passo 1: Entrar no sistema
#abri o navegador

pyautogui.press('win')  #aperta a tecla do windows
pyautogui.write('chrome')  #escreve o nome do navegador
pyautogui.press('enter')  #aperta enter para abrir o navegador
time.sleep(2)  #espera 2 segundos para o navegador abrir
pyautogui.write(link)      #escreve o endereço do sistema
pyautogui.press('enter')  #aperta enter para acessar o sistema
time.sleep(3)  #espera 2 segundos para o sistema carregar

# Passo 2: Fazer login
# clicar no campo de email
pyautogui.click(x=500, y=400)  #clica no campo de email (coordenadas x e y)
pyautogui.write(email)  #escreve o email
pyautogui.press('tab')  #aperta tab para ir para o campo de senha
pyautogui.write(senha)  #escreve a senha
pyautogui.press('tab')  #aperta tab para ir para o botão de login
pyautogui.press('enter')  #aperta enter para fazer login
time.sleep(2)

# Passo 3: Abrir a base de dados (importar o arquivo)   /pip install pandas openpyxl/
 
tabela = pandas.read_csv("data/produtos.csv")  #lê a tabela de produtos
print(tabela)  #mostra a tabela no terminal

for linha in tabela.index:  #para cada linha da tabela
    # Passo 4: Cadastrar 1 produto
    #codigo
    pyautogui.click(x=623, y=298)  #clica no botão de cadastrar produto (coordenadas x e y)

    codigo = str(tabela.loc[linha, "codigo"])  #escreve o código do produto
    pyautogui.write(codigo)  #escreve o código do produto
    pyautogui.press('tab')  #aperta tab para ir para o proximo campo
    #marca
    marca = str(tabela.loc[linha, "marca"])  #escreve a marca do produto
    pyautogui.write(marca)  #escreve a marca do produto
    pyautogui.press('tab')  #aperta tab para ir para o proximo campo
    #tipo
    tipo = str(tabela.loc[linha, "tipo"])  #escreve o tipo do produto
    pyautogui.write(tipo)  #escreve o tipo do produto
    pyautogui.press('tab')  #aperta tab para ir para o proximo campo
    #categoria
    categoria = str(tabela.loc[linha, "categoria"])  #escreve a categoria do produto
    pyautogui.write(categoria)  #escreve a categoria do produto
    pyautogui.press('tab')  #aperta tab para ir para o proximo campoMouse   
    #preco_unitario
    preco = str(tabela.loc[linha, "preco_unitario"])  #escreve o preço unitário do produto
    pyautogui.write(preco)  #substitui o ponto por vírgula para o sistema aceitar o valor
    pyautogui.press('tab')  #aperta tab para ir para o proximo campo
    #custo
    custo = str(tabela.loc[linha, "custo"])  #escreve o custo do produto
    pyautogui.write(custo)  #escreve o custo do produto
    pyautogui.press('tab')  #aperta tab para ir para o proximo campo
    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs == 'nan' or obs == '':  # se for NaN ou vazio
        pyautogui.press('tab')  # só vai para o próximo campo
    else:
        pyautogui.write(obs)  # escreve a observação
        pyautogui.press('tab')  # depois vai para o próximo campo

    pyautogui.press('enter')  #aperta enter para cadastrar o produto

    #voltar para o topo da página
    pyautogui.scroll(5000)  #roda a tela para cima para cadastrar o próximo produto


    

# Passo 5: Repetir o passo 4 até acabar a lista de produtos
