from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import pdfutils

titolo="It\\'s Easy to Make PDF - IEMP "
versione="0.1"
author="https://danieleporcaripython.blogspot.com - Porcari Daniele"
desc="Simple PDF maker open source written in Pyhton.\nYou can charge all you want images(.png) and text files (.txt) and XLS files\n"
sostieni="You can support me with donation on my crypto asset"

class MainApp(App):

    def build(self):
        main_layout = BoxLayout(orientation="vertical")
        hlay_g_big=GridLayout(cols=1,rows=4)
        hlay_g=GridLayout(cols=2,rows=2)
        self.etTitle = Label(text='Title',size_hint=(.2,.2))
        hlay_g.add_widget(self.etTitle)
        self.tit = TextInput(multiline=False, readonly=False, font_size=20, size_hint=(.8,.2))
        hlay_g.add_widget(self.tit)
        self.et = Label(text='subTitle',size_hint=(.2,.2))
        hlay_g.add_widget(self.et)
        self.st = TextInput(multiline=False, readonly=False, font_size=20,size_hint=(.8,.2))
        hlay_g.add_widget(self.st)
        hlay_g_big.add_widget(hlay_g)
        hlay_g=GridLayout(cols=2,rows=1)
        self.etL=Label(text='Lista',size_hint=(.2,.2))
        hlay_g.add_widget(self.etL)
        self.lista = TextInput(multiline=True, readonly=False, font_size=20,size_hint=(.8,.2))
        hlay_g.add_widget(self.lista)
        hlay_g_big.add_widget(hlay_g)
        button=Button(text="make",size_hint=(0.2,0.2))
        button.bind(on_press=self.on_button_press)
        hlay_g_big.add_widget(button)
        self.iter = TextInput(text="PRONTO",multiline=False, readonly=True, font_size=20,size_hint=(.8,.2))
        hlay_g_big.add_widget(self.iter)
        main_layout.add_widget(hlay_g_big)
        return main_layout


    def on_button_press(self, instance):
        titolo=self.tit.text
        sottotitolo=self.st.text
        orientazione='P'
        lista=self.lista.text
        self.iter.text="ATTENDI - ELABORAZIONE IN CORSO"
        pdfutils.elabora(titolo,sottotitolo,orientazione,lista)
        self.iter.text="ESEGUITO - PRONTO"

if __name__ == "__main__":
    app = MainApp()
    app.run()
