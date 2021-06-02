import tkinter as tk

    
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

        # top frame ����

        frame_top = tk.Frame(self, relief="solid", borderwidth = 1)
        frame_top.pack(side = "top", fill = "both", expand=True)

        # top frame�� left frame ����

        frame_left = tk.Frame(frame_top, relief="solid", borderwidth = 1)
        frame_left.pack(side="left", fill="both", expand=True)

        # left frame�� ��ư ��ġ

        checkVar = tk.IntVar()
        checkButton1 = tk.Radiobutton(frame_left, text = "��Ŭ���� �Ÿ� ���絵 ��Ī", variable = checkVar, value = 0)
        checkButton2 = tk.Radiobutton(frame_left, text = "�ڻ��� ���絵 ��Ī", variable = checkVar, value = 1)

        checkButton1.grid(column=0, row=0, sticky="W")
        checkButton2.grid(column=0, row=1, sticky="W")

        # top frame�� right frame ����

        frame_right = tk.Frame(frame_top, relief="ridge", borderwidth = 1)
        frame_right.pack(side="right", fill="both", expand=True)

        img = tk.PhotoImage(file="photo.png")
        lbl = tk.Label(frame_right, image=img)
        lbl.pack()

        # bottom frame ����

        frame_bottom = tk.Frame(self, relief="ridge", borderwidth = 1)
        frame_bottom.pack(side="bottom", fill="both", expand=True)

        

        tk.Button(frame_bottom, text="Next",
                  command=lambda: master.switch_frame(ResultPage)).pack()

class ResultPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="Recommendation", font=('Helvetica', 18, "bold")).pack(side="left", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()


if __name__ == "__main__":
    app = DrawingTrade()\
    # Title ����
    app.title("Drawing Trade")
    # ȭ�� ũ�� ����
    app.mainloop()