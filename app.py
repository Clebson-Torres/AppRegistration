from kivymd.app import MDApp
from kivy.lang import Builder
import sqlite3

con = sqlite3.connect("banco_app.db")
c = con.cursor()

c.execute("""CREATE TABLE if not exists usuarios(user text, senha text)""")

con.commit()
con.close()




class App(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"

    def submit(self):
        con = sqlite3.connect("banco_app.db")
        c = con.cursor()

        c.execute("INSERT INTO usuarios VALUES (:nome, :senha)",
                  {
                      'nome': self.root.ids.login.text,
                      'senha': self.root.ids.senha.text,
                  })
        self.root.ids.label.text = f'Seja bem vindo - {self.root.ids.login.text}'

        self.root.ids.login.text = ""
        self.root.ids.senha.text = ""

        con.commit()
        con.close()

    # def login(self):
    #     if self.root.ids.login.text == "clebs" and self.root.ids.senha.text =="1234":
    #         self.root.ids.label.text = f"Seja bem vindo {self.root.ids.login.text}"
    #     else:
    #         self.root.ids.label.text = "Usuario não encontrado"


# finally, run the app
if __name__ == "__main__":
    App().run()
