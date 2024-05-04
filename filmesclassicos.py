import tkinter as tk
from tkinter import messagebox
import random
import webbrowser

class Noh:
    def __init__(self, titulo, diretor, link):
        self.titulo = titulo
        self.diretor = diretor
        self.link = link
        self.proximo = None
        self.sugerido = False

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def adicionar(self, titulo, diretor, link):
        if not self.cabeca:
            self.cabeca = Noh(titulo, diretor, link)
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = Noh(titulo, diretor, link)

    def filme_aleatorio(self):
        atual = self.cabeca
        filmes_nao_sugeridos = []
        while atual:
            if not atual.sugerido:
                filmes_nao_sugeridos.append(atual)
            atual = atual.proximo
        if filmes_nao_sugeridos:
            escolhido = random.choice(filmes_nao_sugeridos)
            escolhido.sugerido = True
            return escolhido.titulo, escolhido.diretor, escolhido.link
        else:
            return None, None, None
        
        

def popular_filmes(lista):
    filmes = [
        ('Cidadão Kane (1941)', 'Orson Welles', 'https://www.youtube.com/'),
        ('Tempos Modernos (1936)', 'Charlie Chaplin', 'https://www.youtube.com/'),
        ('O Poderoso Chefão (1972)', 'Francis Ford Coppola', 'https://www.youtube.com/'),
        ('A Procura da Felicidade (2006)', 'Gabriele Muccino', 'https://www.youtube.com/'),
        ('Forrest Gump (1994)', 'Winston Groom', 'https://www.youtube.com/'),
        ('Clube da Luta  (1999)', 'David Fincher', 'https://www.youtube.com/'),
        ('Laranja Mecânica (1971)', 'Stanley Kubrick', 'https://www.youtube.com/'),
        ('Dora, a Aventureira (2023)', 'James Bobin', 'https://www.youtube.com/watch?v=tpT2Se8iSgU'),
        ('Pulp Fiction (1994)', 'Quentin Tarantino', 'https://www.youtube.com/'),
        ('2001: Uma Odisseia no Espaço (1968)', 'Stanley Kubrick', 'https://www.youtube.com/'),
        ('O Rei Leão (1994)', 'Roger Allers e Rob Minkoff', 'https://www.youtube.com/'),
        ('Django Livre (2012)', 'Quentin Tarantino', 'https://www.youtube.com/'),
        ('Cães de Aluguel (1992)', 'Quentin Tarantino', 'https://www.youtube.com/'),
        ('Up  Altas Aventuras (2009)', 'Pete Docter', 'https://www.youtube.com/'),
        ('A Lista de Schindler (1993)', 'Steven Spielberg', 'https://www.youtube.com/'),
       
    ]
    for titulo, diretor, link in filmes:
        lista.adicionar(titulo, diretor, link)

class AplicativoRecomendadorFilmes:
    def __init__(self, master):
        self.master = master
        master.title("Recomendador de Filmes Clássicos para Assistir Antes de Morrer")

        self.lista_filmes = ListaEncadeada()
        popular_filmes(self.lista_filmes)

        self.botao_sugerir = tk.Button(master, text="Sugerir Filme Clássico para Assistir Antes de Morrer", command=self.sugerir_filme_aleatorio)
        self.botao_sugerir.pack()

        self.botao_adicionar = tk.Button(master, text="Adicionar Filme", command=self.adicionar_filme)
        self.botao_adicionar.pack()

        self.botao_encerrar = tk.Button(master, text="Encerrar", command=self.encerrar_programa)
        self.botao_encerrar.pack()

        self.rotulo_filme = tk.Label(master, text="")
        self.rotulo_filme.pack()

        self.rotulo_link = tk.Label(master, text="", fg="blue", cursor="hand2")
        self.rotulo_link.pack()
        self.rotulo_link.bind("<Button-1>", lambda e: self.abrir_link(self.link_atual))
        
        self.botao_ver_todos_os_filmes = tk.Button(master, text="Ver Todos os Filmes", command=self.ver_todos_os_filmes)
        self.botao_ver_todos_os_filmes.pack()


    def sugerir_filme_aleatorio(self):
        titulo, diretor, link = self.lista_filmes.filme_aleatorio()
        if titulo:
            self.rotulo_filme.config(text=f"{titulo} dirigido por {diretor}")
            self.rotulo_link.config(text="Clique aqui para assistir")
            self.link_atual = link
        else:
            messagebox.showinfo("Erro", "Nenhum filme disponível. Adicione filmes ou feche o aplicativo.")

    def adicionar_filme(self):
        janela_adicionar = tk.Toplevel(self.master)
        janela_adicionar.title("Adicionar Filme")

        tk.Label(janela_adicionar, text="Título:").grid(row=0, column=0)
        tk.Label(janela_adicionar, text="Diretor:").grid(row=1, column=0)
        tk.Label(janela_adicionar, text="Link:").grid(row=2, column=0)

        entrada_titulo = tk.Entry(janela_adicionar)
        entrada_diretor = tk.Entry(janela_adicionar)
        entrada_link = tk.Entry(janela_adicionar)

        entrada_titulo.grid(row=0, column=1)
        entrada_diretor.grid(row=1, column=1)
        entrada_link.grid(row=2, column=1)

        botao_adicionar = tk.Button(janela_adicionar, text="Adicionar", command=lambda: self.adicionar_filme_lista(entrada_titulo.get(), entrada_diretor.get(), entrada_link.get()))
        botao_adicionar.grid(row=3, columnspan=2)

    def adicionar_filme_lista(self, titulo, diretor, link):
        if titulo and diretor and link:
            self.lista_filmes.adicionar(titulo, diretor, link)
            messagebox.showinfo("Sucesso", "Filme adicionado à lista com sucesso.")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    def abrir_link(self, link):
        webbrowser.open(link)

    def encerrar_programa(self):
        self.master.destroy()
        
    def ver_todos_os_filmes(self):
        janela_ver_filmes = tk.Toplevel(self.master)
        janela_ver_filmes.title("Todos os Filmes")

        texto = tk.Text(janela_ver_filmes, width=50, height=20)
        texto.pack()

        atual = self.lista_filmes.cabeca
        while atual:
            texto.insert(tk.END, f"{atual.titulo} - Dirigido por {atual.diretor}\n")
            atual = atual.proximo

        texto.config(state=tk.DISABLED)

if __name__ == '__main__':
    root = tk.Tk()
    app = AplicativoRecomendadorFilmes(root)
    root.mainloop()

