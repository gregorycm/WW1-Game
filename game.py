class Game:

    def __init__(self, stats):
        self.nation_diplo = ['']
        self.stats = stats
        self.options = {'Diplomacy': self.diplo, 'Research': self.tech, 'Army Management': self.army,
                        'Focuses': self.focuses, 'Production': self.product, 'Construction': self.construct}
        self.to_select = -1
        self.current_option = ''

    def print_situation(self):
        print(self.stats.nation)
        for idx, place in enumerate(self.options, start=1):
            print(f"{idx}. {place}")
        while self.to_select not in range(1, len(self.options) + 1):
            self.to_select = int(input())

    def take_turn(self):
        return True

    def army(self):
        print("REEEEEEEEEEEEE")

    def select(self):
        to_select = -1
        while to_select not in range(1, len(self.options) + 1):
            to_select = int(input())
        self.current_option = self.options[to_select - 1]

    def diplo(self):
        pass

    def tech(self):
        pass

    def focuses(self):
        pass

    def product(self):
        pass

    def construct(self):
        pass
