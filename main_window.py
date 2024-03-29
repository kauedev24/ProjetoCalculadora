"""."""
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    """."""

    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # configurações
        self.widget_central = QWidget()
        self.vLayout = QVBoxLayout()
        self.widget_central.setLayout(self.vLayout)
        self.setCentralWidget(self.widget_central)

        # titulo
        self.setWindowTitle("calculadora")

    def adjustFixedSize(self):
        # ultimo passo
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
