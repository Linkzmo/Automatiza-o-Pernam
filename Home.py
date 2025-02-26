import getpass
import time
import schedule
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import pyperclip
import io

# Configurar o WebDriver automaticamente
service = Service(ChromeDriverManager().install())

# Credenciais
BEEHOME_URL = "https://pernambucanas.mybeehome.com/login"
USUARIO = input("Digite sua chapa: ")
SENHA = getpass.getpass("Digite a senha do Beehome: ")
SENHA_BI = getpass.getpass("Digite a senha do BI: ")

# Destinatário e mensagem
DESTINATARIO = input("Pra quem você vai enviar a mensagem? ")
MENSAGEM = input("Mensagem: ")

def enviar_mensagem():
    print("Iniciando navegador...")
    driver = webdriver.Chrome(service=service)
    driver.get(BEEHOME_URL)

    # Aguarda a página carregar
    time.sleep(5)

    # **(Caso precise de login, preenche os campos)**
    try:
        campo_email = driver.find_element(By.XPATH, '//*[@id="username"]')  # Ajuste se necessário
        campo_senha = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div[2]/div/div[1]/form/div/div[2]/div[1]/input')
        campo_email.send_keys(USUARIO + "@pernambucanas.com.br")
        campo_senha.send_keys(SENHA)
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

        # **Envia a mensagem**
        campo_mensagem = driver.find_element(By.XPATH, '//*[@id="chatInput"]')
        campo_mensagem.send_keys(MENSAGEM)
        campo_mensagem.send_keys(Keys.RETURN)

        print("Mensagem enviada com sucesso para", DESTINATARIO)
        time.sleep(3)

        # **Tira uma captura de tela**
        screenshot_path = "screenshot.png"
        driver.save_screenshot(screenshot_path)
        print(f"Captura de tela salva em {screenshot_path}")

    except Exception as e:
        print("Erro ao enviar a mensagem:", e)

    driver.quit()  # Fecha o navegador

def tirar_foto_BI():
    print("Iniciando navegador...")
    driver = webdriver.Chrome(service=service)
    driver.get('https://app.powerbi.com/groups/me/apps/412ad779-7b38-406d-adaa-d96e44193086/reports/31fc42f0-7572-449c-a8f9-857fa6342de6/ReportSection?ctid=dbc92cdb-dde7-4d1b-ab84-8b2cfaf8134b&experience=power-bi')

    # Aguarda a página carregar
    time.sleep(5)

    try:
        # Preenche o campo de email
        campo_email = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div[1]/div[2]/input')
        campo_email.send_keys(USUARIO + "@pernambucanas.com.br")
        campo_email.send_keys(Keys.RETURN)
        time.sleep(3)  # Espera o próximo passo

        # Preenche o campo de senha
        campo_senha = driver.find_element(By.XPATH, '//*[@id="i0118"]')
        campo_senha.send_keys(SENHA_BI)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(7)  # Espera o login completar

        # Caso haja um botão "Sim" para manter o login
        try:
            botao_sim = driver.find_element(By.XPATH, '//*[@id="idSIButton9"]')
            botao_sim.click()
            time.sleep(5)
        except:
            pass

    except Exception as e:
        print("Erro no login:", e)

    # **Tira uma captura de tela**
    screenshot_path = "screenshot.png"
    driver.save_screenshot(screenshot_path)
    print(f"Captura de tela salva em {screenshot_path}")

    # Copia a imagem para a área de transferência
    image = Image.open(screenshot_path)
    output = io.BytesIO()
    image.save(output, format='PNG')
    pyperclip.copy(output.getvalue())
    print("Captura de tela copiada para a área de transferência")

    # Cola a imagem (Ctrl+V)
    campo_mensagem = driver.find_element(By.XPATH, '//*[@id="chatInput"]')
    campo_mensagem.send_keys(Keys.CONTROL, 'v')
    campo_mensagem.send_keys(Keys.RETURN)

    driver.quit()  # Fecha o navegador

# **Agendar a mensagem para as 9h da manhã**
schedule.every().day.at("18:05").do(tirar_foto_BI)

print("Agendador iniciado...")

while True:
    schedule.run_pending()
    time.sleep(30)  # Verifica a cada 30 segundos