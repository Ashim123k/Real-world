
from PIL import ImageTk, Image, ImageSequence

class image:
    def bg(self):
        self.pic = Image.open(r'./functions/ashim.jpg')
        self.resize_pic = self.pic.resize((600, 600))
        self.img = ImageTk.PhotoImage(self.resize_pic)
        return self.img
    def back(self):
        self.next = Image.open(r'./functions/next.png')
        self.resize_nextpic = self.next.resize((25, 23))
        self.nextimg = ImageTk.PhotoImage(self.resize_nextpic)
        return self.nextimg
    def backimage(self):
        self.backpic = Image.open(r'./functions/images.png')
        self.bresize_pic = self.backpic.resize((50, 25))
        self.bimg = ImageTk.PhotoImage(self.bresize_pic)
        return self.bimg
