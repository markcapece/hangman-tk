import tkinter as tk
from tkinter import messagebox as msg

from hangman.game import Game


class HangMan(tk.Tk):
    def __init__(self):
        super().__init__()

        # Master Window
        self.title('Hangman')
        self.geometry('300x330')

        # Menus
        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.filemenu)

        self.filemenu.add_command(label='New', command=self.new_game,
                                  accelerator='Ctrl-N')  # New Game
        self.filemenu.add_command(label='Scores', command=self.score,
                                  accelerator='Ctrl-S')  # Score History
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Quit', command=self.close_window,
                                  accelerator='Ctrl-Q')

        self.config(menu=self.menubar)

        # Sections
        self.hidden_word = tk.StringVar(self)
        self.hidden_word.set('W E L C O M E * T O * H A N G M A N')
        self.hidden_word_section = tk.Label(self, textvariable=self.hidden_word,
                                            pady=20, height=3, bg='white', fg='black')
        self.hidden_word_section.pack(side=tk.TOP, fill=tk.X)

        self.guess_history = tk.StringVar(self)
        self.guess_history.set('')
        self.guess_history_section = tk.Label(self, textvariable=self.guess_history,
                                              pady=5, height=3, bg='white', fg='black')
        self.guess_history_section.pack(side=tk.TOP, fill=tk.X)

        self.gallow_string = tk.StringVar(self)
        gallow_var = '''
           ---------    
           |         |    
           |       \\O/   
           |         |    
           |        / \\   
           |            
           |            
        -------         '''
        self.gallow_string.set(gallow_var)

        self.gallow_string_section = tk.Label(self, textvariable=self.gallow_string,
                                              pady=5, height=10, bg='white', fg='black', justify=tk.LEFT)
        self.gallow_string_section.pack(side=tk.TOP, fill=tk.BOTH)

        self.user_entry = tk.Text(self, height=1, bg='white', fg='black')
        self.user_entry.pack(side=tk.BOTTOM, fill=tk.BOTH)
        self.user_entry.configure(state='disabled')

        self.instruction_string = tk.StringVar(self)
        self.instruction_string.set('Go to File > New to start!')
        self.instruction_section = tk.Label(self, textvariable=self.instruction_string,
                                            pady=2, bg='white', fg='black')
        self.instruction_section.pack(side=tk.BOTTOM, fill=tk.X)

        # Keybinds
        self.bind('<Control-n>', self.new_game)
        self.bind('<Control-s>', self.score)
        self.bind('<Control-q>', self.close_window)
        self.user_entry.bind('<Return>', self.submit_guess)

    def new_game(self, event=None):
        self.game = Game()
        self.hidden_word.set(self.game.hidden_answer)
        self.guess_history.set(self.game.history)
        self.gallow_string.set(self.game.gallows)
        self.instruction_string.set('Please guess a letter')
        self.user_entry.configure(state='normal')
        self.user_entry.focus_set()

    def score(self, event=None):
        ScoreBoard(self)

    def close_window(self, event=None):
        self.destroy()

    def submit_guess(self, event=None):
        new_guess = self.user_entry.get(1.0, tk.END).strip()
        guess = self.game.guess_letter(new_guess)

        if guess is False:
            msg.showwarning('Invalid Input', 'Please guess a single letter.')

        self.hidden_word.set(self.game.hidden_answer)
        self.guess_history.set(self.game.history)
        self.gallow_string.set(self.game.gallows)

        self.user_entry.delete(1.0, tk.END)

        if self.game.gallows.miss_count >= 6 or '_' not in str(self.game.hidden_answer):
            self.end_game(self.game.gallows.miss_count)

    def end_game(self, misses, event=None):
        if misses < 6:
            msg.showerror('You Win!', 'The word is {}'.format(self.game.correct_answer))
        else:
            msg.showerror('You Lose!', 'The word is {}'.format(self.game.correct_answer))

        self.user_entry.configure(state='disabled')
        self.instruction_string.set('Go to File > New to start!')


class ScoreBoard(tk.Toplevel):
    def __init__(self, master):
        super().__init__()
        self.master = master

        # Top Level Window
        self.title('Score Board')
        self.geometry('200x300')

        # Menus
        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.filemenu)

        self.filemenu.add_separator()
        self.filemenu.add_command(label='Close', command=self.close_window,
                                  accelerator='Ctrl-C')

        self.config(menu=self.menubar)

        # Sections
        self.scores_string = tk.StringVar(self)
        self.scores_string.set('')
        self.score_section = tk.Label(self, textvariable=self.scores_string,
                                      bg='white', fg='black',
                                      padx=5, pady=5, justify=tk.LEFT)
        self.score_section.pack(side=tk.TOP, fill=tk.X)

        # Keybinds
        self.bind('<Control-c>', self.close_window)

        # Show Scores
        with open('hangman/scores.txt', 'r') as fp:
            self.scores = fp.read()
        self.scores_string.set(self.scores)

    def close_window(self, event=None):
        self.destroy()


if __name__ == '__main__':
    hangman = HangMan()
    hangman.mainloop()
