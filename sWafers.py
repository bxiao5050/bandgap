from tkinter import *
import tkinter.ttk as ttk
import pandas as pd


from waferBs import MyButton



class SWafer(ttk.Frame):
    """
complete wafer with 342 buttons, only allow for single-button click
    """
    def __init__(self, master, **kw):
        ttk.Frame.__init__(self, master, **kw)


        self.waferF = Frame(self)
        self.lPos = Label(self, text = '')

        self.lPos.pack(pady = (5,5))
        self.waferF.pack()


        self.logo = PhotoImage(width = 11, height = 11)
        self.pos = 1
        row = 20
        col = 21


        self.pAB = {}

        ll = [4, 2, 0, -2, -4]
        for row in reversed(range(20)):
            for col in range(21):
                if row == 0 and col >= 7 and col <=13:
                    self.newB(row, col, self.pos)
                elif row >= 1 and row <= 5 and col >= 6 - row and col <= row + 14:
                    self.newB(row, col, self.pos)
                elif row == 6 and col >=1 and col <= 19:
                    self.newB(row, col, self.pos)
                elif row <=13 and row >=7:
                    self.newB(row, col, self.pos)
                elif row == 14 and col >= 1 and col <= 19:
                    self.newB(row, col, self.pos)
                elif row >= 15 and row <= 19 and col >= row - 14 and col <= row + ll[row - 15]:
                    self.newB(row, col, self.pos)

        for row in range(21):
            Grid.rowconfigure(self, row, weight = 1)

        for col in range(20):
            Grid.columnconfigure(self, col, weight = 1)



    def on_buttonPress(self, pos):
        self.buttonPress(pos)

    def buttonPress(self, pos):
        for b in self.getpressedButtons():
            b.config(relief = 'raised')
        self.pAB[pos].oneOrTwoclick()

    #override mouse enter
    def on_enter(self, e):
        e.widget.config(bg =  'SkyBlue3')
        self.lPos.config(text = f'''pos: {e.widget.cget('text')}''')
        # print(e.widget.cget('text'))

    # get the names of all pressed button
    def getpressedButtonnames(self):
        return [b.cget('text') for b in self.pAB.values() if b.cget('relief') == 'sunken']

    def getpressedButtons(self):
        return [b for b in self.pAB.values() if b.cget('relief') == 'sunken']

    def getpressedButtonPos(self):
        return [pos for pos, b in self.pAB.items() if b.cget('relief') == 'sunken']

    def getpressedB(self):
        pressedB = {}
        for pos, b in self.pAB.items():
            if b.cget('relief') == 'sunken':
                pressedB[pos] = b
        return pressedB

    #reset buttons
    def raiseButtons(self):
        for b in self.getpressedButtons():
            b.config(relief = 'raised', image = self.logo)



    def newB(self, row, col, pos):
        k = self.pos
        self.pAB[pos] = MyButton(self.waferF, relief = 'raised', text = str(k), image = self.logo)

        #button override press command
        self.pAB[pos].configure(command = lambda k = k : self.on_buttonPress(k))
        self.pAB[pos].mouse_enter(self.on_enter)

        self.pAB[pos].grid(row = row, column = col, sticky=N+S+E+W)
        self.pos += 1


# def main():
#     root = Tk()
#     SWafer(root).pack(fill = 'both', expand = True)

#     root.mainloop()

# if __name__ == '__main__':
#     main()


