import customtkinter as ctk
from pyswip import Prolog

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Recomendações de Filmes")
        self.geometry("400x350")

        self.label_genre = ctk.CTkLabel(self, text="Escolha um gênero:")
        self.label_genre.pack(pady=5)

        self.generos = ["drama", "acao", "crime", "fantasia"]
        self.genero_var = ctk.StringVar(value=self.generos[0])
        self.genero_menu = ctk.CTkOptionMenu(self, variable=self.genero_var, values=self.generos)
        self.genero_menu.pack(pady=5)

        self.label_subgenre = ctk.CTkLabel(self, text="Escolha uma subcategoria:")
        self.label_subgenre.pack(pady=5)

        self.subcategorias = {
            "drama": ["prisao", "mafia", "guerra", "vida_real"],
            "acao": ["super_heroi", "mente", "policial", "ficcao_cientifica", "epico"],
            "crime": ["gangster", "mafia", "serial_killer", "policial", "assalto"],
            "fantasia": ["aventura", "magia", "guerra", "ficcao_cientifica"]
        }

        self.subgenre_var = ctk.StringVar(value=self.subcategorias[self.generos[0]][0])
        self.subgenre_menu = ctk.CTkOptionMenu(self, variable=self.subgenre_var, values=self.subcategorias[self.generos[0]])
        self.subgenre_menu.pack(pady=5)

        self.recomendar_button = ctk.CTkButton(self, text="Recomendar Filme", command=self.recomendar_filme)
        self.recomendar_button.pack(pady=10)

        self.resultado_label = ctk.CTkLabel(self, text="")
        self.resultado_label.pack(pady=5)

        self.prolog = Prolog()
        self.prolog.consult("filmes.pl")

    def recomendar_filme(self):
        genero = self.genero_var.get()
        subcategoria = self.subgenre_var.get()
        query = f"recomenda('{genero}', '{subcategoria}', Filme)"
        try:
            filmes = list(self.prolog.query(query))
        except Exception as e:
            self.resultado_label.configure(text=f"Erro na consulta Prolog: {e}")
            return

        if filmes:
            filme = filmes[0]['Filme']
            self.resultado_label.configure(text=f"Recomendação: {filme}")
        else:
            self.resultado_label.configure(text="Nenhuma recomendação disponível.")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = App()
    app.mainloop()
