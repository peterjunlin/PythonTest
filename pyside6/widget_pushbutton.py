from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PySide6.QtGui import QCloseEvent
from PySide6 import QtCore


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_gui()

    def setup_gui(self):
        btn_quit = QPushButton("Quit", self)
        QtCore.QObject.connect(btn_quit, QtCore.SIGNAL('clicked()'), self.on_btn_quit)

        self.setGeometry(100, 100, 200, 200)
        self.setWindowTitle("testing window")

        self.show()

    def on_btn_quit(self):
        self.close()

    # override
    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Confirm', 'Are you sure you want to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QApplication([])
    main_window = MyWindow()
    app.exec_()


if __name__ == '__main__':
    main()


