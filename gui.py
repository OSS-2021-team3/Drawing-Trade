import tkinter as tk
import os
print (os.path.dirname(os.path.realpath(__file__)) )
import random
import MatchingTest
    
class DrawingTrade(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # top frame 생성

        frame_top = tk.Frame(self, relief="solid", borderwidth = 1)
        frame_top.pack(side = "top", fill = "both", expand=True)

        # top frame의 left frame 생성

        frame_left = tk.Frame(frame_top, relief="solid", borderwidth = 1)
        frame_left.pack(side="left", fill="both", expand=True)

        # left frame에 알고리즘 선택 버튼 배치

        checkVar = tk.IntVar()
        checkButton1 = tk.Radiobutton(frame_left, text = "유클리드 거리 유사도 매칭", variable = checkVar, value = 0)
        checkButton2 = tk.Radiobutton(frame_left, text = "코사인 유사도 매칭", variable = checkVar, value = 1)

        checkButton1.grid(column=0, row=0, sticky="W")
        checkButton2.grid(column=0, row=1, sticky="W")

        # top frame의 right frame 생성

        frame_right = tk.Frame(frame_top, relief="solid", borderwidth = 1)
        frame_right.pack(side="right", fill="both", expand=True)

        # right frame에 사용자가 그린 이미지 배치

        image1 = tk.PhotoImage(file="photo.png")
        lbl = tk.Label(frame_right, image=image1)
        lbl.image = image1
        lbl.grid(row = 3, column = 1, padx = 5, pady = 5)
      

        # bottom frame 생성

        frame_bottom = tk.Frame(self, relief="ridge", borderwidth = 1, width = 100, height = 50)
        frame_bottom.pack(side="bottom", fill="both", expand=True)

        # next screen으로 넘어감

        tk.Button(frame_bottom, text="Next",
                  command=lambda: master.switch_frame(LoadingPage)).pack()
                 
class LoadingPage(tk.Frame):
    def __init__(self, master):

        # 로딩 문구

        text = tk.Label(self, text="Loading...", font=18)
        text.pack()

        # 이미지 생성

        img = tk.PhotoImage(file="./images/" + str(random(10))+ ".png")
        lbl = tk.Label(self, image=img)
        lbl.image = img
        lbl.grid(row = 3, column = 1, padx = 5, pady = 5)

        # 필요한 작업을 진행
        

        # 작업 종료 후, ResultPage로 이동. test를 위해 20초 후 진행

        self.after(20000, master.switch_frame(LoadingPage))

        



class ResultPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        label1 = tk.Label(self, text="Recommendation")
        
        # 가장 유사도가 높은 알트코인 그래프를 추천

         # top frame 생성

        frame_top = tk.Frame(self, relief="solid", borderwidth = 1)
        frame_top.pack(side = "top", fill = "both", expand=True)

        # top frame의 left frame 생성

        frame_left = tk.Frame(frame_top, relief="solid", borderwidth = 1)
        frame_left.pack(side="left", fill="both", expand=True)

        # top frame의 right frame 생성

        frame_right = tk.Frame(frame_top, relief="solid", borderwidth = 1)
        frame_right.pack(side="right", fill="both", expand=True)

        # bottom frame 생성

        frame_bottom = tk.Frame(self, relief="solid", borderwidth = 1)
        frame_bottom.pack(side="bottom", fill="both", expand=True)
        
        # left frame에 사용자 그림, right frame에 그림과 가장 유사한 그래프를 출력

        leftImage = tk.PhotoImage(file="photo.png")
        lbl = tk.Label(frame_left, image=leftImage)
        lbl.image = leftImage
        lbl.grid(row = 3, column = 1, padx = 5, pady = 5)

        rightImage = tk.PhotoImage(file=MatchingTest.data_path+list[0][0]+MatchingTest.extension)
        lbl2 = tk.Label(frame_right, image=rightImage)
        lbl2.image = rightImage
        lbl.grid(row = 3, column = 1, padx = 5, pady = 5)

        # startPage로 넘어감

        tk.Button(frame_bottom, text="Return",
                  command=lambda: master.switch_frame(StartPage)).pack()

   





if __name__ == "__main__":
    app = DrawingTrade()\
    # Title 설정
    app.title("Drawing Trade")
    # 화면 크기 설정
    app.mainloop()

