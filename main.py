from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.editor_screen import EditorScreen

class SyntaxIDE(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(EditorScreen(name='editor'))
        return sm

if __name__ == '__main__':
    SyntaxIDE().run()
