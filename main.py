"""Calculadora com Pyside6/Python"""
from sys import argv
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from variables import WINDOW_ICON_PATH
from display import Display
from info import Info


if __name__ == '__main__':
    # Cria aplicação
    app = QApplication(argv)
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addToVLayout(info)

    # Display
    display = Display()
    # display.setPlaceholderText('digite algo')
    window.addToVLayout(display)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
