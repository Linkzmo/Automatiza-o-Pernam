import getpass
import os
import time
import schedule
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import dados
from Home3 import mensagem_indicador
import pyautogui
import win32clipboard
import io

# Criar o caminho dinâmico usando `os.getenv('USERNAME')`
# chromedriver_path = r"C:\Users\{}\AppData\Local\SeleniumBasic\chromedriver.exe".format(os.getenv('USERNAME'))

# Criar um serviço com o caminho do ChromeDriver
service = Service('C:/Users/marce/OneDrive/Área de Trabalho/chrome-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Credenciais
BEEHOME_URL = "https://pernambucanas.mybeehome.com/login"


# Destinatário e mensagem
DESTINATARIO = "anot"
MENSAGEM = "SEGUE MAPA DE PRODUÇÃO"

def mensagem_obeya2():
    print("Iniciando navegador...")
    driver = webdriver.Chrome(service=service)
    driver.get('https://app.powerbi.com/groups/me/apps/412ad779-7b38-406d-adaa-d96e44193086/reports/31fc42f0-7572-449c-a8f9-857fa6342de6/b2efb1d2ea0ebbd43807?ctid=dbc92cdb-dde7-4d1b-ab84-8b2cfaf8134b&experience=power-bi')

    # Aguarda a página carregar
    time.sleep(5)

    try:
        # Preenche o campo de email
        campo_email = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div[1]/div[2]/input')
        campo_email.send_keys(dados.USUARIO + "@pernambucanas.com.br")
        campo_email.send_keys(Keys.RETURN)
        time.sleep(7)  # Espera o próximo passo

        # Preenche o campo de senha
        campo_senha = driver.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input')
        campo_senha.send_keys(dados.SENHA_BI)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(15)  # Espera o login completar

        # Serve para acessar o botão de tela cheia
        try:
            botao_sim = driver.find_element(By.XPATH, '/html/body/div[1]/root/mat-sidenav-container/mat-sidenav-content/tri-shell-panel-outlet/tri-item-renderer-panel/tri-extension-panel-outlet/mat-sidenav-container/mat-sidenav-content/div/div/div[2]/tri-shell/tri-item-renderer/tri-extension-page-outlet/div[2]/report/exploration-container/div/div/docking-container/div/div/div/section/app-bar/div/div[3]/button[3]/mat-icon[1]')
            botao_sim.click()
            time.sleep(5)

            botao_sim = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/div/div/button[1]')
            botao_sim.click()
            time.sleep(5)
        except:
            pass

    except Exception as e:
        print("Erro no login:", e)

    # Captura a tela inteira
    screenshot = pyautogui.screenshot()

    # Converte a imagem para um objeto de bytes no formato BMP
    img_byte_arr = io.BytesIO()
    screenshot.save(img_byte_arr, format='BMP')  # Salva como BMP
    img_byte_arr = img_byte_arr.getvalue()[14:]  # Remove o cabeçalho BMP (os primeiros 14 bytes)

    # Coloca a imagem na área de transferência usando a API do Windows
    def copy_image_to_clipboard(image_bytes):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, image_bytes)
        win32clipboard.CloseClipboard()

    # Chama a função para copiar a imagem para a área de transferência
    copy_image_to_clipboard(img_byte_arr)
    time.sleep(7)

    driver.quit()  # Fecha o navegador
    time.sleep(7)

    print("Iniciando navegador...")
    driver = webdriver.Chrome(service=service)
    driver.get(BEEHOME_URL)
    
        # Aguarda a página carregar
    time.sleep(5)
    
        # **(Caso precise de login, preenche os campos)**
    try:
            campo_email = driver.find_element(By.XPATH, '//*[@id="username"]')  # Ajuste se necessário
            campo_senha = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div[2]/div/div[1]/form/div/div[2]/div[1]/input')
            campo_email.send_keys(dados.USUARIO + "@pernambucanas.com.br")
            campo_senha.send_keys(dados.SENHA)
            campo_senha.send_keys(Keys.RETURN)
            time.sleep(7)  # Espera o login completar
    except Exception as e:
            print("Erro no login:", e)

    # **Acessar o chat e procurar o destinatário**
    try:
            # Ira selecionar a barra de chat
            campo_pesquisa = driver.find_element(By.XPATH, '/html/body/app-root/app-home/app-header/div[1]/div[1]/ul/li[1]/a')
            campo_pesquisa.click()
            time.sleep(7)
            
            # Seleciona a barra de pesquisa
            campo_pesquisa = driver.find_element(By.XPATH, '/html/body/app-root/app-home/ng-sidebar-container/div/div/app-chat/div[1]/div/div/div/div[1]/div/div[1]/div/div[1]/div/div/input')
            campo_pesquisa.send_keys(DESTINATARIO)
            time.sleep(5)

            # Seleciona o contato
            contato = driver.find_element(By.XPATH, '//*[@id="1831"]/div[2]'.format(DESTINATARIO))
            contato.click()
            time.sleep(5)

            # Cola a imagem
            pyautogui.hotkey('ctrl', 'v')
            print("Captura de tela copiada para a área de transferência")
            time.sleep(3)

            # **Envia a mensagem**
            campo_mensagem = driver.find_element(By.XPATH, '/html/body/app-root/app-home/ng-sidebar-container/div/div/app-chat/div[3]/div/div/div/div[3]/textarea')
            campo_mensagem.send_keys(MENSAGEM)
            time.sleep(3)
            campo_de_envio = driver.find_element(By.XPATH, '/html/body/app-root/app-home/ng-sidebar-container/div/div/app-chat/div[3]/div/div/div/div[3]/button')
            campo_de_envio.click()
            time.sleep(3)

            print("Mensagem enviada com sucesso para", DESTINATARIO)
            time.sleep(3)

    except Exception as e:
            print("Erro ao enviar a mensagem:", e)

    driver.quit()
    mensagem_indicador()
    # Fecha o navegador
    
# **Agendar a mensagem para as 9h da manhã**
# schedule.every().day.at("18:57").do(mensagem_obeya2)

# print("Agendador iniciado...")

# while True:
#     schedule.run_pending()
#     time.sleep(30)  # Verifica a cada 30 segundos