from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi
from translated_screen import show_text

languages_dict = {
    "Эльфийский": "rellanic",
    "Дварфийский": "davek",
    "Драконий": "iokharic",
    "Инфернальный": "infernal",
    "Небесный": "celestial",
    "Великаний": "dethek",
    "Услов. обозначения Арфистов": "harpers",
}


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DnD Translator")
        loadUi('data/ui_files/main_window.ui', self)

        self.bold = False
        self.italic = False

        self.translate_btn.clicked.connect(self.translate_text)

    def translate_text(self):
        if self.bold_checkbox.isChecked():
            self.bold = True
        else:
            self.bold = False
        if self.italic_checkbox.isChecked():
            self.italic = True
        else:
            self.italic = False
        show_text(self.text_editor.toPlainText(),
                  languages_dict[self.language_list.currentText()],
                  self.bold, self.italic)
