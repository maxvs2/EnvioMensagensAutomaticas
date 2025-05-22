import tkinter as tk
import pyautogui
import pygetwindow as gw
import threading
import time

rodando = [False]

def enviar_mensagens(mensagem, intervalo):
    try:
        janela = gw.getWindowsWithTitle("Discord")[0]  # Detecta a janela do Discord
        janela = gw.getWindowsWithTitle("programa")[0]  # Detecta a janela do programa
        janela.activate()
        time.sleep(1)  # Aguarda a janela ativar

        while rodando[0]:
            pyautogui.typewrite(mensagem)
            pyautogui.press('enter')
            print("Mensagem enviada.")
            time.sleep(intervalo)

    except IndexError:
        print("Janela do Discord não encontrada. Abra o Discord antes de iniciar.")
        print("Janela do Programa não encontrada. Abra o programa antes de iniciar.")

def iniciar():
    mensagem = entrada_mensagem.get()
    try:
        intervalo = int(entrada_intervalo.get())
    except ValueError:
        print("Intervalo inválido. Use apenas números.")
        return

    rodando[0] = True
    threading.Thread(target=enviar_mensagens, args=(mensagem, intervalo), daemon=True).start()
    log.insert(tk.END, "Bot iniciado.\n")

def parar():
    rodando[0] = False
    log.insert(tk.END, "Bot parado.\n")

# Interface gráfica
janela = tk.Tk()
janela.title("Bot de Mensagens Discord")
janela.title("Bot de Mensagens programa")

tk.Label(janela, text="Mensagem:").pack()
entrada_mensagem = tk.Entry(janela, width=40)
entrada_mensagem.pack()

tk.Label(janela, text="Intervalo (segundos):").pack()
entrada_intervalo = tk.Entry(janela)
entrada_intervalo.pack()

tk.Button(janela, text="Iniciar", command=iniciar, bg="green", fg="white").pack(pady=5)
tk.Button(janela, text="Parar", command=parar, bg="red", fg="white").pack(pady=5)

log = tk.Text(janela, height=10, width=50)
log.pack(pady=5)

janela.mainloop()
