""" definições main """
import qdarktheme
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMessageBox
from variables import (
    PRIMARY_COLOR, DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR)


class MainWindow(QMainWindow):
    """."""

    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # configurações
        self.widget_central = QWidget()
        self.vLayout = QVBoxLayout()
        self.definitionTheme(self.qss())
        self.widget_central.setLayout(self.vLayout)
        self.setCentralWidget(self.widget_central)

        # titulo
        self.setWindowTitle("calculadora")

    # tema
    def definitionTheme(self, qss):
        qdarktheme.setup_theme(
            theme='dark',
            custom_colors={
                "[dark]": {
                    "primary": f"{PRIMARY_COLOR}"
                }
            },
            additional_qss=f'{qss}'
        )

    # stilo dos botões
    def qss(self):
        return f"""
        QPushButton[cssClass="specialButton"] {{
                color: #fff;
                background: "{PRIMARY_COLOR}";
                }}        
        QPushButton[cssClass="specialButton"]:hover {{
                color: #fff;
                background: "{DARKER_PRIMARY_COLOR}";
                }}
        QPushButton[cssClass="specialButton"]:pressed {{
                color: #fff;
                background: "{DARKEST_PRIMARY_COLOR}";
                }}
        """

    def adjustFixedSize(self):
        # ultima definição
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)
