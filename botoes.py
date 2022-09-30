from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDIconButton, MDFloatingActionButton, MDRaisedButton, MDRectangleFlatButton, MDRectangleFlatIconButton

class AppUm(MDApp):
    Window.size = (300, 600)

    def build(self):
        boxLayout = MDBoxLayout(
            orientation='vertical',
            spacing=15,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        btn1 = MDFlatButton(
            text='Login',
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        btn2 = MDIconButton(
            icon="language-python",
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        btn3 = MDFloatingActionButton(
            icon="arrow-right-bold",
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        btn4 = MDRectangleFlatButton(
            text="login",
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        btn5 = MDRaisedButton(
            text="arrow",
            pos_hint={'center_x': 0.5, 'center_y': 1}
        )

        btn6 = MDRectangleFlatIconButton(
            text="arrow",
            icon="home",
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        boxLayout.add_widget(btn1)
        boxLayout.add_widget(btn2)
        boxLayout.add_widget(btn3)
        boxLayout.add_widget(btn4)
        boxLayout.add_widget(btn5)
        boxLayout.add_widget(btn6)

        return boxLayout

AppUm().run()
