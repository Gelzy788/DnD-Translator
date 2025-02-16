from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi
from translated_screen import show_text


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DnD Translator")
        loadUi('data/ui_files/main_window.ui', self)

        self.translate_btn.clicked.connect(self.translate_text)

    def translate_text(self):
        show_text(self.text_editor.toPlainText(), "InfernalFont-Regular.ttf")
