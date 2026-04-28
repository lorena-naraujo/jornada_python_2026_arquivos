# bibliotecas = pacotes de códigos prontos


# Instalar e importar o pyautogui(pip install pyautogui)
import pyautogui

# Importar o time (já vem instalado com o python)
import time 

# Pausa de x segundos para dar tempo de executar cada comando,e não travar o computador
pyautogui.PAUSE = 0.5

# Variável com o link do sistema da empresa
link_sistema = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Passo a passo de como automatizar o cadastro de produtos

#Passo 1:entrar no sistema
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.sleep(5)

# Redirecionar para o link do sistema
pyautogui.write(link_sistema)
pyautogui.press("enter")

#fazer uma pausa para a página carregar
pyautogui.sleep(5)

#Passo 2:fazer login
pyautogui.click(x=602, y=471) #posicionar o mouse no campo de login
pyautogui.write("guriadohacking@gmail.com") #escrever o login
pyautogui.press("tab") #ir para o campo de senha
pyautogui.write("H@ck&7WQ[") #escrever a senha
pyautogui.press("tab") #ir para o botão de login
pyautogui.press("enter") #clicar no botão de login

#fazer uma pausa para o sistema carregar
pyautogui.sleep(2)

#Passo 3:abrir a base de dados (importar o arquivo)
# Instalar e importar o pandas openpyxl (pip install pandas) 
# Obs: openpyxl é necessário para ler arquivos excel 
import pandas as pd

tabela_produtos = pd.read_csv("../produtos.csv") #ler a tabela de produtos
print(tabela_produtos) #mostrar a tabela de produtos

for linha in tabela_produtos.index: #para cada linha na tabela de produtos
    #Passo 4:cadastrar 1 produto
    pyautogui.click(x=618, y=327) #clicar no campo de codigo do produto

    #codigo do produto
    codigo = str(tabela_produtos.loc[linha, "codigo"])
    pyautogui.write(codigo) #escrever o código do produto
    pyautogui.press("tab") #ir para o próximo campo

    # marca
    marca = str(tabela_produtos.loc[linha, "marca"])
    pyautogui.write(marca) 
    pyautogui.press("tab") 

    # tipo
    tipo = str(tabela_produtos.loc[linha, "tipo"])
    pyautogui.write(tipo) 
    pyautogui.press("tab") 

    # categioria
    categoria = str(tabela_produtos.loc[linha, "categoria"])
    pyautogui.write(categoria) 
    pyautogui.press("tab") 

    # preco
    preco = str(tabela_produtos.loc[linha, "preco_unitario"])
    pyautogui.write(preco) 
    pyautogui.press("tab") 

    # custo
    custo = str(tabela_produtos.loc[linha, "custo"])
    pyautogui.write(custo) 
    pyautogui.press("tab") 

    # obs
    obs = str(tabela_produtos.loc[linha, "obs"])
   

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab") #ir para o botão de enviar

    pyautogui.press("enter") #clicar no botão de enviar

    #voltar para o início da tela
    pyautogui.scroll(5000)

#Passo 5:repetir o passo 4 mais até acabar a lista de produtos

