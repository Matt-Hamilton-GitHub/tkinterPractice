
import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):
        
        self.main_w = tkinter.Tk()
        
        self.top_frame = tkinter.Frame(self.main_w)
        self.bottom_frame = tkinter.Frame(self.main_w)
        
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        self.lab1 = tkinter.Label(self.top_frame,text='Enter a distance in kilometers:')
        self.entry = tkinter.Entry(self.top_frame,width='10')
        
        self.lab1.pack(side='left')
        self.entry.pack(side='left')
        
        self.calcBat = tkinter.Button(self.bottom_frame,text='Convert',command=self.Convert)
        self.quiteBat = tkinter.Button(self.bottom_frame,text='Quite',command=self.main_w.destroy)
        
        self.calcBat.pack(side='left')
        self.quiteBat.pack(side='left')
        
        
        tkinter.mainloop()
        
    def Convert(self):
        kilo = float(self.entry.get())
        
        miles = kilo * 0.6214
        
        tkinter.messagebox.showinfo('Results',str(kilo)+' kilometers is equal to '+ format(miles,'.2f') + ' miles')

myConverter = KiloConverterGUI()
