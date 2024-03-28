"""Calculadora com Pyside6/Python"""
from sys import argv
from PySide6.QtWidgets import QApplication, QLabel
from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(argv)
    window = MainWindow()
    label = QLabel('Não sei')

    label.setStyleSheet('font-size: 150px')
    window.add_widget_to_vlayout(label)
    window.adjust_fixed_size()

    window.show()
    app.exec()
