import sys


class Menu:

    def __init__(self, stats):
        self.menu = {'Start': ['Play', 'Settings', 'Exit'], 'Play': ['Difficulty', 'Nations', 'Start'],
                     'Settings': ['Start', 'Impossible Mode'], 'Exit': ['debug'], 'debug': ['Exit', 'Impossible Mode'],
                     'Impossible Mode': ['debug'], 'Difficulty': ['Easy', 'Medium', 'Hard'],
                     'Nations': ['German Empire', 'British Empire', 'USA', 'France', 'Russian Empire', 'Japan',
                                 'Ottoman Empire', 'Austro Hungarian Empire', 'Italy', 'Belgium', 'Luxembourg',
                                 'Serbia', 'Montenegro']
                     }
        self.stats = stats
        self.nation_list = {'German Empire': stats.german_empire, 'France': stats.france, 'USA': stats.usa,
                            'Japan': stats.japan, 'British Empire': stats.uk, 'Serbia': stats.serbia,
                            'Montenegro': stats.montenegro, 'A-H': stats.austria_hungary, 'Ottoman Empire': stats.otto,
                            'Italy': stats.italy, 'Russian Empire': stats.russia, 'Belgium': stats.bel,
                            'Luxembourg': stats.lux}
        self.current_menu = 'Start'
        self.impossible_mode = 'No'
        self.easy_mode = 'No'
        self.medium_mode = 'Yes'
        self.hard_mode = 'No'

    def do_nation_menu(self):
        for idx, place in enumerate(self.menu['Nations'], start=1):
            print(f"{idx}. {place}")
        to_select = -1
        while to_select not in range(1, len(self.menu['Nations']) + 1):
            to_select = int(input())
        print("REEEEEEEEEEEEEEEEEEEEEE")
        self.nation_list[self.menu['Nations'][to_select - 1]]()
        self.current_menu = 'Nations'

    def select(self):
        to_select = -1
        while to_select not in range(1, len(self.menu[self.current_menu]) + 1):
            to_select = int(input())
        self.current_menu = self.menu[self.current_menu][to_select - 1]

    def print_menu(self):
        for idx, place in enumerate(self.menu[self.current_menu], start=1):
            print(f"{idx}. {place}")

    def check_options(self, options):
        if self.current_menu == 'Exit':
            sys.exit()
            # debug in menu is for stable game running
        if self.current_menu == 'Nations':
            self.do_nation_menu()
            return True
        if self.current_menu == 'Impossible Mode':
            self.impossible_mode = 'On'
            print("Impossible Mode On")
            self.current_menu = 'Start'
        if self.current_menu == 'Easy':
            self.easy_mode = 'On'
            print("Easy Mode On")
            self.current_menu = 'Start'
        if self.current_menu == 'Medium':
            self.medium_mode = 'On'
            print("Medium Mode On")
            self.current_menu = 'Start'
        if self.current_menu == 'Hard':
            self.hard_mode = 'On'
            print("Hard Mode On")
            self.current_menu = 'Start'
        if self.easy_mode == 'On':
            self.medium_mode = 'No'
            self.hard_mode = 'No'
            self.impossible_mode = 'No'
        if self.medium_mode == 'On':
            self.easy_mode = 'No'
            self.hard_mode = 'No'
            self.impossible_mode = 'No'
        if self.hard_mode == 'On':
            self.medium_mode = 'No'
            self.easy_mode = 'No'
            self.impossible_mode = 'No'
        if self.impossible_mode == 'On':
            self.medium_mode = 'No'
            self.hard_mode = 'No'
            self.easy_mode = 'No'
        if options == 'Research':
            pass
        return False
