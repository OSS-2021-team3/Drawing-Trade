import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.uic import loadUi
from mkList import mkList, refreshDatas


class MainPage(QDialog):
    def __init__(self):
        super(MainPage,self).__init__()
        loadUi("main.ui", self)
        self.nextButton.setEnabled(False)

        #Loading페이지에서 선택한 알고리즘에 따라 종목 추천을 하기 위해 사용
        global radio1
        global radio2
        radio1 = self.radioButton
        radio2 = self.radioButton2

        #버튼 활성화 비활성화를 위한 변수 및 함수
        check = 0
        self.initCheck()
        
        #찾아보기 버튼을 클릭하면, 파일 오픈 함수를 호출
        self.search.clicked.connect(self.fileopen)    
        
        #유클리드 거리 유사도 매칭 알고리즘 선택
        self.radioButton.clicked.connect(self.checkButton)
        
        #코사인 유사도 매칭 알고리즘 선택
        self.radioButton2.clicked.connect(self.checkButton)
        
        #next버튼 클릭 후 다음 페이지로 
        self.nextButton.clicked.connect(self.gotoLoadingPage)

    def initCheck(self):
        self.check = 0
    def checkButton(self):
        #찾아보기를 먼저하고 radiobutton을 누르는 경우
        if (self.check == 1):
            self.nextButton.setEnabled(True)

    def fileopen(self):
        global filename
        
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', './', '*.png')
        self.img.setPixmap(QtGui.QPixmap(filename))
        #radiobutton을 누르고 찾아보기를 누르는 경우
        if (filename):
            self.check = 1
            print(self.check)  
            if (self.radioButton.isChecked() or self.radioButton2.isChecked()):
                self.nextButton.setEnabled(True)


    def gotoLoadingPage(self):
        loading=LoadingPage()
        widget.addWidget(loading)
        widget.setCurrentIndex(widget.currentIndex()+1)


    
            
class LoadingPage(QDialog):
    def __init__(self):
        super(LoadingPage, self).__init__()
        loadUi("loading.ui", self)
        #self.img.setPixmap(QtGui.QPixmap(""+".png")) 
        self.img.setPixmap(QtGui.QPixmap("fun.jpg"))
        #start button 클릭 후 작업 진행
        self.start.clicked.connect(self.start_process)
        

        # 처음 실행 시, data를 받아옴
        if (widget.currentIndex() == 0):
            #next 버튼 비활성화
            self.next.setEnabled(False)

        # 처음 실행 하는 것이 아니면, data 받아오는 것을 선택적으로 실행 가능 
        else:
            #start 버튼 비활성화
            self.start.setEnabled(False)
            #Data 클리어
            self.clear.clicked.connect(self.clearData)
            
        #next button 클릭 후 결과 페이지로 이동
        self.next.clicked.connect(self.gotoResultPage)

    def clearData(self):
        self.start.setEnabled(True)
        self.next.setEnabled(False)
        
    def start_process(self):
        # data 클리어
        refreshDatas()
        # results = [ ['KOR-DOGE',20231 ],['KOR-BTC',23434] ... ] 으로 2차원 배열 오름차순으로 되어있음
        global results
        # 유클리드 거리 유사도 매칭    
        if(radio1.isChecked()):
            results = mkList(filename, 1)
        # 코사인 유사도 매칭
        elif(radio2.isChecked()):
            results = mkList(filename, 2)

        #start 버튼 비활성화, next 버튼 활성화
        self.start.setEnabled(False)
        self.next.setEnabled(True)
    
    def start_process2(self):
        # results = [ ['KOR-DOGE',20231 ],['KOR-BTC',23434] ... ] 으로 2차원 배열 오름차순으로 되어있음
        global results
        # 유클리드 거리 유사도 매칭    
        if(radio1.isChecked()):
            results = mkList(filename, 1)
        # 코사인 유사도 매칭
        elif(radio2.isChecked()):
            results = mkList(filename, 2)
                

    def gotoResultPage(self):
        # 첫 실행 시
        if (widget.currentIndex() == 1):
            result=ResultPage()
            widget.addWidget(result)
            widget.setCurrentIndex(widget.currentIndex()+1)
        # 첫 실행이 아닐 시
        else:
            self.start_process2()
            result=ResultPage()
            widget.addWidget(result)
            widget.setCurrentIndex(widget.currentIndex()+1)
    


class ResultPage(QDialog):
    def __init__(self):
        super(ResultPage, self).__init__()
        loadUi("result.ui", self)

        #유저 이미지 배치
        self.userImage.setPixmap(QtGui.QPixmap(filename))

        #추천하는 코인의 이름 표시
        self.label.setText(results[0][0])

        #추천하는 코인의 그래프 배치
        self.resultImage.setPixmap(QtGui.QPixmap('./datas/' + results[0][0] +'.png'))

        #main 페이지로 돌아감
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
