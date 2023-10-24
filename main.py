import sys

from PyQt6.QtWidgets import QApplication, QTextEdit, QLineEdit, QPushButton, \
    QMainWindow

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(700, 500)

        self.inp = QTextEdit(self)
        self.inp.setReadOnly(True)
        self.inp.setGeometry(10, 10, 450, 400)
        self.type = QLineEdit(self)
        self.type.setGeometry(10, 420, 450, 100)
        self.button = QPushButton("send", self)
        self.button.setGeometry(460, 420, 100, 100)



app = QApplication(sys.argv)
app1 = ChatbotWindow()
app1.show()
sys.exit(app.exec())

