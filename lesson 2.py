from kivy.config import Config
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout


Config.set('graphics','resizeble',0)
Config.set('graphics','width',400)
Config.set('graphics','height',500)

class CalculatorApp(App):
    def update_label(self):
        self.lbl.text=self.formula
    def add_num(self, instance):

        self.formula +=str(instance.text)
        self.update_label()

    def add_op(self, instance):
        if (str(instance.text).lower()== "x"):
            self.formula+='*'
        else:
            self.formula +=str(instance.text)
        self.update_label()
    def res(self,instance):
        self.lbl.text= str(eval(self.lbl.text))
        self.formula = ""



    def build(self):
        self.formula =''
        bl = BoxLayout(orientation = 'vertical', padding =25)
        gl = GridLayout(cols=4, spacing =3, size_hint =(1, .7))

        self.lbl = Label(text= '0',halign= 'right', font_size = 40, size_hint =(1,.6), text_size=(400-50,500*.4-50) )
        bl.add_widget(self.lbl)

        gl.add_widget(Button(text="7",on_press = self.add_num))
        gl.add_widget(Button(text="8",on_press = self.add_num))
        gl.add_widget(Button(text="9", on_press = self.add_num))
        gl.add_widget(Button(text="X",on_press = self.add_op))

        gl.add_widget(Button(text="4",on_press = self.add_num))
        gl.add_widget(Button(text="5",on_press = self.add_num))
        gl.add_widget(Button(text="6",on_press = self.add_num))
        gl.add_widget(Button(text="-",on_press = self.add_op))

        gl.add_widget(Button(text="1",on_press = self.add_num))
        gl.add_widget(Button(text="2",on_press = self.add_num))
        gl.add_widget(Button(text="3",on_press = self.add_num))
        gl.add_widget(Button(text="+",on_press = self.add_op))

        gl.add_widget(Button(text="/",on_press = self.add_op))
        gl.add_widget(Button(text="0",on_press = self.add_num))
        gl.add_widget(Button(text=",",on_press = self.add_num))
        gl.add_widget(Button(text="=",on_press = self.res))

        bl.add_widget(gl)
        return bl

if __name__=="__main__":
    CalculatorApp().run()