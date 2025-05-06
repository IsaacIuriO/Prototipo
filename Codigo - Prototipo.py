# Código - Protótipo

import customtkinter as ctk
import time
import threading

    #CONFIGURAÇÃO

#aparência
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Protótipo no CTK - Economia de Energia")
root.geometry("800x500")

    #FUNÇÕES

def esconder():
    ctk.set_appearance_mode("Dark")

    Lsub.pack_forget()
    Ldescanso.pack(pady=10)
    Lconfig.pack_forget()

    EMinutos.pack_forget() 

    BExp1.pack_forget()
    BExp2.pack_forget()
    BExp3.pack_forget()
    BMain1.pack_forget()
    BConfig.pack_forget()
    BDefinir.pack_forget()
    LResult.pack_forget()
    BMain2.pack(pady=20)

def aparecer():
    ctk.set_appearance_mode("Light")

    Lsub.pack(pady=15)
    Ldescanso.pack_forget()
    Lconfig.pack_forget()

    EMinutos.pack_forget()

    BExp1.pack(pady=10)
    BExp2.pack(pady=10)
    BExp3.pack(pady=10)
    BMain1.pack(pady=50)
    BConfig.pack(pady=0)
    BDefinir.pack_forget()
    LResult.pack_forget()
    BMain2.pack_forget()

def configurar():
    ctk.set_appearance_mode("Dark")

    Lsub.pack_forget()
    Ldescanso.pack_forget()
    Lconfig.pack(pady=10)

    EMinutos.pack(pady=10)

    BExp1.pack_forget()
    BExp2.pack_forget()
    BExp3.pack_forget()
    BMain1.pack_forget()
    BConfig.pack_forget()
    BDefinir.pack(pady=10)
    LResult.pack(pady=10)
    BMain2.pack(pady=20)

def timer():
    try:
        minutos = int(EMinutos.get())

        if minutos >= 1:
            while minutos > 0:
                resultado.set(f"Tempo restante: {minutos} minutos")
                time.sleep(60)
                minutos -= 1
                print(minutos)
            esconder()
        else:
            resultado.set(f"Tempo restante: Menos de 1 minuto")

    except:
        resultado.set("Erro!")

def timer_start():
    thread = threading.Thread(target=timer)
    thread.start()

    #ELEMENTOS

Lsub=ctk.CTkLabel(root,text="Computador Pessoal", font=("Arial", 20, "bold"))
Lsub.pack(pady=15)

Ldescanso=ctk.CTkLabel(root, text="Em Descanso...")
Ldescanso.pack_forget()

Lconfig=ctk.CTkLabel(root, text="Digite o tempo restante para seu computador ter um descanso")
Lconfig.pack_forget()

BExp1=ctk.CTkButton(root, text="Tarefas")
BExp1.pack(pady=10)

BExp2=ctk.CTkButton(root, text="Horário")
BExp2.pack(pady=10)

BExp3=ctk.CTkButton(root, text="Terminal")
BExp3.pack(pady=10)

BMain1=ctk.CTkButton(root, text="DARKNESS", command=esconder)
BMain1.pack(pady=50)

BMain2=ctk.CTkButton(root, text="VOLTAR", command=aparecer)
BMain2.pack_forget()

BConfig=ctk.CTkButton(root, text="CONFIGURAÇÕES", command=configurar)
BConfig.pack(pady=0)

BDefinir=ctk.CTkButton(root, text="Definir Timer", command=timer_start)
BDefinir.pack_forget()

EMinutos=ctk.CTkEntry(root, placeholder_text="Digite o tempo em minutos", width=200)
EMinutos.pack_forget()

#váriavel resultado
resultado = ctk.StringVar()

# rótulo para resultado
LResult=ctk.CTkLabel(root, textvariable=resultado, font=("Arial", 16, "bold"))
LResult.pack_forget()

    #INICIAR
root.mainloop()
