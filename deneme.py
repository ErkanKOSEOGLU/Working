# Started from http://zetcode.com/gui/pysidetutorial/firstprograms/ and
# connections program from chap 4 of Summerfield's PyQt book

import sys
from PySide import QtGui


def createThingy():
    thing1 = thingy("thingName", 3, wid)
    lbl1.setText(thing1.name + " created.")
    return


def updateNum():
    lbl1.setText("number: " + str(thing1.number))

    return


class thingy(object):
    def __init__(self, name, number, mainWindow):
        self.name = name
        self.number = number

    def func1(self):
        return "Something to return"

    def rtnNum(self):
        return "Num: " + str(self.number)

app = QtGui.QApplication(sys.argv)

wid = QtGui.QWidget()
wid.resize(250, 150)
wid.setWindowTitle('Example')

btn1 = QtGui.QPushButton("Create thingy")
btn2 = QtGui.QPushButton("Number")
lbl1 = QtGui.QLabel("---")

vlayout = QtGui.QVBoxLayout()
vlayout.addWidget(btn1)
vlayout.addWidget(btn2)
vlayout.addWidget(lbl1)
wid.setLayout(vlayout)

btn1.clicked.connect(createThingy)
btn2.clicked.connect(updateNum)

wid.show()
wid.raise_()
sys.exit(app.exec_())

