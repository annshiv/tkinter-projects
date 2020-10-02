import Tkinter
class Tipcalculator:
    def __init__(self):
        window = Tk()
        window.title("Tip calculator")
        window.configure(background="sky blue")
        window.geometry("375x250")
        window.resizable(width=False,height=False)
        window.mainloop()
    
Tipcalculator()