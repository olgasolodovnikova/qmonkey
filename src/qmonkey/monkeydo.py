class hungry_monkey():
    def __init__(self, bananas, fullness):
        self.bananas = bananas
        self.fullness = fullness

    def eat_banana(self):
        if self.bananas > 0:
            self.fullness += 1
            self.bananas -1
        else:
            raise ValueError('Qmonkey doesn\'t have any more bananas.')
        if self.fullness == 100:
            print('Qmonkey exploded from too many bananas.')
        
            
    def give_banana(self):
        self.bananas += 1

        
        