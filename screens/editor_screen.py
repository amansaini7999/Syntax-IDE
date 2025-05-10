from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from kivy.uix.label import Label
from pygments.lexers import PythonLexer
from runners.python_runner import run_python_code

class EditorScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        self.code_input = CodeInput(lexer=PythonLexer(), font_size=40)
        layout.add_widget(self.code_input)

        self.output_label = Label(text="", size_hint_y=0.3, font_size=40)
        layout.add_widget(self.output_label)

        run_button = Button(text='Run', size_hint_y=None, height=50)
        run_button.bind(on_press=self.run_code)
        layout.add_widget(run_button)

        self.add_widget(layout)

    def run_code(self, *args):
        code = self.code_input.text
        output = run_python_code(code)
        self.output_label.text = output