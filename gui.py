
import tkinter
from tkinter import *
import logic


class Gui:
    def __init__(self, window):
        self.votes = []

        # frame for main  window
        self.voting_window = window
        self.candidate_frame = Frame(self.voting_window)
        self.candidate_label = Label(self.candidate_frame, text='Voting\n')
        self.candidate_label.pack(side='top')
        self.candidate_frame.pack(anchor='n')

        # frame for candidate 1
        self.option1 = Frame(self.voting_window)
        self.var = IntVar()
        self.var.set(0)
        self.candidate1 = Radiobutton(self.option1, text='Brad', variable=self.var, value=1)
        self.candidate1_desc = Button(self.option1, text='Description', command=logic.description1)
        self.candidate1.pack()
        self.candidate1_desc.pack(pady=10)
        self.option1.pack()

        # frame for candidate 2
        self.option2 = Frame(self.voting_window)
        self.candidate2 = Radiobutton(self.option2, text='Charlie', variable=self.var, value=2)
        self.candidate2_desc = Button(self.option2, text='Description', command=logic.description2)
        self.candidate2.pack()
        self.candidate2_desc.pack(pady=10)
        self.option2.pack()

        # frame for candidate 3
        self.option3 = Frame(self.voting_window)
        self.candidate3 = Radiobutton(self.option3, text='Cindy', variable=self.var, value=3)
        self.candidate3_desc = Button(self.option3, text='Description', command=logic.description3)
        self.candidate3.pack()
        self.candidate3_desc.pack(pady=10)
        self.option3.pack()

        # frame for voting buttons
        self.buttons_frame = Frame(self.voting_window)
        self.submit = Button(self.buttons_frame, text='Submit', command=self.submit)
        self.clear = Button(self.buttons_frame, text='Clear', command=self.clear)
        self.tally_button = Button(self.buttons_frame, text='Tally', command=self.tally)
        self.submit.pack(side='left',pady=5)
        self.clear.pack(side='left',padx=15, pady=5)
        self.tally_button.pack(side='left',pady=5)
        self.buttons_frame.pack()

        # frame fro text to confirm that vote was successful/if errors were encountered
        self.text_frame = Frame(self.voting_window)
        self.text = Label(self.text_frame, text="")
        self.text.pack(side='bottom', pady=15)
        self.text_frame.pack(anchor='s')

    # takes selected radio button and appends name of candidate to the votes list
    def submit(self):
        variable = self.var.get()
        if variable == 1:
            self.votes.append('Brad')
            self.text.config(text="Voted Brad")
        elif variable == 2:
            self.votes.append('Charlie')
            self.text.config(text="Voted Charlie")
        elif variable == 3:
            self.votes.append('Cindy')
            self.text.config(text="Voted Cindy")
        elif variable == 0:
            self.text.config(text="Please Select a Candidate")

    clears all radio buttons and winner text
    def clear(self):
        self.var.set(0)
        winner = ''
        self.text.config(text='')

    #counts the number of votes recieved by each candidate to determine whether a winner was found, a tie occurred, 
    #or there were no votes at all
    def tally(self):
        count = len(self.votes)
        brad_count = self.votes.count("Brad")
        charlie_count = self.votes.count("Charlie")
        cindy_count = self.votes.count("Cindy")
        winner = ''

        # if statements to determine the winner
        if brad_count > cindy_count and brad_count > charlie_count:
            winner = "\nThe Winner Is \n \n \n Brad!!\n \n \n"
        elif charlie_count > brad_count and charlie_count > cindy_count:
            winner = "\nThe Winner Is \n \n \nCharlie!!\n \n \n"
        elif cindy_count > brad_count and cindy_count > charlie_count:
            winner = "\nThe Winner Is \n \n \nCindy!!\n \n \n"
        elif count == 0:
            winner = "\n There are no votes\n \n \n"
        elif brad_count == charlie_count and brad_count == cindy_count:
             winner = "\nIt's a three way tie!!\n \n \n"
        elif brad_count == cindy_count:
            winner = "\nIt's a tie between Brad and Cindy!!\n \n \n"
        elif brad_count == charlie_count:
            winner = "\nIt's a tie between Brad and Charlie!!\n \n \n"
        elif charlie_count == cindy_count:
            winner = "\nIt's a tie between Charlie and Cindy!!\n \n \n"

        # code for the tally window
        self.top4 = Toplevel()
        self.top4.title("Election Results")
        self.top4.geometry('200x200')
        self.top4.resizable(False, False)

        # label for the results label
        results = Label(self.top4, text='Results')
        results.pack(side='top')

        #label for the winner text
        results_text = Label(self.top4, text=str(winner))
        results_text.pack()

        # code for the new election button
        new_el_frame = Frame(self.top4)
        new_election_but = Button(new_el_frame, text="New Election", command=self.new_election)

        new_el_frame.pack()
        new_election_but.pack(side='bottom')

    # function that clears all radio buttons, destorys the tally window, and empties the votes list and all necesssary labels
    def new_election(self):
        self.votes.clear()
        self.var.set(0)
        winner = ''
        self.top4.destroy()
        self.top4.update()
        self.text.config(text='')
