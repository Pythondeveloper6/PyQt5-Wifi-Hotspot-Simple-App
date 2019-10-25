__author__ = 'Mahmoud Ahmed'
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
from os import path
import os , time
from os import *


FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"main.ui"))


class main(QMainWindow,FORM_CLASS):
    def __init__(self,parent=None):
        super(main,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.run_flash()
        self.button()
        self.run_flash()


    def run_flash(self):
        ##flash
        self.movie_screen = QLabel()
        self.movie_screen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)        
        self.movie_screen.setAlignment(Qt.AlignCenter) 
        self.verticalLayout.addWidget(self.movie_screen)
        self.setLayout(self.verticalLayout) 
        self.movie = QMovie("network.gif", QByteArray(), self) 
        self.movie.setCacheMode(QMovie.CacheAll) 
        self.movie.setSpeed(100) 
        self.movie_screen.setMovie(self.movie) 


    def button(self):
        # self.connect(self.pushButton, SIGNAL("clicked()"), self.create_button_clicked)
        self.pushButton.clicked.connect(self.create_button_clicked)

    def create_button_clicked(self):
        if self.pushButton.text() == 'Create Hotspot':
            self.start()
            self.create_wifi()

        elif self.pushButton.text() == 'Stop Hotspot':
            self.stop()


    def start(self):
        self.movie.start()
        self.pushButton.setText('Stop Hotspot')
        
    def stop(self):
        self.movie.stop()
        self.pushButton.setText('Create Hotspot')
        os.popen("netsh wlan stop hostednetwork")

        

    def create_wifi(self):
        os.system("cls")
        wifi_name = self.lineEdit.text()
        string = self.lineEdit_2.text()
        if string=="":
            string="Hotspot"
        if len(string)<8:
            print (" String must be longer than 8 chars")
        os.popen("netsh wlan set hostednetwork mode=allow ssid={} key={}".format(wifi_name,string))
        os.popen("netsh wlan start hostednetwork")
        print('Done')

    def minimize(self):
        self.setWindowFlags(self.windowFlags()|Qt.WindowMinimizeButtonHint |
        Qt.WindowSystemMenuHint)


def main_app():
    app = QApplication(sys.argv)
    window = main()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main_app()







