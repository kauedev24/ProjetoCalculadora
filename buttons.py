""" . """
import math
from typing import TYPE_CHECKING
from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber


# checagem -> True
# executando -> False
if TYPE_CHECKING:
    from display import Display
    from info import Info


class Button(QPushButton):
    """ estilo dos botões"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        font.setBold(True)
        self.setMinimumSize(75, 75)
        self.setFont(font)


class ButtonsGrid(QGridLayout):
    """ grid+botões """

    def __init__(
            self, display: 'Display', info: 'Info', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # lista dos caracteres
        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self._equation = ''
        self.equationInitialValue = 'Sua conta'
        self._left = None  # primeiro número -> esquerda
        self._right = None  # segundo número -> direita
        self._operator = None  # operador aritmético
        self.equation = self.equationInitialValue
        self._makeGrid()

    # getter e setter

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        """ inserindo os botões na grid """
        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)

                # estilo para os caracteres especiais -> não números
                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty("cssClass", "specialButton")
                    self._configSpecialButton(button)

                self.addWidget(button, i, j)
                slot = self._makeSlot(self._insertButtonTextDisplay, button)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        """ conecta o clique com o caractere """
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        """ encontra os caracteres especiais e define suas funções """
        text = button.text()

        if text == 'C':
            slot = self._makeSlot(self._clear)
            self._connectButtonClicked(button, slot)

        if text == '◀':
            slot = self._makeSlot(self.display.backspace)
            self._connectButtonClicked(button, slot)

        if text in '-+*/^':
            slot = self._makeSlot(self._arithmeticOperators, button)
            self._connectButtonClicked(button, slot)

        if text in '=':
            self._connectButtonClicked(button, self._result)

    def _makeSlot(self, func, *args, **kwargs):
        """ recebe o clique e qual o caractere """
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextDisplay(self, button):
        """ encontra qual é o caractere(numeros) ao clicar """
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return
        self.display.insert(buttonText)

    def _clear(self):
        self._left = None
        self._right = None
        self._operator = None
        self.equation = self.equationInitialValue
        self.display.clear()

    def _arithmeticOperators(self, button):
        buttonText = button.text()  # +-*/
        displayText = self.display.text()  # número da esquerda
        self.display.clear()  # limpa o display

        # se não tem número da esquerda o botão não faz nada -> return
        if not isValidNumber(displayText) and self._left is None:
            return

        if self._left is None:
            self._left = float(displayText)

        self._operator = buttonText
        self.equation = f'{self._left} {self._operator} ??'

    def _result(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        self._right = float(displayText)
        self.equation = f'{self._left} {self._operator} {self._right}'
        result = 'error'

        try:
            if '^' in self.equation and isinstance(self._left, float):
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            print('Zero Division Error')
        except OverflowError:
            print('Numero muito grande')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None

        if result == 'error':
            self._left = None
