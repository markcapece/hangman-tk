from random import choice


class CorrectAnswer(object):
    def __init__(self, word_list):
        self.answer = choice(word_list).upper()

    def __str__(self):
        return self.answer

    def __repr__(self):
        return self.answer
