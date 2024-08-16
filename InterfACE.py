from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

app=QApplication([])



win=QWidget()
win.resize(520,520)
win.show()
win.setWindowTitle("WindiwTitle")

EnterPassword=QLineEdit()
EnterLogin=QLineEdit()

EnterLogin.setPlaceholderText("Enter login")

EnterPassword.setPlaceholderText("Enter password")


EnterButton=QPushButton("Log in")

LineH=QHBoxLayout()
LineV=QVBoxLayout()
LineH.addWidget(EnterLogin)
LineH.addWidget(EnterPassword)
LineV.addLayout(LineH)
LineV.addWidget(EnterButton)

win.setLayout(LineV)

def CheckPassword():
    password=EnterPassword.text()
    if(len(password)<6):
        ErrorMessage=QMessageBox()
        ErrorMessage.setText("Please enter longer password than 6 characters1")
        ErrorMessage.show()
        ErrorMessage.exec_()
    else:
        ErrorMessage=QMessageBox()
        ErrorMessage.setText("correct pss pss pss")
        ErrorMessage.show()
        ErrorMessage.exec_()

EnterButton.clicked.connect(CheckPassword)

app.exec_()