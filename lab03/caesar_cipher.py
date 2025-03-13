import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnEncrypt.clicked.connect(self.encrypt)
        self.ui.btnDecrypt.clicked.connect(self.decrypt)

    def encrypt(self):
        url = "http://127.0.0.1:5001/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.txtPlainText.toPlainText(),
            "key": self.ui.txtKey.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txtCipherText.setText(data['encrypted_message'])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Success")
                msg.exec_()
            else:
                print("Error")
        except Exception as e:
            print(e)

    def decrypt(self):
        url = "http://127.0.0.1:5001/api/caesar/decrypt"

        payload = {
            "cipher_text": self.ui.txtCipherText.toPlainText(),
            "key": self.ui.txtKey.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txtPlainText.setText(data['decrypted_text'])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Success")
                msg.exec_()
            else:
                print("Error")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
