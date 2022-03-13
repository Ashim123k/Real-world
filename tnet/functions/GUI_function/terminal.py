
import subprocess
import threading 
# --- classes ---

class Redirect():

    def __init__(self, widget, autoscroll=True):
        self.widget = widget
        self.autoscroll = autoscroll

    def write(self, text):
        self.widget.insert('end', text)
        print(text)
        if self.autoscroll:
            self.widget.see("end")  # autoscroll

    def flush(self):
        print("HI")
    
# --- functions ---

def run(a, b, c,text):
    global ip
    global fil
    global function
    global tex
    # ip=StringVar()
    # fil=StringVar()
    # function=StringVar()
    ip = a
    fil = b
    function = c
    tex=text
    threading.Thread(target=test).start()


def test():
    print("Thread: start")
    a = ' ' + ip  # " 127.0.0.1"
    b = fil  # " GUI_function/eigrp_ddos.py"
    c = function  # " ddos"
    d = "python3"
    lan = d + b + c + a
    print(lan)
    p = subprocess.Popen(lan.split(), stdout=subprocess.PIPE, bufsize=1, text=True)
    while p.poll() is None:

        msg = p.stdout.readline().strip()  # read a line from theoutput
        if msg:
            print(msg)
    print("Thread: end")




