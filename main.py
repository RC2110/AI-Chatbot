import sys

from PyQt6.QtWidgets import QApplication, QTextEdit, QLineEdit, QPushButton, \
    QMainWindow
from backend import ChatBot
import threading
class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.bot = ChatBot()
        self.setMinimumSize(500, 500)

        self.inp = QTextEdit(self)
        self.inp.setReadOnly(True)
        self.inp.setGeometry(10, 10, 350, 300)
        self.type = QLineEdit(self)
        self.type.setGeometry(10, 320, 350, 46)
        self.type.returnPressed.connect(self.send_msg)
        self.button = QPushButton("send", self)
        self.button.clicked.connect(self.send_msg)
        self.button.setGeometry(370, 318, 50, 50)

        self.show()

    def send_msg(self):
        user_inpt = self.type.text().strip()
        self.inp.append(f"<p style='color:#333333'> Me: {user_inpt}</p>")
        self.type.clear()

        thread= threading.Thread(target=self.bot_action, args= (user_inpt,))
        # thread.daemon = True
        thread.start()

    def bot_action(self, user_inpt):
        response = self.bot.get_response(user_inpt)
        self.inp.append(f"<p style='color:#333333; background-color:#E9E9E9'> Bot: {response}</p>")


app = QApplication(sys.argv)
app1 = ChatbotWindow()
app1.show()
sys.exit(app.exec())

