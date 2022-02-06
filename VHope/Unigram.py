class unigram:
    def __init__(self, term):
        if len(term) == 3:
            self.text = term[0]
            self.label = term[1]
            self.score = term[2]
            
        elif len(term) == 5:
            self.text = term[1]
            self.label = term[3]
            self.score = term[4]
