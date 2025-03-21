import getpass
import time
import os
import schedule
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import dados
from Home import mensagem_obeya
import pyautogui
import win32clipboard
import io

# Criar o caminho dinâmico usando `os.getenv('USERNAME')`
# chromedriver_path = r"C:\Users\{}\AppData\Local\SeleniumBasic\chromedriver.exe".format(os.getenv('USERNAME'))

# # Criar um serviço com o caminho do ChromeDriver
# service = Service(chromedriver_path)
# driver = webdriver.Chrome(service=service)

# Credenciais
# BEEHOME_URL = "https://pernambucanas.mybeehome.com/login"


# Destinatário e mensagem
# DESTINATARIO = "Anotações"
# MENSAGEM = "Segue projeção Separação"

def loops():
   mensagem_obeya() 
    
# **Agendar a mensagem para as 9h da manhã**
# schedule.every().day.at("18:57").do(mensagem_obeya2)

# print("Agendador iniciado...")

# while True:
#     schedule.run_pending()
#     time.sleep(30)  # Verifica a cada 30 segundos