import customtkinter as ctk
from tkinter import messagebox
import random

ctk.set_appearance_mode('dark')

class JogoAdivinhacao:
    def __init__(self, root):
        self.root = root
        self.root.title('Jogo da Adivinhação')
        self.root.geometry('600x800')
        self.numeroSecreto = random.randint(1, 101)
        self.chance = 0
        self.maxChances = 0
        self.tentativas = set()

        self.placaLabel = ctk.CTkLabel(self.root, text='Jogo da Adivinhação', font=('Times New Roman', 35, 'italic'))
        self.placaLabel.pack(pady=20)

        self.nomeJogador = ctk.CTkEntry(self.root, placeholder_text='Insira seu nome...', width=250)
        self.nomeJogador.pack(pady=12)
        self.dificuldadeLabel = ctk.CTkLabel(self.root, text='Escolha uma dificuldade', font=('Times New Roman', 17, 'italic'))
        self.dificuldadeLabel.pack()
        self.dificuldadeEscolhida = ctk.StringVar()
        self.dificuldadeCombobox = ctk.CTkComboBox(self.root, variable=self.dificuldadeEscolhida, values=['Fácil', 'Médio', 'Difícil'], width=250)
        self.dificuldadeCombobox.pack(pady=8)
        self.dificuldadeCombobox.configure(state='readonly')
        self.dificuldadeCombobox.set('Selecione uma opção...')
        self.iniciarButton = ctk.CTkButton(self.root, text='Iniciar Jogo', command=self.iniciarJogo, width=175, font=('Times New Roman', 15, 'bold'))
        self.iniciarButton.pack(pady=8)
        self.resultadoLabel = ctk.CTkLabel(self.root, text='', font=('Times New Roman', 17, 'italic'))
        self.resultadoLabel.pack(pady=8)

    def iniciarJogo(self):
        self.nome = self.nomeJogador.get()
        if len(self.nome) > 15:
            messagebox.showerror('Erro', 'O nome não pode ter mais de 15 caracteres')
            self.nomeJogador.delete(0, ctk.END)
            return
        
        dificuldade = self.dificuldadeEscolhida.get()

        self.tentativas.clear()

        if not self.nome or not dificuldade:
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
        
        if dificuldade == 'Fácil':
            self.maxChances = 15
        elif dificuldade == 'Médio':
            self.maxChances = 10
        else:
            self.maxChances = 5

        self.chances = self.maxChances
        self.resultadoLabel.configure(text=f'Olá, {self.nome}! Você tem {self.chances} chances para adivinhar o número secreto entre 1 e 100')
        self.numeroSecreto = random.randint(1, 101)
        self.nomeJogador.configure(state='disabled')
        self.dificuldadeCombobox.configure(state='disabled')
        self.iniciarButton.configure(state='disabled')
        self.adicionarInterface()

    def adicionarInterface(self):
        self.tentativaEntry = ctk.CTkEntry(self.root, placeholder_text='Insira um número...', width=120)
        self.tentativaEntry.pack(pady=10)
        self.tentativaButton = ctk.CTkButton(self.root, text='Tentar', command=self.verificarNumero, width=175, font=('Times New Roman', 15, 'bold'))
        self.tentativaButton.pack(pady=5)

    def limparInterface(self):
        self.tentativaEntry.delete(0, ctk.END)
        self.tentativaEntry.configure(state='normal')

        self.resultadoLabel.configure(text='')

        self.iniciarButton.configure(state='normal')
        self.nomeJogador.configure(state='normal')
        self.dificuldadeCombobox.configure(state='readonly')

        self.tentativaButton.destroy()
        self.tentativaEntry.destroy()

        self.tentativas.clear()

        self.nomeJogador.focus_set()

    def verificarNumero(self):
        try:
            tentativa = int(self.tentativaEntry.get())

            if  tentativa < 0:
                messagebox.showerror('Erro', 'O número não pode ser negativo')
                self.tentativaEntry.delete(0, ctk.END)
                return

            if 1 > tentativa > 100:
                messagebox.showerror('Erro', 'O número deve estar entre 1 e 100')
                self.tentativaEntry.delete(0, ctk.END)
                return
            
            if tentativa in self.tentativas:
                messagebox.showerror('Erro', 'Você já tentou esse número')
                self.tentativaEntry.delete(0, ctk.END)
                return
            else:
                self.tentativas.add(tentativa)

            self.chances -= 1
            if tentativa < self.numeroSecreto:
                resultado = f'Tente um número maior. Você tem {self.chances} chances restantes.'
                self.tentativaEntry.delete(0, ctk.END)
            elif tentativa > self.numeroSecreto:
                resultado = f'Tente um número menor. Você tem {self.chances} chances restantes.'
                self.tentativaEntry.delete(0, ctk.END)
            else:
                resultado = f'Parabéns, {self.nome}! Você acertou o número {self.numeroSecreto} em {self.maxChances - self.chances} tentativas.'

                self.tentativaButton.configure(state='disabled')

                self.limparInterface()

            if self.chances <= 0 and tentativa != self.numeroSecreto:
                resultado = f'Você perdeu! O número secreto era {self.numeroSecreto}'

                self.tentativaEntry.configure(state='disabled')
                self.tentativaButton.configure(state='disabled')
                self.limparInterface()
            
            self.resultadoLabel.configure(text=resultado)

        except ValueError:
            messagebox.showerror('Erro', 'Insira um número inteiro')
            self.tentativaEntry.delete(0, ctk.END)
            return
        

        if self.chances <= 0 or tentativa == self.numeroSecreto:
            self.nomeJogador.configure(state='normal')
            self.dificuldadeCombobox.configure(state='readonly')
            self.iniciarButton.configure(state='normal')

            if tentativa != self.numeroSecreto:
                self.resultadoLabel.configure(text=f'Você perdeu! O número secreto era {self.numeroSecreto}')

    def iniciarInterface(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = ctk.CTk()
    jogo = JogoAdivinhacao(root)
    jogo.iniciarInterface()
