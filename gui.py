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
        

    def fileopen(self):
        global filename
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File')
        self.img.setPixmap(QtGui.QPixmap(filename))
        if (filename):
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

        self.img.setPixmap(QtGui.QPixmap(""+".png"))
        global count
        count = 0
        self.start_process()



    def addValue(self):
        self.count += 1
        return self.count   

    # progress 화면에 표시
    def timer_prog(self):

        self.addValue(self)

        # ProgressBar의 값이 최대값 이상 Timer를 중지
        if count >= 10000():
            self.timeVar.stop()        

    


    # 타이머 시작
    def start_process(self):
        # Timer 세팅
        self.timeVar = QTimer()
        self.timeVar.setInterval(100)
        self.timeVar.timeout.connect(self.timer_prog)
        self.timeVar.start()

        # results = [ ['KOR-DOGE',20231 ],['KOR-BTC',23434] ... ] 으로 2차원 배열 오름차순으로 되어있음

        # 유클리드 거리 유사도 매칭
        file_url = QUrl.fromLocalFile(filename)
        global results
        if MainPage.radioButton.isChecked():
            results = mkList(file_url,1)

        # 코사인 거리 유사도 매칭    
        elif MainPage.radioButton2.isChecked():
            results = mkList(file_url,2)
        
        self.gotoResultPage()
        


    def gotoResultPage(self):
        result=ResultPage()
        widget.addWidget(result)
        widget.setCurrentIndex(widget.currentIndex()+1)
    


class ResultPage(QDialog):
    def __init__(self):
        super(ResultPage, self).__init__()
        loadUi("result.ui", self)
        self.userImage.setPixmap(QtGui.QPixmap(filename))
        self.resultImage.setPixmap(QtGui.QPixmap('./data/' + results[0][0] +'.png'))
        self.returnButton.clicked.connect(self.gotoMainPage)

        # 결과 data url : './data/' + results[0][0] +'.png' 
        # 2등결과 results[1][0]

    def gotoMainPage(self):
        widget.setCurrentIndex(widget.currentIndex()-2)





app = QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
myWindow = MainPage()
widget.addWidget(myWindow)
widget.setFixedWidth(839)
widget.setFixedHeight(727)
widget.show()
app.exec_()