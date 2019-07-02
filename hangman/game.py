from string import ascii_letters

from hangman.correctanswer import CorrectAnswer
from hangman.customdictionary import CUSTOM_DICTIONARY
from hangman.gallows import Gallows
from hangman.hiddenanswer import HiddenAnswer
from hangman.history import History


class Game(object):
    def __init__(self, custom_dictionary=CUSTOM_DICTIONARY):
        self.correct_answer = CorrectAnswer(custom_dictionary)
        self.hidden_answer = HiddenAnswer(str(self.correct_answer))
        self.gallows = Gallows()
        self.history = History()

        self.lost = False
        self.won = False

    def guess_letter(self, user_guess):
        user_guess = user_guess.upper()
        if user_guess not in ascii_letters or len(user_guess) > 1:
            print('Invalid guess. You must guess a single letter.')
            return False

        if repr(self.history) is not None and user_guess in repr(self.history):
            hit = False
        elif user_guess in repr(self.correct_answer):
            hit = True
        else:
            hit = False

        self.update_gamestate(user_guess=user_guess, hit=hit)

    def update_gamestate(self, user_guess, hit):
        self.history.add_guess(user_guess)
        if hit:
            self.hidden_answer.reveal(user_guess)
        else:
            self.gallows.increment_gallows()

        if '_' not in str(self.hidden_answer):
            self.won = True
            self.record_score()
        elif self.gallows.miss_count == 6:
            self.lost = True
            self.record_score()

    def display_gamestate(self):
        print(self.hidden_answer)
        print(self.history)
        print(self.gallows)

    def record_score(self):
        score = '{: <4} - {} - {}\n'.format(
            'Won' if self.won else 'Lost' if self.lost else None,
            self.gallows.miss_count,
            str(self.correct_answer)
        )
        with open('./hangman/scores.txt', 'a') as fp:
            fp.writelines(score)
