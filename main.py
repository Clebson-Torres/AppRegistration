from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import sqlite3

con = sqlite3.connect("banco_app.db")
c = con.cursor()

c.execute("""CREATE TABLE if not exists usuarios(user text, senha text)""")

con.commit()
con.close()


class TelaCadastro(Screen):
    def submit(self):
        con = sqlite3.connect("banco_app.db")
        c = con.cursor()
        app = App.get_running_app()
        tela_cadastro = app.root.get_screen('tela2')

        c.execute("INSERT INTO usuarios VALUES (:nome, :senha)",
                  {
                      'nome': tela_cadastro.ids.login1.text,
                      'senha': tela_cadastro.ids.senha1.text,
                  })

        tela_cadastro.ids.login1.text = ""
        tela_cadastro.ids.senha1.text = ""

        con.commit()
        con.close()


class TelaUsuario(Screen):
    pass


class TelaLogin(Screen):
    def __init__(self, **kw):
        super(TelaLogin, self).__init__(**kw)
        self.dialog = None
        self.a = App.get_running_app()

    def show_alert_dialog2(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Usuario não localizado, tente novamente",
                buttons=[
                    MDFlatButton(
                        text="fechar",
                        on_release=self.fechar
                    ),
                ],
            )
        self.dialog.open()

    def fechar(self, obj):
        self.dialog.dismiss()

    def set_screen(self):
        App.get_running_app().root.current = 'TelaUsuario'

    def login(self):
        con = sqlite3.connect("banco_app.db")
        c = con.cursor()
        app = App.get_running_app()
        tela_login = app.root.get_screen('tela1')
        sm = ScreenManager

        usuario = tela_login.ids.login2.text
        senha1 = tela_login.ids.senha2.text

        statement = f"SELECT user FROM usuarios WHERE user= '{usuario}' AND senha= '{senha1}';"

        c.execute(statement)
        if not c.fetchone():
            self.show_alert_dialog2()
        else:
            print("logado com sucesso")
            self.set_screen()

        tela_login.ids.login2.text = ""
        tela_login.ids.senha2.text = ""


class Windowmanager(ScreenManager):
    pass


class App(MDApp):
    dialog = None

    def build(self, **kwargs):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        kv = Builder.load_file('app.kv')
        return kv

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Usuario cadastrado com sucesso, volte a tela de Login!!",

                buttons=[
                    MDFlatButton(
                        text="fechar",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color, on_release=self.fechar
                    ),
                ],
            )
        self.dialog.open()

    def fechar(self, obj):
        self.dialog.dismiss()


App().run()
