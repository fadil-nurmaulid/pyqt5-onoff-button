#on_off button

import sys, os
from PyQt5.QtWidgets import (QApplication, QPushButton, 
                            QWidget, QHBoxLayout, QLabel)
from PyQt5.QtGui import QIcon

class Lamp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("On_Off Button")
        icon_path = os.path.join(os.path.dirname(__file__), "Icon.jpg")
        self.setWindowIcon(QIcon(icon_path))
        self.setFixedSize(340, 100)
        
        self.button = QPushButton("", self)
        self.label = QLabel("OFF", self)
        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout()
        hbox.addWidget(self.button)
        hbox.addWidget(self.label)

        self.setLayout(hbox)
        
        self.setStyleSheet("""
        QPushButton, QLabel{
            padding: 5px;
        }
        QPushButton{
            font-size: 60px;
            background-color: green;                                  
        }
        QLabel{
            font-size: 55px;
            font-weight: bold;
            font-family: Arial;
            background-color: gray;
        }                          
    """)

        self.lamp_on = False
        self.button.clicked.connect(self.toggle)

    def toggle(self):
        self.lamp_on = not self.lamp_on
        
        if self.lamp_on:
            self.button.setStyleSheet("background-color: red;")
            self.label.setStyleSheet("background-color: yellow;")
            self.label.setText("ON")

        else:
            self.button.setStyleSheet("background-color: green;") 
            self.label.setStyleSheet("background-color: gray;")
            self.label.setText("OFF")       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    lamp_app = Lamp()
    lamp_app.show()
    sys.exit(app.exec_())