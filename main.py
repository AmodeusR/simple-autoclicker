import pyautogui
import keyboard
import time
from threading import Thread

# Configurações de usuário (User configurations)
atalho = "ctrl + space"
intervalo = 0.5  # Intervalo entre os cliques (em segundos)


ativo = False  # Estado inicial do auto-clicker

def auto_clicker():
    """Executa os cliques repetidos enquanto estiver ativo"""
    while True:
        if ativo:
            print("Clicando...")
            pyautogui.click()
            time.sleep(intervalo)
        time.sleep(0.05)

def toggle_auto_clicker():
    """Ativa/desativa o auto-clicker com a tecla de atalho"""
    global ativo
    ativo = not ativo
    status = "ATIVADO" if ativo else "DESATIVADO"
    print(f"Auto-clicker {status}!")

# Inicialização da thread do auto-clicker
thread_clicker = Thread(target=auto_clicker)
thread_clicker.daemon = True  # Permite que o programa feche mesmo se a thread estiver rodando
thread_clicker.start()

print(f"Pressione {atalho} para iniciar/parar. Ctrl + C para sair.")
keyboard.add_hotkey(atalho, toggle_auto_clicker)
keyboard.wait()
