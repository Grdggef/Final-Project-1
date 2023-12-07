from tkinter import *


# top level description window for candidate 1
def description1():
    top1 = Toplevel()
    top1.title("Brad's Description")
    top1.geometry('310x200')

    description = Label(top1, text='BRAD')
    description.pack(side='top')

    description_text = Label(top1, text=f'\n \n Brad is a known cat lover who always strives to put \n'
                                        'forward the best foot when it come to animal rights and \n '
                                        'preventing cruel treatment.')
    description_text.pack()


# top level description window for candidate 2
def description2():
    top2 = Toplevel()
    top2.title("Charlie's Description")
    top2.geometry('310x200')

    description = Label(top2, text='CHARLIE')
    description.pack(side='top')

    description_text = Label(top2, text=f'\n \nCharlie likes to spend his free time helping orphans. \n'
                                        'He believes that to be able to help the less fortunate \n '
                                        'is the best part of being a man with means.')
    description_text.pack()


# top level description window for candidate 3
def description3():
    top3 = Toplevel()
    top3.title("Cindy's Description")
    top3.geometry('310x200')

    description = Label(top3, text='CINDY')
    description.pack(side='top')

    description_text = Label(top3, text=f'\n \nCindy is a known woman around the community. If there \n'
                                        'is an event benefiting the community she is right there \n '
                                        'helping to make the event a success')
    description_text.pack()




