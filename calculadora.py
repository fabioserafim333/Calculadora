import tkinter as tk


class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("360x560")
        self.root.resizable(False, False)
        self.root.configure(bg="#1C1C1E")

        self.expressao = ""

        # -----------------------------
        # VISOR
        # -----------------------------
        self.display = tk.Label(
            root,
            text="0",
            anchor="e",
            bg="#1C1C1E",
            fg="#FFFFFF",
            font=("Segoe UI", 38),
            padx=25
        )
        self.display.pack(fill="x", pady=(35, 20))

        # -----------------------------
        # ÁREA DOS BOTÕES
        # -----------------------------
        frame = tk.Frame(root, bg="#1C1C1E")
        frame.pack(expand=True, fill="both", padx=15, pady=10)

        botoes = [
            ("AC", 0, 0), ("±", 0, 1), ("%", 0, 2), ("÷", 0, 3),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("×", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("−", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("+", 3, 3),
            ("0", 4, 0), (".", 4, 2), ("=", 4, 3)
        ]

        for texto, linha, coluna in botoes:

            # O zero ocupa duas colunas
            if texto == "0":
                coluna_span = 2
            else:
                coluna_span = 1

            botao = tk.Button(
                frame,
                text=texto,
                font=("Segoe UI", 20),
                bd=0,
                relief="flat",
                cursor="hand2",
                command=lambda valor=texto: self.clicar(valor)
            )

            # Cores minimalistas
            if texto in ("÷", "×", "−", "+", "="):
                botao.configure(
                    bg="#FF9F0A",
                    fg="#FFFFFF",
                    activebackground="#FFB340",
                    activeforeground="#FFFFFF"
                )

            elif texto in ("AC", "±", "%"):
                botao.configure(
                    bg="#636366",
                    fg="#FFFFFF",
                    activebackground="#7A7A7E",
                    activeforeground="#FFFFFF"
                )

            else:
                botao.configure(
                    bg="#2C2C2E",
                    fg="#FFFFFF",
                    activebackground="#3A3A3C",
                    activeforeground="#FFFFFF"
                )

            botao.grid(
                row=linha,
                column=coluna,
                columnspan=coluna_span,
                sticky="nsew",
                padx=5,
                pady=5
            )

        # Faz os botões ocuparem o espaço igualmente
        for i in range(5):
            frame.rowconfigure(i, weight=1)

        for i in range(4):
            frame.columnconfigure(i, weight=1)

        # -----------------------------
        # TECLADO
        # -----------------------------
        self.root.bind("<Key>", self.teclado)

    # -----------------------------
    # CLIQUE NOS BOTÕES
    # -----------------------------
    def clicar(self, valor):

        if valor == "AC":
            self.expressao = ""
            self.atualizar_display()

        elif valor == "=":
            self.calcular()

        elif valor == "±":
            self.alternar_sinal()

        elif valor == "%":
            self.porcentagem()

        elif valor == "÷":
            self.expressao += "/"
            self.atualizar_display()

        elif valor == "×":
            self.expressao += "*"
            self.atualizar_display()

        elif valor == "−":
            self.expressao += "-"
            self.atualizar_display()

        else:
            self.expressao += valor
            self.atualizar_display()

    # -----------------------------
    # ATUALIZA O VISOR
    # -----------------------------
    def atualizar_display(self):

        if self.expressao == "":
            self.display.config(text="0")
        else:
            texto = self.expressao

            texto = texto.replace("*", "×")
            texto = texto.replace("/", "÷")
            texto = texto.replace("-", "−")

            self.display.config(text=texto)

    # -----------------------------
    # CALCULAR
    # -----------------------------
    def calcular(self):

        try:
            resultado = eval(self.expressao)

            if isinstance(resultado, float) and resultado.is_integer():
                resultado = int(resultado)

            self.expressao = str(resultado)
            self.atualizar_display()

        except:
            self.display.config(text="Erro")
            self.expressao = ""

    # -----------------------------
    # PORCENTAGEM
    # -----------------------------
    def porcentagem(self):

        try:
            resultado = eval(self.expressao) / 100

            self.expressao = str(resultado)
            self.atualizar_display()

        except:
            self.display.config(text="Erro")
            self.expressao = ""

    # -----------------------------
    # ALTERAR SINAL
    # -----------------------------
    def alternar_sinal(self):

        try:
            resultado = eval(self.expressao)

            resultado *= -1

            self.expressao = str(resultado)
            self.atualizar_display()

        except:
            pass

    # -----------------------------
    # TECLADO
    # -----------------------------
    def teclado(self, evento):

        tecla = evento.keysym

        if evento.char in "0123456789.":
            self.clicar(evento.char)

        elif evento.char == "+":
            self.clicar("+")

        elif evento.char == "-":
            self.clicar("−")

        elif evento.char == "*":
            self.clicar("×")

        elif evento.char == "/":
            self.clicar("÷")

        elif tecla == "Return":
            self.clicar("=")

        elif tecla == "Escape":
            self.clicar("AC")

        elif tecla == "BackSpace":

            self.expressao = self.expressao[:-1]
            self.atualizar_display()


# -----------------------------
# INICIAR PROGRAMA
# -----------------------------

janela = tk.Tk()

calculadora = Calculadora(janela)

janela.mainloop()
