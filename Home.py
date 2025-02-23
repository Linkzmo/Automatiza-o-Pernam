import getpass
import time
import schedule
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Configurar o WebDriver automaticamente
service = Service(ChromeDriverManager().install())

# Credenciais
BEEHOME_URL = "https://pernambucanas.mybeehome.com/login"
USUARIO = input("Digite sua chapa: ")
SENHA = getpass.getpass("Digite a senha do Beehome: ")

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
        #Ira selecionar a barra de chat
        campo_pesquisa = driver.find_element(By.XPATH, '/html/body/app-root/app-home/app-header/div[1]/div[1]/ul/li[1]/a')
        campo_pesquisa.click()
        time.sleep(7)
        
        #Seleciona a barra de pesquisa
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
    except Exception as e:
        print("Erro ao enviar a mensagem:", e)

    driver.quit()  # Fecha o navegador

# **Agendar a mensagem para as 9h da manhã**
schedule.every().day.at("11:05").do(enviar_mensagem)

print("Agendador iniciado...")

while True:
    schedule.run_pending()
    time.sleep(30)  # Verifica a cada 30 segundos
