import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QWidget
from PyQt5 import QtCore

#class giao diện
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #màn hình window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 200)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Khung nhap lieu
        self.txtdisplay = QLineEdit(self.centralwidget)
        self.txtdisplay.setGeometry(QtCore.QRect(50, 50, 200, 30))
        self.txtdisplay.setObjectName("txtdisplay")

        #Nút để bấm
        self.btclick = QPushButton(self.centralwidget)
        self.btclick.setGeometry(QtCore.QRect(50, 100, 200, 30))
        self.btclick.setObjectName("btclick")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hiển thị tên"))
        self.btclick.setText(_translate("MainWindow", "Hiển thị"))


#class xử lí
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btclick.clicked.connect(self.display_text)
        
        #label của kết quả nhập liệu
        self.output_label = QLabel(self.centralWidget())
        self.output_label.setGeometry(50, 150, 300, 30)

    def display_text(self):
        input_text = self.ui.txtdisplay.text()
        self.output_label.setText(f"Tên của bạn là: {input_text}")

def main():
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()