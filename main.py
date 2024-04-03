"""Calculadora com Pyside6/Python"""
from sys import argv
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from variables import WINDOW_ICON_PATH
from display import Display
from info import Info
from buttons import Button, ButtonsGrid


if __name__ == '__main__':
    # cria aplicação
    app = QApplication(argv)
    window = MainWindow()

    # define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # info
    info = Info('')
    window.addWidgetToVLayout(info)

    # display
    display = Display()
    # display.setPlaceholderText('digite algo')
    window.addWidgetToVLayout(display)

    buttonsGrid = ButtonsGrid(display, info)
    window.vLayout.addLayout(buttonsGrid)

    # executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()

    # buttonsGrid.addWidget(Button('1'), 0, 0)
    # buttonsGrid.addWidget(Button('2'), 0, 1)
    # buttonsGrid.addWidget(Button('3'), 0, 2)
    # buttonsGrid.addWidget(Button('/'), 0, 3)
    # buttonsGrid.addWidget(Button('4'), 1, 0)
    # buttonsGrid.addWidget(Button('5'), 1, 1)
    # buttonsGrid.addWidget(Button('6'), 1, 2)
    # buttonsGrid.addWidget(Button('*'), 1, 3)
    # buttonsGrid.addWidget(Button('7'), 2, 0)
    # buttonsGrid.addWidget(Button('8'), 2, 1)
    # buttonsGrid.addWidget(Button('9'), 2, 2)
    # buttonsGrid.addWidget(Button('-'), 2, 3)
    # buttonsGrid.addWidget(Button('0'), 3, 0)
    # buttonsGrid.addWidget(Button('='), 3, 1, 1, 2)
    # buttonsGrid.addWidget(Button('+'), 3, 3)
