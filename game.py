class Game:

    def __init__(self, stats):
        self.stats = stats
        self.options = ['Diplomacy', 'Research', 'Army Management', 'Focuses', 'Production', 'Construction']
        self.to_select = -1

    def print_situation(self):
        print(self.stats.nation)
        for idx, place in enumerate(self.options, start=1):
            print(f"{idx}. {place}")
        while self.to_select not in range(1, len(self.options) + 1):
            self.to_select = int(input())

    def take_turn(self):
        self.options[self.to_select]
        return True

    def army(self):
        pass
