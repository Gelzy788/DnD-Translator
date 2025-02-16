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
        self.background = None

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
                  self.background[0], self.color, self.bold, self.italic)

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color = (color.red(), color.green(), color.blue())

    def load_background(self):
        self.background = QFileDialog.getOpenFileName(
            self, "Выберите фон", "data/backgrounds", "Изображения (*.png *.jpg *.jpeg)")

        if self.background[0]:  # Проверяем, что файл был выбран
            original_file_name = os.path.basename(
                self.background[0])  # Извлекаем имя файла
            destination_path = os.path.join(
                "data/backgrounds", original_file_name)  # Полный путь к новому файлу

            # Проверяем, находится ли файл в той же папке
            if os.path.dirname(self.background[0]) == os.path.dirname(destination_path):
                print(
                    "Файл не может быть сохранен в той же папке, откуда он был выбран.")
            else:
                # Проверяем, существует ли файл с таким именем
                if os.path.exists(destination_path):
                    print("Файл с таким именем уже существует. Сохранение отменено.")
                else:
                    # Копируем файл
                    shutil.copy(self.background[0], destination_path)
