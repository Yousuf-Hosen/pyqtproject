import sys
from PyQt5.QtWidgets import QApplication,QWidget,QDialog
from PyQt5.QtGui import QIcon


class windowExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,600,500)# x -axis,y_axis,height,width
        self.show()



app=QApplication(sys.argv)
window=windowExample()
sys.exit(app.exec_())