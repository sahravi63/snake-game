from tkinter import Tk, PhotoImage
from userInterface import Display

def main():
    master = Tk()
    master.title("Snake and Ladder")
    master.geometry("850x600")
    # Provide the absolute path to the image file
    img = PhotoImage(file=r"E:\snake\lenna.gif")
    x = Display(master, img)
    master.mainloop()

if __name__ == "__main__":
    main()
