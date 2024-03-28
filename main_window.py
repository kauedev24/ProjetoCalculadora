"""."""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    """."""

    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        """initial"""

        super().__init__(parent, *args, **kwargs)

        # configurações
        self.widget_central = QWidget()
        self.v_layout = QVBoxLayout()
        self.widget_central.setLayout(self.v_layout)
        self.setCentralWidget(self.widget_central)

        # titulo
        self.setWindowTitle("calculadora")

    def adjust_fixed_size(self):
        """."""

        # ultimo passo
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def add_widget_to_vlayout(self, widget: QWidget):
        """."""

        self.v_layout.addWidget(widget)
