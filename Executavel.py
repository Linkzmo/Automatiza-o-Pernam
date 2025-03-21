from HomeV import loops
import time
import schedule

# Chama as funções uma vez
loops()

# Exemplo de agendamento (comentado)
# schedule.every().day.at("08:00").do(mensagem_indicador)
# schedule.every().day.at("10:00").do(mensagem_indicador2)

print("Agendador iniciado...")

# Mantém o script em execução para agendamentos
while True:
    schedule.run_pending()
    time.sleep(1)