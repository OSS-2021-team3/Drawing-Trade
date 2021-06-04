import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer, QUrl
from mkList import mkList


class MainPage(QDialog):
    def __init__(self):
        super(MainPage,self).__init__()
        loadUi("main.ui", self)
        self.nextButton.setEnabled(False)
        self.search.clicked.connect(self.fileopen)
        self.nextButton.clicked.connect(self.gotoLoadingPage)

        global radio1
        global radio2
        radio1 = self.radioButton
        radio2 = self.radioButton2
        

    def fileopen(self):
        global filename
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File')
        self.img.setPixmap(QtGui.QPixmap(filename))
        if ((filename and self.radioButton.isChecked()) or (filename and self.radioButton2.isChecked())):
            self.nextButton.setEnabled(True)
            print(self.nextButton)

    def gotoLoadingPage(self):
        loading=LoadingPage()
        widget.addWidget(loading)
        widget.setCurrentIndex(widget.currentIndex()+1)


    
            
class LoadingPage(QDialog):
    def __init__(self):
        super(LoadingPage, self).__init__()
        loadUi("loading.ui", self)
        self.next.setEnabled(False)
        self.img.setPixmap(QtGui.QPixmap("fun.jpg"))
        self.next.clicked.connect(self.gotoResultPage)
        #self.img.setPixmap(QtGui.QPixmap(""+".png"))
        global count
        global check
        count = 0
        check = 0
        if (check == 0):
            self.start_process()
            self.next.setEnabled(True)
            

    # 타이머 시작
    def start_process(self):
        # Timer 세팅
        

        # results = [ ['KOR-DOGE',20231 ],['KOR-BTC',23434] ... ] 으로 2차원 배열 오름차순으로 되어있음

        # 유클리드 거리 유사도 매칭
        global results
        if(radio1.isChecked()):
            results = mkList(filename, 1)
        # 코사인 유사도 매칭
        elif(radio2.isChecked()):
            results = mkList(filename, 2)


    def gotoResultPage(self):
        result=ResultPage()
        widget.addWidget(result)
        widget.setCurrentIndex(widget.currentIndex()+1)
    


class ResultPage(QDialog):
    def __init__(self):
        super(ResultPage, self).__init__()
        loadUi("result.ui", self)
        self.userImage.setPixmap(QtGui.QPixmap(filename))
        self.label.setText(results[0][0])
        self.resultImage.setPixmap(QtGui.QPixmap('./datas/' + results[0][0] +'.png'))
        self.returnButton.clicked.connect(self.gotoMainPage)

        # 결과 data url : './data/' + results[0][0] +'.png' 
        # 2등결과 results[1][0]

    def gotoMainPage(self):
        main=MainPage()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)





app = QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
myWindow = MainPage()
widget.addWidget(myWindow)
widget.setFixedWidth(1028)
widget.setFixedHeight(710)
widget.show()
app.exec_()
