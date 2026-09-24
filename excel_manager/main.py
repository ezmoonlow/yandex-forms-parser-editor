import sys

from PyQt5.QtWidgets import QApplication

from ui.main_window import MainWindow
from ui.styles import DARK_QSS


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(DARK_QSS)
    app.setApplicationName("Работа с анкетами")

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
