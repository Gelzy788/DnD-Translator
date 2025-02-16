from PyQt6.QtWidgets import QMainWindow, QColorDialog, QFileDialog
from PyQt6.uic import loadUi
import shutil
from translated_screen import show_text
import os

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
        self.color = (255, 255, 255)

        self.translate_btn.clicked.connect(self.translate_text)
        self.color_btn.clicked.connect(self.choose_color)
        self.background_btn.clicked.connect(self.load_background)

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

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color = (color.red(), color.green(), color.blue())

    def load_background(self):
        self.background = QFileDialog.getOpenFileName(
            self, "Выберите фон", "data/backgrounds", "Изображения (*.png *.jpg *.jpeg)")

        if self.background[0]:
            existing_files = os.listdir("data/backgrounds")

            max_number = 0
            for file in existing_files:
                if file.startswith("background") and file.endswith(".png"):
                    try:
                        number = int(file[10:-4])
                        if number > max_number:
                            max_number = number
                    except ValueError:
                        continue

            new_file_name = f"background{max_number + 1}.png"
            destination_path = os.path.join("data/backgrounds", new_file_name)

        shutil.copy(self.background[0], destination_path)
