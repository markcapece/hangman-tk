
class History(object):
    def __init__(self):
        self.history = []

    def add_guess(self, user_guess):
        self.history.append(user_guess)

    def __str__(self):
        return '{}'.format(self.history)

    def __repr__(self):
        return '{}'.format(self.history)
