
class HiddenAnswer(object):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer
        self.hidden_answer = '_' * len(self.correct_answer)

    def reveal(self, guessed_letter):
        hidden = ''
        for position, letter in enumerate(self.correct_answer):
            if letter == guessed_letter:
                hidden += letter
            else:
                hidden += self.hidden_answer[position]
        self.hidden_answer = hidden

    def __str__(self):
        return ' '.join([l for l in self.hidden_answer])

    def __repr__(self):
        return ' '.join([l for l in self.hidden_answer])
