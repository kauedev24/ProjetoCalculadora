"""."""
import qdarktheme
from variables import (
    PRIMARY_COLOR, DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR)
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    """."""

    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # configurações
        self.definitionTheme(self.qss)
        self.widget_central = QWidget()
        self.vLayout = QVBoxLayout()
        self.widget_central.setLayout(self.vLayout)
        self.setCentralWidget(self.widget_central)

        # titulo
        self.setWindowTitle("calculadora")

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

    def qss(self):
        return f"""
        PushButton[cssClass="specialButton"] {{
                color: #fff;
                background: "{PRIMARY_COLOR}";
                }}        

        PushButton[cssClass="specialButton"]:hover {{
                color: #fff;
                background: "{DARKER_PRIMARY_COLOR}";
                }}
        PushButton[cssClass="specialButton"]:pressed {{
                color: #fff;
                background: "{DARKEST_PRIMARY_COLOR}";
                }}
        """

    def adjustFixedSize(self):
        # ultimo passo
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
