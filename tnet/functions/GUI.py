from tkinter import *
from tkinter import messagebox
import time
from PIL import ImageTk, Image, ImageSequence
from tkinter import ttk
from . picture import image
import sys
from functions.GUI_function import terminal
#def calling(a,b,c):
    #from . GUI_function import mediator
    #wn=Tk(className='win')
    #mediator.win(a,b,c,wn)
    #wn.resizable(0,0)
def cll(a,b,c):
	global ap
	global fil
	global func
	ap=StringVar()
	fil=StringVar()
	func=StringVar()
	ap=a
	fil=b
	func=c
	print(ap)
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        # Setup Frame
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry('600x550+450+100')

        self._frame = None
        self.switch_frame(Home)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid(row=0,column=0)


class Home(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.window.title('Home Page')
        self.home_frame = Frame(self.window, bg='black')
        self.home_frame.grid(row=1,column=0)
        self.label = Label(self.home_frame, image=image.bg(self),foreground="red")
        self.label.grid(row=0,column=0)
        ##button_EIGRP
        self.button1 = Button(self.home_frame, text="EIGRP ATTACK", font="Helvetica,60,Bold",width=13,height=5,borderwidth=2,background="#2B547E",command=self.eigrp)
        self.button1.place(x=45, y=90)
        self.button1.bind('<Enter>', self.on_enter)
        self.button1.bind('<Leave>', self.on_leave)
        self.button2 = Button(self.home_frame,text="RIP ATTACK",font="Helvetica,60,Bold",width=13,height=5,background="#2B547E",command=self.rip_frame)
        self.button2.place(x=45, y=210)
        self.button2.bind('<Enter>', self.on_enterlb2)
        self.button2.bind('<Leave>', self.on_leavelb2)
        #self.button2.bind("<Button-1>", lambda e: Program_pod())
        self.button3 = Button(self.home_frame, text="POD ATTACK", font="Helvetica,60,Bold", width=13, height=5,background="#2B547E",command=self.pod_frame)
        self.button3.place(x=45, y=330)
        self.button3.bind('<Enter>', self.on_enterlb3)
        self.button3.bind('<Leave>', self.on_leavelb3)
        # self.button2.bind("<Button-1>", lambda e: Program_pod())
        self.my_menu = Menu(self.home_frame)#tearoff=True)
        self.window.config(menu=self.my_menu)
        ITEM = Menu(self.my_menu)
        self.my_menu.add_cascade(label="Help", menu=ITEM)
        ITEM.add_cascade(label="Eigrp")
        ITEM.add_cascade(label="RIP")
        ITEM.add_cascade(label="POD")

    def on_enter(self,e):
        self.button1.config( foreground="black",background="#838996")

    def on_leave(self,e):
        self.button1.config( foreground='white',background="#2B547E")
    ###Label2
    def on_enterlb2(self,e):
        self.button2.config( foreground="black",background="#838996")
    def on_leavelb2(self,e):
        self.button2.config( foreground='white',background="#2B547E")
    ###Label3
    def on_enterlb3(self, e):
        self.button3.config(foreground="black", background="#838996")
    def on_leavelb3(self, e):
        self.button3.config(foreground='white', background="#2B547E")

    def eigrp(self):
        self.window.switch_frame(eigrp)
        self.home_frame.destroy()
    def rip_frame(self):
        self.window.switch_frame(rip)
        self.home_frame.destroy()
    def pod_frame(self):
        self.window.switch_frame(pingofdeath)
        self.home_frame.destroy()




class eigrp(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.window.title('Eigrp')
        self.eigrp_frame = Frame(self.window, bg='black')
        self.eigrp_frame.grid(row=1, column=0)
        self.label = Label(self.eigrp_frame, image=image.bg(self), foreground="red")
        self.label.grid(row=0, column=0)
        self.button2 = Button(self.window, text="EIGRP DOS", font="Helvetica,60,Bold", width=14, height=5,
                              background="#2B547E",command=self.dos_eigrp)
        self.button2.place(x=45, y=290)
        self.button2.bind('<Enter>', self.on_enterlb2)
        self.button2.bind('<Leave>', self.on_leavelb2)
        # self.button2.bind("<Button-1>", lambda e: Program_pod())
        self.button3 = Button(self.window, text="EIGRP NEGHBOR", font="Helvetica,5,Bold", width=14, height=5,
                              background="#2B547E",command=self.neighbor_eigrp)
        self.button3.place(x=45, y=150)
        self.button3.bind('<Enter>', self.on_enterlb3)
        self.button3.bind('<Leave>', self.on_leavelb3)
        # self.button2.bind("<Button-1>", lambda e: Program_pod())

        self.back_btn= Button(self.window,image=image.backimage(self),command=self.home)
        self.back_btn.place(x=545,y=0)
    def on_enterlb2(self,e):
        self.button2.config( foreground="black",background="#BCC6CC")
    def on_leavelb2(self,e):
        self.button2.config( foreground='white',background="#2B547E")
    ###Label3
    def on_enterlb3(self, e):
        self.button3.config(foreground="black", background="#BCC6CC")
    def on_leavelb3(self, e):
        self.button3.config(foreground='white', background="#2B547E")

    def home(self):
        self.window.switch_frame(Home)
    def dos_eigrp(self):
        self.window.switch_frame(eigrp_dos)
    def neighbor_eigrp(self):
        self.window.switch_frame(eigrp_neighbor)


class eigrp_dos(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.wn = window
        self.wn.title('Eigrp Dos Attack')
        global ip
        ip=StringVar()
        self.eigrpdos_frame = Frame(self.wn, bg='black')
        self.eigrpdos_frame.grid(row=1, column=0)
        self.label = Label(self.eigrpdos_frame, image=image.bg(self), foreground="red")
        self.label.grid(row=0, column=0)
        self.ent = Entry(self.eigrpdos_frame, font='Arial 15 bold',textvariable=ip)
        self.ent.place(x=50,y=100)
        self.btn=Button(self.eigrpdos_frame,image=image.back(self),command=self.call)
        self.btn.place(x=275,y=100)
        self.back_btn = Button(self.eigrpdos_frame, image=image.backimage(self), command=self.eigrp)
        self.back_btn.place(x=545, y=0)

    def eigrp(self):
        self.wn.switch_frame(eigrp)
    def call(self):
    	self.ip=ip.get()
    	self.file=" functions/GUI_function/eigrp_ddos.py"
    	self.function=" ddos"
    	self.wn.switch_frame(newwindow)
    	self.eigrpdos_frame.destroy()
    	cll(self.ip,self.file,self.function)
    	


class eigrp_neighbor(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.wn = window
        self.wn.title('Eigrp Neighbor attack')
        global ip 
        ip=StringVar()
        self.eigrpneighbor_frame = Frame(self.wn, bg='black')
        self.eigrpneighbor_frame.grid(row=1, column=0)
        self.label = Label(self.eigrpneighbor_frame, image=image.bg(self), foreground="red")
        self.label.grid(row=0, column=0)
        self.ent = Entry(self.eigrpneighbor_frame, font='Arial 15 bold',textvariabl=ip)
        self.ent.place(x=50, y=100)

        self.btn = Button(self.eigrpneighbor_frame, image=image.back(self),command=self.call)
        self.btn.place(x=275, y=100)
        self.back_btn = Button(self.eigrpneighbor_frame, image=image.backimage(self), command=self.eigrp)
        self.back_btn.place(x=545, y=0)
    def eigrp(self):
        self.wn.switch_frame(eigrp)
    def call(self):
    	self.wn.switch_frame(newwindow)
    	self.ip=ip.get()
    	self.file=" ./functions/GUI_function/eigrp_neighbor.py"
    	self.function=" eigrp"
    	self.eigrpneighbor_frame.destroy()
    	cll(self.ip,self.file,self.function)
    	

class rip(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.wn = window
        self.wn.title('RIP Dos attack')
        global ip
        ip = StringVar()
        self.rip_frame = Frame(self.wn, bg='black')
        self.rip_frame.grid(row=1, column=0)
        self.label = Label(self.rip_frame, image=image.bg(self), foreground="red")
        self.label.grid(row=0, column=0)
        self.ent = Entry(self.rip_frame, font='Arial 15 bold', textvariable=ip)
        self.ent.place(x=50, y=100)

        self.btn = Button(self.rip_frame, image=image.back(self), command=self.calls)
        self.btn.place(x=275, y=100)
        self.back_btn = Button(self.rip_frame, image=image.backimage(self), command=self.home)
        self.back_btn.place(x=545, y=0)

    def home(self):
        self.wn.switch_frame(Home)


    def calls(self):
        self.ip = ip.get()
        self.file = " functions/GUI_function/rip.py"
        self.function = " rip_ddos"
        cll(self.ip, self.file, self.function)
        self.wn.switch_frame(newwindow)
        self.rip_frame.destroy()
	


class pingofdeath(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.wn = window
        self.wn.title('Ping of Death')
        global ip
        ip =StringVar()
        self.pod_frame = Frame(self.wn, bg='black')
        self.pod_frame.grid(row=1, column=0)
        self.label = Label(self.pod_frame, image=image.bg(self), foreground="red")
        self.label.grid(row=0, column=0)
        self.ent = Entry(self.pod_frame, font='Arial 15 bold',textvariable=ip)
        self.ent.place(x=50, y=100)

        self.btn = Button(self.pod_frame, image=image.back(self),command=self.call)
        self.btn.place(x=275, y=100)
        self.back_btn = Button(self.pod_frame, image=image.backimage(self), command=self.Home)
        self.back_btn.place(x=545, y=0)

    def Home(self):
        self.wn.switch_frame(Home)
    def call(self):
    	self.wn.switch_frame(newwindow)
    	self.ip=ip.get()
    	self.file=" functions/GUI_function/POD.py"
    	self.function=" Pod"
    	cll(self.ip,self.file,self.function)
    	self.pod_frame.destroy()
    	
class newwindow(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.wn = window
        self.wn.title('Terminal')
        self.new_frame = Frame(self.wn)
        self.new_frame.grid(row=1, column=0)

        self.text = Text(self.new_frame)
        self.text.grid(row=1, column=0)
        self.back_btn = Button(self.new_frame, image=image.backimage(self), command=self.Home)

        self.back_btn.place(x=545, y=0)
        self.button = Button(self.wn, text='ATTACK', command=lambda: terminal.run(ap, fil, func,self.text))
        self.button.place(x=250, y=430)

        old_stdout = sys.stdout
        print('hello')
        sys.stdout = terminal.Redirect(self.text)

        # - after close window -

        sys.stdout = old_stdout


    def Home(self):
        self.wn.switch_frame(Home)
        self.new_frame.destroy()
app = App()
app.mainloop()
