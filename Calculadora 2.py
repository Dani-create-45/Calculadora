import tkinter as tk
import math
def calcular():
    try:
        expressao = entrada.get()
        partes = expressao.split()

        if len(partes) != 3:
            entrada.delete(0, tk.END)
            entrada.insert(0, "Formato inválido")
            return

        num1 = float(partes[0])
        operador = partes[1]
        num2 = float(partes[2])

        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            if num2 == 0:
                resultado = "Erro: divisão por zero"
            else:
                resultado = num1 / num2
        else:
            resultado = "Operador inválido"

        entrada.delete(0, tk.END)
        entrada.insert(0, str(round(resultado)) if isinstance(resultado, float) else resultado)

    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

def clicar_botao(valor):
    entrada.insert(tk.END, valor)

def limpar():
    entrada.delete(0, tk.END)

janela = tk.Tk()
janela.title("Calculadora")

entrada = tk.Entry(janela, width=25, font=("Arial", 18), borderwidth=2, relief="solid")
entrada.grid(row=0, column=0, columnspan=4)

botoes = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (texto, linha, coluna) in botoes:
    if texto == "=":
        tk.Button(janela, text=texto, width=5, height=2, command=calcular).grid(row=linha, column=coluna)
    else:
        comando = lambda t=texto: clicar_botao(f" {t} " if t in "+-*/" else t)
        tk.Button(janela, text=texto, width=5, height=2, command=comando).grid(row=linha, column=coluna)

tk.Button(janela, text="C", width=22, height=2, command=limpar).grid(row=5, column=0, columnspan=4)

janela.mainloop()