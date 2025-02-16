# build.py
import os
import sys
from PyInstaller.__main__ import run

if __name__ == '__main__':
    # Определяем пути
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(current_dir, 'src')
    data_dir = os.path.join(current_dir, 'data')

    # Опции для PyInstaller
    options = [
        '--name=DnD_Translator',  # Имя выходного файла
        '--onefile',              # Создать один исполняемый файл
        '--windowed',             # Окно без консоли
        '--icon=data/program_icon.ico',   # Иконка приложения
        # Добавляем папку backgrounds
        '--add-data={};data/backgrounds'.format(
            os.path.join(data_dir, 'backgrounds')),
        # Добавляем папку fonts
        '--add-data={};data/fonts'.format(os.path.join(data_dir, 'fonts')),
        # Добавляем папку ui_files
        '--add-data={};data/ui_files'.format(
            os.path.join(data_dir, 'ui_files')),
        os.path.join(src_dir, 'main.py')  # Файл запуска
    ]

    # Запускаем PyInstaller
    run(options)
