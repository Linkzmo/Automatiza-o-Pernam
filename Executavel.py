from HomeV import loops
import time
import schedule

loops()
# Executa a função mensagem_indicador
# schedule.every().day.at("08:00").do(loops)
# schedule.every().day.at("10:00").do(loops)
# schedule.every().day.at("12:00").do(loops)
# schedule.every().day.at("14:00").do(loops)

print("Agendador iniciado...")

while True:
   schedule.run_pending()
   time.sleep(30)  # Verifica a cada 30 segundos