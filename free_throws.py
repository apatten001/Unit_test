

class Students:

    def __init__(self, first, last, num_shots, missed):
        self.first = first
        self.last = last
        self.num_shots = num_shots
        self.missed = missed


    def fullname(self):
        return "{} {}".format(self.first,self.last)

    def shots_took(self):

        return "{} {} took {} shots.".format(self.first, self.last, self.num_shots)

    def shots_missed(self):

        return "{} missed {} shots".format(self.fullname(), self.missed)
    def shot_percentage(self,):

        self.percentage = ((self.num_shots-self.missed)*10)

        return "{}'s shooting percentage is {}%".format(self.fullname(), int(self.percentage))





