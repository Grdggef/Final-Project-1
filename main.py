from gui import *


def main():
    window = Tk()
    window.title('final project 1')
    window.geometry('500x325')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()


if __name__ == '__main__':
    main()