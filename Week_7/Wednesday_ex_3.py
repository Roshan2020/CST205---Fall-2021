##############################################################################################################
# Layout code sample
##############################################################################################################
import sys
from PySide2.QtWidgets import (QWidget,QApplication, QLabel,QVBoxLayout)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.label1 = QLabel('Label 1', self)
        self.label2 = QLabel('Label 2', self)
        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        self.setLayout(vbox)
        self.setGeometry(100,100,600,400)
        self.show()

app = QApplication([])
ex = Example()
app.exec_()