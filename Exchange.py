from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

app=QApplication([])



win=QWidget()
win.resize(520,520)
win.show()
win.setWindowTitle("WindiwTitle")

EnterAmountOFDolar=QLineEdit()

EnterAmountOFDolar.setPlaceholderText("Enter amount of dolar")

EnterButton=QPushButton("EXCHENGE!")

LineH=QHBoxLayout()
LineV=QVBoxLayout()
LineH.addWidget(EnterAmountOFDolar)
LineV.addLayout(LineH)
LineV.addWidget(EnterButton)

win.setLayout(LineV)
def EXCHENGE():
    Amount=EnterAmountOFDolar.text()
    if(int(Amount)<0):
        ErrorMessage=QMessageBox()
        ErrorMessage.setText("  DWQFE")
        ErrorMessage.show()
        ErrorMessage.exec_()
        
    AmountFinal=41*int(Amount)
    MoneyMessage=QMessageBox()
    MoneyMessage.setText("Сума в гривнях:"+str(AmountFinal))
    MoneyMessage.show()
    MoneyMessage.exec_()



EnterButton.clicked.connect(EXCHENGE)


app.exec_()